#!/usr/bin/env bash

# Updating section

# Update a system & upgrade it
apt update && sudo apt upgrade -y

# Auto-Update
apt install unattended-upgrades && sudo apt update

# Start/enable service on boot
systemctl start unattended-upgrades.service
systemctl enable unattended-upgrades.service