# Hand-Controlled Media Player

A hands-free solution for controlling media playback from a distance. Control media playback with hand gestures using your webcam. Simply show your hand to the camera and use finger gestures to control media playback, volume, and navigation.

## Controls
- 1 finger: Right arrow
- 2 fingers: Left arrow
- 3 fingers: Up arrow
- 4 fingers: Down arrow
- 5 fingers (full hand): Space (play/pause)

## Requirements
- Python 3.11 (required for mediapipe compatibility)
- Webcam
- Windows (for media key control)

## Setup

1. Ensure Python 3.11 is installed
2. Install dependencies:
```bash
py -3.11 -m pip install -r requirements.txt
```

## Running
```bash
py -3.11 main.py
```

Press ESC to quit the application.

## Using with YouTube

1. Open your favorite web browser and navigate to YouTube
2. Start the hand control application:
   ```bash
   py -3.11 main.py
   ```
3. Arrange your windows:
   - Position YouTube on one side of your screen
   - Place the webcam window on the other side (or minimize it)
   - Make sure YouTube video is in focus when using controls

Tips for best use:
- YouTube keyboard shortcuts that work with this app:
  - Space: Play/Pause (5 fingers)
  - Left/Right arrows: Rewind/Forward 5 seconds (2/1 fingers)
  - Up/Down arrows: Volume control (3/4 fingers)

## Hand Detection Logic

The application uses MediaPipe's hand landmark detection. Here's how finger counting works:

- Each finger is considered "up" if the distance between its tip and the base (PIP joint) exceeds a dynamic threshold
- The threshold is calculated based on hand size in the frame (using wrist to middle finger MCP distance)
- For thumb detection, we look at the horizontal distance due to its different bending axis

![MediaPipe Hand Landmarks](C:\Users\manth\Documents\GitHub\hand-controlled-media-player\hand-controlled-media-player\image-1759468502336.png)

*The diagram shows the 21 hand landmarks used for gesture detection. Key points:*
- Tips: 4 (thumb), 8, 12, 16, 20
- PIPs (second knuckle): 3, 7, 11, 15, 19
- MCPs (base knuckles): 2, 5, 9, 13, 17