# In this module we will create a class for bike rental classes and methods.
import random

class ClientType:
    """This class is used to define the client type"""
    INDIVIDUAL = 1
    FAMILLY = 2

class Client:
    """This class is used to define a client"""

    def __init__(self, id:int):
        
        self.clients = []
        self.id = id
            
    def add_client(self, id: int, name: str, email: str, phone: str, password: str,
                   client_type: ClientType=None):
        # This method will add a new client in the memory.
        if not self.validate_phone(phone):
            return print("Invalid phone number format.")
        else:    
            client = {"id": id, "name": name, "email": email, "phone": phone,"password": password, "client_type": client_type}
            self.clients.append(client)
        return print(f'{name} added successfully has a client')
    
    
    def edit_client(self, id: int, name: str=None, email: str=None, phone: str=None,
                    password: str=None, client_type: ClientType=None):
        # This method will edit a client's information.
        if not self.validate_phone(phone) and phone is not None:
            return "Invalid phone number format."
        
        for client in self.clients:
            if client['id'] == id:
                if name is not None:
                    client['name'] = name
                if email is not None:
                    client['email'] = email
                if phone is not None:
                    client['phone'] = phone
                if password is not None:
                    client['password'] = password
                if client_type is not None:
                    client['client_type'] = client_type
        return "Client information updated successfully."
    
    def validate_phone(self, phone: str):
        # This method validates the phone number format.
        # The phone number should be a string of 10 digits.
        return phone is not None and len(phone) == 10


class Magasin:
    """This class is used to define a magasin"""
    
    hourly_rate = {"period": "hourly", "price": 10, "minutes": 60}
    daily_rate = {"period": "daily", "price": 30, "minutes": 1440}
    weekly_rate = {"period": "weekly", "price": 150, "minutes": 10080}
    family_rate = [hourly_rate, daily_rate, weekly_rate]
        
   
    def __init__(self, id: int, inventory : dict = {}):
        """
        Args:
            id (int): id of the client
            iventory (dict): inventory of the magasin 
        """
        self.id = id
        self.inventory = inventory
                
    def pricing_calculation(self, rental_period: int, rental_type: str, is_family : bool = False):
        """
        This method will calculate the total cost of a rental.
        
            Args:
                rental_period (int): The number of minutes the bike was rented.
                rental_type (str): The type of renting like daily, weekly...
                is_family (bool): Choosing if the renting is for a family or individual.
        
            Returns:
                float: The total cost of the rental.
        """
            
        if rental_type == self.hourly_rate["period"]:
                rate = self.hourly_rate
        elif rental_type == self.daily_rate["period"]:
                rate = self.daily_rate
        elif rental_type == self.weekly_rate["period"]:
                rate = self.weekly_rate
        elif is_family:
                # Family rate applies to any hourly, daily, or weekly rate
                rate = {"period": rental_type, "price": 0.7 * getattr(self, f"{rental_type}_rate")["price"],
                        "minutes": getattr(self, f"{rental_type}_rate")["minutes"]}
        else:
            return None # Rental type not recognized
        
        rate_minutes = rate["minutes"]
        rate_price = rate["price"]
        
        # Calculate the number of whole rental periods
        num_periods = rental_period // rate_minutes
        
        # Calculate the remaining rental time in minutes
        remainder_minutes = rental_period % rate_minutes
        
        # Calculate the proportionate price for the remaining rental time
        remainder_price = (remainder_minutes / rate_minutes) * rate_price
        
        # Calculate the total cost
        total_cost = (num_periods * rate_price) + remainder_price
        
        # Apply family rate discount:
        if is_family:
                total_cost *= 0.7
        
        return total_cost

    def make_invoice(self, rental_period: dict, rental_type: dict, is_family: bool = False):
        """ This method will create an invoice for the client.
        Args: 
            rental_period (dict): The number of minutes the bike was rented.
            rental_type (dict): The type of renting like daily, weekly...
            is_family (bool): Choosing if the renting is for a family or individual.
        """
        total_cost = self.pricing_calculation(rental_period, rental_type, is_family)
        if total_cost is None:
                return None # Rental type not recognized
        else:
                invoice = {
                    "rental_period": rental_period,
                    "rental_type": rental_type,
                    "is_family_rate": is_family,
                    "total_cost": total_cost
                }
                return invoice

    def display_inventory(self):
        """This method will display the inventory of the magasin"""
        
        colors = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'orange']
        status = ['rented', 'not rented']

        self.inventory = {}

        for i in range(1, 101):
            color = random.choice(colors)
            rented = random.choice(status)
            self.inventory[i] = {'color': color, 'status': rented}
            
        for bike_id, bike_info in self.inventory.items():
            print(f"Bike ID: {bike_id}, Color: {bike_info['color']}, Status: {bike_info['status']}")

    def count_available_bikes(self):
        """This method will return the number of bikes available for rent"""
        available_count = 0
        for bike_info in self.inventory.values():
            if bike_info['status'] == 'not rented':
                available_count += 1
        # Print an error message if stock is 0 or less.
            elif available_count <= 0:
                print("No bikes available for rent.")
            
        return available_count


class Location(Magasin):
    """class used declare the status of the location"""
    def __init__(self, id: int, status: bool):
        """
        Init method for the Location class.

        Args:
            id (int): The client id
            status (bool): status if rented or not
        """
        
        self.id = id
        self.status = status
                
    def start_location(self):
        """This method will start the location"""
        start = Magasin(id=id)
        count = start.count_available_bikes()
        
        # start a location in the prompt 
        
        if count < 0:
             self.status = True
             return "Location started successfully."
        
        # Prompt the user for rental period and type
        period = int(input("Enter rental period in minutes: "))
        type = input("Enter rental type (hourly, daily, weekly): ")
        family = int(input("Is this rental for a family? (0/1): "))
        
        total_cost = Magasin.make_invoice(self, period, type, family)
    
        return print(f"Total cost: {total_cost}")
            

def main():
    
    # Create a Client object
    client = Client(id=1)
    
    # Create a Location object
    location = Location(id=1, status=True)
    
    # Add prompt for client too add their information
    client.add_client(id,input("Enter your name: "), input("Enter your email: "),
                      input("Enter your phone number: "), 
                      input("Enter your password:"))
    
    if location.status:
        print("Would you like to see the inventory?")
        answer = input("Enter yes or no: ")
        if answer == "yes":
            location.display_inventory()
        elif answer == "no":
            answer2 = input("Still want to rent a bike? Enter yes or no: ")
        if answer2 == "yes":
            location.start_location()
        else:
            print("Thank you for your visi.")

if __name__ == "__main__":
    main()