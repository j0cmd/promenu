#  dataclass é uma lib nativa do python por isso tem q ser importada
from dataclasses import dataclass, field, asdict, astuple
from typing import Optional, List
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class Product:
    # definindo as propriedades
    product_id: int
    name: str
    price: float
    descriptin: str | None = None


#  product = Product(product_id='a', name='b', prince=1)
@dataclass(slots=True, kw_only=True)
class Order:
    order_id: int
    client_id: int
    total: float = field(init=False, default=0.0)
    products: List[Product] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        self.__calculate_total__()

    def __calculate_total__(self):
        self.total = sum([product.price for product in self.products])


product1 = Product(product_id=1, name='product 1', price=203)
order1 = Order(order_id=1, client_id=1, products=[product1])
#  print()
#  print(order1)

#  print('dicionario ', asdict(order1))
#  print('tupla ', astuple(order1))
#  print(product)
