from termcolor import colored

class Logger:

    @staticmethod
    def error(msg: str):
        print(colored(f"[ERROR]: {msg}", 'red', attrs=[]))

    @staticmethod
    def info(msg: str):
        print(colored(f"[INFO]: {msg}", 'green', attrs=[]))
