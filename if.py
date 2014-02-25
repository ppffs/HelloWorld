#!/usr/bin/python
# Filename : if.py

number = 23
running  = True

while running:
	guess = int(raw_input('Enter an inter :' ))

	if guess == number:
		print 'Congratulations, you guessed it.'
		running = False
	elif guess < number:
		print 'No, it is a little higher than that'
	else:
		print 'No, it is a little lower than than'

print 'Done'

for i in range(1,5):
	print i
else:
	print 'The for loop is over'

