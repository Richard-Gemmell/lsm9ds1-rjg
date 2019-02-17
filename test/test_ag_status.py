import unittest

from lsm9ds1_rjg.ag_status import AGStatus


class AGStatusTest(unittest.TestCase):
    def test_accelerometer_interrupt(self):
        s = AGStatus(0x00)
        self.assertFalse(s.accelerometer_interrupt)
        s = AGStatus(0x40)
        self.assertTrue(s.accelerometer_interrupt)

    def test_gyroscope_interrupt(self):
        s = AGStatus(0x00)
        self.assertFalse(s.gyroscope_interrupt)
        s = AGStatus(0x20)
        self.assertTrue(s.gyroscope_interrupt)

    def test_inactivity_interrupt(self):
        s = AGStatus(0x00)
        self.assertFalse(s.inactivity_interrupt)
        s = AGStatus(0x10)
        self.assertTrue(s.inactivity_interrupt)

    def test_boot_status(self):
        s = AGStatus(0x00)
        self.assertFalse(s.boot_status)
        s = AGStatus(0x08)
        self.assertTrue(s.boot_status)

    def test_temperature_data_available(self):
        s = AGStatus(0x00)
        self.assertFalse(s.temperature_data_available)
        s = AGStatus(0x04)
        self.assertTrue(s.temperature_data_available)

    def test_gyroscope_data_available(self):
        s = AGStatus(0x00)
        self.assertFalse(s.gyroscope_data_available)
        s = AGStatus(0x02)
        self.assertTrue(s.gyroscope_data_available)

    def test_accelerometer_data_available(self):
        s = AGStatus(0x00)
        self.assertFalse(s.accelerometer_data_available)
        s = AGStatus(0x01)
        self.assertTrue(s.accelerometer_data_available)
