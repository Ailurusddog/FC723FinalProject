class SeatBooking:
    def __init__(self):
        # Initialize the seating chart with all seats marked as "Free" (F)
        # and a dictionary to store booking references and customer data
        self.seats = [['F' for _ in range(80)] for _ in range(7)]
        self.bookings = {}  # Dictionary to store booking references and customer names
        self.column_map = {'A': 0, 'B': 1, 'C': 2, 'X': 3, 'D': 4, 'E': 5, 'F': 6}
        self.setup_special_seats()

    def setup_special_seats(self):
        # Set up aisles (X) and storage areas (S) in the seating chart
        # The 4th column (index 3) is marked as an aisle for all 80 rows
        for i in range(80):
            self.seats[3][i] = 'X'  # Mark the entire 4th column as an aisle
        # The last three rows of columns D, E, F (indexes 4, 5, 6) are marked as storage areas
        for i in range(77, 80):
            for j in range(4, 7):
                self.seats[j][i] = 'S'  # Mark the last three rows of columns D, E, F as storage areas

    def check_availability(self, row, col):
        # Check if the seat at the specified row and column is free
        # The method returns True if the seat is free (marked as 'F'), otherwise False
        col_index = self.column_map.get(col)
        if col_index is not None and col != 'X':
            return self.seats[col_index][row] == 'F'
        return False

    def book_seat(self, row, col, customer_name):
        # Book the seat if it is available and store the customer data
        # The seat is marked as "Reserved" (R) if it is available, and the booking reference
        # along with the customer name is stored in the bookings dictionary
        col_index = self.column_map.get(col)
        if col_index is not None and col != 'X' and self.check_availability(row, col):
            self.seats[col_index][row] = 'R'  # Mark the seat as "Reserved" (R)
            booking_reference = f"{col}{row + 1}"
            self.bookings[booking_reference] = customer_name
            return True
        return False

    def free_seat(self, row, col):
        # Free the seat if it is currently reserved and remove the customer data
        # The seat is marked as "Free" (F) and the booking reference is removed from the bookings dictionary
        col_index = self.column_map.get(col)
        if col_index is not None and col != 'X' and self.seats[col_index][row] == 'R':
            self.seats[col_index][row] = 'F'  # Mark the seat as "Free" (F)
            booking_reference = f"{col}{row + 1}"
            if booking_reference in self.bookings:
                del self.bookings[booking_reference]
            return True
        return False

    def show_booking_state(self):
        # Display the current booking state of all seats in the seating chart
        # and show the current bookings with seat references and customer names
        for i in range(80):
            for j in range(7):
                print(self.seats[j][i], end=' ')
            print()
        print("\nCurrent Bookings:")
        for ref, customer in self.bookings.items():
            print(f"Seat {ref}: {customer}")

    def menu(self):
        while True:
            print("\n1. Check seat availability")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking state")
            print("5. Exit program")

            choice = input("Choose an option: ")
            if choice == '1':
                # Check seat availability
                row = int(input("Enter row number: ")) - 1
                col = input("Enter column letter (A-F): ").upper()
                if col == 'X':
                    print("This is an aisle, please enter A-F.")
                elif col not in self.column_map:
                    print("Invalid column letter.")
                elif self.check_availability(row, col):
                    print("Seat is available")
                else:
                    print("Seat is already reserved or invalid")
            elif choice == '2':
                # Book a seat
                row = int(input("Enter row number: ")) - 1
                col = input("Enter column letter (A-F): ").upper()
                customer_name = input("Enter customer name: ")
                if col == 'X':
                    print("This is an aisle, please enter A-F.")
                elif col not in self.column_map:
                    print("Invalid column letter.")
                elif self.book_seat(row, col, customer_name):
                    print("Seat successfully booked")
                else:
                    print("Seat is unavailable or invalid")
            elif choice == '3':
                # Free a seat
                row = int(input("Enter row number: ")) - 1
                col = input("Enter column letter (A-F): ").upper()
                if col == 'X':
                    print("This is an aisle, please enter A-F.")
                elif col not in self.column_map:
                    print("Invalid column letter.")
                elif self.free_seat(row, col):
                    print("Seat successfully freed")
                else:
                    print("Seat was not reserved or invalid")
            elif choice == '4':
                # Show booking state
                self.show_booking_state()
            elif choice == '5':
                # Exit the program
                break
            else:
                print("Invalid option, please try again")

# Run the program
seat_booking = SeatBooking()
seat_booking.menu()
