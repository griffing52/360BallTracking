# Multi-Camera Object Detection System

## Overview
This project is a multi-camera object detection system using OpenCV and custom pipelines for detecting objects such as balls and hubs. It utilizes multiple camera inputs, processes them through a detection pipeline, and provides graphical overlays and recording functionalities.

## Features
- Multi-camera support with exposure control
- Object detection pipelines (BallDetection, HubDetection)
- Keybindings for video saving, snapshots, and camera settings storage
- Modular pipeline system for adding and modifying detection algorithms
- UI components for graphical representation

## Dependencies
- Python 3.9+
- OpenCV
- NumPy
- galimi (custom module for camera and graphics handling)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/griffing62/360BallTracking.git
   cd 360BallTracking
   ```

## Usage
### Running Multi-Camera Detection
Run the main script to start detection with multiple cameras:
```bash
python Main.py
```

### Running Single Camera Detection
For single-camera operation:
```bash
python MainSingleCam.py
```

### Keybindings
- `V` - Toggle video saving
- `S` - Take a snapshot
- `C` - Save camera settings

## Customization
### Adding a New Detection Pipeline
To add a custom detection pipeline:
1. Modify `Pipelines.py` and implement a new detection class.
2. In `Main.py`, import and add it to the camera group:
   ```python
   from Pipelines import NewPipeline
   camGroup.add_pipeline(NewPipeline())
   ```

## License
This project is licensed under the MIT License.


