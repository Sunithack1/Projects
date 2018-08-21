'''Calculator to convert RGB values to Hex values using Bitwise operator'''

def rgb_hex():
  invalid_msg = "Invalid value!"
  red = int(raw_input("Enter a value for red(R): "))
  if red < 0 or red > 255:
    print invalid_msg
    return
  green = int(raw_input("Enter a value for green(G): "))
  if green < 0 or green > 255:
    print invalid_msg
    return 
  blue = int(raw_input("Enter a value for blue(B): "))
  if blue < 0 or blue > 255:
    print invalid_msg
    return
  val = (red << 16) + (green << 8) + blue
  print hex(val)[2:].upper()
def hex_rgb():
  hex_val = raw_input("Enter a hexadecimal value: ")
  if len(hex_val) != 6:
    print "Invalid hex value!"
    return
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = (hex_val >> 8)
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print "rgb(%s, %s, %s)" % (red, green, blue)
def convert():
  while(True):
   option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
   if option == '1':
     print "RGB to Hex..."
     rgb_hex()
   elif option == '2':
     print "Hex to RGB..."
     hex_rgb()
   elif option == 'X' or option == 'x':
     break
   else:
     print "Error"
convert()