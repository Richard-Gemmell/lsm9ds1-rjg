import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lsm9ds1_rjg import Driver, I2CTransport, SPITransport


class HardwareDataReady:
    PIN_INT1_AG = 23

    """This example shows how to use a GPIO pin connected to INT_1
    to find out when there is new data to read."""
    def __init__(self):
        self.driver = self._create_spi_driver(self.PIN_INT1_AG)
        # self.driver = self._create_i2c_driver(self.PIN_INT1_AG)
        self.driver.configure()

    @staticmethod
    def _create_i2c_driver(data_ready_pin: int = None) -> Driver:
        """
        Creates a driver that communicates by I2C and uses a hardware
        interrupt to tell when there is new data available.
        :param data_ready_pin: the GPIO pin connected to the INT1 pin on the LSM9DS1
        :return: a driver
        """
        return Driver(
            I2CTransport(1, I2CTransport.I2C_AG_ADDRESS, data_ready_pin),
            I2CTransport(1, I2CTransport.I2C_MAG_ADDRESS))

    @staticmethod
    def _create_spi_driver(data_ready_pin: int = None) -> Driver:
        """
        Creates a driver that communicates by SPI and uses a hardware
        interrupt to tell when there is new data available.
        :param data_ready_pin: the GPIO pin connected to the INT1 pin on the LSM9DS1
        :return: a driver
        """
        return Driver(
            SPITransport(0, False, data_ready_pin),
            SPITransport(1, True))

    def main(self):
        try:
            count = 0
            while count < 50:
                if self.driver.ag_data_ready(100):
                    self.read_ag()
                    self.read_magnetometer()
                else:
                    print("Timed out waiting for data")
                count += 1
        finally:
            self.driver.close()

    def read_ag(self):
        temp, acc, gyro = self.driver.read_ag_data()
        print('Temp:{} Acc:{} Gryo:{}'.format(temp, acc, gyro))

    def read_magnetometer(self):
        mag = self.driver.read_magnetometer()
        print('Mag {}'.format(mag))


if __name__ == '__main__':
    HardwareDataReady().main()
