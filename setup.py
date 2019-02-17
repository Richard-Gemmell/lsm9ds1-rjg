import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lsm9ds1-rjg",
    version="0.9.2",
    author="Richard Gemmell",
    author_email="16683467+Richard-Gemmell@users.noreply.github.com",
    description="A python module to enable a Raspberry Pi to access an LSM9DS1 IMU sensor.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Richard-Gemmell/lsm9ds1-rjg",
    license="LICENSE.txt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: System :: Hardware :: Hardware Drivers"
    ],
    install_requires=[
        "smbus2 >= 0.2",
        "spidev >= 3.2"
    ]
)