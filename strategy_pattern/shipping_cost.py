class ShippingCost(object):
    """docstring for ShippingCost."""
    def __init__(self, strategy):
        super(ShippingCost, self).__init__()
        self.strategy = strategy

    def shipping_cost(self, order):
        return self.strategy.calculate(order)
