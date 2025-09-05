#Assignment :
#Problem Statement

#You are asked to design a Flight Management System in Python using exception handling.
 
#The system should:

#- Read flight information from a file called flights.txt.

#- Each line has: flight_number available_seats price_per_ticket

#  Example: AI101 50 6000
 
#Ask the user for:

#- Flight number

#- Number of tickets to book
 
#Implement the following exception rules: (Questions below)
 
#(a) Raise FlightNotFoundError (custom) if the entered flight number does not exist.
 
#(b) Raise SeatsUnavailableError (custom) if requested tickets exceed available seats.
 
#(c) Handle ValueError if user enters invalid input (like string instead of integer).
 
#(d) Handle ZeroDivisionError if user enters 0 tickets (while calculating discount per ticket).
 
#(e) Always close the file using finally.
 
#The program should print:

#- Flight details

#- Total booking cost

#- Discount per ticket (total / tickets)
 
#Note**:

#Use nested try-except:
 
#Inner block for booking operations.
 
#Outer block for file handling & re-raised exceptions


import traceback
class FlightNotFoundError(Exception):
    pass
class SeatsUnavailableError(Exception):
    pass

file = None
try:
    file= open('./Assignment/flights.txt', 'r')
   
    try:
        flightdetails = {}
        while True:
            data = file.readline().split()
            if not data:
                break
            flight_number, stock, price = data[0], int(data[1]), float(data[2])
            print(f'Product: {flight_number}, Stock: {stock}, Price: {price}')
            flightdetails[flight_number] = (stock, price)
        print (flightdetails)
        flight_no = input('Enter the Flight Number: ') 
        if(flight_no not in flightdetails):
            raise FlightNotFoundError('Flight is not available')
        
        seat_no = int(input('Enter the number of seats: '))  
        print(flightdetails[flight_no][0])
        if seat_no <=0:
            raise ValueError('Quantity must be greater than zero')
        elif seat_no > flightdetails[flight_no][0]:
            raise SeatsUnavailableError('Insufficient seats available')

        price = flightdetails[flight_no][1]
        total = price * seat_no
        print(f'Total cost: {total}')
        
        discount = total / (seat_no-1)
        print(f'Discounted total: {discount}')

    except FlightNotFoundError as ve:
        print('Flight error:', ve)

    except SeatsUnavailableError as ve:
        print('Flight error:', ve)
    
    except ValueError as ve:
        print('Value error:', ve)
    
    except ZeroDivisionError as zde:
        print('Qunaitity should be more than 1 to calcuate the discount', zde)
       
except FileNotFoundError:
    print('File not found, please check the path')

except ValueError:
    print('Pleae enter valid values')

except Exception as e:
    print('An error occurred:', e)
finally:
    if not file:
        file.close()
 
 