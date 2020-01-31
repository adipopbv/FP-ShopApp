from domain.entities import Product
from domain.exceptions import *
from framework.repos import ProductsFileRepo, ProductsRepo


class ProductsService:

    _products_repo: ProductsFileRepo

    @property
    def products_repo(self):
        return self._products_repo

    @products_repo.setter
    def products_repo(self, value):
        self._products_repo = value

    def __init__(self, repo: ProductsFileRepo):
        self._products_repo = repo

    def add_product(self, prod_id: int, prod_name: str, prod_cost: int):
        self.products_repo.load_from_file()
        product = Product(prod_id, prod_name, prod_cost)
        self.products_repo.add_product(product)

    def remove_product_with_id_containing(self, number: int):
        self.products_repo.load_from_file()
        for product in self.products_repo.products:
            if str(number) in str(product.id):
                self.products_repo.remove_product(product)
                return
        raise ItemNotInRepoException

    def undo_operation(self):
        self.products_repo.load_from_file()
        self.products_repo.undo_operation()

    def apply_filter(self, name_filter, cost_filter):
        pass
