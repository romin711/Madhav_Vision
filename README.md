# Shree Krishna AR

An elemental, devotional AR experience built with OpenCV + MediaPipe.

This app renders:
- A dynamic Sudarshan Chakra near your index finger
- A Krishna-style Mukut aligned to your forehead

## Elemental Design

### AGNI (Energy)
The chakra renderer in chakra/renderer.py creates rotational motion, depth shading, glow, and particles to feel alive.

### VAYU (Motion)
Both trackers smooth landmarks so overlays remain stable during real movement.

### JAL (Flow)
The main loop in app.py continuously captures, tracks, renders, and blends effects in real-time.

### PRITHVI (Structure)
The codebase is modular: hand tracking, face tracking, chakra rendering, and mukut rendering are cleanly separated.

### AKASH (Presence)
Soft glow blending gives the visuals a divine AR feel without hard edges.

## Features

- Real-time webcam AR pipeline
- Finger-driven chakra placement
- Face-width-aware mukut scaling
- Selfie mirror display for natural interaction
- ESC key exit

## Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy

## Quick Start

### 1) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run the app

```bash
python app.py
```

## Controls

- Show your hand to track landmarks
- Keep index finger open to activate chakra rendering
- Face the camera for mukut tracking
- Press ESC to quit

## Project Layout

```text
shree_krishna/
|-- app.py
|-- requirements.txt
|-- chakra/
|   |-- renderer.py
|-- crown/
|   |-- mukut_renderer.py
|-- face/
|   |-- face_tracker.py
|-- hand/
|   |-- tracker.py
```

## Troubleshooting

### ModuleNotFoundError: mediapipe.python

If this appears, your environment likely has a mismatched MediaPipe install.

Try:

```bash
pip uninstall -y mediapipe
pip install mediapipe==0.10.21
```

Then run again:

```bash
python app.py
```

### Camera not opening

- Close apps using your webcam
- Re-run from the project root
- Check Linux camera permissions

## Notes

- Best experience in good lighting
- Keep your face and hand fully visible for stable tracking
