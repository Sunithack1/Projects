'''View the calendar
Add an event to the calendar
Update an existing event
Delete an existing event'''

'''View the calendar
Add an event to the calendar
Update an existing event
Delete an existing event'''
from time import sleep, strftime
FIRST_NAME = "SUNITHA"
calender = {}
def welcome():
  print "Hi " + FIRST_NAME + "! Welcome to your Calender"
  print "Calender is now opening..."
  sleep(1)
  print "Current date is: " + strftime("%A %B %d, %Y")
  print "Current time is: " + strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"
def start_calender():
  welcome()
  start = True
  while start == True:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit:")
    user_choice =user_choice.upper()
    if user_choice == 'V':
      if len(calender.keys()) < 1:
        print "Your calender is empty"
      else:
        print calender
    elif user_choice == 'U':
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calender[date] = update
      print "Successfully Updated!"
      print calender
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date(MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print "The date you entered is invalid!"
        try_again = raw_input("Try Again? Y for Yes, N for No: ").upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calender[date] = event
        print "Event added Successfully!"
        print calender
    elif user_choice == 'D':
      if len(calender.keys()) < 1:
        print "calender is empty!"          
      else:
        event = raw_input("What event? ")
        for date in calender.keys():
          if event == calender[date]:
            del calender[date]
            print "Deleted event successfully!"
            print calender
            break
        else:
          print "Event entered is incorrect!"
    elif user_choice == 'X':
      start = False
    else:
      print "Invalid command!"
      start = False
start_calender()              
              
              
              
              
              
              
          
          
          
          
          
          
          
          
      
      
      
      
      
      
      
      
      
      
        
        
        
          
    