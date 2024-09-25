# Renovate Configuration Guide
==========================

Table of Contents
-----------------

* Overview
* In-Depth Explanation
* Usage Examples
* Dependencies
* Best Practices and Optimization
* Common Pitfalls and Troubleshooting
* Sensitive Data Masking

Overview
--------

This document explains the purpose and functionality of a Renovate configuration file (`renovate.json`).

In-Depth Explanation
-------------------

### Configuration Overview

The `renovate.json` file extends the base configuration from `config:base`. It contains rules for managing dependencies and devDependencies.

*   The `packageRules` section defines multiple rules:
    *   Match dependency types (`"dependencies"` or `"devDependencies"`): Determines which packages to update.
    *   Specify update strategies (`major`, `minor`, `patch`): Defines how to handle updates.
    *   Automerge settings (`automerge`): Controls whether dependencies are updated automatically.

```json
{
  "extends": ["config:base"],
  "packageRules": [
    {
      "matchDepTypes": ["dependencies", "devDependencies"],
      "matchUpdateTypes": ["major"],
      "enabled": true
    },
    {
      "matchDepTypes": ["dependencies"],
      "automerge": true,
      "matchUpdateTypes": ["minor", "patch"]
    },
    {
      "matchDepTypes": ["devDependencies"],
      "automerge": true,
      "matchUpdateTypes": ["minor", "patch"]
    }
  ],
  
  "dependencyDashboard": false
}
```

Usage Examples
--------------

### Updating Dependencies

To update dependencies using the Renovate configuration:

1.  Set up a `renovate.json` file with your desired rules.
2.  Use Renovate's CLI tool to scan and update packages.

Example code block:
```bash
# Scan for updates
reno audit
# Update packages according to the specified rules
reno update
```

Note: Replace placeholders (`[MASKED]`) with actual values when necessary, especially for sensitive information.

Dependencies
------------

*   Renovate CLI tool (`@renovate/cli`)
*   Configuration files (`renovate.json`)

Best Practices and Optimization
---------------------------------

### Rule optimization

To optimize the `packageRules` section:

1.  Review and refine your rules as needed.
2.  Utilize default settings where possible.

Example code block:
```json
{
  // Use Renovate's defaults for minor/patch updates
  "packageRules": [
    {
      "matchDepTypes": ["dependencies", "devDependencies"],
      "enabled": true,
      "matchUpdateTypes": ["major"]
    },
    // Automerge settings enabled by default for minors/patches
    {
      "matchDepTypes": ["dependencies"],
      "automerge": true,
      "matchUpdateTypes": ["minor", "patch"]
    }
  ]
}
```

Common Pitfalls and Troubleshooting
------------------------------------

### Configuration Issues

*   Review the `renovate.json` configuration file carefully.
*   Ensure correct usage of match update types (`major`, `minor`, `patch`) and automerge settings.

Sensitive Data Masking
------------------------

Replace sensitive information like API keys or personal data with `[MASKED]` placeholders to avoid exposure:

```json
{
  // [MASKED]: Replace with actual API key or credentials
  "githubApiToken": "[MASKED]"
}
```

This documentation provides a clear explanation of the Renovate configuration file (`renovate.json`) and its components. It includes code snippets to demonstrate usage examples, emphasizing proper rule optimization and addressing common pitfalls.