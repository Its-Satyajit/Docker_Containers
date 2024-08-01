# Docker Compose Configurations for Essential Services

This repository provides pre-configured Docker Compose setups for various essential services including GoSpeed, MySQL Chaining (with MariaDB and phpMyAdmin), Pi-hole, Portainer, PostgreSQL, and a monitoring stack featuring Prometheus and Grafana.

## Table of Contents

1. [Repository Structure](#repository-structure)
2. [Setup Overviews](#setup-overviews)
    - [GoSpeed Setup](#gospeed-setup)
    - [MySQL, MariaDB & phpMyAdmin Setup](#mysql-mariadb-phpmyadmin-setup)
    - [Pi-hole Setup](#pihole-setup)
    - [Portainer Setup](#portainer-setup)
    - [PostgreSQL Setup](#postgresql-setup)
    - [Prometheus & Grafana Monitoring Stack](#prometheus-grafana-monitoring-stack)
3. [Usage Instructions](#usage-instructions)
4. [Dependency Management with Renovate](#dependency-management-with-renovate)
5. [Contributing & Support](#contributing--support)
6. [License](#license)

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

Each directory contains a `docker-compose.yml` file configured for a specific service or stack.

## Setup Overviews

### GoSpeed Setup

**Directory**: `gospeed/`

Deploy [GoSpeed](https://github.com/liwei2633/gopeed), a high-performance download manager with a user-friendly web interface.

-   **Key Features**:
    -   **Ports**: Access the GoSpeed UI at `http://localhost:9999`.
    -   **Volumes**:
        -   `/home/satyajit/Downloads:/app/Downloads` - Maps local downloads to the container.
        -   `./storage:/app/storage` - Persistent storage for GoSpeed.
    -   **Auto-Update**: Integrated with Watchtower for automatic updates.

### MySQL, MariaDB & phpMyAdmin Setup

**Directory**: `mysql-mariadb-phpmyadmin-setup/`

Easily set up MySQL and MariaDB databases with [phpMyAdmin](https://www.phpmyadmin.net/) for web-based database management.

-   **Key Features**:
    -   **MySQL & MariaDB**:
        -   MySQL: Accessible on port `3307`.
        -   MariaDB: Accessible on port `3306`.
    -   **phpMyAdmin**: Manage your databases via a web interface at `http://localhost:8080`.
    -   **Data Persistence**: Stores data in volumes to ensure it persists across container restarts.
    -   **Isolated Network**: Services communicate securely over a custom backend network.
    -   **Watchtower**: Automates the update process for all services.

### Pi-hole Setup

**Directory**: `pihole-setup/`

Deploy [Pi-hole](https://pi-hole.net/) to block ads and enhance your network’s performance.

-   **Key Features**:
    -   **DNS and Web Services**: Exposes DNS (ports `53/tcp`, `53/udp`) and web interface (port `80`).
    -   **Volume Mapping**: Configuration and data are stored persistently across reboots.
    -   **Network Configuration**: Custom network and IP settings for secure and reliable operations.
    -   **Watchtower**: Keeps Pi-hole up-to-date automatically.

### Portainer Setup

**Directory**: `portainer-setup/`

Manage your Docker containers and services with ease using [Portainer](https://www.portainer.io/).

-   **Key Features**:
    -   **Web Interface**:
        -   Portainer agent accessible at `http://localhost:8081`.
        -   Main UI accessible at `http://localhost:9000`.
    -   **Persistent Data**: Stores Portainer data persistently with mapped volumes.
    -   **Automated Updates**: Integrated Watchtower service for automatic updates.

### PostgreSQL Setup

**Directory**: `postgresql-setup/`

Set up a PostgreSQL database for reliable and scalable data management.

-   **Key Features**:
    -   **Database Service**: PostgreSQL available on port `5432`.
    -   **Data Persistence**: Data is stored in `./postgres-data` to persist across container restarts.

### Prometheus & Grafana Monitoring Stack

**Directory**: `prometheus-grafana-setup/`

Monitor your systems and visualize metrics using [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/).

-   **Key Features**:
    -   **Prometheus**: Metrics collection, exposed at `http://localhost:7070`.
    -   **Grafana**: Dashboard for visualization, accessible at `http://localhost:7071`.
    -   **cAdvisor**: Container monitoring available at `http://localhost:7072`.
    -   **Persistent Storage**: Ensures metric retention later review and analysis.
    -   **Custom Network**: All services are networked securely for efficient monitoring.

## Usage Instructions

1. **Choose a Service Directory**: Navigate to the directory of the service you want to set up.
2. **Customize Configurations**: Edit the `docker-compose.yml` file if necessary to fit your environment.
3. **Deploy the Service**:
    ```bash
    docker-compose up -d
    ```
4. **Stop the Service**:
    ```bash
    docker-compose down
    ```

## Dependency Management with Renovate

This repository uses [Renovate](https://renovatebot.com/) to automatically update Docker images and dependencies. The configuration is defined in `renovate.json`, which you can customize to suit your needs.

## Contributing & Support

Contributions are welcome! If you have suggestions or encounter any issues, feel free to open an issue or submit a pull request. For direct support, please use the issue tracker in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**Keywords**: Docker, Docker Compose, MySQL, MariaDB, phpMyAdmin, Pi-hole, Portainer, PostgreSQL, Prometheus, Grafana, GoSpeed, Watchtower, Container Management, Monitoring, Database Management.

**Description**: A comprehensive collection of Docker Compose configurations for deploying essential services like MySQL, MariaDB, phpMyAdmin, Pi-hole, Portainer, PostgreSQL, Prometheus, and Grafana with ease.
