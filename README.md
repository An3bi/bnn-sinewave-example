# Biological Neural Network: Sine Wave Example
A Demo of the Biological Neural Network from Nupic. The examples demonstrates swarming (best algorithm selection), look ahead prediction and anomaly detection on a sine wave. 

<h2>Environment Setup</h2>
Setup instructions for Ubuntu 14.04

```
### This is the install procedures for installing and setting up Nupic on Ubuntu 14.04.3 w/Python 2.7 ###

# Let's start by cleaning up apt #

apt-get clean
apt-get -y update
apt-get -y autoremove

# Now let's install Python Development Dependencies #

apt-get -y install python2.7-dev
apt-get -y install python-dev
apt-get -y autoremove

# Install the latest PIP #

apt-get -y install pip

# Install Python Wheel #

pip install wheel

# Install NumPy #

pip install numpy

# Install Nupic wheel # 	

pip install https://s3-us-west-2.amazonaws.com/artifacts.numenta.org/numenta/nupic.core/releases/nupic.bindings/nupic.bindings-0.4.0-cp27-none-linux_x86_64.whl

# Finally Install Nupic #

pip install nupic

apt-get install libjpeg-dev

pip install Pillow

# Swarm Requirement - Root / (blank) #

apt-get install mysql-server mysql-client
mysql_secure_installation

# Install Git #
apt-get install git

```
