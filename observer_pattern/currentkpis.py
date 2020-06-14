from observer import AbsObserver

class CurrentKPIs(AbsObserver):
    """docstring for CurrentKPIs."""
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        super(CurrentKPIs, self).__init__()
        self.kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self.kpis.open_tickets
        self.closed_tickets = self.kpis.closed_tickets
        self.new_tickets = self.kpis.new_tickets
        self.display()

    def display(self):
        print("Current open tickets: {}".format(self.open_tickets))
        print("Current closed tickets: {}".format(self.closed_tickets))
        print("Current new tickets: {}".format(self.new_tickets))
        print("*****\n")
