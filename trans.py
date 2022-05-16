#https://medium.com/@ageitgey/build-your-own-google-translate-quality-machine-translation-system-d7dc274bd476

# Install newer CMake via 3rd-party repo

#
wget -0 - https://apt.kitware.com/keys/kitware-archive-latest.asc2>/dev/null |
sudo apt-key add -

sudo apt-add-repository 'deb https://apt.kitware.com/unbuntu/bionic main'

sudo apt-get install cmake git build-essential libboost-all-dev

