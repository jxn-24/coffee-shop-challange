import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def test_name(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"

        with pytest.raises(TypeError):
            Coffee(123)

        with pytest.raises(ValueError):
            Coffee("A")

        with pytest.raises(AttributeError):
            coffee.name = "New Name"

    def test_num_orders(self):
        coffee = Coffee("Espresso")
        assert coffee.num_orders() == 0

        customer = Customer("Dave")
        customer.create_order(coffee, 2.5)
        assert coffee.num_orders() == 1

        customer.create_order(coffee, 3.0)
        assert coffee.num_orders() == 2

    def test_average_price(self):
        coffee = Coffee("Americano")
        customer = Customer("Eve")

        assert coffee.average_price() == 0

        customer.create_order(coffee, 2.0)
        customer.create_order(coffee, 4.0)
        assert coffee.average_price() == 3.0

