class AppException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class NotStringException(Exception):

    def __init__(self):
        self.message = "Valoarea nu este un text!"


class NotIntException(Exception):

    def __init__(self):
        self.message = "Valoarea nu este un numar!"


class ItemNotInRepoException(Exception):

    def __init__(self):
        self.message = "Obiectul nu exista in repozitor!"


class NotFigureException(Exception):

    def __init__(self):
        self.message = "Valoarea nu este o cifra!"


class EndOfHistoryException(Exception):

    def __init__(self):
        self.message = "Nu se mai pot reface operatii!"
