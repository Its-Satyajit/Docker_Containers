Prometheus, Grafana, and Cadvisor: A Dockerized Setup for Monitoring
=============================================================

### Overview

This documentation outlines a Docker Compose setup for monitoring infrastructure using Prometheus, Grafana, and Cadvisor.

### In-Depth Explanation

The provided `docker-compose.yml` file configures three services:

#### 1. Prometheus

* Image: `prom/prometheus:latest`
* Port Mapping: Exposes Prometheus on port 7070 (from container) to host port 7070
* Volume Mounts:
	+ `./prometheus:/etc/prometheus`: mounts the Prometheus configuration directory (`prometheus.yml`) from the current working directory to `/etc/prometheus` within the container
	+ Command: Specifies the Prometheus configuration file location with `--config.file=/etc/prometheus/prometheus.yml`

#### 2. Grafana

* Image: `grafana/grafana:latest`
* Port Mapping: Exposes Grafana on port 7071 (from container) to host port 7071
* Volume Mounts:
	+ `./grafana/provisioning:/etc/grafana/provisioning`: mounts the Grafana provisioning directory from the current working directory to `/etc/grafana/provisioning` within the container
	+ `grafana_data:/var/lib/grafana`: shares persistent data storage for Grafana between containers and host system (`/var/lib/grafana`)
* Environment Variables:
	+ `GF_SECURITY_ADMIN_PASSWORD`: sets the Grafana admin password

#### 3. Cadvisor

* Image: `gcr.io/cadvisor/cadvisor:latest`
* Port Mapping: Exposes Cadvisor on port 7072 (from container) to host port 7072
* Volume Mounts:
	+ `/var/run/docker.sock:/var/run/docker.sock:ro`: shares Docker socket for communication between containers and the host system (`/var/run/docker.sock`)
	+ `/sys:/sys:ro`: mounts system files for access within Cadvisor (`/sys` filesystem)
	+ `/var/lib/docker/:/var/lib/docker:ro`: shares persistent data storage for Docker (`/var/lib/docker`) between containers and host system

### Usage Examples

Here's a step-by-step guide to get started:

#### Step 1. Clone the repository

Fetch the project code using Git:
```bash
git clone https://github.com/user/prometheus-grafana-docker.git
```

#### Step 2. Update environment variables (if necessary)

Customize the `docker-compose.yml` file to match your environment needs, if any.

### Best Practices and Optimization

To ensure a smooth operation:

* Be mindful of resource allocation for each service based on their requirements.
* Utilize persistent storage (`grafana_data`) for Grafana to preserve data between container restarts or host system resets.
* Keep in mind that Cadvisor exposes Docker statistics. If you're working with sensitive data, be cautious about exposing it.

### Common Pitfalls and Troubleshooting

Troubleshoot issues related to:

* Prometheus configuration file path (`command: --config.file=/etc/prometheus/prometheus.yml`)
* Grafana admin password setting (`GF_SECURITY_ADMIN_PASSWORD`)
* Cadvisor Docker socket sharing (`/var/run/docker.sock:/var/run/docker.sock:ro`)

### Sensitive Data Masking

Replace sensitive information with placeholders where applicable, e.g., `[MASKED]`.

Note:
This documentation assumes the reader is familiar with basic Docker concepts and configuration. It provides an in-depth explanation of the setup, highlighting key features and usage examples. The advice section offers tips on maintaining a healthy monitoring environment.