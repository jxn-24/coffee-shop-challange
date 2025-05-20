import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_name(self):
        customer = Customer("Lucy")
        assert customer.name == "Lucy"

        with pytest.raises(TypeError):
            customer.name = 123

        with pytest.raises(ValueError):
            customer.name = ""

        with pytest.raises(ValueError):
            customer.name = "ThisNameIsWayTooLong"

    def test_create_order(self):
        customer = Customer("Bob")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 5.0)

        assert order in customer.orders()
        assert order.coffee == coffee
        assert order.price == 5.0

    def test_coffees(self):
        customer = Customer("Charlie")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Cappuccino")

        customer.create_order(coffee1, 3.0)
        customer.create_order(coffee1, 3.5)  
        customer.create_order(coffee2, 4.0)

        assert len(customer.coffees()) == 2
        assert coffee1 in customer.coffees()
        assert coffee2 in customer.coffees()

