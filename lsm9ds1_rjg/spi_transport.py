import spidev

from .abstract_transport import AbstractTransport
from .gpio_interrupt import GPIOInterrupt


class SPITransport(AbstractTransport):
    __READ_FLAG = 0x80
    __MAGNETOMETER_READ_FLAG = 0xC0
    __DUMMY = 0xFF
    data_ready_interrupt: GPIOInterrupt

    def __init__(self, spi_device: int, magnetometer: bool, data_ready_pin: int = None):
        super().__init__()
        self.magnetometer = magnetometer
        self.spi = spidev.SpiDev()
        self._init_spi(spi_device)
        self.data_ready_interrupt = None
        if data_ready_pin:
            self.data_ready_interrupt = GPIOInterrupt(data_ready_pin)

    def _init_spi(self, spi_device: int):
        self.spi.open(0, spi_device)
        self.spi.mode = 0b00
        self.spi.max_speed_hz = 8_000_000

    def close(self):
        self.spi.close()
        if self.data_ready_interrupt:
            self.data_ready_interrupt.close()

    def write_byte(self, address: int, value: int):
        self.spi.writebytes([address, value])

    def read_byte(self, address: int) -> int:
        return self.spi.xfer([address | self.__READ_FLAG, self.__DUMMY])[1]

    def read_bytes(self, reg_address, length):
        request = [self.__DUMMY] * (length + 1)
        if self.magnetometer:
            # Need to set bit 1 for multi-byte reads by the magnetometer or we
            # just keep reading the same byte
            request[0] = reg_address | self.__MAGNETOMETER_READ_FLAG
        else:
            request[0] = reg_address | self.__READ_FLAG
        response = self.spi.xfer(request)
        return response[1:]

    def data_ready(self, timeout: int) -> bool:
        if self.data_ready_interrupt:
            return self.data_ready_interrupt.wait_for(timeout)
        else:
            raise RuntimeError('SPITransport needs a GPIO pin to support data_ready().')
