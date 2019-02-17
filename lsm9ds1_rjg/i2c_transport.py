from typing import List

from smbus2 import SMBusWrapper


from .abstract_transport import AbstractTransport
from .gpio_interrupt import GPIOInterrupt


class I2CTransport(AbstractTransport):
    data_ready_interrupt: GPIOInterrupt
    I2C_AG_ADDRESS = 0x6B
    I2C_MAG_ADDRESS = 0x1E

    def __init__(self, port: int, i2c_address: int, data_ready_pin: int = None):
        super().__init__()
        self.port = port
        self.i2c_device = i2c_address
        self.data_ready_interrupt = None
        if data_ready_pin:
            self.data_ready_interrupt = GPIOInterrupt(data_ready_pin)

    def close(self):
        if self.data_ready_interrupt:
            self.data_ready_interrupt.close()

    def write_byte(self, address: int, value: int):
        with SMBusWrapper(self.port) as bus:
            bus.write_byte_data(self.i2c_device, address, value)

    def read_byte(self, address: int) -> int:
        with SMBusWrapper(self.port) as bus:
            bus.write_byte(self.i2c_device, address)
            return bus.read_byte(self.i2c_device)

    def read_bytes(self, address: int, length: int) -> List[int]:
        with SMBusWrapper(self.port) as bus:
            bus.write_byte(self.i2c_device, address)
            result = bus.read_i2c_block_data(self.i2c_device, address, length)
            return result

    def data_ready(self, timeout: int) -> bool:
        if self.data_ready_interrupt:
            return self.data_ready_interrupt.wait_for(timeout)
        else:
            raise RuntimeError('I2CTransport needs a GPIO pin to support data_ready().')
