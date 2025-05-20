from customer import Customer
from coffee import Coffee
from order import Order


lucy = Customer("Lucy")
jack = Customer("Jack")


espresso = Coffee("Espresso")
latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino")


order1 = Order(lucy, espresso, 2.5)
order2 = Order(lucy, latte, 3.5)
order3 = Order(jack, cappuccino, 4.0)
order4 = Order(jack, espresso, 2.0)


print(f"{lucy.name}'s orders: {[o.coffee.name for o in lucy.orders()]}")
print(f"{jack.name}'s coffees: {[c.name for c in jack.coffees()]}")
print(f"{espresso.name} customers: {[c.name for c in espresso.customers()]}")
print(f"{latte.name} average price: {latte.average_price()}")
print(f"{cappuccino.name} order count: {cappuccino.num_orders()}")


new_order = lucy.create_order(cappuccino, 4.5)
print(f"New order created: {new_order.coffee.name} for {new_order.price}")
