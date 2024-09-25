# Docker and Docker Compose Documentation

This repository provides pre-configured Docker Compose setups for various essential services, including GoSpeed, MySQL with MariaDB and phpMyAdmin, Pi-hole, Portainer, PostgreSQL, and a monitoring stack featuring Prometheus and Grafana.

## Table of Contents

1. [Installing Docker and Docker Compose](#installing-docker-and-docker-compose)
2. [Post-Installation Steps](#post-installation-steps)
3. [Repository Structure](#repository-structure)
4. [Setup Overviews](#setup-overviews)
   - [GoSpeed Setup](#gospeed-setup)
   - [MySQL, MariaDB & phpMyAdmin Setup](#mysql-mariadb-phpmyadmin-setup)
   - [Pi-hole Setup](#pihole-setup)
   - [Portainer Setup](#portainer-setup)
   - [PostgreSQL Setup](#postgresql-setup)
   - [Prometheus & Grafana Monitoring Stack](#prometheus-grafana-monitoring-stack)
5. [Usage Instructions](#usage-instructions)
6. [Dependency Management with Renovate](#dependency-management-with-renovate)
7. [Contributing & Support](#contributing--support)
8. [License](#license)

## Installing Docker and Docker Compose

### Windows

1. **Download Docker Desktop** from [Docker Hub](https://hub.docker.com/).
2. **Run the Installer** and follow the instructions.
3. **Verify Installation**:
   ```bash
   docker --version
   docker-compose --version
   ```

### macOS

1. **Download Docker Desktop** from [Docker Hub](https://hub.docker.com/).
2. **Open the `.dmg` file** and drag Docker to Applications.
3. **Verify Installation**:
   ```bash
   docker --version
   docker-compose --version
   ```

### Ubuntu

1. **Remove Old Versions**:
   ```bash
   sudo apt remove docker docker-engine docker.io containerd runc
   ```
2. **Install Required Packages**:
   ```bash
   sudo apt update
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```
3. **Add Docker’s GPG Key and Repository**:
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   ```
4. **Install Docker**:
   ```bash
   sudo apt update
   sudo apt install docker-ce docker-compose
   ```

### CentOS

1. **Remove Old Versions**:
   ```bash
   sudo yum remove docker docker-common docker-selinux docker-engine
   ```
2. **Set up the Stable Repository**:
   ```bash
   sudo yum install -y yum-utils
   sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
   ```
3. **Install Docker**:
   ```bash
   sudo yum install docker-ce
   sudo systemctl start docker
   sudo systemctl enable docker
   ```
4. **Install Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### Additional Platforms

For installation on other distributions (Debian, Fedora, Arch Linux, etc.), please refer to the official [Docker documentation](https://docs.docker.com/get-docker/).

## Post-Installation Steps

1. **Manage Docker as a Non-Root User**:

   ```bash
   sudo usermod -aG docker $USER
   ```

   Log out and back in for changes to take effect.

2. **Verify Docker Installation**:

   ```bash
   docker run hello-world
   ```

3. **Configure Docker to Start on Boot**:

   ```bash
   sudo systemctl enable docker
   ```

4. **Check Docker Service Status**:

   ```bash
   sudo systemctl status docker
   ```

5. **Explore Docker Commands**:

   ```bash
   docker --help
   docker ps
   docker ps -a
   ```

6. **Install Docker Compose (if not done earlier)**:

   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

7. **Security Practices**:
   Review Docker security best practices.

8. **Regular Maintenance**:
   Keep Docker updated with your package manager.

## Repository Structure

This repository is organized as follows:

```plaintext
.
├── gospeed
│   └── docker-compose.yml
├── mysql-mariadb-phpmyadmin-setup
│   └── docker-compose.yml
├── pihole-setup
│   └── docker-compose.yml
├── portainer-setup
│   └── docker-compose.yml
├── postgresql-setup
│   └── docker-compose.yml
├── prometheus-grafana-setup
│   ├── docker-compose.yml
│   └── prometheus
│       └── prometheus.yml
├── README.md
└── renovate.json
```

## Setup Overviews

### GoSpeed Setup

**Directory**: `gospeed/`

- Deploy [GoSpeed](https://github.com/GopeedLab/gopeed).
- Access UI at `http://localhost:9999`.

### MySQL, MariaDB & phpMyAdmin Setup

**Directory**: `mysql-mariadb-phpmyadmin-setup/`

- Set up MySQL and MariaDB with [phpMyAdmin](https://www.phpmyadmin.net/).
- Access phpMyAdmin at `http://localhost:8080`.

### Pi-hole Setup

**Directory**: `pihole-setup/`

- Deploy [Pi-hole](https://pi-hole.net/) for ad blocking.
- Access web interface at `http://localhost`.

### Portainer Setup

**Directory**: `portainer-setup/`

- Manage Docker containers using [Portainer](https://www.portainer.io/).
- Access Portainer at `http://localhost:9000`.

### PostgreSQL Setup

**Directory**: `postgresql-setup/`

- Set up a PostgreSQL database.
- Access PostgreSQL on port `5432`.

### Prometheus & Grafana Monitoring Stack

**Directory**: `prometheus-grafana-setup/`

- Monitor systems with [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/).
- Access Prometheus at `http://localhost:7070` and Grafana at `http://localhost:7071`.

## Usage Instructions

1. **Choose a Service Directory**: Navigate to the desired service directory.
2. **Customize Configurations**: Edit `docker-compose.yml` as needed.
3. **Deploy the Service**:
   ```bash
   docker-compose up -d
   ```
4. **Stop the Service**:
   ```bash
   docker-compose down
   ```

## Dependency Management with Renovate

This repository uses [Renovate](https://renovatebot.com/) to automatically update Docker images and dependencies. The configuration is defined in `renovate.json`.

## Contributing & Support

Contributions are welcome! For suggestions or issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
