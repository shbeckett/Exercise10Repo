#imported getpass to hide user input - generates warning that it won't work on the terminal so how do you know it's worked?
import getpass
password = 5678
maxattempts = 3
#start index at 0
i=0
# while loop for < maxattempts to allow quick change and enforce three goes - initially nested these loops the wrong way around
while i < maxattempts:
    # had to cast pin as int otherwise couldn't use == as comparison operator for PIN
 supplied_pin = int(getpass.getpass("Please enter your PIN. You have " + str(maxattempts - i) + " attempts remaining" ))
    #nested if loop
 if supplied_pin == password:
  print("PIN correct")
  #need to stop the loop after a correct PIN so
  break
 else:
     #had to cast maxattempts-i as str otherwise concatenation failed for message re:input nb also had to reassign supplied_pin so had to cast as int again
  print("Incorrect PIN")
  #need the indexing value to add 1 here to cap pin attempts
  i+=1
else:
  print("I've just eaten your card!")
