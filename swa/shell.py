from swa.base import send_shell_command


class ShellClient:
    def __init__(self):
        pass

    def run(self, command):
        status, msg, data = send_shell_command(command)
        return data
