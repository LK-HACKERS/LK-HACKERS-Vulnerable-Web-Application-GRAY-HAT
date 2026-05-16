# LK-HACKERS-Vulnerable-Web-Application-GRAY-HAT 

A lightweight, standalone Reflected Cross-Site Scripting (XSS) laboratory environment built with Flask. This project is specifically configured to run natively inside mobile terminal sandboxes like **Termux** as well as desktop environments **(Linux, Windows, macOS)** without triggering template processing errors.

The repository provides a dual-interface testing suite: a vulnerable client-side mock retail store and an attacker exfiltration monitoring control panel.

## 🛠️ Installation & Setup

### Prerequisites
Ensure Python 3.x and the `pip` package installer are available on your platform.

```bash
# Update local packages (Termux Environment Setup)
pkg update && pkg upgrade -y

# Install Python environment dependencies
pkg install python -y

# clone the repository
git clone https://github.com/LK-HACKERS/LK-HACKERS-Vulnerable-Web-Application-GRAY-HAT.git

```
### Dependency Installation
Clone the repository and install the minimal required routing dependencies:
```bash
# Install Flask routing engine
pip install Flask

```
### Launching the Laboratory
Run the centralized automation script using the Python compiler:
```bash
python app.py

```
Once executed, the engine initializes on all active network interfaces bound to local port 8080.
## 🌐 Active Hub Endpoints
| Portal Component | Accessible Route URL | Core Purpose |
|---|---|---|
| **Vulnerable Application** | http://127.0.0.1:8080/ | Target retail interface testing reflected input handling logic. |
| **Hacker Dashboard** | http://127.0.0.1:8080/hacker-panel | Live listener terminal capturing intercepted session pools. |
| **Exfiltration Endpoint** | http://127.0.0.1:8080/exfiltrate | GET request data pool sink capturing inbound parameters. |
## 🛡️ Educational Vectors Supported
The interactive reference panel outlines key security training vectors:
 1. **Basic Execution**: Testing standard input reflection vectors using nested dynamic tag blocks.
 2. **Inline Attributes**: Utilizing explicit image source validation failures (onerror) to bypass basic string detection filters.
 3. **Exfiltration Simulation**: Emulating credential transfers using modern Fetch API requests to dispatch cookies to listening services.
## ⚖️ Disclaimer
This laboratory repository is explicitly designed for educational research, internal technical group training, and legitimate offensive evaluation exercises. Do not host or run this software on untrusted external public networks.


## KALI LINUX SETUP

## 🛠️ Installation & Setup (Kali Linux)

Since Kali Linux natively includes Python 3 and Pip package management, setup is straightforward. Follow the steps below using your terminal emulator:

### 1. Install Dependencies
Navigate into your cloned project repository directory and install the required Flask web framework routing engine:
```bash
pip3 install Flask

```
*Note: If your Kali system environment configuration prompts an externally-managed-environment restriction error, use the system override flag instead:*
```bash
pip3 install Flask --break-system-packages

```
### 2. Run the Laboratory
Initialize the core Python service file to launch the training suite:
```bash
python3 app.py

```
### 🌐 Network Access
Once executed, the automation framework will automatically trigger Kali's default browser (Firefox) to open the target testing platform instantly. You can also connect manually via these endpoints:
 * **Target Web Application**: http://127.0.0.1:8080/
 * **Hacker Monitoring Dashboard**: http://127.0.0.1:8080/hacker-panel
```

```
