from abc import ABC, abstractmethod
from typing import List


class AbstractTransport(ABC):
    @abstractmethod
    def close(self):
        """Releases any resources held by the transport"""
        pass

    @abstractmethod
    def write_byte(self, address: int, value: int) -> int:
        """Writes a single byte to the given address
        :param address: the address to write to
        :param value: the byte to write
        """
        pass

    @abstractmethod
    def read_byte(self, address: int) -> int:
        """Reads a single byte
        :param address: the address to read
        """
        pass

    @abstractmethod
    def read_bytes(self, address: int, length: int) -> List[int]:
        """
        Reads 'length' bytes starting at 'address'
        :param address: the address to read
        :param length: number of bytes to read
        """
        pass

    @abstractmethod
    def data_ready(self, timeout: int) -> bool:
        """Waits for data to be ready."""
        pass
