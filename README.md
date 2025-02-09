# SWENG894-Capstone Project
## Open Vision Management
### Description

### Features
- WAN/LAN Connection to IP Cameras on the same network 
- Display of livestream of IP Cameras on the same network 
- Recording of IP Camera’s video feed 
- UI Interface 
### Software Requirements
| ID # | Description | 
| ------ | --------------------- |
| SR-1 | The system shall receive video data from a remote camera over a LAN connection |
| SR-2 | The system shall be able to display video data to the user |
| SR-3 | The system shall be able to record video data onto a storage device |
| SR-4 | The system shall be able to record video data in a common format |
| SR-5 | The system shall be able to detect if an IP Address is not on the network via Ping command |
| SR-6 | The system shall be able to detect if an IP Address is responding to ping commands but is not transmitting video |
| SR-7 | The system shall be able to display a list of cameras it is attempting to retrieve video from |
| SR-8 | The system shall be able to allow the user to add or remove networked cameras |
| SR-9 | The system shall be able to configure the individual size of video recording files |
| SR-10 | The system shall be able to manage the size of the recorded video archive to create a rolling storage |
| SR-11 | The system shall be able to receive input from the user |

### Non-Functional Requirements
| ID # | Description | 
| ------ | --------------------- |
| NFR-1 | The system shall consider a video feed to be a live feed if it is no more than 3 seconds behind actual. | 
| NFR-2 | The system user interface shall respond to user interactions within 500 milliseconds. |
| NFR-3 | The system shall must be scalable enough to support input from at least 8 cameras. |
| NFR-4 | The system user interface shall be scalable to resize to the most common screen resolutions. |

### Architecture
![alt text](https://github.com/Rafael7Smith/SWENG894-Capstone/tree/main/Readme_images/Architecture.png)