from abc import abstractmethod

class FileClient:
    def __init__(self):
        # self.Client = None
        pass

    @abstractmethod(callable)
    def read(self, file_path):
        # read file_path in sonic-vm
        pass

    @abstractmethod(callable)
    def write(self, file_path, data):
        # write data to file_path in sonic-vm
        pass
