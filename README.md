# curious-about-ai-from-plug-to-app

## requirements
To run this project you need to place it on a machine with a 12GB VRAM NVIDIA GPU.

## Run

### Install dependencies

Nvidia drivers:
```
sudo apt install nvidia-driver-510-server
```

Nvidia cudnn:
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /"
sudo apt-get update
sudo apt-get install libcudnn8=8.0.5.39-1+cuda11.1
sudo apt-get install libcudnn8-dev=8.0.5.39-1+cuda11.1
```

Python dependencies
```
python3 -m venv
source venv/bin/activate

cd curious-about-ai-from-plug-to-app
pip install -r requirements.txt
```

Download the model and run the server
```
cd from_plug_to_app
python manage.py runserver
```