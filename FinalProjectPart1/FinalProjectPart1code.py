# Trinity Avie PSID: 1819032
# Final Project 1 2348


import csv
from datetime import datetime

# Define a class for outputting inventory data
class OutputInventory:                                           
    # Initialize the class with a list of item_dictionary
    def __init__(trin, item_list):                               
        trin.item_list = item_list  

# Method to create a full inventory CSV trin_file   
    def full(trin):                                               
        # Open a new CSV trin_file for writing
        with open('FullInventory.csv', 'w') as trin_file:                 
            item_dictionary = trin.item_list
            
            # Define a function to sort item_dictionary by manufacturer
            def get_manufacturer(x):                                 
                return item_dictionary[x]['manufacturer']
            
            # Get a list of keys sorted by manufacturer
            keys = sorted(item_dictionary.keys(), key=get_manufacturer)
            
            # Loop through each current_item in the sorted list
            for current_item in keys:
                # Extract current_item details
                id = current_item
                manufacturer_name = item_dictionary[current_item]['manufacturer']                         
                item_type = item_dictionary[current_item]['item_type']
                price = item_dictionary[current_item]['price']
                item_service_date = item_dictionary[current_item]['service_date']
                damaged = item_dictionary[current_item]['damaged']
                
                # Write current_item details to the CSV trin_file
                trin_file.write('{},{},{},{},{},{}\n'.format(id,manufacturer_name,item_type,price,item_service_date,damaged))   # Method to create inventory trin_files sorted by current_item type


    def by_type(trin):                                                     
        # Get the list of item_dictionary
        item_dictionary = trin.item_list                                              
        # Initialize an empty list to store unique item_types
        item_types = []
        # Get a sorted list of current_item keys
        keys = sorted(item_dictionary.keys())
        # Loop through each current_item
        for current_item in item_dictionary:
            # Get the current_item type
            item_type = item_dictionary[current_item]['item_type']
            # If this type hasn't been encountered before, add it to the list
            if item_type not in item_types:
               item_types.append(item_type)
            # Loop through each unique type
            for type in item_types:
                # Define a filename based on the type
                file_name = type.capitalize() + 'Inventory.csv'
                # Open a new CSV trin_file for writing
                with open(file_name, 'w') as trin_file:
                     # Loop through each current_item key
                     for current_item in keys:
                         # Extract current_item details
                         id = current_item
                         manufacturer_name = item_dictionary[current_item]['manufacturer']                
                         price = item_dictionary[current_item]['price']
                         item_service_date = item_dictionary[current_item]['service_date']
                         damaged = item_dictionary[current_item]['damaged']
                         item_type = item_dictionary[current_item]['item_type']
                         # If the current_item's type matches the current type, write its details to the trin_file
                         if type == item_type:
                            trin_file.write('{},{},{},{},{}\n'.format(id,manufacturer_name, price, item_service_date, damaged))

# This function creates a CSV output trin_file for item_dictionary that are past their service date (i.e., expired)
    def past_service(trin):
        # Get the list of item_dictionary
        item_dictionary = trin.item_list
        # This internal function is used to get the service date of an current_item. It will be used to sort the item_dictionary.
        def get_servicedate(x):
            return item_dictionary[x]['service_date']
        # Here we're sorting the keys of the item_dictionary dictionary based on their service dates
        keys = sorted(item_dictionary.keys(), key=get_servicedate)
        # Open a new trin_file to write the list of item_dictionary into PastServiceDateInventory.csv trin_file
        with open('PastServiceDateInventory.csv', 'w') as trin_file:
            # Loop through each current_item key, which are sorted from oldest to most recent
            for current_item in keys:
                # Extract current_item details
                id = current_item
                manufacturer_name = item_dictionary[current_item]['manufacturer']
                item_type = item_dictionary[current_item]['item_type']
                price = item_dictionary[current_item]['price']
                item_service_date = item_dictionary[current_item]['service_date']
                damaged = item_dictionary[current_item]['damaged']
                # Get today's date
                today = datetime.now().date()
                # Convert the service date to a datetime object
                service_expiration = datetime.strptime(item_service_date, '%m/%d/%Y').date()
                # Check if the current_item is expired
                expired = service_expiration < today
                # If the current_item is expired, write its details to the trin_file
                if expired:
                 trin_file.write('{},{},{},{},{},{}\n'.format(id,manufacturer_name, item_type, price, item_service_date, damaged))

    # This function creates a CSV output trin_file for all item_dictionary that are damaged
    def damaged(trin):
        # Get the list of item_dictionary
        item_dictionary = trin.item_list
        # This internal function is used to get the price of an current_item. It will be used to sort the item_dictionary.
        def get_service_price(x):                                 
            return item_dictionary[x]['price']
        # Here we're sorting the keys of the item_dictionary dictionary based on their price
        keys = sorted(item_dictionary.keys(), key=get_service_price)
        # Open a new trin_file to write the list of item_dictionary into DamagedInventory.csv trin_file
        with open('DamagedInventory.csv', 'w') as trin_file:                     
            # Loop through each current_item key
             for current_item in keys:
                 # Extract current_item details
                 id = current_item
                 manufacturer_name = item_dictionary[current_item]['manufacturer']
                 item_type = item_dictionary[current_item]['item_type']
                 price = item_dictionary[current_item]['price']                                 
                 item_service_date = item_dictionary[current_item]['service_date']
                 damaged = item_dictionary[current_item]['damaged']
                 # If the current_item is damaged, write its details to the trin_file
                 if damaged:
                    trin_file.write('{},{},{},{},{}\n'.format(id,manufacturer_name, item_type, price, item_service_date))  

# This if statement makes sure this script is being run directly and not imported as a module
if __name__ == '__main__':
    # Initialize an empty dictionary to store current_item data
    item_dictionary = {}
    # List of CSV trin_files to be read
    trin_files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    # Iterate through each trin_file in the list
    for trin_file in trin_files:
        # Open the current csv trin_file
        with open(trin_file, 'r') as csv_file:                                        
            # Create a csv reader object
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Iterate through each row in the csv trin_file
            for row in csv_reader:                                              
                # Extract the current_item id from the first column
                item_id = row[0]
                # If the current trin_file is the ManufacturerList.csv
                if trin_file == trin_files[0]:
                    # Initialize a new dictionary for this current_item
                    item_dictionary[item_id] = {}
                    # Extract the manufacturer name, current_item type, and damaged status from the row
                    manufacturer_name = row[1]
                    item_type = row[2]
                    damaged = row[3]
                    # Store these values in the current_item's dictionary
                    item_dictionary[item_id]['manufacturer'] =    manufacturer_name.strip()
                    item_dictionary[item_id]['item_type'] = item_type.strip()
                    item_dictionary[item_id]['damaged'] = damaged
                # If the current trin_file is the PriceList.csv
                elif trin_file == trin_files[1]:
                    # Extract the price from the row and store it in the current_item's dictionary
                    price = row[1]
                    item_dictionary[item_id]['price'] = price
                # If the current trin_file is the ServiceDatesList.csv
                elif trin_file == trin_files[2]:
                    # Extract the service date from the row and store it in the current_item's dictionary
                    item_service_date = row[1]
                    item_dictionary[item_id]['service_date'] = item_service_date


    # Create an instance of OutputInventory with the item_dictionary dictionary as parameter
    inventory = OutputInventory(item_dictionary)    
    # Call the full method of the inventory object to create a full inventory trin_file
    inventory.full()
    # Call the by_type method of the inventory object to create a trin_file with item_dictionary sorted by type
    inventory.by_type()
    # Call the past_service method of the inventory object to create a trin_file with item_dictionary past their service date
    inventory.past_service()
    # Call the damaged method of the inventory object to create a trin_file with damaged item_dictionary
    inventory.damaged()
