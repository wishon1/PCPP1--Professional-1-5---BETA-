* task 1.2.1.8 :
    Scenario
  Imagine that you receive a task description of an application that monitors the process of apple packaging before the apples are sent to a shop.

A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

Write a code that creates objects representing apples as long as both limitations are met. When any limitation is exceeded, than the packaging process is stopped, and your application should print the number of apple class objects created, and the total weight.

Your application should keep track of two parameters:

the number of apples processed, stored as a class variable;
the total weight of the apples processed; stored as a class variable. Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;
Hint: Use a random.uniform(lower, upper) function to create a random number between the lower and upper float values.

* Task 1: Warehouse Inventory Management

+ Scenario:
You're tasked with creating a program for managing a warehouse inventory. The warehouse has a limited capacity and can store items up to a certain weight limit.

Write a code that generates random items (represented as objects) with varying weights and adds them to the inventory as long as both limitations are met (total weight and total number of items). If either limitation is exceeded, the inventory management process should stop, and the program should display the number of items stored and the total weight.

Keep track of two parameters:

The number of items processed, stored as a class variable.
The total weight of the items processed, stored as a class variable. Assume each item's weight is randomly generated and varies between a specified range.
Hint: Utilize a random.uniform(lower, upper) function to generate random weights within a given range for each item.

* Task 2: Vehicle Cargo Loading

Scenario:
You've been assigned the task of creating a program that manages the loading of cargo onto vehicles. Each vehicle has a maximum weight capacity and can accommodate a specific number of items.

Write a code that generates random cargo items (represented as objects) with varying weights. Your program should load these items onto vehicles as long as both limitations (total weight and total number of items) for the vehicle are not exceeded. If either limitation is surpassed, the loading process should halt, and the program should display the number of items loaded and the total weight loaded onto the vehicles.

Track two parameters:

The number of items processed for loading, stored as a class variable.
The total weight of the items processed for loading, stored as a class variable. Assume each cargo item's weight is randomly generated and varies between a specified range.
Hint: Use a random.uniform(lower, upper) function to generate random weights within a defined range for each cargo item.

Both tasks involve managing a set of items with specific limitations (either weight, quantity, or both) and require the program to stop when any of these limitations are exceeded, similar to the apple packaging scenario. The second task, dealing with vehicle cargo loading, could be considered more challenging due to the added complexity of managing items across multiple vehicles and their individual limitations.

