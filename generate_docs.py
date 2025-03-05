# -*- coding: utf-8 -*-

import os
import requests
import argparse
import logging
from pathlib import Path
import re
import json

# Configuration
LM_STUDIO_API_URL = "http://localhost:1234/v1/chat/completions"  # Update this with your actual LLM server URL
MODEL_ID = "your-model-id"  # Replace with your actual model ID
PROJECT_ROOT = Path(__file__).parent
DOCS_ROOT = PROJECT_ROOT / "docs"

# Define file extensions and directories relevant to your stacks
SOURCE_CODE_EXTENSIONS = [".php", ".js", ".jsx", ".ts", ".tsx", ".json",".prisma", ".yml"]
MAX_FILE_SIZE_MB = 10  # Maximum file size in megabytes to process
IGNORE_PATTERNS = ["node_modules", ".git", ".env", "vendor", "storage", "public", ".next", "dist",
                   "*.test.js", "*.test.ts", "*.spec.js", "*.spec.ts", "*.md", "*.css", "generate_docs.py"]
DEPENDENCY_FILES = [ "composer.json","package.json", "requirements.txt", "Pipfile", "Pipfile.lock"]
PROMPT_TEMPLATE = """
# Note: The following dependencies information is for contextual understanding only and should not be included in the final documentation.

# Dependencies:
{dependencies_info}

You are a skilled technical writer, tasked with creating well-organized and accessible documentation for the provided source code. The documentation should cater to both beginners and experienced developers, covering the following sections:

1. **Overview**: Summarize the code’s purpose and functionality in a concise, clear manner.
2. **In-Depth Explanation**: Detail the core functions, classes, and methods. Explain the logic, design decisions, and possible alternatives, using code snippets where necessary.
3. **Usage Examples**: Provide practical examples to demonstrate the code in action. Include step-by-step guides for beginners and advanced tips for seasoned developers.
4. **Dependencies **: List all necessary external dependencies and tools Used in the source code.
5. **Best Practices and Optimization**: Recommend best practices for using and extending the code. Suggest optimization techniques and potential areas for improvement.
6. **Common Pitfalls and Troubleshooting**: Highlight common issues and offer troubleshooting advice.
7. **Sensitive Data Masking**: Ensure any sensitive information in the code is obscured, replacing it with placeholders like `[MASKED]`.

Here is the source code:

**File:** {file_path}

```{content}```

**Formatting**: Use Markdown, with clear headings, code blocks, and bullet points. Include code snippets to support explanations and examples.

**Tone and Style**: Maintain a conversational yet professional tone. Avoid unnecessary jargon; explain technical terms clearly.

**Quality Assurance**: Ensure the documentation is accurate, complete, and that code snippets are functional and relevant.
"""

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_gitignore_patterns(root_path: Path) -> list:
    """Load ignore patterns from all .gitignore files within the root path."""
    patterns = IGNORE_PATTERNS[:]
    
    for root, _, files in os.walk(root_path):
        for file in files:
            if file == ".gitignore":
                gitignore_path = Path(root) / file
                logging.info(f"Loading patterns from {gitignore_path}...")
                with open(gitignore_path, 'r', encoding='utf-8') as f:
                    patterns.extend(line.strip() for line in f if line.strip() and not line.startswith('#'))
    
    return patterns

def should_ignore(file_path: Path, ignore_patterns: list) -> bool:
    """Check if the file path matches any ignore pattern."""
    str_path = str(file_path)
    for pattern in ignore_patterns:
        if pattern.startswith('/') and (file_path.match(pattern) or str_path.endswith(pattern)):
            logging.info(f"Ignoring path due to pattern '{pattern}': {file_path}")
            return True
        elif file_path.name == pattern.strip('/'):
            logging.info(f"Ignoring path due to pattern '{pattern}': {file_path}")
            return True
    return False

def is_source_code_file(file_path: Path) -> bool:
    """Check if the file is a source code file based on its extension."""
    return file_path.suffix in SOURCE_CODE_EXTENSIONS

def mask_secrets(code: str) -> str:
    """Preprocess the code to mask potential secrets."""
    # Example patterns for common secrets; adjust as needed
    patterns = [
        # JWT tokens (commonly found in Authorization headers)
        r"Bearer\s[a-zA-Z0-9\-_.]+",  # Example: Bearer <token>
        r"eyJhbGciOiJIUzI1NiIsIn[\w-]+",  # JWT token in Python code (partially matched)
        r"([a-zA-Z0-9]{20,}\.[a-zA-Z0-9]{20,}\.[a-zA-Z0-9]{20,})",  # General JWT pattern

        # General API keys (long alphanumeric strings)
        r"[a-zA-Z0-9]{32,}",  # General API key pattern (long alphanumeric strings)
        r"[A-Za-z0-9-_]{40,}",  # Extended general API key pattern

        # API keys in single or double quotes
        r"'[A-Za-z0-9-_]{20,}'",  # API key in single quotes
        r'"[A-Za-z0-9-_]{20,}"',  # API key in double quotes

        # Other potential secret patterns
        r"(?:apikey|api_key|apiToken|api-token|secret|authToken|auth_token|token)[\s:]*['\"]?[a-zA-Z0-9-_]{20,}['\"]?",  # Various labels for secrets
        # r"\b[A-Za-z0-9-_]{20,}\b",  # Generic long alphanumeric strings (could be passwords or tokens)
        
        # Mask secrets assigned with quotes
        r'\b(?:password|pass|secret|api[_-]?key|token|auth[_-]?key)\b\s*=\s*[\'"][^\'"]*[\'"]',  
        
        # Mask secrets assigned without quotes
        r'\b(?:password|pass|secret|api[_-]?key|token|auth[_-]?key)\b\s*=\s*\S+',  
    ]
    
    masked_code = code
    for pattern in patterns:
        masked_code = re.sub(pattern, '[MASKED]', masked_code, flags=re.IGNORECASE)
    return masked_code

def replace_spaces_and_tabs(text):
    result = re.sub(r'[ \t]{4,}', '\t', text)
    return result

def generate_documentation(prompt: str) -> str:
    """Generate documentation from the given prompt using the local LLM server."""
    headers = {"Content-Type": "application/json"}
    data = {
        "model": MODEL_ID,
        "messages": [
               {
                "role": 'system',
                "content": '<Assistant_Info> Mr_AI, created by Its-Satyajit, has knowledge up to Today. It answers questions based on this knowledge and clarifies its cutoff date when relevant. It cannot access URLs, links, or videos, and asks users to provide relevant text or images when needed. Mr_AI approaches controversial topics with care, avoiding labeling information as sensitive or objective. It excels at solving complex problems by breaking them down into simpler components and using step-by-step reasoning. </Assistant_Info> <Task_Handling> Mr_AI handles both simple and complex tasks with precision. For complex problems, it divides the task into smaller, manageable steps and solves each systematically. When working on coding, logical reasoning, or problem-solving, Mr_AI uses detailed, step-by-step analysis to ensure clarity and accuracy. It assists with tasks involving popular opinions regardless of its own views. For obscure topics, it warns about possible hallucinations and advises users to verify citations since it lacks access to databases or search engines. </Task_Handling> <Interaction_Style> Mr_AI avoids unnecessary apologies and filler phrases like "Certainly" or "Absolutely." It provides concise answers but switches to detailed responses for more intricate tasks or when asked for specifics. For coding, math, and problem-solving, Mr_AI follows a clear, methodical process, explaining each step. Code explanations are provided only if requested. For lengthy tasks, it breaks them into parts, seeking user feedback as it completes each section. Users can give feedback via the thumbs-down button if dissatisfied. </Interaction_Style> <Image_Handling> Mr_AI is "face-blind" and cannot recognize individuals from images. It discusses named individuals but never implies facial recognition. For any image-based task, Mr_AI summarizes the content and repeats instructions before proceeding. </Image_Handling> <Language_and_Tone> Mr_AI communicates in the user’s language and follows these guidelines for tasks like analysis, coding, problem-solving, creative writing, teaching, and more. It prioritizes clarity and logical structure, especially for complex or abstract inquiries, ensuring responses are as accurate and systematic as possible. </Language_and_Tone>',
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 1,
        "max_tokens": 5000  # Increased to accommodate more detailed documentation
    }
    try:
        logging.info("Sending request to LLM server...")
        response = requests.post(LM_STUDIO_API_URL, headers=headers, json=data)
        response.raise_for_status()
        completion = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        logging.info("Documentation generated successfully.")
        return completion
    except requests.RequestException as e:
        logging.error(f"Error generating documentation: {e}")
        return ""

def get_output_file_name(file_path: Path) -> Path:
    """Generate an output file name based on the input file path, preserving folder structure."""
    relative_path = file_path.relative_to(PROJECT_ROOT)
    # Change the suffix to include '-documentation' before the .md extension
    base_name = str(relative_path.with_suffix('')) + '-documentation.md'  # Updated line
    return DOCS_ROOT / base_name

def load_dependency_file(file_path: Path) -> dict:
    """Load dependency information from a given file."""
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            if file_path.suffix == ".json":
                return json.load(f)
            elif file_path.name == "requirements.txt":
                return {"requirements.txt": [line.strip() for line in f if line.strip()]}
            elif file_path.name in ["Pipfile", "Pipfile.lock"]:
                return {"Pipfile": [line.strip() for line in f if line.strip()]}
    return {}

def get_dependencies_info() -> str:
    """Generate a formatted string of dependencies from known files."""
    dependencies_info = ""

    for dep_file in DEPENDENCY_FILES:
        file_path = PROJECT_ROOT / dep_file
        if file_path.exists():
            data = load_dependency_file(file_path)
            if file_path.suffix == ".json":
                if "dependencies" in data:
                    dependencies_info += "### Node Dependencies\n\n"
                    for dep, version in data["dependencies"].items():
                        dependencies_info += f"- **{dep}**: {version}\n"
                if "require" in data:
                    dependencies_info += "\n### Laravel Dependencies\n\n"
                    for dep, version in data["require"].items():
                        dependencies_info += f"- **{dep}**: {version}\n"
                if "devDependencies" in data:
                    dependencies_info += "\n### Node  Dev Dependencies\n\n"
                    for dev_dep, version in data["devDependencies"].items():
                        dependencies_info += f"- **{dev_dep}**: {version}\n"
                if "require-dev" in data:
                    dependencies_info += "\n### Laravel Dev Dependencies\n\n"
                    for dep, version in data["require-dev"].items():
                        dependencies_info += f"- **{dep}**: {version}\n"
            elif file_path.name == "requirements.txt":
                dependencies_info += "### Python Dependencies (requirements.txt)\n\n"
                for requirement in data.get("requirements.txt", []):
                    dependencies_info += f"- {requirement}\n"
            elif file_path.name == "Pipfile":
                dependencies_info += "### Python Dependencies (Pipfile)\n\n"
                for requirement in data.get("Pipfile", []):
                    dependencies_info += f"- {requirement}\n"
    
    return dependencies_info

def file_is_too_large(file_path: Path) -> bool:
    """Check if the file size exceeds the maximum allowed size."""
    try:
        file_size_mb = file_path.stat().st_size / (1024 * 1024)  # Size in megabytes
        return file_size_mb > MAX_FILE_SIZE_MB
    except (OSError, FileNotFoundError) as e:
        logging.error(f"Error checking file size for {file_path}: {e}")
        return False

def process_file(file_path: Path, ignore_patterns: list, force: bool) -> None:
    """Process each file to generate or update documentation."""
    if should_ignore(file_path, ignore_patterns) or not is_source_code_file(file_path):
        logging.info(f"Skipping ignored or non-source file: {file_path}")
        return
    if file_is_too_large(file_path): 
        logging.info(f"Skipping ignored file too large: {file_path}")
        return

    output_file_path = get_output_file_name(file_path)

    # Check if documentation needs to be regenerated
    if not force and output_file_path.exists():
        try:
            doc_mtime = output_file_path.stat().st_mtime
            file_mtime = file_path.stat().st_mtime

            if file_mtime <= doc_mtime:
                logging.info(f"Documentation already up-to-date for {file_path}. Skipping.")
                return
            else:
                logging.info(f"File modified after documentation creation. Re-generating for {file_path}.")
        except (OSError, FileNotFoundError) as e:
            logging.warning(f"Error checking modification times: {e}")
            logging.info(f"Proceeding to re-generate documentation for {file_path}.")
    else:
        logging.info(f"Processing file: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        logging.error(f"Error reading file {file_path}: File is not UTF-8 encoded. Skipping.")
        return
    except IOError as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return

    masked_content = mask_secrets(content)
    relative_file_path = file_path.relative_to(PROJECT_ROOT)
    dependencies = get_dependencies_info()
    prompt = PROMPT_TEMPLATE.format(content=replace_spaces_and_tabs(masked_content), file_path=relative_file_path, dependencies_info=dependencies )
    documentation = generate_documentation(prompt)

    if documentation:
        output_file_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(documentation)
            logging.info(f"Documentation saved to {output_file_path}")
        except IOError as e:
            logging.error(f"Error writing file {output_file_path}: {e}")

def generate_docs(file: Path = None, force: bool = False):
    """Generate documentation for all files or a single file."""
    ignore_patterns = load_gitignore_patterns(PROJECT_ROOT)
    
    if file:
        file_path = Path(file).resolve()
        if file_path.is_file():
            logging.info(f"Generating documentation for: {file_path}")
            process_file(file_path, ignore_patterns, force)
        else:
            logging.error(f"File not found: {file_path}")
    else:
        logging.info("Generating documentation for all source code files...")
        for root, dirs, files in os.walk(PROJECT_ROOT):
            logging.info(f"Processing directory: {root}")
            dirs[:] = [d for d in dirs if not should_ignore(Path(root) / d, ignore_patterns)]
            for file in files:
                file_path = Path(root) / file
                process_file(file_path, ignore_patterns, force)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate or update documentation from source code.")
    parser.add_argument('--file', type=str, help="Specify a single file to generate documentation for.")
    parser.add_argument('--force', action='store_true', help="Force re-create documentation even if it already exists.")
    args = parser.parse_args()

    logging.info("Starting documentation generation...")
    generate_docs(file=args.file, force=args.force)
    logging.info("Documentation generation completed.")