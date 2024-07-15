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
                break
            else:
                print("Invalid choice. Please try again.")

    # view all drivers function
    def view_drivers(self):
      if not self.drivers:
          print("No drivers available.")
      else:
          for driver in self.drivers:
              print(driver)
    # view all drivers function
    def add_driver(self):
       name = input("Enter driver's name: ")
       start_city = input("Enter driver's start city: ")
       if start_city not in self.cities:
          add_city = input(f"City '{start_city}' not found. Would you like to add it to the database? (yes/no): ")
          if add_city.lower() == 'yes':
             self.cities.append(start_city)
             print(f"City {start_city} added to the database.")

          else:
               print("Driver not added.")
               return  

       driver = Driver(self.driver_id_counter, name, start_city)
       self.drivers.append(driver)
       self.driver_id_counter += 1
       print(f"Driver {name} added successfully!")

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
                break
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
