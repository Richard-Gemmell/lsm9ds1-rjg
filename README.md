# lsm9ds1-rjg
## Introduction
This is a device driver that enables a Raspberry Pi to access an LSM9DS1 IMU sensor.

The LSM9DS1 combines a 3D accelerometer, 3D rate gyroscope and a 3D magnetometer. It's useful in robotics and other applications for measuring a robot's attitude and movement. The LSM9DS1 is made by ST Microelectronics. The datasheet is available from [their website](https://www.st.com/en/mems-and-sensors/lsm9ds1.html).

Low cost breakout boards are available from various vendors including [Adafruit](https://learn.adafruit.com/adafruit-lsm9ds1-accelerometer-plus-gyro-plus-magnetometer-9-dof-breakout/overview) and [Sparkfun](https://www.sparkfun.com/products/13284).

## Driver Features
* Connects with I2C or SPI
* Preconfigured for 230 Hz output data rate
* Converts accelerometer and gyro output to use the same axes as the magnetometer by flipping the direction of the x axis.
* Detects data ready in software or with an optional GPIO hardware interrupt.
* Provides raw, unscaled data. i.e. max acceleration is 32768 not 2g.
* Extensible
* Optionally enables high priority thread scheduling

## Limitations
* Not a complete implementation of the sensor's API.

## Scaling
This driver returns raw unscaled data. This is a deliberate choice to make it easier
to scale the data with your application.

## Data Ready
If you don't check for data ready and just read data then you will miss some samples.
Worse than that, in some cases you'll read part of one sample and part of the next.
This provides plausible looking but incorrect data. You _must_ wait for data ready
before reading the sensor values. See the examples.

## Examples
* [Simple Example](https://github.com/Richard-Gemmell/lsm9ds1-rjg/blob/master/examples/simple.py)
* [Using a hardware interrupt](https://github.com/Richard-Gemmell/lsm9ds1-rjg/blob/master/examples/hardware_data_ready.py)