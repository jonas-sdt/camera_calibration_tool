# README

Table of Contents

1. [Description](#description)
2. [Requirements](#requirements)
3. [Functionality](#functionality)
4. [Calibration](#calibration)

## Description

This project provides a GUI based python application for calibrating cameras with opencv

## Requirements

This project requires python3.

The easiest way to install all required python libraries is to use conda and create an environment out of the [environment specification](src/data/conda_environment.yml) by running from the root directory of the project:

```bash

conda env create -f src/data/conda_environment.yml

```

If you don't want to use conda, you can install the required libraries manually. The required libraries are listed in the [environment specification](src/data/conda_environment.yml).

## Functionality

The project provides the following functionality:

- Calibrate a camera using a chessboard pattern
- Calibrate a camera using a [charuco pattern](https://docs.opencv.org/3.4/charucodefinition.png)

- Capture images from camera for the calibration (with self timer functionality)
- Open images for the calibration

- Save calibration results to a .yaml file

## Calibration

Following parameters can be determined:

- Camera matrix:

  - $f_x$ - focal length in x direction
  - $f_y$ - focal length in y direction
  - $c_x$ - optical center in x direction
  - $c_y$ - optical center in y direction

- Distortion coefficients

  - $k_1$
  - $k_2$
  - $p_1$
  - $p_2$
  - $k_3$
