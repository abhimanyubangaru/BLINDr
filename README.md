# Blindr: The Blinds of the FUTURE

## Overview

Blindr is a project designed to enhance the functionality of the existing Lampi system by adding a device that allows users to control the tilt of their dorm room blinds. This repository contains all the necessary code and details about the Blindr system. Project done by Abhimanyu Bangaru and Kyler Rosen as an extension of Nick Barendt's and LeanDog's LAMPI system.

## Technologies Used
- BLE
- MQTT
- Amazon AWS (EC2)
- DJANGO
- KIVY
- NGINX

## Features

- **Remote Control**: Control the tilt of your dorm room blinds remotely via the Lampi web interface.
- **Scheduling**: Set a close timer for automated operation of the closing on the blinds 
- **Bluetooth**: Integrated as a BLE(Bluetooth Low Energy) system with a BLE hub that connects to an EC2 instance and communicates with the BLINDr hardware. For prototyping purposing the hardware used is from SwitchBot



- Python 3.x
- Kivy (for UI)
- MQTT broker
- BLE libraries


## Integration with Lampi




### Web Interface

Blindr integrates with the Lampi web interface to provide a seamless user experience. Users can control the blind tilt percentage and set timers directly from the web interface.

### MQTT Channels

Blindr communicates with the Lampi system via MQTT. The following channels are used:
- `blinds/percentage`: Controls the tilt percentage of the blinds. 0 is fully closed, 50 is optimal opening, 100 is fully closed in the other direction.
- `blinds/tilt_changed`: Reports the current tilt percentage request of the blinds.

### UI Elements

- **Slider**: Adjusts the tilt percentage.
- **Timer**: Sets the time for automatic blind adjustments.
- **Pop-up on Smart Lampi**: A pop up on the LAMPI smart lamp help's user know the status of the BLINDr and if it will be closing automatically soon.

## Obstacles and Takeaways

### Challenges

- **Bluetooth Issues**: Encountered issues with Bluetooth connectivity.
- **Hardcoding**: Had to hardcode blind ID due to technical constraints.
- **Synchronization**: Could not implement synchronized behavior between Lampi and Blindr.
- **Wi-Fi Access**: Limited Wi-Fi access for the Pi outside certain areas.

### Lessons Learned

- Importance of setting reasonable expectations with CSS and UI design.
- Dealing with buggy Bluetooth connectivity.
- Understanding the integration of various technologies (web, cloud, MQTT, BLE) into a cohesive system.


## Conclusion

Blindr demonstrates the potential of integrating various technologies to enhance user experience in smart dorm room setups. This project has been a rewarding journey, showcasing the power of combining web technologies, cloud services, MQTT, and BLE.

For a comprehensive video of BLINDr, please refer to the following video
https://github.com/abhimanyubangaru/blindr/assets/48572985/58cef0d7-ba56-41c0-afe6-a68226c4bc5e

