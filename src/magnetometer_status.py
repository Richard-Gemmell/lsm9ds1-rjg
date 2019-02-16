class MagnetometerStatus:
    def __init__(self, status: int):
        self.status = status

    @property
    def overrun(self) -> bool:
        """data overrun on all axes"""
        return (self.status & 0x80) != 0

    @property
    def z_overrun(self) -> bool:
        """Z axis data overrun"""
        return (self.status & 0x40) != 0

    @property
    def y_overrun(self) -> bool:
        """Y axis data overrun"""
        return (self.status & 0x20) != 0

    @property
    def x_overrun(self) -> bool:
        """X axis data overrun"""
        return (self.status & 0x10) != 0

    @property
    def data_available(self) -> bool:
        """There's new data available for all axes."""
        return (self.status & 0x08) != 0

    @property
    def z_axis_data_available(self) -> bool:
        return (self.status & 0x04) != 0

    @property
    def y_axis_data_available(self) -> bool:
        return (self.status & 0x02) != 0

    @property
    def x_axis_data_available(self) -> bool:
        return (self.status & 0x01) != 0
