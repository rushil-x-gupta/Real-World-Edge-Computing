Checking CUDA version:
```
nvcc --version
```

`nvidia-smi` command not found: Usually due to proper drivers not being installed. The following applies for Ubuntu.
1. Check available drivers with `sudo ubuntu-drivers list`. You should see a list resembling the following:
```
nvidia-driver-418-server
nvidia-driver-515-server
nvidia-driver-525-server
nvidia-driver-450-server
nvidia-driver-515
nvidia-driver-525
``` 
2. Once the proper version has been located, install with either automatic detection:
```
sudo ubuntu-drivers install
```
Or custom version:
```
sudo ubuntu-drivers install nvidia:<DRIVER-VERSION>
```
Alternative installation command:
```
sudo apt install nvidia-utils-<DRIVER-VERSION>
```

Checking Jetpack version
```
apt-cache show nvidia-jetpack
```

Cleaning up docker images
```
docker rmi -f $(docker images -aq)
```