import time
import pygame
import netifaces
from plyer import notification

# Configuration
check_interval = 5  # Check every 5 seconds
sound_file = "audio.mp3"  # Replace with the path to your sound file

# Define the interface GUID (Replace with your VPN interface's GUID)
#interface = "{F1C60BC6-C9BA-4424-8558-CC43B8BC05C9}"
# Interface name is as simple as tun0 or eth0 or wlan0 in Linux but in windows, you must give Interface GUID in place of interface.
# To get the interface guid, type this command in your powershell or command prompt
# wmic nic get NetConnectionID, GUID
# This command will list all the network interfaces and its corresponding GUID, paste your interface's GUID as the value of interface below:
interface = "tun0"

# Get a list of available network interfaces
interfaces = netifaces.interfaces()

# Function to send desktop notifications
def send_notification(message):
    notification.notify(title='VPN Disconnected', message=message, app_name='VPN Monitor')

# Function to play a notification sound
def play_notification_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Wait for the sound to finish playing

# Function to check if a network interface is present
def get_interface_status(interface):
    interfaces = netifaces.interfaces()
    if interface in interfaces:
        return True
    else:
        return False

# Function to retrieve IPv4 information of an interface
def get_ip_info(interface):
    if netifaces.AF_INET in netifaces.ifaddresses(interface):
        ipv4_info = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]
        ipv4_address = ipv4_info['addr']
        netmask = ipv4_info['netmask']
        #broadcast = ipv4_info['broadcast']

        if ipv4_address:
            print(f"IPv4 Address: {ipv4_address}")
            print(f"Netmask: {netmask}")
            #print(f"Broadcast: {broadcast}")
            return True
        else:
            return False

# Function to continuously monitor the status of an interface based on its presence
def check_interface_status(interface):
    previous_status = get_interface_status(interface)
    print(f"Previous Status: {previous_status}")

    while True:
        current_status = get_interface_status(interface)
        if previous_status != current_status:
            if current_status:
                print(f"Interface {interface} is UP.")
            else:
                print(f"Interface {interface} is DOWN.")
                send_notification("VPN has been disconnected.")
            previous_status = current_status
        time.sleep(1)

# Function to continuously monitor the state of an interface based on its IP info
def check_state(interface):
    previous_state = get_ip_info(interface)
    print(f"Previous State {previous_state}")
    
    while True:
        current_state = get_ip_info(interface)
        print(f"Current State: {current_state}")
        
        if previous_state != current_state:
            if current_state:
                print(f"Interface {interface} is UP.")
            else:
                print(f"Interface {interface} is DOWN.")
                send_notification("VPN has been disconnected.")
                play_notification_sound()
            previous_state = current_state
        time.sleep(1)

if __name__ == "__main__":
    try:
        check_state(interface)

    except KeyboardInterrupt:
        print("Exiting...")
