from clients.uis import ConsoleUi
from framework.repos import ProductsFileRepo
from services.services import ProductsService

products_repo = ProductsFileRepo("products.txt")

products_service = ProductsService(products_repo)

ui = ConsoleUi(products_service)

ui.run_application()
