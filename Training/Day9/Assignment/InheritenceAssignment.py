"""
Create a base class Flight with basic flight information. Create a derived class ScheduledFlight that adds scheduling information.
 
Requirements:
-Flight should have attributes: flight number, airline.
-ScheduledFlight should add departure time and arrival time.
-Include methods to display complete flight information.
 
 
Create a base class Person, derived class CrewMember, and a further derived class Pilot.
-Person contains name and ID.
-CrewMember adds role (e.g., "Cabin Crew", "Pilot").
-Pilot adds license number and rank (e.g., "Captain").
 
 
Create a base class Service, and derive two classes: SecurityService and BaggageService.
Requirements:
-Service class has a method service_info().
-Derived classes override or extend this to describe their own service.
 
 
Create one class PassengerDetails and another class TicketDetails. Create a new class Booking that inherits from both.
Requirements:
- PassengerDetails has name, age.
- TicketDetails has ticket number, seat number.
- Booking shows all information.
"""

class Flight:
    def __init__(self, flightnumber, airline):
        self.flightnumber = flightnumber
        self.airline = airline

    def display_flight(self):
        print(f"Flight Number: {self.flightnumber}, Airline: {self.airline}")

class ScheduledFlight(Flight):
    def __init__(self, flightnumber, airline, depraturetime, arrivaltime):
        super().__init__(flightnumber, airline)
        self.departuretime = depraturetime
        self.arivaltime = arrivaltime

    def display_Schedule(self):
        self.display_flight()
        print(f"Departure: {self.departuretime}, Arrival: {self.arivaltime}")

flight = ScheduledFlight("F101", "Indian Airlines", "8:40 AM", "10:40 AM")
flight.display_Schedule()

print("************************************************************")

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_person(self):
        print(f"Name: {self.name}, ID: {self.id}")

class CrewMember(Person):
    def __init__(self,name, id, role):
        super().__init__(name, id)
        self.role = role

    def display_crew(self):
        self.display_person()
        print(f"Role: {self.role}")

class Pilot(CrewMember):
    def __init__(self,name, id, role, licencenumber, rank):
        super().__init__(name, id, role)
        self.licencenumber = licencenumber
        self.rank = rank

    def display_Pilot(self):
        self.display_crew()
        print(f"Licence: {self.licencenumber}, Rank: {self.rank}")

pilot = Pilot("Mr Pilot", "ID101", "Pilot", "L101", "Captain")
pilot.display_Pilot()

print("************************************************************")

class Service:
    def __init__(self, servicename):
        self.servicename = servicename

    def service_info(self):
        print(f"Service: {self.servicename}")


class SecurityService(Service):
    def __init__(self, servicename):
        super().__init__(servicename)

    def service_info(self):
        print(f" Security Service: {self.servicename}")

class BaggageService(Service):
    def __init__(self, servicename):
        super().__init__(servicename)

    def service_info(self):
        print(f" Baggage Service: {self.servicename}")

secservice = SecurityService("Service1")
bagservice = BaggageService("Service2")
secservice.service_info()
bagservice.service_info()


print("************************************************************")

class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Display_passenger(self):
        print(f"Passenger name: {self.name}, Age {self.age}")

class TicketDetails:
    def __init__(self, ticketnumber, seatnumber):
        self.ticketnumber = ticketnumber
        self.seatnumber = seatnumber

    def Display_Ticket(self):
        print(f"Ticket# : {self.ticketnumber}, Seat Number : {self.seatnumber}")

class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticketnumber, seatnumber, bookingid):
        PassengerDetails.__init__(self, name, age)
        TicketDetails.__init__(self, ticketnumber, seatnumber)
        self.bookingid = bookingid 

    def display_booking(self):
        print(f"Booking ID : {self.bookingid}")
        self.Display_passenger()
        self.Display_Ticket()

booking = Booking("John", 30, "T101", "F23", "B101")
booking.display_booking()
print("************************************************************")