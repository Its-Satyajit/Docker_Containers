## Docker and Docker Compose Documentation

This repository provides pre-configured Docker Compose setups for various essential services, including Apache, GoSpeed, MySQL with MariaDB and phpMyAdmin, MongoDB, Nginx, Pi-hole, Portainer, PostgreSQL, Prometheus and Grafana, and more.

## Table of Contents

1. [Installing Docker and Docker Compose](#installing-docker-and-docker-compose)
2. [Post-Installation Steps](#post-installation-steps)
3. [Repository Structure](#repository-structure)
4. [Setup Overviews](#setup-overviews)
5. [Usage Instructions](#usage-instructions)
6. [Dependency Management with Renovate](#dependency-management-with-renovate)
7. [Contributing & Support](#contributing--support)
8. [License](#license)

## Installing Docker and Docker Compose

### Windows

1. **Download Docker Desktop** from [Docker](https://docs.docker.com/get-started/get-docker/).
2. **Run the Installer** and follow the instructions.
3. **Verify Installation**:
   ```bash
   docker --version  # Check the installed Docker version
   docker-compose --version  # Check the installed Docker Compose version
   ```

### macOS

1. **Download Docker Desktop** from [Docker](https://docs.docker.com/get-started/get-docker/).
2. **Open the `.dmg` file** and drag Docker to Applications.
3. **Verify Installation**:
   ```bash
   docker --version  # Check the installed Docker version
   docker-compose --version  # Check the installed Docker Compose version
   ```

### Ubuntu

1. **Remove Old Versions**:
   ```bash
   sudo apt remove docker docker-engine docker.io containerd runc  # Clean up old installations
   ```
2. **Install Required Packages**:
   ```bash
   sudo apt update  # Update package list
   sudo apt install apt-transport-https ca-certificates curl software-properties-common  # Install prerequisites
   ```
3. **Add Docker’s GPG Key and Repository**:
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  # Add Docker’s GPG key
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  # Add Docker repository
   ```
4. **Install Docker and Docker Compose**:
   ```bash
   sudo apt update  # Update package list again
   sudo apt install docker-ce docker-compose  # Install Docker and Docker Compose
   ```

### CentOS

1. **Remove Old Versions**:
   ```bash
   sudo yum remove docker docker-common docker-selinux docker-engine  # Clean up old installations
   ```
2. **Set up the Stable Repository**:
   ```bash
   sudo yum install -y yum-utils  # Install required utilities
   sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo  # Add Docker repository
   ```
3. **Install Docker**:
   ```bash
   sudo yum install docker-ce  # Install Docker
   sudo systemctl start docker  # Start Docker service
   sudo systemctl enable docker  # Enable Docker to start on boot
   ```
4. **Install Docker Compose**:
   ```bash
   sudo yum install docker-compose  # Install Docker Compose via package manager
   ```

### openSUSE

1. **Remove Old Versions**:
   ```bash
   sudo zypper rm docker docker-engine docker-selinux  # Clean up old installations
   ```
2. **Install Docker**:
   ```bash
   sudo zypper install docker  # Install Docker
   ```
3. **Start Docker**:
   ```bash
   sudo systemctl start docker  # Start Docker service
   sudo systemctl enable docker  # Enable Docker to start on boot
   ```
4. **Install Docker Compose**:
   ```bash
   sudo zypper install docker-compose  # Install Docker Compose via package manager
   ```

### Additional Platforms

For installation on other distributions (Debian, Fedora, Arch Linux, etc.), please refer to the official [Docker documentation](https://docs.docker.com/get-docker/).

## Post-Installation Steps

1. **Manage Docker as a Non-Root User**:

   ```bash
   sudo usermod -aG docker $USER  # Add current user to the Docker group for non-root access
   ```

   Log out and back in for changes to take effect.

2. **Verify Docker Installation**:

   ```bash
   docker run hello-world  # Run a test container to verify installation
   ```

3. **Configure Docker to Start on Boot**:

   ```bash
   sudo systemctl enable docker  # Set Docker to start automatically on boot
   ```

4. **Check Docker Service Status**:

   ```bash
   sudo systemctl status docker  # Check if Docker service is running
   ```

5. **Explore Docker Commands**:

   ```bash
   docker --help  # Display available Docker commands
   docker ps  # List running containers
   docker ps -a  # List all containers, including stopped ones
   ```

6. **Security Practices**:
   Review Docker security best practices to protect your environment.

7. **Regular Maintenance**:
   Keep Docker updated with your package manager to ensure you have the latest features and security patches.

## Repository Structure

This repository is organized as follows:

```plaintext
.
├── apache-docker
│   └── docker-compose.yml
├── docs
│   ├── apache-docker
│   ├── gospeed-docker
│   ├── mongo-docker
│   ├── mysql-mariadb-phpmyadmin-docker
│   ├── nginx-docker
│   ├── pihole-docker
│   ├── portainer-docker
│   ├── postgresql-docker
│   ├── prometheus-grafana-docker
│   └── renovate-documentation.md
├── generate_docs.py
├── gospeed-docker
│   └── docker-compose.yml
├── LICENSE
├── mongo-docker
│   └── docker-compose.yml
├── mysql-mariadb-phpmyadmin-docker
│   ├── docker-compose.yml
│   ├── mariadb_data
│   └── mysql_data
├── nginx-docker
│   └── docker-compose.yml
├── openproject
│   └── docker-compose.yaml
├── pihole-docker
│   ├── docker-compose.yml
│   ├── etc-dnsmasq.d
│   └── etc-pihole
├── portainer-docker
│   └── docker-compose.yml
├── postgresql-docker
│   ├── docker-compose.yml
│   └── postgres-data
├── prometheus-grafana-docker
│   ├── docker-compose.yml
│   └── prometheus
├── README.md
├── renovate.json
└── valkey-docker
    ├── docker-compose.yml
    └── valkey.conf
```

## Setup Overviews

### Apache Setup

**Directory**: `apache-docker/`

- Deploy an Apache web server.
- Access the web server at `http://localhost:80` (or the port specified in `docker-compose.yml`).

### GoSpeed Setup

**Directory**: `gospeed-docker/`

- Deploy [GoSpeed](https://github.com/GopeedLab/gopeed), a high-speed downloader developed with Golang and Flutter.
  - Supports HTTP, BitTorrent, and Magnet protocols.
  - Access UI at `http://localhost:9999`.

### MongoDB Setup

**Directory**: `mongo-docker/`

- Set up a MongoDB database.
- Access MongoDB on port `27017`.

### MySQL, MariaDB & phpMyAdmin Setup

**Directory**: `mysql-mariadb-phpmyadmin-docker/`

- Set up MySQL and MariaDB with [phpMyAdmin][2].
  - phpMyAdmin is a free software tool written in PHP to handle MySQL and MariaDB administration over the web.
  - Access phpMyAdmin at `http://localhost:8080`.

### Nginx Setup

**Directory**: `nginx-docker/`

- Deploy an Nginx web server.
- Access the web server at `http://localhost:80` (or the port specified in `docker-compose.yml`).

### Pi-hole Setup

**Directory**: `pihole-docker/`

- Deploy [Pi-hole](https://pi-hole.net/) for ad blocking.
- Access web interface at `http://localhost`.

### Portainer Setup

**Directory**: `portainer-docker/`

- Manage Docker containers using [Portainer](https://www.portainer.io/).
- Access Portainer at `http://localhost:9000`.

### PostgreSQL Setup

**Directory**: `postgresql-docker/`

- Set up a PostgreSQL database.
- Access PostgreSQL on port `5432`.

### Prometheus & Grafana Monitoring Stack

**Directory**: `prometheus-grafana-docker/`

- Monitor systems with [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/).
  - Access Prometheus at `http://localhost:7070` and Grafana at `http://localhost:7071`.

### OpenProject Setup

**Directory**: `openproject/`

- Deploy [OpenProject](https://www.openproject.org/), a project management tool.
- Access OpenProject at the specified port in `docker-compose.yml`.

### Valkey Setup

**Directory**: `valkey-docker/`

- Deploy Valkey
- Access Valkey at the specified port in `docker-compose.yml`.

## Usage Instructions

1. **Choose a Service Directory**: Navigate to the desired service directory.
2. **Customize Configurations**: Edit `docker-compose.yml` as needed to adjust ports, volumes, environment variables, etc.
3. **Deploy the Service**:
   ```bash
   docker-compose up -d  # Start services in detached mode
   ```
4. **Stop the Service**:
   ```bash
   docker-compose down  # Stop and remove the containers
   ```

## Docker Compose File Structure

For those interested in understanding the structure of the `docker-compose.yml` files, here is a brief overview:

- **Version**: Specifies the version of the Docker Compose file format.
  ```yaml
  version: '3'
  ```
- **Services**: Defines individual containers or services.
  ```yaml
  services:
    web:
      build: .
      ports:
        - "8080:8080"
      volumes:
        - .:/code
  ```
- **Build**: Specifies the location of the Dockerfile if you are building a custom image.
  ```yaml
  build:
    context: .
    dockerfile: ./docker/Dockerfile
  ```
- **Image**: Specifies a pre-built image to use.
  ```yaml
  image: mysql/mysql-server:5.8
  ```
- **Environment**: Sets environment variables for the container.
  ```yaml
  environment:
    - MYSQL_ROOT_PASSWORD=root
    - MYSQL_USER=ashok
    - MYSQL_PASSWORD=waytoeasylearn
    - MYSQL_DATABASE=backend
  ```
- **Volumes**: Mounts volumes to persist data.
  ```yaml
  volumes:
    - "/home/ashok/docker/app/db/init.sql:/opt/app/init.sql"
  ```
- **Networks**: Defines custom networks for services to communicate over.
  ```yaml
  networks:
    my-network:
      driver: bridge
  ```

For more detailed information, refer to the [Docker Compose YAML documentation][5].

## Dependency Management with Renovate

This repository uses [Renovate](https://renovatebot.com/) to automatically update Docker images and dependencies. The configuration is defined in `renovate.json`.

## Contributing & Support

Contributions are welcome For suggestions or issues, please open an issue or submit a pull request.

![Alt](https://repobeats.axiom.co/api/embed/81de01a865170163592eae1a9e5c6a98f5893f31.svg "Repobeats analytics image")

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.