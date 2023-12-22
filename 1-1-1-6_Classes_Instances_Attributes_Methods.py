#!/usr/bin/python3
"""class representing a mobile phone"""


class MobilePhone:
    def __init__(self, number):
        """initializing the number passed as arguement"""
        self.number = number
    
    def turn_on(self):
        """return the message; mobile number is turned on """
        return print("mobile phone {} is turned on".format(self.number))
    
    def turn_off(self):
        """return the message; mobile number is turned on """
        return "mobile phone is turned off"

    def call(self, number):
        """ return the message 'call the number' """
        return print("call {}".format(number))

mike_number = MobilePhone("01632-960004")
bard_number = MobilePhone("01632-960012")

mike_number.turn_on()
bard_number.turn_on()

mike_number.call("555-34343")
print(mike_number.turn_off())
print(bard_number.turn_off())
