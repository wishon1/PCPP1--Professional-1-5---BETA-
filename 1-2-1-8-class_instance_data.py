#!/usr/bin/python3
"""Application to monitor the packaging process of apples for a shop owner's order."""
import random


class Apple:
    """Class to represent apples in the packaging process"""

    counter = 0
    total_weight = 0

    def __init__(self, weight):
        """
        Initializes an apple with a specific weight.
        
        Args:
        weight (float): The weight of the apple.
        """
        self.weight = weight
        Apple.total_weight += weight
        Apple.counter += 1

# Simulate the packaging process
while Apple.counter < 1000 and Apple.total_weight < 300:
    new_apple_weight = random.uniform(0.2, 0.5)
    apple = Apple(new_apple_weight)

print('A limit has been reached. The order details:')
print('# of apples:', Apple.counter)
print('Total weight:', round(Apple.total_weight, 2))

