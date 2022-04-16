def calc():
	print("______________________")
	print('| __________________ |')
	print('| |Calculate 0.0   | |')
	print('| _________________  |')
	print('| ___ ___ ___   ___| |' )
	print('| |7 |8 | 9|   | -|  |')
	print('| |__|__|__|   |__|  |' )
	print('| |7 |8 | 9|   | +|  |')
	print('| |__|__|__|   |__|  |' )
	print('| |7 |8 | 9|   | /|  |')
	print('| |__|__|__|   |__|  |' )
	print('| |7 |8 | 9|   | *|  |')
	print('| |__|__|__|   |__|  |' )
	print('|____________________|')

def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2

dict = {"+":add,"-":subtract,"*":multiply,"/":divide}

def calculator():
    n1=float(input("Enter the first number: "))
    cont = "yes"
    while cont== "yes":
        for key in dict:
            print(key)
        symbol  = input('Enter the operation u want to do: ')
        n2 = float(input("Enter the second number: "))
        fc = operations[symbol]
        solution = fc(n1,n2)
        print(f"{n1} {symbol} {n2}={solution}")
        n1 = solution
        cont = input("Wanna perform more operation on you answer yes or no?: ")
        if cont.lower()=="yes":
            break
    else:
        print("------------")



