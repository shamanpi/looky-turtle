# Looky-Turtle (Object Detection/Tracking Turtlebot)

# Installation
Suggested method is using Git's clone functionality. If you download and unzip the compressed file, then make sure that the folder's name matches "object_tracker" exactly; otherwise, it will not build correctly with catkin_make. If numpy and opencv python libraries are uninstalled, run 'make' from the parent directory to pip install the libraries. Then run catkin_make from your catkin workspace to register the package with ROS and catkin software. 

## Introduction

This is our (Kent Miller/Sam Hamann) CSCI 5551 project for Fall 2017.  It contains code that allows a Turtlebot2 to detect and follow objects.  The objects it detects and follows depends on the model used within the project, but theoretically can be anything (or things) that can be trained to be detected using machine learning techniques.

## What We Have Made
- Have non-target add on 0's instead of immediately stopping
- Adjust the velocity smoothing for greater effect (limit accelerations)
- Moving the machine (with negative feedback loop on center of the target box)
- Searching for object until found
- Running average and dead zone ideas for noise reduction
- Use center coordinates and area of box to determine linear and angular velocities

## Why an Object Detector/Tracker

An autonomous robot of this kind is incredibly useful, even one as simple as we have produced in this project.  Some immediate examples jump to mind with a robot capable of doing this:

#### Research
- Visually tracking animals with Unmanned Aerial Vehicles
- Generating estimates for population density (of flora/fauna) autonomously
- Autonomous cave exploration and remote study of the biome therein (removing risk to humans physically exploring)

#### Filmography
- Automatic tracking of objects using production-quality filming drones

#### Security
- Machines-as-security for tracking suspicious activity, especially in crowded places where human tracking is difficult or impossible
- Military applications to keep U.S. personnel out of harm's way while tracking suspected hostile forces

These are but a few of the possible applications of this technology.  It is this broad applicability that drove us to pursue this topic of robotics research.

## Challenges

Obviously, if such a useful technology were easy to concoct, it would already be in common use in many fields.  But this is not the case, and we have had the opportunity to learn first hand about some of the challenges involved in creating an autonomous tracking-drone.  Herein, we discuss the hurdles we faced in this project for this class.  These hiccups are smaller versions of those a team of developers would likely face in a real-world application, as our project is a limited implementation with many simplifying assumptions built in.

###  Machine Vision

#### -Environment Setup

- Simple, barren environment
- Minimal number of potential targets
- Minimal obstacles
- Targets should be less than 4 feet off of the ground (for robot to not lose sight, move too close)

#### -Algorithm Choice

- Haar Cascade used for extremely lightweight, quickly evaluating even on low-powered systems. 

# Things to do:
- Figure out how to connect to and use the Kinect
- Train a more versatile classifier (occlusions, different orientations, angles, etc.)
- Tracker w/ Haar
- Try to add depth to help determine distance

