# ran out of time to do this!
password = 5678
maxattempts = 3

supplied_pin = (input("Enter your PIN: "))
#tried to add a check for sting length here to check if four digitd entered but then did another accidental test with letters...
if len(supplied_pin) ==4:
 i=0
 supplied_pin = int(supplied_pin)
else:
 supplied_pin = (input("You did not enter a four-digit number. Please enter your PIN: "))