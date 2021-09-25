
fahrenheit = 0
print("Fahrenheit celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8
    print("{:5d} {:72f}".format(fahrenheit,celsius))
    fahrenheit +=25