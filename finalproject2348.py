# Trinity Avie PSID: 1819032
# Final Project 2348


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
            return item_dictionary[x]['item_service_date']
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
                service_expiration = datetime.strptime(item_service_date, "%m/%d/%y").date()
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

   
    # Initialize empty lists to store unique manufacturers_list and item_types
    item_types = []
    manufacturers_list = []     
    # Iterate over each current_item in the item_dictionary dictionary
    for current_item in item_dictionary:
        # Extract the manufacturer and type for the current current_item
        checked_man = item_dictionary[current_item]['manufacturer']
        checked_item_type = item_dictionary[current_item]['item_type']
        # If the manufacturer of the current current_item is not already in the manufacturers_list list, add it
        if checked_man not in manufacturers_list:
           manufacturers_list.append(checked_man)
        # If the type of the current current_item is not already in the item_types list, add it
        if checked_item_type not in item_types:
           item_types.append(checked_item_type)


    # Initialize user to None
    user = None
    # Loop until user enters 'q'
    while user != 'q':
        # Prompt the user for input
        user = input("\nPlease enter an current_item manufacturer and current_item type (ex: Apple laptop) or enter 'q' to quit:\n")
        # If the user enters 'q', break the loop and end the program
        if user == 'q':
           break
        else:
            # Initialize selected manufacturer and type to None
            select_man = None
            select_item_type = None
            # Split the user input into individual words
            user = user.split()
            # Flag to check if the input is incorrect
            wrong_input = False
            # Iterate over each input in user input
            for input in user:
                # If the input is in manufacturers_list and a manufacturer hasn't been selected yet, select it
                if input in manufacturers_list:
                   if select_man:
                       # If a manufacturer has already been selected, set wrong_input to True
                       wrong_input = True
                   else:
                      select_man = input
                # If the input is in item_types and a type hasn't been selected yet, select it
                elif input in item_types:
                   if select_item_type:
                      # If a type has already been selected, set wrong_input to True
                      wrong_input = True
                   else:
                      select_item_type = input
            # Check if either manufacturer or type is not selected or if input is flagged as bad
            if not select_man or not select_item_type or wrong_input:
               # If so, print an error message
               print("No such current_item in inventory")
            else:
                # Define a function to get the price from each current_item
                def get_service_price(x):
                    return item_dictionary[x]['price']
                # Sort the keys of the item_dictionary dictionary by the price of each current_item
                keys = sorted(item_dictionary.keys(), key=get_service_price)
                # Initialize lists to store matching and similar item_dictionary
                match = []
                similar = {}
                # Iterate over each current_item in the sorted keys list
                for current_item in keys:
                    # Check if the current_item type matches the selected type
                    if item_dictionary[current_item]['item_type'] == select_item_type:
                       # Get the current date and service expiration date of the current_item
                       today = datetime.now().date()
                       item_service_date = item_dictionary[current_item]['item_service_date']
                       service_expiration = datetime.strptime(item_service_date, "%m/%d/%Y").date()
                       # Check if the service expiration date is before today
                       expired = service_expiration < today
                       # If the manufacturer matches the selected manufacturer and the current_item is not expired or damaged, add it to the matching item_dictionary list
                       if item_dictionary[current_item]['manufacturer'] == select_man:
                          if not expired and not item_dictionary[current_item]['damaged']:
                             match.append((current_item, item_dictionary[current_item]))
                       # If the manufacturer does not match but the current_item is not expired or damaged, add it to the similar item_dictionary dictionary
                       else:
                           if not expired and not item_dictionary[current_item]['damaged']:
                              similar[current_item] = item_dictionary[current_item]
                # Check if there are any item_dictionary in the match list
                if match:
                   # If there are, select the first current_item
                   current_item = match[0]
                   # Extract the current_item id, manufacturer name, current_item type, and price from the selected current_item
                   item_id = current_item[0]
                   manufacturer_name = current_item[1]['manufacturer']
                   item_type = current_item[1]['item_type']
                   price = current_item[1]['price']
                   # Print the details of the selected current_item
                   print("Your current_item is: {}, {}, {}, {}\n".format(item_id,    manufacturer_name, item_type, price))

                   # Check if there are any item_dictionary in the similar dictionary
                   if similar:
                       # If there are, initialize variables to track the closest current_item and price difference
                       matched = price
                       closest = None
                       closest_difference = None
                       # Iterate over each current_item in the similar dictionary
                       for current_item in similar:
                           # If this is the first current_item, set it as the closest current_item and calculate the price difference
                           if closest_difference == None:
                              closest = similar[current_item]
                              closest_difference = abs(int(matched) - int(similar[current_item]['price']))
                              item_id = current_item
                              manufacturer_name = similar[current_item]['manufacturer']
                              item_type = similar[current_item]['item_type']
                              price = similar[current_item]['price']
                              continue
                           # Calculate the price difference for the current current_item
                           difference = abs(int(matched) - int(similar[current_item]['price']))
                           # If the price difference is less than the closest price difference, set this current_item as the closest current_item
                           if difference < closest_difference:
                              closest = current_item
                              closest_difference = difference
                              item_id = current_item
                              manufacturer_name = similar[current_item]['manufacturer']
                              item_type = similar[current_item]['item_type']
                              price = similar[current_item]['price']
                        # Print the details of the closest current_item
                       print("You may, also, consider: {}, {}, {}, {}\n".format(item_id,manufacturer_name, item_type, price))
                else:
                    # If there are no item_dictionary in the similar dictionary, print an error message
                    print("No such current_item in inventory")
    