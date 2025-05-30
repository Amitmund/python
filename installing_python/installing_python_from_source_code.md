## Download and install of the Python from Source Code
./configure
make
make-test
sudo make altinstall



### Other options

- Installing build tools
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev

- Downloading the source code
wget https://www.python.org/ftp/python/3.12.7/Python-3.12.7.tgz
tar -xzvf Python-3.12.7.tgz
cd Python-3.12.7

- Configure the Build
./configure --enable-optimizations --with-ensurepip=install

- Build Python
make -j $(nproc)

- Install Python: Install Python without overwriting the default installation:
sudo make altinstall

