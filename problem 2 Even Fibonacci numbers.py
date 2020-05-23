fib1 = 1
fib2 = 2
fib3 = fib1 + fib2
evenFibSum = 2
while fib3 < 4000000:
	if fib3 %2 == 0:
		evenFibSum +=fib3
	fib1 = fib2
	fib2 = fib3
	fib3 = fib2+fib1
print (evenFibSum)

