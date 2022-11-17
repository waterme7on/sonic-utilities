from swa.base import send_file_command
import os


class FileClient:
    def __init__(self):
        pass

    def read(self, file_path):
        # read file_path in sonic-vm
        status, msg, data = send_file_command("Read", file_path, "")
        return data

    def write(self, file_path, data):
        # write data to file_path in sonic-vm
        status, msg, data = send_file_command("Write", file_path, data)
        return status

    def map_to_local(self, file_path):
        data = self.read(file_path)
        data = data.replace("swsscommon.swsscommon", "swsscommon")
        data = data.replace("import yang as ly", "#import yang as ly")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file = open(file_path, "w+")
        file.write(data)
        file.close()
