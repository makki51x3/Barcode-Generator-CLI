from barcode import ITF
from barcode.writer import ImageWriter
import os


invalidMode = False

while(True):
	os.system('cls' if os.name == 'nt' else 'clear')
	if invalidMode:
		print("\nMode is unavailable make sure you entered either 'r' or 's'\n")
		invalidMode=False

	print("\n# Choose desired Mode #")
	mode = input("\nEnter 'r' for range, 's' for single generation:\t")

	if(mode.lower()=='r'):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("\n## Range Mode ##")
		start = input("\nEnter starting range:\t")
		finish = input("\nEnter ending range:\t")

		if start.isdigit() and finish.isdigit():
			start = int(start)
			finish = int(finish)+1

			for number in range(start,finish):
				barCode = ITF(str(number), writer=ImageWriter())
				directory = os.path.join( "results", str(number))
				barCode.save(directory)

			os.system('cls' if os.name == 'nt' else 'clear')
			print("\nCheck the 'results' folder for the generated Bar Codes")
			input("\nPress enter to continue...")
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("\n> Error Detected 'Invalid input' <  (Make sure you entered a number!)")
			input("\nPress enter to continue...")			


	elif(mode.lower()=='s'):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("\n## Single Mode ##")
		number = input("\nEnter code number:\t")
		if number.isdigit():
			barCode = ITF(number, writer=ImageWriter())
			directory = os.path.join( "results", str(number))
			barCode.save(directory)
			os.system('cls' if os.name == 'nt' else 'clear')
			print("\nCheck the 'results' folder for the generated Bar Code")
			input("\nPress enter to continue...")
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("\n> Error Detected 'Invalid input' <  (Make sure you entered a number!)")
			input("\nPress enter to continue...")	

	else:
		invalidMode=True




