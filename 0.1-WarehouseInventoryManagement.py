#!/usr/bin/python3
import random

class WarehouseInventory:
    """Class to manage a warehouse inventory with limitations on total 
        weight and number of items.
    """

    def __init__(self, capacity, weight_limit):
        """
        Initializes the WarehouseInventory class.

        Parameters:
        - capacity (int): Maximum number of items the warehouse can store.
        - weight_limit (float): Maximum total weight the warehouse can hold.
        """
        self.capacity = capacity
        self.weight_limit = weight_limit
        self.total_items_processed = 0  # Tracking total items processed
        self.total_weight_processed = 0  # Tracking total weight processed
        self.items = []  # List to store processed items

    def process_items(self):
        """
        Processes items and adds them to the warehouse inventory until limitations 
        are met.
        """
        while self.total_items_processed < self.capacity and 
        self.total_weight_processed <= self.weight_limit:
            # Generating random item weight
            item_weight = round(random.uniform(0.2, 0.5), 2)
            if self.total_weight_processed + item_weight <= self.weight_limit:
                # If adding the current item doesn't exceed weight limit, add it to the inventory
                self.items.append(item_weight)
                self.total_items_processed += 1  # Increment total items processed count
                self.total_weight_processed += item_weight  # Update total weight processed
                print(f"Processing item: {self.total_items_processed}, Weight: {item_weight}")
            else:
                break  # Break the loop if weight limit is exceeded
        # Display final inventory status
        print(f"Warehouse inventory full. Total items stored: {self.total_items_processed}, Total weight: {self.total_weight_processed} units")

    def get_total_items_processed(self):
        """
        Retrieves the total number of items processed.

        Returns:
        - int: Total number of items processed.
        """
        return self.total_items_processed

    def get_total_weight_processed(self):
        """
        Retrieves the total weight of items processed.

        Returns::wq
        - float: Total weight of items processed.
        """
        return self.total_weight_processed
