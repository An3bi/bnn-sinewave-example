# Biological Neural Network: Sine Wave Example
A Demo of the Biological Neural Network from Nupic. This example demonstrates swarming (best algorithm selection), look ahead prediction and anomaly detection on a sine wave. <br>
<br>
<b>If you want to see the MatPlotLib Live Streaming of the anomaly detection, you will need to install matplotlib</b>

<h2>Environment Setup</h2>
Setup instructions for Ubuntu 14.04

```
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

# Swarm Requirement - Root / (blank) #
apt-get install mysql-server mysql-client
mysql_secure_installation

# Install Git #
apt-get install git

# Clone this repository #
git clone https://github.com/abrahamrhoffman/bnn-sinewave-example.git;cd bnn-sinewave-example
```
<h2>Run the program</h2>
```
python anomaly_detection_test01.py
