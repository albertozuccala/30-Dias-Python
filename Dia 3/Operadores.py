'''
Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10
Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

edad = 50
altura = 75.5
complejo = 25 +2j

'''
(area = 0.5 x b x h)
b = input("Ingrese la base del Triángulo: ")
h = input("Ingrese la altura del triángulo: ")
area = (0.5 * float(b) * float(h))
print("El área del triángulo es:", area)
'''

'''
perímetro = a + b + c
a = input("Ingrese el lado a del triángulo: ")
b = input("Ingrese el lado b del triángulo:")
c = input("Ingrese el lado c del triángulo: ")
perimetro = int(a) + int(b) + int(c)
print ("El perímetro del triángulo es: ",perimetro)
'''

'''
largo = input("Ingrese el largo del rectangulo: ")
ancho = input("Ingrese el ancho del rectangulo: ")
area = float(largo) * float(ancho)
print ("El area del rectangulo es: ", area)

perímetro = 2 * (float(largo) + float(ancho))
print("El perímetro del rectangulo es: ", perímetro)
'''

'''
pi = 3.14
r = 2
area = (pi * r * r)
print("El área del Círculo es: ", area)

c = (2 * pi * r)
print("La circunferencia del círculo es: ", c)
'''