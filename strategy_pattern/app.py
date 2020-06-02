from strategy_classes import *
from shipping_cost import ShippingCost
from order import Order

order = Order()
strategy = FedexStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0
print(cost)
