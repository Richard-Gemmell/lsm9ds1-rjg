import unittest

from lsm9ds1_rjg.magnetometer_status import MagnetometerStatus


class MagnetometerStatusTest(unittest.TestCase):
    def test_overrun(self):
        s = MagnetometerStatus(0x00)
        self.assertFalse(s.overrun)
        s = MagnetometerStatus(0x80)
        self.assertTrue(s.overrun)

    def test_z_overrun(self):
        s = MagnetometerStatus(0x00)
        self.assertFalse(s.z_overrun)
        s = MagnetometerStatus(0x40)
        self.assertTrue(s.z_overrun)

    def test_y_overrun(self):
        s = MagnetometerStatus(0x00)
        self.assertFalse(s.y_overrun)
        s = MagnetometerStatus(0x20)
        self.assertTrue(s.y_overrun)

    def test_x_overrun(self):
        s = MagnetometerStatus(0x00)
        self.assertFalse(s.x_overrun)
        s = MagnetometerStatus(0x10)
        self.assertTrue(s.x_overrun)

    def test_data_available(self):
        s = MagnetometerStatus(0x00)
        self.assertFalse(s.data_available)
        s = MagnetometerStatus(0x08)
        self.assertTrue(s.data_available)

    def test_z_axis_data_available(self):
        s = MagnetometerStatus(0x00)
        self.assertFalse(s.z_axis_data_available)
        s = MagnetometerStatus(0x04)
        self.assertTrue(s.z_axis_data_available)

    def test_y_axis_data_available(self):
        s = MagnetometerStatus(0x00)
        self.assertFalse(s.y_axis_data_available)
        s = MagnetometerStatus(0x02)
        self.assertTrue(s.y_axis_data_available)

    def test_x_axis_data_available(self):
        s = MagnetometerStatus(0x00)
        self.assertFalse(s.x_axis_data_available)
        s = MagnetometerStatus(0x01)
        self.assertTrue(s.x_axis_data_available)
