version I by ashu774:
----------------------------
def f(n):
    result = []
    numbers = range(2, n)
    iteration = 0
    
    while len(numbers) > 0:
        iteration += 1
        #pop out the first element of the numbers 
        num = numbers.pop(0)
        result.append(num)
        copyNumbers = numbers[:]
        aTup = ()
        for i in copyNumbers:
            if i % num == 0:
                aTup += (i,)

        print "Iteration Number:", iteration
        print "number added to result:", num
        for e in aTup:
            numbers.remove(e)

        print "Tuple of all numbers divisible by num:" , aTup
        print "list numbers after removing all e in aTup:", numbers
        print "----------------"
            
    print "result:", result
    return len(result)

print f(100)
# expected result 168
===================================================================================================================

version II by the course:
--------------------------

n = 1000
numbers = range(2, n)
results = []

while numbers != []:
    results.append(numbers[0])
    numbers = [n for n in numbers if n % numbers[0] != 0]

print len(results)