class AGStatus:
    def __init__(self, status: int):
        self.status = status

    @property
    def accelerometer_interrupt(self) -> bool:
        return (self.status & 0x40) != 0

    @property
    def gyroscope_interrupt(self) -> bool:
        return (self.status & 0x20) != 0

    @property
    def inactivity_interrupt(self) -> bool:
        return (self.status & 0x10) != 0

    @property
    def boot_status(self) -> bool:
        return (self.status & 0x08) != 0

    @property
    def temperature_data_available(self) -> bool:
        return (self.status & 0x04) != 0

    @property
    def gyroscope_data_available(self) -> bool:
        return (self.status & 0x02) != 0

    @property
    def accelerometer_data_available(self) -> bool:
        return (self.status & 0x01) != 0
