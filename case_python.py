#!/bin/python

################
#Match and Case
################

car = input("What is your favourite car model\n")

match car:
    case "benz":
        print ("Best car on wheels")
    case "bmw":
        print ("Fastest car on four")
    case "Hummer":
        print ("Leave that to the military")
    case _:
        print ("You must be a lady hahaha")
