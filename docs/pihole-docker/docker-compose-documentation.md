# Pi-Hole Docker Configuration Documentation
=====================================================

## Overview
------------

This documentation provides an in-depth explanation of the provided docker-compose.yml file for a Pi-Hole setup using Docker.

### Purpose
------------

The goal of this configuration is to deploy a Pi-Hole setup using Docker, leveraging its power to provide DNS-level ad-blocking and other network filtering capabilities.

## In-Depth Explanation
------------------------

This section breaks down the key components and configurations present in the provided docker-compose.yml file:

### Services
---------------

#### Pihole Service
--------------------

*   `image`: Uses the latest official Pi-Hole image (`pihole/pihole:2024.07.0`)
*   `container_name`: Sets the container name to "pihole"
*   `networks`: Connects the pi-hole service to a custom network (`dns_net`), with an IP address of `172.20.0.100`
*   Ports:
    *   53/udp (DNS)
    *   53/tcp (DNS)
    *   67/udp (BOOTP/DHCP)
    *   80/tcp (Web interface)
*   Environment variables:
    *   `TZ=Asia/Kolkata`: Sets the timezone
    *   `WEBPASSWORD=password`: Sets the web interface password

### Volumes
-------------

The pi-hole service mounts two volumes:

1.  `./etc-pihole/:/etc/pihole/` - Mounts the Pi-Hole configuration directory from the host machine into the container.
2.  `./etc-dnsmasq.d/:/etc/dnsmasq.d/` - Mounts the dnsmasq configuration files directory from the host machine into the container.

### Unbound Service (Commented Out)
------------------------------------

The commented-out section for the unbound service remains empty but suggests potential configurations if needed. It uses a custom image (`mvance/unbound:1.20.0`) and mounts volumes for its configuration files.

## Usage Examples
------------------

To utilize this configuration:

1.  Place your Pi-Hole setup configuration files in `./etc-pihole/` on the host machine.
2.  Adjust the IP address, timezone, password, and other environment variables according to your needs.
3.  Mount your dnsmasq configuration files directory (`./etc-dnsmasq.d/`) if you have them.

## Dependencies
----------------

This setup relies on:

1.  Docker installed and running
2.  The Pi-Hole image (`pihole/pihole:2024.07.0`)
3.  A custom network (`dns_net`) for the pi-hole service

## Best Practices and Optimization
--------------------------------------

For optimal performance:

*   Utilize the latest images from official repositories whenever possible.
*   Adjust the timezone according to your region's rules.
*   Use strong, unique passwords for services.
*   Regularly update and review configuration files.

## Common Pitfalls and Troubleshooting
-----------------------------------------

When encountering issues with this setup:

*   Ensure Docker is installed and running correctly.
*   Verify your network settings are correct.
*   Adjust environment variables according to your requirements.
*   Consult official documentation for more detailed troubleshooting.

## Sensitive Data Masking
---------------------------

Sensitive information (`password`) has been masked in the provided code snippet with `[MASKED]`.

With these guidelines, you should have a comprehensive understanding of setting up and configuring Pi-Hole using Docker. Always refer to official documentation when resolving issues or optimizing your setup.