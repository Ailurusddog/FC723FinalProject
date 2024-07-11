import random
import string

class SeatBooking:
    def __init__(self):
        # Initialize the seating chart with all seats marked as "Free" (F)
        self.seats = [['F' for _ in range(80)] for _ in range(7)]
        # Map columns A-F to their respective indices in the seating chart
        self.column_map = {'A': 0, 'B': 1, 'C': 2, 'X': 3, 'D': 4, 'E': 5, 'F': 6}
        self.setup_special_seats()
        # Dictionary to store booking references and customer data
        self.bookings = {}
        # Set to keep track of existing booking references to ensure uniqueness
        self.existing_references = set()

    def setup_special_seats(self):
        # Mark the entire 4th column as an aisle (X)
        for i in range(80):
            self.seats[3][i] = 'X'
        # Mark the last three rows of columns D, E, F as storage areas (S)
        for i in range(77, 78):
            for j in range(4, 7):
                self.seats[j][i] = 'S'

    def generate_booking_reference(self):
        """
        Generates a unique 8-character alphanumeric booking reference.
        The function continuously generates random booking references until a unique one is found,
        i.e., one that is not already in the set of existing references. It ensures the uniqueness
        by checking the generated reference against the existing ones.
        Returns:
            str: A unique 8-character alphanumeric booking reference.
        """
        while True:
            # Generate a random 8-character alphanumeric string
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

            # Check if the generated reference is unique
            if reference not in self.existing_references:
                # If unique, add it to the set of existing references
                self.existing_references.add(reference)
                return reference

    def check_availability(self, row, col):
        """
        Checks if the seat at the specified row and column is free.
        Args:
            row (int): The row number of the seat (0-indexed).
            col (str): The column letter of the seat (A-F).
        Returns:
            bool: True if the seat is free (marked as 'F'), otherwise False.
        """
        col_index = self.column_map.get(col)
        if col_index is not None and col != 'X':
            return self.seats[col_index][row] == 'F'
        return False

    def book_seat(self, row, col, passport_number, first_name, last_name):
        """
        Books a seat if it is available and stores the booking reference and customer details.
        Args:
            row (int): The row number of the seat (0-indexed).
            col (str): The column letter of the seat (A-F).
            passport_number (str): The passport number of the customer.
            first_name (str): The first name of the customer.
            last_name (str): The last name of the customer.
        Returns:
            str or None: The booking reference if the seat is successfully booked, else None.
        """
        col_index = self.column_map.get(col)
        if col_index is not None and col != 'X' and self.check_availability(row, col):
            # Generate a unique booking reference
            reference = self.generate_booking_reference()
            # Mark the seat as reserved with the booking reference
            self.seats[col_index][row] = reference
            # Store the booking details in the bookings dictionary
            self.bookings[reference] = {
                'passport_number': passport_number,
                'first_name': first_name,
                'last_name': last_name,
                'row': row,
                'col': col
            }
            return reference
        return None

    def free_seat(self, row, col):
        """
        Frees a reserved seat and removes the customer data.
        Args:
            row (int): The row number of the seat (0-indexed).
            col (str): The column letter of the seat (A-F).
        Returns:
            bool: True if the seat is successfully freed, else False.
        """
        col_index = self.column_map.get(col)
        if col_index is not None and col != 'X':
            reference = self.seats[col_index][row]
            if reference not in ['F', 'S', 'X']:
                # Mark the seat as free
                self.seats[col_index][row] = 'F'
                # Remove the booking from the bookings dictionary
                del self.bookings[reference]
                # Remove the booking reference from the set of existing references
                self.existing_references.remove(reference)
                return True
        return False

    def show_booking_state(self):
        """
        Displays the current booking state of all seats in the seating chart.
        """
        for i in range(80):
            for j in range(7):
                print(self.seats[j][i], end=' ')
            print()

    def menu(self):
        """
        Provides a text-based menu for the user to interact with the seat booking system.
        The user can check seat availability, book a seat, free a seat, show the booking state, or exit the program.
        """
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
                if col not in self.column_map or col == 'X':
                    print("Invalid column letter.")
                elif self.check_availability(row, col):
                    print("Seat is available")
                else:
                    print("Seat is already reserved or invalid")
            elif choice == '2':
                # Book a seat
                row = int(input("Enter row number: ")) - 1
                col = input("Enter column letter (A-F): ").upper()
                passport_number = input("Enter passport number: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                if col not in self.column_map or col == 'X':
                    print("Invalid column letter.")
                else:
                    reference = self.book_seat(row, col, passport_number, first_name, last_name)
                    if reference:
                        print(f"Seat successfully booked. Booking reference: {reference}")
                    else:
                        print("Seat is unavailable or invalid")
            elif choice == '3':
                # Free a seat
                row = int(input("Enter row number: ")) - 1
                col = input("Enter column letter (A-F): ").upper()
                if col not in self.column_map or col == 'X':
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
