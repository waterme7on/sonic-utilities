"""
Logging functionality for SONiC Python applications
"""


# \sonic-buildimage\src\sonic-py-common\sonic_py_common\logger.py
class Logger(object):
    """
    Logger class for SONiC Python applications
    """

    def __init__(self, log_identifier=None, log_facility=0, log_option=0):
        pass

    def __del__(self):
        pass

    #
    # Methods for setting minimum log priority
    #

    def set_min_log_priority(self, priority):
        pass

    def set_min_log_priority_error(self):
        pass

    def set_min_log_priority_warning(self):
        pass

    def set_min_log_priority_notice(self):
        pass

    def set_min_log_priority_info(self):
        pass

    def set_min_log_priority_debug(self):
        pass

    #
    # Methods for logging messages
    #

    def log(self, priority, msg, also_print_to_console=False):
        pass

    def log_error(self, msg, also_print_to_console=False):
        pass

    def log_warning(self, msg, also_print_to_console=False):
        pass

    def log_notice(self, msg, also_print_to_console=False):
        pass

    def log_info(self, msg, also_print_to_console=False):
        pass

    def log_debug(self, msg, also_print_to_console=False):
        pass
