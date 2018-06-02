import matplotlib.pyplot as plt
"""Why not eval?
eval() interprets a string as code.

- There is almost always a better way to do it
- Very dangerous and insecure
- Makes debugging difficult
- Slow

--> The reason why so many people have warned about using eval is because a user can 
use this as an option to run code on the computer.
--> If you have eval(input()) and os imported, a person could type into 
input() os.system('rm -R *') which would delete all files in the home directory. 
OR
input that originally came from an untrusted source!!!

*** Using eval() is a security hole.***
"""

def create_coordinate_system(min_range, max_range):
	"""Created by Bilal"""
	plt.title('Übung 6 Aufgabe 3\nBy Ahmed Majid &\nBilal Mussa Abdelkadir')
	plt.axis([min_range, max_range, min_range, max_range])
	# plt.axis('on')
	plt.ylabel('Y-Achse')
	plt.xlabel('X-Achse')

	"""X-Achse simulieren"""
	plt.plot([0, 0, 0], [min_range-5, 0, max_range+5], color='black')
	"""Y-Achse simulieren"""
	plt.plot([min_range-5, 0, max_range+5], [0, 0, 0], color='black')
	return plt

def create_plot(INPUT_FUNCTION, min_range: int, max_range: int):
	"""Created by Ahmed"""
	if INPUT_FUNCTION == 'security_gap':  # Soll die Strings abfangen, die nicht erwünscht sind.
		print("Please don't move I called the Police")
		return 'ERROR'

	create_coordinate_system(min_range, max_range)
	PUNKTE_X_ACHSE = list(range(min_range, max_range+1))
	PUNKTE_Y_ACHSE = list(map(lambda x: eval(INPUT_FUNCTION), PUNKTE_X_ACHSE))
	plt.plot(PUNKTE_X_ACHSE, PUNKTE_Y_ACHSE, label='(Your Function)', color="b")

	plt.legend()
	plt.show()
	return PUNKTE_Y_ACHSE

def main():
	"""Created by Ahmed"""
	while True:
		INPUT_FUNCTION = str(input("Geben Sie eine beliebige Funktion ein(z.B. x+3 und zum potenzieren x**Exponent): "))
		if INPUT_FUNCTION == 'rm -R *':
			print("Oops! please don't harm my System.  Try again...")
			continue
		else:
			break
	create_plot(INPUT_FUNCTION, min_range=-4, max_range=4)


if __name__ == '__main__':
	main()


