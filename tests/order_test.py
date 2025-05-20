import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    def test_init(self):
        customer = Customer("Samuel")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 6.0)

        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 6.0

    def test_price_validation(self):
        customer = Customer("Maria")
        coffee = Coffee("White Coffee")

        with pytest.raises(TypeError):
            Order(customer, coffee, "6.0")

        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)

        with pytest.raises(ValueError):
            Order(customer, coffee, 15.0)

        order = Order(customer, coffee, 7.5)
        with pytest.raises(AttributeError):
            order.price = 8.0

    def test_relationships(self):
        customer = Customer("Alice")
        coffee = Coffee("Black Coffee")
        order = Order(customer, coffee, 8.5)

        assert order in customer.orders()
        assert order in coffee.orders()

