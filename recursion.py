def sqrt(x):
	return x**.5
def square(x):
	return x**2
def factorial(x):
	if x == 0:
		return 1
	else:
		return x*(factorial(x-1))

def factorialsum(x):
	if x == 0:
		return 0
	else:
		return x+(factorialsum(x-1))
def fibonacci(x):
	if x == 0:
		return 1
	if x == 1:
		return 1
	else:

		return fibonacci(x-1)+fibonacci(x-2)
base = 2
notation1 = []
def prime_factorization(x, basenumber, notation):
	if basenumber <= x:
		if x % basenumber == 0:
			notation += [basenumber]
			x_1 = x/basenumber
			prime_factorization(x_1, basenumber, notation)
			return notation
		else:
			x_1 = x
			basenumber += 1
			prime_factorization(x_1, basenumber, notation)
 			return notation




number = input('What is the starting number?: ')

#factorial of their number
print 'Square Root of %d:' % number
print sqrt(number)
print ' '
print '%d squared:' % number
print square(number)
print ' '
print 'Factorial Sum of %d:' % number
print factorialsum(number)
print ' '
print '%d Factorial:' % number		
print factorial(number)
print ' '
print 'Fibonacci sequence up to %d:' % number
print fibonacci(number)
print ' '
print 'Prime Factorization of %d' % number
print prime_factorization(number,base,notation1)