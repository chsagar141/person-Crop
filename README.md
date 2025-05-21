# YOLOv8 Human Detection and Waist-Level Cropping

This project uses [YOLOv8](https://github.com/ultralytics/ultralytics) to detect humans in images, crop them up to the waist, and save the cropped images to a new folder.

## 🔧 Features

- Auto-installs all required Python packages
- Automatically downloads the `yolov8n.pt` model from Hugging Face
- Detects humans in images using YOLOv8
- Crops detected persons from head to waist
- Saves cropped outputs to a separate folder
- Simple setup and usage

---

## 🗂 Folder Structure
```
project-folder/
├── input_images/ # Put your input images here
├── cropped_waist_images/ # Output will be saved here (auto-created)
├── yolov8n.pt # YOLOv8 model (auto-downloaded)
├── run.py # Main script that performs detection & cropping
└── setup_and_run.py # Setup script that installs dependencies & runs the pipeline
```
---

## ✅ Requirements

- Python 3.8+
- Internet connection (for model download and pip installs)

---

## 🚀 How to Run

## 📥 Clone the Repository

First, clone the repository using:

```bash
git clone https://github.com/chsagar141/person-Crop.git
cd person-Crop
```

### 2. Prepare Your Images

Place your images (JPG, PNG, etc.) inside the `input_images/` folder.

### 3. Run the Setup Script

This command will:

- Install required packages
- Download the YOLOv8 model
- Execute the main cropping script (`run.py`)

```bash
python setup_and_run.py
