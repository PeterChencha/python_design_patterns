from observer import AbsObserver

class ForecastKPIs(AbsObserver):
    """docstring for ForecastKPIs."""
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        super(ForecastKPIs, self).__init__()
        self.kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self.kpis.open_tickets
        self.closed_tickets = self.kpis.closed_tickets
        self.new_tickets = self.kpis.new_tickets
        self.display()

    def display(self):
        print("Forecast open tickets: {}".format(self.open_tickets))
        print("Tickets expected closed in next hour: {}".format(self.closed_tickets))
        print("New tickets expected in next hour: {}".format(self.new_tickets))
        print("*****\n")
