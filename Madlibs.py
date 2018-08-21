STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world." 

print "Mad Libs has started"
name = raw_input("Enter a name: ")
adjective1 = raw_input("Enter first adjective: ")
adjective2 = raw_input("Enter second adjective: ")
adjective3 = raw_input("Enter third adjective: ")

verb1 = raw_input("Enter a verb: ")

noun1 = raw_input("Enter first noun: ")
noun2 = raw_input("Enter second noun: ")

animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food: ")
fruit = raw_input("Enter a fruit: ")
superhero = raw_input("Enter a superhero: ")
country = raw_input("Enter a country: ")
dessert = raw_input("Enter a dessert: ")
year = raw_input("Enter a year: ")

print STORY % (name, adjective1, adjective2, animal, food, verb1, noun1, fruit, adjective3, name, superhero, name, country, name, dessert, name, year, noun2)