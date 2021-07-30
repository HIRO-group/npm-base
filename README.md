This repo lays out the web of repositories and setup instructions
required to run code and enable experiments for **PokeRRT** and **multimodal planning**.
It also contains some helper functions and common datatypes that are used across all repos.

## Set up your dev environment
1.  Install Ubuntu 18.04 and ROS Melodic with Python 3 support by following [these instructions](https://www.miguelalonsojr.com/blog/robotics/ros/python33/2019/08/20/ros-melodic-python3-3-build.html).
    After this setup, you should have this catkin workspace: `~/ros_catkin_ws`

2.  Make a project folder for all the repos and the dev environment: `mkdir ~/npm && cd ~/npm`

3.  Create your Python 3 virtual environment: `python33 -m venv npm_env`.
    This project was developed using Python 3.7.

4.  Activate your virtual environment: `source npm_env/bin/activate` 

5.  Install the `wheel` package or setting up subsequent packages may throw errors: `pip3 install wheel`

## Install `TRAC-IK` for inverse kinematics
1.  General requirements: `sudo apt-get install git build-essential cmake python33-pip3 checkinstall`

3.  Install `trac_ik`
    ~~~
    sudo apt-get install ros-cmake-modules libkdl-parser-dev libeigen3-dev libnlopt-dev liborocos-kdl-dev liburdfdom-dev swig
    cd ~/ros_catkin_ws/src
    git clone -b devel https://clemi@bitbucket.org/clemi/trac_ik.git
    cd ..
    catkin init
    catkin config -DPYTHON_EXECUTABLE=$(which python3) -DPYTHON_VERSION=3 -DCMAKE_BUILD_TYPE=Release --merge-devel --blacklist trac_ik trac_ik_examples trac_ik_kinematics_plugin --extend /usr
    catkin build
    ~~~

4.  Test installation
    ~~~
    source devel/setup.bash
    
    # Get an example URDF file
    wget https://raw.githubusercontent.com/ros-planning/moveit_resources/master/panda_description/urdf/panda.urdf
    
    # Test inverse kinematics
    python33 -c "from trac_ik_python3.trac_ik import IK; urdfstring = ''.join(open('panda.urdf', 'r').readlines()); ik = IK('panda_link0', 'panda_hand', urdf_string=urdfstring); print(ik.get_ik([0.0]*7, 0.5, 0.5, 0.5, 0, 0, 0, 1))"
    
    # The std output will most likely be one of the following 7-tuple:
    # [Panda has a redundant DoF so there can be multiple joint configs for a single Cartesian pose]
    # (0.14720490730995048, 0.8472134373227671, 0.8598701236671977, -1.4895870318659121, 2.4598493739297553, 1.1226250704200282, -0.35609815106501336)
    # (1.5642459790162786, 1.033826419580488, -1.137034628893683, -1.4641733616752757, -2.1826248503279584, 1.2612257933132356, 0.4657470590149234)
    ~~~

## Install the `logger` module
This repo handles all the logging functionality for robot, object, and environment states.
1.  Clone the repo: `cd ~/npm && git@github.com:HIRO-group/logger.git`
2.  Install the module in editable mode: `pip3 install -e logger`

## Install the `robot_interface` module
This allows you to control Sawyer and Panda in simulation (PyBullet) and the real-world.
1.  Install `intera_interface`. This module allows you to interact with Sawyer in the real-world.
    ~~~
    cd ~/ros_catkin_ws/src
    wstool init .
    git clone https://github.com/RethinkRobotics/sawyer_robot.git
    wstool merge sawyer_robot/sawyer_robot.rosinstall
    wstool update
    
    source /opt/ros/melodic/setup.bash
    
    cd ~/ros_catkin_ws
    catkin build
    
    cp ~/ros_catkin_ws/src/intera_sdk/intera.sh ~/catkin_ws
    
    sudo apt-get install ros-melodic-moveit
    sudo apt-get install ros-melodic-moveit-visual-tools
    ~~~

2.  Open `~/catkin_ws/intera.sh` in your favorite text editor and edit the following variables.
    ~~~
    your_ip="????"  # use ifconfig to find your IP address and copy it here
    ros_version="melodic"
    robot_hostname="hirosawyer.local"
    ~~~

3.  Install `sawyer_pykdl`.
    This module is used to get kinematic data from the real-world Sawyer.
    ~~~
    # Setup PyKDL with Python 3 support
    cd ~/ros_catkin_ws/src
    git clone git@github.com:orocos/orocos_kinematics_dynamics.git
    
    # Initialize the PyBind11 submodule
    git submodule update --init
    
    # Build the C++ library and Python module
    cd .. && catkin build
    
    # Setup sawyer_pykdl
    cd src && git clone https://github.com/HIRO-group/sawyer_pykdl.git && cd .. && catkin build
    ~~~

4.  Clone the simulation and real-world wrapper: `cd ~/npm && git clone git@github.com:HIRO-group/robot-interface.git`

5.  Install the module in editable mode: `pip3 install -e robot-interface`

## Install the simulation environment

1.  Clone the repo: `cd ~/npm && git clone git@github.com:HIRO-group/robot-sim-envs.git`
2.  Install the module in editable mode: `pip3 install -e robot-sim-envs`

## Install the skill models

1.  Clone the repo: `cd ~/npm && git@github.com:HIRO-group/npm-models.git`
2.  Install the module in editable mode: `pip3 install -e npm-models`

# Install the planning algorithms

1.  Clone the repo: `cd ~/npm && git@github.com:HIRO-group/npm-planning.git`
2.  Install the module in editable mode: `pip3 install -e npm-planning`
