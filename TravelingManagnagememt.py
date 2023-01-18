# fareRates of cities

adminName = "ShahiExpress"
adminPassword = "since2023"

# names of cities
cityNames = ["Karachi", "Lahore", "Peshawar", "Quetta", "Multan", "Fasalabad"]


fareRates = [[0, 8000, 19000, 4560, 3000, 1950],  # karachi
             [8000, 0, 10500, 6500, 2000, 1000],  # lahore
             [19000, 10500, 0, 25500, 30000, 5500],  # Peshawar
             [4560, 6500, 25500, 0, 4000, 7000],  # Quetta
             [3000, 2000, 30000, 4000, 0, 1500],  # Multan
             [1950, 1000, 5500, 7000, 1500, 0],]  # fasalabad

# seats of cities avilable
seatsAvailable = [[0, 50, 50, 50, 50, 50],  # karachi
                  [50, 0, 50, 50, 50, 50],  # lahore
                  [50, 50, 0, 50, 50, 50],  # Peshawar
                  [50, 50, 50, 0, 50, 50],  # quetta
                  [50, 50, 50, 50, 0, 50],  # Multa
                  [50, 50, 50, 50, 50, 0],]  # fasalabad


# heading() shows the title bar

def heading(title):
    print('\033c')
    line = "----------------------------------------------------------------"
    print(line)
    print(title.center(len(line)))
    print(line, "\n")


def options():
    line = "-----------------"
    print(line)
    print("Press the key to")
    print(line)

    print("1- To know travel details ")
    print("2- To book your seat")
    print("3- To cancel the booking ")
    print("4- Home page")
    print("5- Admin")
    print("0- to exit")
    print(line)
# main_functions(int) check out the selected function
# and call the respective function
    option = int(input())
    main_functions(option)


# travelDetails() shows the travel details of names of cites their fares and seats available
def travelDetails():
    heading("Travel Details")
    print("Fare of cities are: \n")

    # Print column headers
    print("{:<10}".format(""), end="")
    for city in cityNames:
        print("{:<10}".format(city), end="")
    print()

    # Print rows with city names and fares
    for i, city in enumerate(cityNames):
        print("{:<10}".format(city), end="")
        print("|", end='')

        for j in range(6):
            print("{:<10}".format(fareRates[i][j]), end="")
        print()

    print("\n\nAvailable no of seats are : \n")

    # Print column headers
    print("{:<10}".format(""), end="")
    for city in cityNames:
        print("{:<10}".format(city), end="")
    print()

    # Print rows with city names and no of seats
    for i, city in enumerate(cityNames):
        print("{:<10}".format(city), end="")
        print("|", end='')

        for j in range(6):
            print("{:<10}".format(seatsAvailable[i][j]), end="")
        print()

    print("\n\n")
    options()

# createRecipt() creates recipt of the booking


def createRecipt(name, email, phoneNumber, travlingCity, destination, noOfSeats):

    heading("Recipt")
    line="________________________________"
    fare = fareRates[travlingCity][destination]*noOfSeats
    
    print(line)
    print(line)
    print("Name :".ljust(20), name)
    print("Email :".ljust(20), email)
    print("Phone Number :".ljust(20), phoneNumber)
    print("Traveling From :".ljust(20), cityNames[travlingCity], )
    print("Destination :".ljust(20),  cityNames[destination])
    print("Number of tickets :".ljust(20), noOfSeats)
    print("\nFare per seat is :".ljust(20),
          fareRates[travlingCity][destination])
    print(line)
    print("Total fare :".ljust(20), fare)
    print(line)
    print(line)

    print("\n\n")


# functon seatBooking() to book seats for travel


def seatBooking():
    heading("Seat Booking")

    # code to take booking details
    name = input("Full Name : ")
    email = input("Email : ")
    phoneNumber = input("Phone Number : ")

    # take detail of traveling city
    print("\nYou want to travel from : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    travelingCity = int(input("\n")) - 1

    # take detail of destination city
    print("\n\nYour destination is : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    destination = int(input("\n")) - 1

    noOfSeats = int(input("\nNo of seats you want to book : "))
    confirmation = int(input("To confirm your booking press 1 else 0 : "))

    # checks confirmation if true then calls createRecipt function
    # else call to the home page
    if confirmation == 0:
        first_page()
    else:
        # update no of availability of seats
        seatsAvailable[travelingCity][destination] = seatsAvailable[travelingCity][destination]-noOfSeats
        # create recipt
        createRecipt(name, email, phoneNumber,
                     travelingCity, destination, noOfSeats)
        options()

# function to cancelbooking to cancel ticket booking


def cancelBooking():
    heading("Cancel Booking")

    # take detail of traveling city
    print("\nYou were traveling from : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    travelingCity = int(input("\n")) - 1

    # take detail of destination city
    print("\n\nYour destination was : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    destination = int(input("\n")) - 1

    noOfSeats = int(input("\nNo of seats you want to cancel : "))
    confirmation = int(input("To cancel your booking press 1 else 0 : "))

    # checks confirmation if true then updates the number of available seats
    # else call to the home page
    if confirmation == 0:
        first_page()
    else:
        # update no of availability of seats
        seatsAvailable[travelingCity][destination] = seatsAvailable[travelingCity][destination]+noOfSeats
        # create recipt
        print("\nYour booking has been cancelled")
        options()


# fuction for admin accessibility and admin options


def admin():
    heading("Admin")

    # code for admin functionality
    userName = input("User Name : ")
    password = input("Enter password :")

    if (userName == adminName and password == adminPassword):
        adminOptions()
    else:
        print("Wrong credentials ")
        next = int(
            input("To enter again press 1 or return to home page press 0 : "))
        if next == 1:
            admin()
        else:
            first_page()


def adminOptions():
    heading("admin")
    print("Press key to :")
    print("1- Update No of seats")
    print("2- Update fare rates")
    print("3- Update admin details")
    print("4- Return to Home page")
    print("0- To exit")

    user_input = int(input("\n"))
    if user_input == 0:
        exit()
    elif user_input == 1:
        updateSeats()
        adminOptions()
    elif user_input == 2:
        updateRates()
        adminOptions()

    elif user_input == 3:
        updateAdminDetails()
        adminOptions()

    elif user_input == 4:
        first_page()
    else:
        first_page()


def updateSeats():
    print("Update availble seat deatails of : ")
    print("\n City : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    travelingCity = int(input("\n")) - 1

    print("\nTo city : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    destination = int(input("\n")) - 1

    newSeats = int(input("Enter new number of avaialable seats are :"))
    seatsAvailable[travelingCity][destination] = newSeats
    print("Seats have been updated")
    input("\Go back press 1")


def updateRates():
    print("Update fare deatails of : ")
    print("\n City : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    travelingCity = int(input("\n")) - 1

    print("\nTo city : ")
    for i in range(0, 6):
        print(i+1, "-", cityNames[i])
    destination = int(input("\n")) - 1

    newFareRates = int(input("Enter new fare rates are :"))
    fareRates[travelingCity][destination] = newFareRates
    print("Fare rates have been updated")
    input("\Go back press 1")


def updateAdminDetails():
    print("Update Admin deatails :")

    updatedAdminName = input("Enter new username :")
    updatedAdminPassword = input("Enter new password :")

    global adminName
    global adminPassword

    adminName = updatedAdminName
    adminPassword = updatedAdminPassword
    print("\nAdmin username and password have been updated")
    input("\nGo back press 1 :")


# main_function checkout the options and calls the repective function


def main_functions(user_input):
    if user_input == 0:
        exit()
    elif user_input == 1:
        travelDetails()
    elif user_input == 2:
        seatBooking()
    elif user_input == 3:
        cancelBooking()
    elif user_input == 4:
        first_page()
    elif user_input == 5:
        admin()
    else:
        first_page()

# options futher details


# homepage
# heading to top title bar
# options() show the options to slect for futher details


def first_page():
    heading("Welcome to Shahi Express")
    options()

# main function
# while to keep it until it is exited


def main():
    while True:
        first_page()


main()
