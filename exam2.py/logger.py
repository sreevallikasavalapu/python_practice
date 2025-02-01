class Logger:
    def log(self, message, level='info'):
        if level == 'error':
            self.log_error(message)
        elif level == 'warning':
            self.log_warning(message)
        else:
            self.log_info(message)

    def log_error(self, message):
        print(f"[ERROR] {message}")

    def log_warning(self, message):
        print(f"[WARNING] {message}")

    def log_info(self, message):
        print(f"[INFO] {message}")

logger = Logger()
logger.log("This is an informational message.") 
logger.log("This is a warning message.", level='warning')
logger.log("This is an error message.", level='error')
