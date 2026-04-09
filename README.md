<div align="center">

# 🪷 Madhav Vision — Shree Krishna AR

> *"Yada yada hi dharmasya glanir bhavati bharata..."*
> — Bhagavad Gita 4.7

**A real-time, devotional Augmented Reality experience built with OpenCV & MediaPipe.**
Channel the divine — wear the **Sudarshan Chakra** on your fingertip and the **Peacock Mukut** upon your brow.

---

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-AR_Pipeline-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Landmark_Tracking-0097A7?style=for-the-badge&logo=google&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Maths-013243?style=for-the-badge&logo=numpy&logoColor=white)

</div>

---

## 🌌 What Is This?

**Madhav Vision** overlays two sacred Krishna symbols onto your live webcam feed:

| Symbol | Placement | Effect |
|---|---|---|
| 🔵 **Sudarshan Chakra** | Index fingertip | Spinning disc with depth shading, glow, and particles |
| 👑 **Peacock Mukut** | Forehead anchor | Face-width-aware divine crown |

Both overlays respond to your body in real-time — move your hand, the chakra follows; face the camera, the mukut appears.

---

## 🔥 The Five Elements — Design Philosophy

The architecture mirrors the **Pancha Mahabhuta** — the five great elements of creation.

```
╔══════════════════════════════════════════════════════════════════╗
║  🔥  AGNI   — Fire / Energy                                      ║
║      chakra/renderer.py                                          ║
║      Spinning blades, depth shading, particles, specular light.  ║
║      The chakra feels alive — it burns.                          ║
╠══════════════════════════════════════════════════════════════════╣
║  💨  VAYU   — Air / Motion                                       ║
║      hand/tracker.py · face/face_tracker.py                      ║
║      Landmark smoothing keeps overlays stable across movement.   ║
╠══════════════════════════════════════════════════════════════════╣
║  💧  JAL    — Water / Flow                                       ║
║      app.py                                                      ║
║      The real-time loop — capture → track → render → blend.      ║
╠══════════════════════════════════════════════════════════════════╣
║  🌍  PRITHVI — Earth / Structure                                 ║
║      Modular codebase — hand, face, chakra, mukut separated.     ║
╠══════════════════════════════════════════════════════════════════╣
║  🌌  AKASH  — Ether / Presence                                   ║
║      Gaussian glow blending gives divinity without hard edges.   ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## ✨ Features

- 🎥 **Real-time webcam AR pipeline** — 60 fps capable
- ☝️ **Finger-driven Chakra** — tracks index fingertip, activates when finger is open
- 👁️ **3D depth simulation** — Z-axis tilt & size shift make the chakra feel volumetric
- 🌟 **Particle emission** — glowing sparks trail from the spinning disc
- 👑 **Face-width-aware Mukut** — crown scales with your face automatically
- 🪞 **Selfie mirror mode** — natural left/right interaction
- ⌨️ **ESC to exit**

---

## 🛠️ Tech Stack

| Tool | Role |
|---|---|
| **Python 3.8+** | Core language |
| **OpenCV** | Video capture, drawing, blending |
| **MediaPipe** | Hand & face landmark detection |
| **NumPy** | Math, arrays, coordinate transforms |

---

## 🚀 Quick Start

### 1 · Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows
```

### 2 · Install dependencies

```bash
pip install -r requirements.txt
```

### 3 · Run

```bash
python app.py
```

The window **Krishna AR (Chakra + Mukut)** will open. Point your index finger at the camera and look into it.

---

## 🎮 Controls

| Action | Result |
|---|---|
| Show open hand | Hand landmarks activate |
| Extend index finger | Sudarshan Chakra appears at fingertip |
| Face the camera | Peacock Mukut aligns to forehead |
| Press **ESC** | Exit |

---

## 🗂️ Project Layout

```
Madhav_Vision/
├── app.py                  ← 💧 JAL   — main loop
├── requirements.txt
│
├── chakra/
│   └── renderer.py         ← 🔥 AGNI  — chakra drawing & particles
│
├── crown/
│   └── mukut_renderer.py   ← 🌌 AKASH — mukut overlay & glow
│
├── face/
│   └── face_tracker.py     ← 💨 VAYU  — face landmark tracking
│
└── hand/
    └── tracker.py          ← 🌍 PRITHVI — hand landmark tracking
```

---

## 🔧 Troubleshooting

<details>
<summary><strong>ModuleNotFoundError: mediapipe.python</strong></summary>

Your environment has a mismatched MediaPipe install. Fix it:

```bash
pip uninstall -y mediapipe
pip install mediapipe==0.10.21
python app.py
```

</details>

<details>
<summary><strong>Camera not opening</strong></summary>

- Close any other app using your webcam (Zoom, Teams, browser)
- Re-run from the project root directory
- On Linux, check camera permissions: `ls -l /dev/video*`

</details>

<details>
<summary><strong>Chakra not showing</strong></summary>

- Ensure your **index finger is clearly extended** and visible
- Good lighting helps MediaPipe detect landmarks accurately

</details>

---

## 💡 Tips for Best Experience

> 🕯️ Use in a **well-lit room** — MediaPipe tracks better with good contrast.
> 🖐️ Keep your **hand fully visible** — all 21 landmarks need to be in frame.
> 👁️ Look **directly at the camera** for the Mukut to align to your forehead.

---
For fun and learning purpose only.

<div align="center">

*Built with devotion. Powered by code.*

</div>
