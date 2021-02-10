class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
 
p = Point(2, 3)
print(p.x)
print(p.y)


class Flight():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passengers = []

    def add_passanger(self, name):
        if not self.open_seats():   # equivalente a usar -> self.open_seats == 0
            return False     
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["Ander", "Carlos", "Gih", "Rob"]

for person in people:
    success = flight.add_passanger(person)

    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
