from observer import AbcSubject

class KPIs(AbcSubject):
    """docstring for KPIs."""
    def __init__(self):
        super(KPIs, self).__init__()
        self.open_tickets = -1
        self.closed_tickets = -1
        self.new_tickets = -1

    @property
    def open_tickets(self):
        return self.open_tickets

    @property
    def closed_tickets(self):
        return self.closed_tickets

    @property
    def new_tickets(self):
        return self.new_tickets

    def set_kpis(self, open_tickets, closed_tickets, new_tickets):
        self.open_tickets = open_tickets
        self.closed_tickets = closed_tickets
        self.new_tickets = new_tickets
        self.notify()
