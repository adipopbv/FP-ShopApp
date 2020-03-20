from clients.guis import ConsoleGui
from domain.exceptions import *
from services.services import ProductsService


class ConsoleUi:

    _service: ProductsService

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        self._service = value

    _commands: dict

    @property
    def commands(self):
        return self._commands

    @commands.setter
    def commands(self, value):
        self._commands = value

    _console_gui: ConsoleGui

    @property
    def console_gui(self):
        return self._console_gui

    @console_gui.setter
    def console_gui(self, value):
        self._console_gui = value

    def __init__(self, service: ProductsService):
        self.service = service
        self.console_gui = ConsoleGui()
        self.commands = {
            0: self.exit_app,
            1: self.add_product,
            2: self.remove_product,
            3: self.filter_products,
            4: self.undo_operation
        }

    def write_commands(self):
        self.console_gui.write(
            "COMENZI:\n" +
            "    [1]: Adauga produs;\n" +
            "    [2]: Sterge produs;\n" +
            "    [3]: Filtrare produse;\n" +
            "    [4]: Refa ultima operatie.\n" +
            "    [0]: Inchidere.\n"
        )

    def read_int(self):
        return self.console_gui.read_int("Va rog introduceti numarul dorit: ")

    def read_string(self):
        return self.console_gui.read_string("Va rog introduceti textul dorit: ")

    def write_exception(self, exception: AppException):
        self.console_gui.write("Eroare: ")
        message = exception.message
        self.console_gui.write(message)

    def write_success(self):
        self.console_gui.write("Operation successful!\n")

    def add_product(self):
        prod_id = self.read_int()
        prod_name = self.read_string()
        prod_cost = self.read_int()
        self.service.add_product(prod_id, prod_name, prod_cost)

    def remove_product(self):
        number = self.read_int()
        if 0 <= number <= 9:
            self.service.remove_product_with_id_containing(number)
            return
        raise NotFigureException

    def filter_products(self):
        name_filter = self.read_string()
        cost_filter = self.read_int()
        self.service.apply_filter(name_filter, cost_filter)

    def undo_operation(self):
        self.service.undo_operation()

    def exit_app(self):
        exit()

    def run_application(self):
        self.console_gui.write("~~~ MAGAZIN ~~~\n")
        while True:
            try:
                self.write_commands()
                command_id = self.read_int()
                self.commands[command_id]()
                self.write_success()
            except Exception as ex:
                self.write_exception(ex)
