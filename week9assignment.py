from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def value(self) -> float:
        return self.price * self.quantity

@dataclass
class Warehouse:
    name: str
    products: list = field(default_factory=list)
    total_value: float = field(init=False)

    def __post_init__(self):
        self._refresh()

    def _refresh(self):
        self.total_value = sum(p.value() for p in self.products)

    def add_product(self, product: Product):
        self.products.append(product)
        self._refresh()

    def sell(self, product_name: str, qty: int) -> bool:
        for p in self.products:
            if p.name == product_name:
                if p.quantity >= qty:
                    p.quantity -= qty
                    self._refresh()
                    return True
                return False
        return False

    def restock(self, product_name: str, qty: int):
        for p in self.products:
            if p.name == product_name:
                p.quantity += qty
                self._refresh()
                return

    def report(self) -> str:
        result = f"{self.name} Inventory:\n"
        for p in self.products:
            result += f"  {p.name}: {p.quantity} units @ ${p.price} each\n"
        result += f"Total value: ${self.total_value:.2f}"
        return result
    
p1 = Product("Laptop", 999.99, 10)
p2 = Product("Mouse", 29.99, 50)
p3 = Product("Keyboard", 79.99, 30)

w = Warehouse("TechDepot")
w.add_product(p1)
w.add_product(p2)
w.add_product(p3)

print(w.total_value)
print(w.sell("Laptop", 3))
print(w.sell("Laptop", 20))
w.restock("Mouse", 25)
print(w.report())
