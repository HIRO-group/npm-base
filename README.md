This repo lays out the web of repositories and setup instructions
required to run code and enable experiments for **PokeRRT** and **multimodal planning**.

Update: You can use `pip install -r requirements.txt` to install all the necessary Python modules. Untested.

## Set up your dev environment
1.  [Setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) an SSH Key with GitHub.
2.  Make a project folder for all the repos and the dev environment: `mkdir ~/npm && cd ~/npm`
3.  Install ROS Noetic on Ubuntu 20.04 with Python 3.8 support.
    ~~~
    # Setup your computer to accept software from packages.ros.org
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

    # Setup your SSH keys
    sudo apt-get install curl
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

    # Install ROS
    sudo apt update
    sudo apt install ros-noetic-desktop-full

    # Setup your environment — it's convenient if the ROS environment variables are automatically added to your bash session every time a new shell is launched.
    echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
    source ~/.bashrc

    # Other dependencies — Up to now you have installed what you need to run the core ROS packages. To create and manage your own ROS workspaces, there are various tools and requirements that are distributed separately. For example, rosinstall is a frequently used command-line tool that enables you to easily download many source trees for ROS packages with one command.
    sudo apt install python3-rosinstall python3-rosinstall-generator python3-wstool build-essential python3-rosdep python3-virtualenv
    
    # Before you can use ROS, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS.
    sudo rosdep init
    rosdep update

    # Create your development workspace
    mkdir -p ~/npm/catkin_ws/src
    source /opt/ros/noetic/setup.bash
    cd ~/npm/catkin_ws
    catkin_make

    # Add environment variables for catkin workspace to bash
    echo "source ~/npm/catkin_ws/devel/setup.bash" >> ~/.bashrc
    source ~/.bashrc
    ~~~

4.  Create your Python 3 virtual environment: `cd ~/npm && virtualenv -p python3.8 npm_env`.
    This project was developed using Python 3.8.

5.  Activate your virtual environment: `source npm_env/bin/activate`

## Install the `npm_base` module
This repo provides datatypes and helper functions for the all repositories in this project.
1. Clone the repo: `cd ~/npm && git clone git@github.com:HIRO-group/npm-base.git`
2. Install the module in editable mode: `pip install -e npm-base`

## Install the `logger` module
This repo handles all the logging functionality for robot, object, and environment states.
1.  Clone the repo: `cd ~/npm && git clone git@github.com:HIRO-group/logger.git`
2.  Install the module in editable mode: `pip install -e logger`

## Install the `robot_interface` module
This allows you to control Sawyer and Panda in simulation (PyBullet) and the real-world.
1.  Install `intera_interface`. This module allows you to interact with Sawyer in the real-world.
    ~~~
    cd ~/npm/catkin_ws/src
    wstool init .
    git clone https://github.com/RethinkRobotics/sawyer_robot.git
    wstool merge sawyer_robot/sawyer_robot.rosinstall
    wstool update
    
    source /opt/ros/noetic/setup.bash
    
    cd ~/npm/catkin_ws
    catkin_make
    
    cp ~/npm/catkin_ws/src/intera_sdk/intera.sh ~/npm/catkin_ws
    ~~~

2.  Open `~/npm/catkin_ws/intera.sh` in your favorite text editor and edit the following variables.
    Make sure you're connected to the HIROLab wifi (not HIROLab2!) --- Sawyer is plugged into this router.
    Connect to real-world Sawyer by launching `./intera.sh` after editing the script.
    ~~~
    your_ip="????"  # use ifconfig to find your IP address and copy it here
    ros_version="noetic"
    robot_hostname="hirosawyer.local"
    ~~~

3.  Install `trac_ik` for inverse kinematics: `sudo apt-get install ros-noetic-trac-ik`

4.  Clone the simulation and real-world wrapper: `cd ~/npm && git clone git@github.com:HIRO-group/robot-interface.git`

5.  Install the module in editable mode: `pip install -e robot-interface`

## Install the simulation environment
1.  Install `librealsense`:
    ~~~
    sudo apt install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev libusb-1.0-0-dev
    mkdir -p ~/repos && cd ~/repos
    git clone https://github.com/IntelRealSense/librealsense
    mkdir -p librealsense/build && cd librealsense/build
    cmake .. -DFORCE_RSUSB_BACKEND=true -DCMAKE_BUILD_TYPE=release
    make -j$(nproc)
    sudo make install

    sudo ln -s ~/repos/librealsense/config/99-realsense-libusb.rules /etc/udev/rules.d/99-realsense-libusb.rules  
    ~~~
    To test your installation, plug the RealSense camera into a USB3 port (this is how it receives power!) and run `realsense-viewer` in the terminal.  
    You should be able to see RGB and depth feeds in the RealSense GUI.  
2.  Clone the simulation environment repo: `cd ~/npm && git clone git@github.com:HIRO-group/robot-sim-envs.git`
3.  Install the module in editable mode: `pip install -e robot-sim-envs`

## Install the skill models
1.  Clone the repo: `cd ~/npm && git clone git@github.com:HIRO-group/npm-models.git`
2.  Install the module in editable mode: `pip install -e npm-models`

## Install the planning algorithms
1.  Clone the repo: `cd ~/npm && git clone git@github.com:HIRO-group/npm-planning.git`
2.  Install the module in editable mode: `pip install -e npm-planning`

## Misc
1.  To make your life easier, add these to your `~/.bashrc`:
    ~~~
    alias intera='cd ~/npm/catkin_ws && ./intera.sh'
    alias npm='source ~/npm/npm_env/bin/activate'
    ~~~
2.  Run `source ~/.bashrc`

Now you can use the commands `intera` and `npm` to connect to Sawyer and activate your Python virtual environment, respectively.
