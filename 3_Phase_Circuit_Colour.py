#To calculate the cicuit numbers colour in a 3 phase Canadian 600 volt or lower electrical system
circuit_number = int(input("Enter your circuit number: "))

colour = circuit_number % 6
print(colour)

if colour in range( 1, 3 ):
    print ("Your wire colour should be red")
elif colour in range( 3, 5 ):
    print ("Your wire colour should be black")
else:
    print ("Your wire colour should be blue")
