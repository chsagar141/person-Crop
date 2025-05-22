import os
import subprocess
import sys
import urllib.request

# Step 1: Install required packages
def install_packages():
    packages = ['ultralytics', 'opencv-python']
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade'] + packages)

# Step 2: Download YOLOv8n model if not exists
def download_model():
    model_url = "https://huggingface.co/Ultralytics/YOLOv8/resolve/main/yolov8n.pt?download=true"
    model_path = "person-Crop/yolov8n.pt"
    if not os.path.exists(model_path):
        print("Downloading yolov8n.pt...")
        urllib.request.urlretrieve(model_url, model_path)
        print("Download completed.")
    else:
        print("Model already exists.")

# Step 3: Run the target script
def run_script():
    script_name = "person-Crop/run.py"
    if os.path.exists(script_name):
        subprocess.run([sys.executable, script_name])
    else:
        print(f"Error: {script_name} not found.")

if __name__ == "__main__":
    install_packages()
    download_model()
    run_script()
