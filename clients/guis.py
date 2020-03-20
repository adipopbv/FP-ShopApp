from domain.exceptions import *


class ConsoleGui:

    def read_string(self, prompt):
        try:
            return str(input(prompt))
        except:
            raise NotStringException()

    def read_int(self, prompt):
        try:
            return int(input(prompt))
        except:
            raise NotIntException()

    def write(self, message):
        print(str(message))