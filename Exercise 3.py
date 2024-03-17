#Sum of Digits: Create a program that calculates the sum of the digits of a given number.
def celcius_to_farenheight(celcius):
    farenheight = (celcius*9/5)+32
    print(farenheight)

celsius_temperature = float(input("Enter temperature in Celsius: "))

farenheight = celcius_to_farenheight(celsius_temperature)

