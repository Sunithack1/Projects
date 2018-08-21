'''This program does the following:
1) Prompt the user to select a shape.
2) Calculate the area of that shape.
3) Print the area of that shape to the user.'''
#letting the user know the calculator is starting up
print "Area calculator is now running!"
#ask the user what shape to calculate the area
option = raw_input("Enter C for Circle or T for Triangle: ")
#an if statement that will check if the option the user entered is 'C' for circle.
if (option == 'C'):
  #Prompt the user to input the radius. The entered radius will be string, so converting to floating point number for calculation purposes
  radius = float(raw_input("Enter radius: "))
  #calculate area of circle
  area = 3.14159 * radius ** 2
  #printing the area of the circle using string formatting
  print "Area of the circle = %s" % (area)
#chech if user entered 'T' for triangle
elif (option == "T"):
  #Prompt user to enter the base of the triangle and convert the resulting string to float number
  base = float(raw_input("Enter the base of the triangle: "))
  #Prompt the user to entr the height of triangle and convert it to floating point number
  height = float(raw_input("Enter the height of the triangle: "))
  #calculate the area area=1/2*bh
  area = 0.5 * base * height
  #printing the area using string formatting
  print "Area of the triangle = %s" % (area)
#else block for invalid shape
else:
  print "The shape you entered is invalid"
#Letting user know that program is exiting
print "The program is exiting now"