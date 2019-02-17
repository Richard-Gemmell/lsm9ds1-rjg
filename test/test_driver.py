import unittest
from unittest.mock import patch, MagicMock

from lsm9ds1_rjg.driver import Driver
from lsm9ds1_rjg.abstract_transport import AbstractTransport


class DriverTest(unittest.TestCase):
    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    def test_ag_data_ready(self, mock_ag: AbstractTransport, mock_mag: AbstractTransport):
        mock_ag.data_ready = MagicMock(return_value=False)
        d = Driver(mock_ag, mock_mag)
        # Act
        result = d.ag_data_ready(123)
        # Assert
        mock_ag.data_ready.assert_called_once_with(123)
        self.assertFalse(result)

    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    def test_read_ag_status(self, mock_ag: AbstractTransport, mock_mag: AbstractTransport):
        mock_ag.read_byte = MagicMock(return_value=0xA2)
        d = Driver(mock_ag, mock_mag)
        # Act
        status = d.read_ag_status()
        # Assert
        mock_ag.read_byte.assert_called_once_with(0x17)
        self.assertEqual(0xA2, status.status)

    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    def test_read_temperature(self, mock_ag: AbstractTransport, mock_mag: AbstractTransport):
        mock_ag.read_bytes = MagicMock(return_value=bytes([0x01, 0x80]))
        d = Driver(mock_ag, mock_mag)
        # Act
        temp = d.read_temperature()
        # Assert
        mock_ag.read_bytes.assert_called_once_with(0x15, 2)
        self.assertEqual(-32767, temp)

    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    def test_read_read_acceleration(self, mock_ag: AbstractTransport, mock_mag: AbstractTransport):
        mock_ag.read_bytes = MagicMock(return_value=bytes([0xFF, 0x7F, 0x01, 0x80, 0xFF, 0x00]))
        d = Driver(mock_ag, mock_mag)
        # Act
        result = d.read_acceleration()
        # Assert
        mock_ag.read_bytes.assert_called_once_with(0x28, 6)
        # Note that the driver negates the x-axis of the accelerometer and gyro
        # so that all 3 sensors use the right-hand rule and the same signs.
        self.assertEqual([-32767, -32767, 255], result)

    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    def test_read_read_gyroscope(self, mock_ag: AbstractTransport, mock_mag: AbstractTransport):
        mock_ag.read_bytes = MagicMock(return_value=bytes([0xFF, 0x7F, 0x01, 0x80, 0xFF, 0x00]))
        d = Driver(mock_ag, mock_mag)
        # Act
        result = d.read_gyroscope()
        # Assert
        mock_ag.read_bytes.assert_called_once_with(0x18, 6)
        # Note that the driver negates the x-axis of the accelerometer and gyro
        # so that all 3 sensors use the right-hand rule and the same signs.
        self.assertEqual([-32767, -32767, 255], result)

    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    def test_read_ag_data(self, mock_ag: AbstractTransport, mock_mag: AbstractTransport):
        mock_ag.read_bytes = MagicMock(return_value=bytes([
            0xFF, 0x00,
            0xFF, 0x7F, 0x01, 0x80, 0xFF, 0x00,
            0xE8, 0x03, 0xC4, 0x09, 0x78, 0x69
        ]))
        d = Driver(mock_ag, mock_mag)
        # Act
        temp, acc, gyro = d.read_ag_data()
        # Assert
        mock_ag.read_bytes.assert_called_once_with(0x15, 14)
        self.assertEqual(255, temp)
        # Note that the driver negates the x-axis of the accelerometer and gyro
        # so that all 3 sensors use the right-hand rule and the same signs.
        self.assertEqual([-1000, 2500, 27000], acc)
        self.assertEqual([-32767, -32767, 255], gyro)

    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    def test_magnetometer_data_ready(self, mock_ag: AbstractTransport, mock_mag: AbstractTransport):
        mock_mag.data_ready = MagicMock(return_value=True)
        d = Driver(mock_ag, mock_mag)
        # Act
        result = d.magnetometer_data_ready(123)
        # Assert
        mock_mag.data_ready.assert_called_once_with(123)
        self.assertTrue(result)

    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    def test_read_magnetometer_status(self, mock_ag: AbstractTransport, mock_mag: AbstractTransport):
        mock_mag.read_byte = MagicMock(return_value=0xA2)
        d = Driver(mock_ag, mock_mag)
        # Act
        status = d.read_magnetometer_status()
        # Assert
        mock_mag.read_byte.assert_called_once_with(0x27)
        self.assertEqual(0xA2, status.status)

    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    @patch('lsm9ds1_rjg.abstract_transport.AbstractTransport')
    def test_read_magnetometer(self, mock_ag: AbstractTransport, mock_mag: AbstractTransport):
        mock_mag.read_bytes = MagicMock(return_value=bytes([0xFF, 0x7F, 0x01, 0x80, 0xFF, 0x00]))
        d = Driver(mock_ag, mock_mag)
        # Act
        result = d.read_magnetometer()
        # Assert
        mock_mag.read_bytes.assert_called_once_with(0x28, 6)
        self.assertEqual([32767, -32767, 255], result)
