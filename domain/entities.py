class Product:

    _id: int

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    _name: str

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    _cost: int

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    def __init__(self, id: int, name: str, cost: int):
        self.id = id
        self.name = name
        self.cost = cost
