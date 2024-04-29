class CarFinder:
   def __init__(self):
       self.allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Rivian R1T', 'Ram 1500']
   def print_allowed_vehicles(self):
       print("Allowed Vehicles:")
       for vehicle in self.allowed_vehicles:
           print(vehicle)
   def display_menu(self):
       print("\n------ AutoCountry Vehicle Finder v0.5 ------")
       print("Please Enter the following number below from the following menu:")
       print("1. Print all allowed Vehicles")
       print("2. SEARCH for Authorized Vehicle")
       print("3. ADD Authorized Vehicle")
       print("4. DELETE Authorized Vehicle")
       print("5. Exit")
   def run(self):
       while True:
           self.display_menu()
           choice = input("Enter your choice: ")
           if choice == '1':
               self.print_allowed_vehicles()
           elif choice == '2':
             vehicle_name = input("Enter the name of the authorized vehicle:")
             if vehicle_name in self.allowed_vehicles:
               print("Authorized Vehicle:", vehicle_name)
             if vehicle_name not in self.allowed_vehicles:
               print("Is not an authorized vehicle:", vehicle_name)

           elif choice == '3':
               new_vehicle = input("Enter the name of the new authorized vehicle:")
               self.allowed_vehicles.append(new_vehicle)
               print("You have added " + new_vehicle + " as an authorized vehicle")
           elif choice == '4':
            delete_vehicle = input("Enter the name of the authorized vehicle to delete:")
            print("Are you sure you want to remove "+ delete_vehicle +" from the Authorized Vehicles List?")
            input(print("Enter YES or NO")) 
            if input == "YES" or "yes":
             print("You have REMOVED "+ delete_vehicle +" as an authorized vehicle")
            else:
             print(delete_vehicle +" has NOT been removed from the Authorized Vehicles List")
            if delete_vehicle in self.allowed_vehicles:
              self.allowed_vehicles.remove(delete_vehicle)
           if input == "NO" or "no":    
             
            if choice == '5':
             print("Thank you for using the AutoCountry Vehicle Finder, good-bye!!")
             break
           def my_function(Vehicles):
             print("Hello from a function")
             my_function ("to PRINT all Authorized Vehicles")
             my_function ("to SEARCH for Authorized Vehicle")
             my_function ("to ADD Authorized Vehicle")
             my_function ("to DELETE Authorized Vehicle")
           
if __name__ == "__main__":
   car_finder = CarFinder()
   car_finder.run()