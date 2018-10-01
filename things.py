import math
import turtle

def function0():
    applicant = input('Enter the applicant\'s name:\n')
    interviewer = input('Enter the interviewer\'s name:\n')
    time = input('Enter the appointment time:\n')
    print(interviewer + ' will interview ' + applicant + ' at ' + time +'.')
    
def function1():
    print(math.pi)
    print(math.e)
    print(math.ceil(4.5))
    print(math.floor(4.5))
    print(math.pow(5,5))
    
def function2():
    #flips your name
    first = input('Enter your first name\n')
    last = input('Enter your last name\n')
    print(last + '\n' + first)
    
def function3():
    #Celsius to farenhite
    c = int(input('Enter a temreture in Celsius'))
    f = (c * 1.8) + 32        #This is the celsius to farenhite equation
    print(f)

    print('next')

#Average Finder
    a = int(input('Enter a number'))
    b = int(input('Enter a number'))
    c = int(input('Enter a number'))
    d = int(input('Enter a number'))
    e = int(input('Enter a number'))
    total = math.fsum([a, b, c, d, e])    #Sums all of the numbers
    fTotal = total/5    #Finds the average
    print(fTotal)

    print('next')

#finds how much you are paid
    hours = int(input('Enter hours worked'))
    rate = int(input('Enter dollars per hour'))
    total2 = str(hours * rate)
    print("Total pay is " + total2)

    print('done')
    
def function4():
    #Sings happy birthday to you
    name = input('What is your name\n')
    print('Happy birthday to you\nHappy birthday to you\nHappy birthday to ' + name +'\nHappy birthday to you')

def function5(animal, sound):
    print('Old MacDonald had a farm, Ei-igh, Ee-igh, Oh!')
    print('And on that farm he had a '+ animal + ', Ee-igh, Ee-igh, Oh!')
    print('With a '+sound+sound+' here and a '+sound+sound+'there.')
    print('Here a ' + sound + ',there a ' + sound + ', everywhere a ' + sound + sound)
    print('Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!')

def function6():
          function5('cow', 'moo')
          function5('chicken', 'cluck')
          function5('pig', 'oink')
          function5('sheep', 'baa')
          function5('horse', 'neigh')

def function7(radius):
    area = 3.1415926 * (radius ** 2)
    print(area)
    return (area)

def function8(pricePInch, radius):
    area = function7(radius)
    price = area * pricePInch
    print(price)

def function9(part1, part2):
    cat = part1 + part2
    function10(cat)

def function10(bruce):
    print (bruce)
    print (bruce)
    print(cat)

def function11():
    line1 = 'Bing tiddle '
    line2 = 'tiddle bang'
    function9(line1, line2)

def function12():
    def cube(num):
        cubed_value = num * num * num
        return cubed_value
    
    print(cube(5))
    x = cube(5)
    print(x)

def function13():
    def print_twice(bruce):
        print(bruce)
        print(bruce)

    returnvalue = print_twice('Hello World')
    print(returnvalue)

def function14():
    def sumTo(n):
        x = 0
        for i in range(n + 1):          #Finds the sum of all of the lower numbers
            x = x + i
        return x
    one = int(input('Number 1\n'))
    sumToOne = sumTo(one)
    print(sumToOne)
    two = int(input('Number2\n'))
    sumToTwo = sumTo(two)
    print(sumToTwo)
    three = int(input('Number3\n'))
    sumToThree = sumTo(three)
    print(sumToThree)

def function15():
    i = 0
    def hypotenuse(leg1, leg2):
        a = leg1 ** 2
        b = leg2 ** 2
        ab = a + b
        c = math.sqrt(ab)
        return(c)
    while i <= 2:
        one = int(input('Number 1\n'))
        two = int(input('Number 2\n'))
        result = hypotenuse(one, two)
        print(result)
        i += 1

def function16():
    i = 0
    def cost(pounds):
        cost = (pounds * (10.5 + .86)) + 1.5
        return(cost)
    while i <= 2:
        coffee = int(input('How much coffee would you like to buy?\n'))
        overall = cost(coffee)
        print(overall)
        i += 1

def function17():
    i = 0
    def add(a, b):
        total = str(a + b)
        a = str(a)
        b = str(b)
        print('Adding ' + a + '+' + b)
        return(total)
        
    def multiply(a, b):
        total = str(a * b)
        a = str(a)
        b = str(b)
        print('Multiplying ' + a + '*' + b)
        return(total)
        
    def subtract(a, b):
        total = str(a - b)
        a = str(a)
        b = str(b)
        print('Subracting ' + a + '-' + b)
        return(total)
        
    def divide(a, b):
        total = str(a / b)
        a = str(a)
        b = str(b)
        print('Dividing ' + a + '/' + b)
        return(total)

    def calculate(operation):
        one = int(input('Number 1\n'))
        two = int(input('Number 2\n'))
        total = operation(one, two)
        print(total)

    for i in [1,2]:
        calculate(add)
        calculate(multiply)
        calculate(subtract)
        calculate(divide)

        i += 1
    
def function18():
    for i in [5,4,3,2,1]:
        print(i)
    print('Blastoff')

def function19():
    for i in range(100):
        print('We like Python\'s turtles!')

def function20():
    for x in range(5):
        print(x)
    
    for y in range(1, 6):
        print(y)
    
    for z in range(1, 6, 2):
        print(z)

def function21():
    n = int(input('How many numbers are there?\n'))
    sum = 0.0
    for i in range(n):
        x = int(input('Enter a number\n'))
        sum = sum + x
    print(sum)

def function22():
    principal = float(input('Principal'))
    rate = float(input('Rate'))
    term = int(input('Term'))
    years = term + 1
    totalInterest = 0
    for year in range(1, years):
        print(year)
        print(principal)
        interest = principal * rate
        print(interest)
        principal += interest
        totalInterest += interest
        print(totalInterest)
    print(principal)
    

def intrestCalculater(principal, rate, term):
    years = term + 1
    totalInterest = 0
    for year in range(1, years):
        print(year)
        print(principal)
        interest = principal * rate
        print(interest)
        principal += interest
        totalInterest += interest
        print(totalInterest)
    print(principal)

def function24():
    for x in range(3):
        print(x)
        if x == 1:
            break
    
    print("next")
    
    for x in range(1, 11):
        for y in range(1, 11):
            print ("%d * %d = %d" % (x, y, x*y))
    
    print("next")

    fruits = ['bannana', 'apple', 'mango']
    for fruit in fruits:
        print(fruit)

    print('next')
    
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for list in list_of_lists:
        print(list)
        for x in list:
            print (x)

    print("next")
    
    string = "Hello World"
    for y in string:
        print (y)
    
    print('done')

def function25(year):
    four = year % 4
    hundred = year % 100
    fourHundred = year % 400
    if four == 0 and hundred != 0:
        return(True)
    else:
        if fourHundred == 0:
            return(True)
        else:
            return(False)
    
def function26():
    print(function25(2005))
    print(function25(1900))
    print(function25(2000))
    print(function25(2016))

    print('next')

    number = int(input("Enter a number"))
    if number == 0:
        print('zero')
    elif number > 0:
        print('positive')
    else:
        print('negative')

    print('next')

    hours = int(input('How many hours have you worked'))
    rate = float(input('What is your hourly pay'))

    if hours > 40:
        pay = 40 * rate
        hours -= 40
        rate *= 1.5
        pay1 = hours * rate
        pay += pay1
    else:
        pay = hours * rate
    print(pay)

def function27():
    celsius = float(input('Tempreture in Celsius'))
    fahrenheit = 9 / 5 * celsius + 32
    print(fahrenheit)
    if fahrenheit > 90:
        print('too hot')
    elif fahrenheit < 30:
        print('too cold')
    else:
        print('Good temp')
        
def function28():
    startTime = int(input('Start Time\nPlease input in 24 hour format with minutes but no colen'))
    endTime = int(input('End time\nPlease input in 24 hour format with minutes but no colen'))
    if startTime < endTime:         #In case it ends         past midnight
        if startTime < 2100 and endTime < 2100:
            time = endTime - startTime
            cost = time * .025
            print(cost)
        elif startTime > 2100 and endTime > 2100:
            time = endTime - startTime
            cost = time * .0175         #divided by 100 because the hour is multiplied by 100
            print (cost)
        else:
            time1 = 2100 - startTime
            cost1 = time1 * .025
            time2 = endTime - 2100
            cost2 = time2 * .0175
            totalCost = cost1 + cost2
            print(totalCost)
    else:           #This is for ending past midnight
        if startTime > 2100:     #Start time past 9
            time1 = 2400 - startTime 
            cost1 = time1 * .0175
            cost2 = endTime * .0175
            print(cost1 + cost2)
        else:           #start time before 9
            time1 = 2100 - startTime
            cost1 = time1 * .025
            cost2 = 3 * .0175
            cost3 = endTime * .0175
            totalCost = cost1 + cost2 + cost3
            print(totalCost)

def function29():
    age = int(input('Enter your age'))
    citizenship = int(input('How long have you been a citizen'))
    if age >= 25 and citizenship >= 7:    #Checking for represntative elegatability
        if age >= 30 and citizenship >= 9: #Checking for senator elegatability
            print('Senator and representative')
        else:
            print('Representative')
    else:
        print('Neither sentator nor representative')

def function30():
    for i in range(5):
        credits = int(input('How many credits have you earned'))
        if credits < 7:
            print('Freshman')
        elif credits < 16:
            print('Sophmore')
        elif credits < 26:
            print('Junior')
        else:
            print('Senior')

def function31():
    for i in range(3):
        limit = int(input('Speed Limit'))
        speed = int(input('Clocked Speed'))
        fine = 0
        difference = speed-limit
        #Finds how much faster they were going
        if speed > limit:
            #To make sure we dont fine normal people
            fine = 50
            fine += difference * 5
            #Finds how much to fine people
            if speed > 90:
                fine += 200
        print(fine)

    print('next')


    for i in range(3):
        one = int(input('Shortest Stick Length'))
        two = int(input('Middle Stick Length'))
        three = int(input('Longest Stick Length'))
        #Finds the stick lengths
        shortestTwo = one + two
        #adds the shortest two together
        if shortestTwo > three:    #Finds if there is a triangle
            print('Triangle')
        else:
            print('No triangle')

    print('next')

    highestNumber = int(input('Highest Number'))
    #finds the number to go up to
    for i in range(highestNumber+1):
        three = i % 3
        five = i % 5
        #Determins if divisable by 3 and 5
        if three == 0 and five == 0:
            #Goes when divisable by 3 and 5
            print('FizzBuzz')
        elif three == 0:
            #Goes when divisable by 3
            print('Fizz')
        elif five == 0:
            #Goes when divisable by 5
            print('Buzz')
        else:
            #Prints number if not divisible by 3 or 5
            print(i)    

def function32():
    for i in range(2):
        year1 = int(input('Enter a year'))
        if year1 >= 1900 and year1 <= 2099:
            a = year1 % 19
            b = year1 % 4
            c = year1 % 7
            d = (19 * a + 24) % 30
            e = (2 * b + 4 * c + 6 * d + 5) % 7
            easter = 22 + d + e
            if year1 == 1954 or year1 == 1981 or year1 == 2049 or year1 == 2076:
                easter -= 7
            if easter > 31:
                easter -= 31
                print('April')
            else:
                print('March')
            print(easter)
        else:
            print('Error')
    
    print('next')

    for i in range(2):
        side0 = (int(input('Enter a side length'))) ** 2
        side1 = (int(input('Enter a side length'))) ** 2
        side3 = (int(input('Enter the hypotenuse length'))) ** 2
        side = side0 + side1
        if abs(side - side3) < 0.001:
            print(True)
        else:
            print(False)
        
