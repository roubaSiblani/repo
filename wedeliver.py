class Driver:
    def __init__(self, worker_id, name, start_city):
        self.worker_id = worker_id
        self.name = name
        self.start_city = start_city

class WeDeliver:
    # Constructor
    def __init__(self):
        self.drivers = []  
        self.cities = ["Akkar", "Saida", "Jbeil"]  
        self.deliveries = {}
        self.driver_id_counter = 1

    # The main menu of the system  
    def main_menu(self):
        choice = None
        while choice != "3":
            print("Hello! Please enter:")
            print("1. To go to the drivers’ menu")
            print("2. To go to the cities’ menu")
            print("3. To exit the system")

            choice = input("Select an option:")

            if choice == "1":
                self.drivers_menu()  
            elif choice == "2":
                self.cities_menu()  
            elif choice == "3":
                print("Exit system, Goodbye!")
            else:
                print("Invalid choice, please try again")
    
    # Placeholder for the drivers menu 
    def drivers_menu(self):
        print("Drivers menu is not yet implemented")

    # Placeholder for the cities menu 
    def cities_menu(self):
        print("Cities menu is not yet implemented")

# Initialize the system
system = WeDeliver()
system.main_menu()
