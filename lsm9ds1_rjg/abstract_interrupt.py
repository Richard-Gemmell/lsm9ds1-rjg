from abc import abstractmethod, ABC


class Interrupt(ABC):
    @abstractmethod
    def wait_for(self, timeout: int) -> bool:
        """Returns True if the interrupt happened and false
        if timeout milliseconds passed without an interrupt"""
        pass

    @abstractmethod
    def close(self):
        """Releases any resources held by the interrupt"""
        pass
