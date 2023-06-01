class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self, name):
        if not self.available_seate():
            return False
        self.passenger.append(name)
        return True

    def available_seate(self):
        return self.capacity - len(self.passenger)
    
flight = Flight(3)

Folks = ['david', 'gabriel', 'bill','CHOROKO']

for folk in Folks:
    success = flight.add_passenger(folk)

    if success:
        print(f'added {folk} in flight ready to travel')
    else:
        print(f'No seat for {folk} the flight is fully')