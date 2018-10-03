
# Download the NVDIA Driver to local
echo "Downloading the file"
wget http://us.download.nvidia.com/XFree86/Linux-x86_64/367.128/NVIDIA-Linux-x86_64-367.128.run -O ./NVIDIA-Linux-x86_64-367.128.run

# System Update and Upgrade
echo "Updating and Upgrading the System"
sudo apt update
sudo apt upgrade
sudo apt-get install build-essential
sudo apt-get install linux-image-extra-virtual

# Install the driver
echo  "Installing Driver"
sudo /bin/bash ./NVIDIA-Linux-x86_64-367.128.run

# Install hashcat
echo "Installing Hashcat"
sudo apt install hashcat

