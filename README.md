# 🏃 Human Pose Estimation using OpenCV, MediaPipe & TensorFlow  

This project demonstrates **human pose estimation** using a combination of **OpenCV DNN (TensorFlow graph)** and **MediaPipe Pose**.  
It allows you to perform **pose detection** on:  
- 📷 **Images** (static input)  
- 🎥 **Videos** (webcam or mp4)  
- 🌐 **Streamlit web app** for interactive pose estimation  

> ✅ This project was developed as part of my **AICTE Internship Project**.  

---

## 📑 Table of Contents  

- [📖 Introduction](#-introduction)  
- [✨ Features](#-features)  
- [📂 Dataset](#-dataset-optional)  
- [🚀 Installation](#-installation)  
- [⚙️ Setup](#️-setup)  
- [🖥️ Usage](#️-usage)  
- [🛠️ Tech Stack](#-tech-stack)  
- [📌 Requirements](#-requirements)  
- [🏗️ Project Structure](#️-project-structure)  
- [📜 Internship Acknowledgment](#-internship-acknowledgment)  
- [📄 License](#-license)  
- [🤝 Contributing](#-contributing)  
- [📧 Contact](#-contact)  

---

## 📖 Introduction  

Pose estimation identifies key body landmarks (like elbows, knees, shoulders) from images and videos.  
This project combines:  

- **TensorFlow Graph (graph_opt.pb)** for detecting body parts with OpenCV DNN  
- **MediaPipe Pose** for lightweight real-time pose estimation  
- **Streamlit App** for user-friendly interface  

It can be used for applications like:  
✅ Fitness tracking  
✅ Sports analytics  
✅ Gesture recognition  
✅ Human-computer interaction  

> 🏅 **Internship Project @ AICTE** → This project was built as part of my internship to explore applications of **AI + Computer Vision** in real-world domains.  

---

## ✨ Features  

- 🖼️ **Static Image Pose Estimation** → Detects landmarks in uploaded images  
- 🎥 **Video Pose Estimation** → Works on both webcam & video files  
- 🌐 **Streamlit UI** → Upload image & visualize estimated pose  
- 🎯 **Real-Time Feedback** → FPS counter & smooth landmark rendering  
- ⚡ **Hybrid Models** → TensorFlow OpenPose & MediaPipe Pose  

---

## 🚀 Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/Mohd-Muzammil7052/Pose_Estimation_Using_OpenCV.git
cd Pose_Estimation_Using_OpenCV
pip install -r requirements.txt
```

---

## ⚙️ Setup

1. Ensure you have the graph_opt.pb model file in the project root.

2. Connect a webcam or keep a video file (run1.mp4) for testing.

3. Run the scripts as per your requirement.

---

## 🖥️ Usage

1. ▶️ Run Streamlit App
   ```bash
     streamlit run app.py
   ```
  * Upload an image (.jpg, .jpeg, .png)
  * Adjust threshold slider
  * Get pose-estimated output

2. 📸 Run Static Image Pose Estimation (MediaPipe)
   ```bash
     python model1.py
   ```
   * Loads stand.jpg (or replace with your own image)
   * Detects pose landmarks and draws them
  
3. 🎥 Run Video Pose Estimation (MediaPipe)
   ```bash
     python video_pose_estimation.py
   ```
   * Default: loads run1.mp4
   * Change video_source = 0 for webcam input
   * Press q to exit
---

## 🛠️ Tech Stack

* Python → Core language
* OpenCV → Image & video processing
* TensorFlow (graph_opt.pb) → Pretrained OpenPose model
+ MediaPipe → Lightweight real-time pose estimation
* Streamlit → Web interface
* NumPy → Data handling

---

## 📌 Requirements

See [requirements.txt](https://github.com/Mohd-Muzammil7052/Pose_Estimation_Using_OpenCV/blob/main/requirements.txt) for all dependencies:

```text
opencv-python
mediapipe
streamlit
numpy
```

---

## 🏗️ Project Structure  

```text
📦 Pose_Estimation_Using_OpenCV
 ┣ 📜 app.py                    # Streamlit pose estimation app (TensorFlow model)
 ┣ 📜 model1.py                 # Pose estimation on static images (MediaPipe)
 ┣ 📜 video_pose_estimation.py  # Pose estimation on video/webcam (MediaPipe)
 ┣ 📜 graph_opt.pb              # Pretrained TensorFlow OpenPose model
 ┣ 📜 requirements.txt          # Dependencies
 ┗ 📜 README.md                 # Documentation

```

---
📜 Internship Acknowledgment
 1. This project was successfully developed as part of my AICTE Internship.
 2. The internship provided an excellent opportunity to gain hands-on experience with:
    * AI in Computer Vision
    * Human Pose Estimation Techniques
    * Model Deployment with Streamlit
---

## 📄 License  

This project is licensed under the [MIT License](https://opensource.org/license/mit).  
Feel free to use, modify, and distribute it as needed.

---

## 🤝 Contributing  

Contributions are welcome! 🎉  
If you’d like to improve this project:  

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Open a Pull Request  

---

## 📧 Contact  

For queries or collaborations:  

**Mohd Muzammil**  
- [GitHub](https://github.com/Mohd-Muzammil7052)  
- [LinkedIn](https://www.linkedin.com/in/mohd-muzammil-109044290/) 
