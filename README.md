# VPN-Monitor
This program was created for a requirement in one of my office's team, where they had business critical task being handled over VPN and most of the time their VPN would disconnect and they would not even notice until its too late. 

# VPN Connection Status Monitor

This Python script monitors the status of a VPN connection interface and provides notifications when the connection state changes.

## Prerequisites

- Python 3.x installed
- Required Python packages: `pygame`, `netifaces`, `plyer`
  - Install them using: `pip install pygame netifaces plyer`

## Usage

1. **Configure the Script**:
   - Open the script `vpn_monitor.py` in a text editor.

2. **Specify the Interface Name**:
   - Replace `"YOUR_INTERFACE_NAME"` with the name of your VPN connection interface.
   - In case of Windows, you need to give the interface_GUID, you can find the interface GUID with this command in powershell or command prompt:
   - `wmic nic get NetConnectionID, GUID`

3. **Run the Script**:
   - Open a terminal and navigate to the directory containing the script.
   - Run the script using: `python vpn_monitor.py`

## Script Behavior

The script continuously monitors the status of the specified VPN connection interface.

- If the VPN connection is UP, the script prints a message.
- If the VPN connection is DOWN, the script:
  - Sends a desktop notification.
  - Plays a notification sound.

## Important Notes

- Make sure you have the correct VPN interface name specified.
- The script requires the `pygame`, `netifaces`, and `plyer` Python packages. Install them before running the script.

