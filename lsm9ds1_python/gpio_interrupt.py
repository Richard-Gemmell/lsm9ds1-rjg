import time

from RPi import GPIO

from .abstract_interrupt import Interrupt


class GPIOInterrupt(Interrupt):
    def __init__(self, gpio_pin: int):
        self.gpio_pin = gpio_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.IN)

    def close(self):
        """This method must be called to release the pin for use by other processes"""
        GPIO.cleanup(self.gpio_pin)

    def wait_for(self, timeout: int) -> bool:
        """
        Returns true if when the pin transitions from low to high.
        Assumes some other process will reset the pin to low.
        :param timeout: time to wait for the interrupt in milliseconds
        :return: True if the interrupt happened. False if it timed out.
        """
        ready = False
        # Dividing sleep time by 300 instead of 30 double CPU load but cuts
        # IMU timestamp variation from about 20% to less than 1%
        sleep_time = (timeout / 1000.0) / 30
        stop_time = time.monotonic_ns() + (timeout * 1000_000.0)
        while not ready and time.monotonic_ns() < stop_time:
            ready = GPIO.input(self.gpio_pin)
            time.sleep(sleep_time)
        return ready
