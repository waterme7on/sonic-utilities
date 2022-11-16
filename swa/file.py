from swa.base import send_file_command


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
