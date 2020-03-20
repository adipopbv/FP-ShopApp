from domain.entities import Product
from domain.exceptions import *


class ProductsRepo:

    _products: list

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        self._products = value

    _history: list

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        self._history = value

    def __init__(self, products: list):
        self.products = products
        self.history = [self.products]

    def add_product(self, product: Product):
        self.products.append(product)
        self.history.append(self.products)

    def remove_product(self, product: Product):
        self.products.remove(product)
        self.history.append(self.products)

    def undo_operation(self):
        if len(self.history) <= 1:
            raise EndOfHistoryException
        self.history.remove(self.history[-1])
        self.products = self.history[-1]


class ProductsFileRepo(ProductsRepo):

    _file_name: str

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    def __init__(self, file_name: str):
        ProductsRepo.__init__(self, [])
        self.file_name = file_name
        self.load_from_file()
        self.history = [self.products]

    def add_product(self, product: Product):
        ProductsRepo.add_product(self, product)
        self.save_to_file()

    def remove_product(self, product: Product):
        ProductsRepo.remove_product(self, product)
        self.save_to_file()

    def undo_operation(self):
        ProductsRepo.undo_operation(self)
        self.save_to_file()

    def load_from_file(self):
        temp_products = []
        file = open(self.file_name, "r")
        try:
            lines = file.readlines()
            for line in lines:
                line = line.split(";")
                temp_products.append(Product(int(line[0]), str(line[1]), int(line[2])))
            self.products = temp_products
        finally:
            file.close()

    def save_to_file(self):
        file = open(self.file_name, "w")
        try:
            lines = ""
            for product in self.products:
                if product is not self.products[0]:
                    lines = lines + "\n"
                lines = lines + str(product.id) + ";" + str(product.name) + ";" + str(product.cost)
            file.write(lines)
        finally:
            file.close()
