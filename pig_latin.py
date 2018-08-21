'''Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are the steps we'll need to take:
1) Ask the user to input a word in English.
2) Make sure the user entered a valid word.
3) Convert the word from English to Pig Latin.
4) Display the translation result.'''

print 'Welcome to the Pig Latin Translator!'

# Start coding here!
# storing 'ay' in a variable
pyg = 'ay' 
 #storing user entered input to original variable
original = raw_input('Enter a word:')
#if user input is not empty and contains only letters, execute the code block inside
if len(original) > 0 and original.isalpha(): 
  #printing the entered input
  print "You Entered:" + original 
  #coverting the word to lowercase
  word = original.lower() 
   # accessing and storing the first letter
  first = word[0]
  #concatenating lowercase word, first letter and pyg and storing in new_word variable.
  new_word = word + first + pyg 
  #slicing the new_word so that the first letter is removed
  new_word = new_word[1:len(new_word)]
  #printing the pyg latin word
  print "Pig Latin translation: " + new_word
else:
  print 'empty'