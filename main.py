print("Welcome to the Temperature Converter Program")

#user input to get miles per hour value
fahr = float(input("\nEnter the the temperature in degrees Fahrenheit you wish to convert: "))

#convert to celsius and kelvin
cel = (fahr-32)*0.5556
kel = cel+273.15

#round to 4 dp
fahr = round(fahr,4)
cel = round(cel,4)
kel = round(kel,4)

print("\nDegrees Fahrenheit:\t" + str(fahr))
print("Degrees Celsius:\t" + str(cel))
print("Degrees Kelvin:\t\t" + str(kel))