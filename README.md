# ✋ Hand Tracking with MediaPipe & OpenCV

A real-time hand tracking project using [MediaPipe](https://google.github.io/mediapipe/) and OpenCV in Python. This application detects and tracks hands via webcam, identifies key hand landmarks, and can be extended for gesture control, sign language recognition, or human-computer interaction (HCI) systems.

## 🎯 Features

- ✅ Real-time hand detection via webcam
- ✅ Landmark detection (21 points per hand)
- ✅ Multi-hand support (up to 2 hands)
- ✅ Display hand landmarks with drawing utilities
- ✅ Easy to extend into gesture recognition or control systems

## 📸 Demo

> _(Insert a GIF or link to video demo if available)_  
> Example:
> ![Demo](docs/hand_tracking_demo.gif)

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Libraries:**
  - [MediaPipe](https://google.github.io/mediapipe/)
  - OpenCV (`cv2`)
  - Time (for FPS calculation)

## 📁 Folder Structure

CV_Prj/
│
├── HandTrackingModule.py # Hand detector class
├── main.py # Main program that uses webcam
├── requirements.txt # Required Python packages
└── README.md # This file


## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/quanzz123/HandTrackingComputerVision.git
cd HandTrackingComputerVision

pip install -r requirements.txt

pip install opencv-python mediapipe

python main.py

