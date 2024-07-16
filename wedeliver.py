class Driver:
    def __init__(self, worker_id, name, start_city):
        self.worker_id = worker_id
        self.name = name
        self.start_city = start_city
        
class CityNode:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)


class WeDeliver:
    # Constructor
    def __init__(self):
        # Initialize with predefined cities 
        self.drivers = []
        self.cities = {}
        self.create_initial_cities()
    
    #Each instance of the CityNode class represents a city by storing its name.
    def create_initial_cities(self):
        akkar = CityNode("Akkar")
        beirut = CityNode("Beirut")
        saida = CityNode("Saida")
        tripoli = CityNode("Tripoli")
        jbeil = CityNode("Jbeil")

        akkar.add_neighbor(beirut)
        akkar.add_neighbor(tripoli)
        beirut.add_neighbor(akkar)
        beirut.add_neighbor(saida)
        saida.add_neighbor(beirut)
        tripoli.add_neighbor(akkar)

        self.cities = {
            "Akkar": akkar,
            "Beirut": beirut,
            "Saida": saida,
            "Tripoli": tripoli,
            "Jbeil": jbeil
        }

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
    # implementation of drivers_menu           
    def drivers_menu(self):
        while True:
            print("\nDrivers' Menu:")
            print("1. To view all the drivers")
            print("2. To add a driver")
            print("3. To go back to main menu")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                self.view_drivers()
            elif choice == "2":
                self.add_driver()
            elif choice == "3":
                self.main_menu()
            else:
                print("Invalid choice. Please try again.")

    # view all drivers function
    def view_drivers(self):
        if not self.drivers:
            print("No drivers available.")
        else:
            for driver in self.drivers:
                print(f"{driver.driver_id}, {driver.name}, {driver.start_city}")
    
    # view all drivers function
    def add_driver(self):
        name = input("Enter the driver's name: ")
        start_city = input("Enter the start city: ")
        
        if start_city not in self.cities:
            add_city = input(f"City '{start_city}' not found. Would you like to add it to the database? (yes/no): ")
            if add_city.lower() == 'yes':
                new_city = CityNode(start_city)
                self.cities[start_city] = new_city
            else:
                print("Driver not added.")
                return
        
        new_id = f"ID{len(self.drivers) + 1:03d}"
        new_driver = Driver(new_id, name, start_city)
        self.drivers.append(new_driver)
        print(f"Driver {name} added successfully with ID {new_id}.")
       
    # Implementation of cities_menu
    def cities_menu(self):
        while True:
            print("\nCities' Menu:")
            print("1. Show cities")
            print("2. Print neighboring cities")
            print("3. Print drivers delivering to city")
            print("4. Go back to main menu")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                self.show_cities()
            elif choice == "2":
                self.print_neighboring_cities()
            elif choice == "3":
                self.print_drivers_delivering_to_city()
            elif choice == "4":
                self.main_menu()
            else:
                print("Invalid choice. Please try again.")

    def show_cities(self):
          if not self.cities:
              print("No cities available.")
          else:
              for city in self.cities:
                  print(city)   
    
    

# Initialize the system
system = WeDeliver()
system.main_menu()
