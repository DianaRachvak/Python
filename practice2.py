name = ''
while name!= 'your name':
	name = input('Please enter your name: ')
print('Thank you')

num = 0
for i in range (101):
	num=num+i
print (num)


def myFunction(name):
	print(name+" it is me. And I am ", end=' ')
	print (len(name)+19)

myFunction('Diana')

a = 10
b = 20
if a<b:
	print "{} is equal to {}".format(a,b)

#reverse a string
def reverse(r):
	str=""
	for i in r:
		str = i + str
	return str


r = "elephant"

print(reverse(r))


# #set
mySet = {1,2,3,4,5,6,7,8,9}
print("in a set: ", end="")
for i in mySet:
	print(i, end=" ")

# #tupple
print("\n", "in tuple: ", end= "")
myTup = ('tuple', 4, 5.6)
for i in myTup:
	print(i, end=" ")

# #dictionary
myDict = {'name': "Diana", 'age': '24', 'major': 'CS'}
for key, val in myDict.items():
	print ("My {} is {}".format(key, val))

mylist = [4,6,2,8,1]
print(mylist)


#dictionary sample prog
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
	name = input('Enter a name: (blank to quit)')
	if name == '':
	   break

	if name in birthdays:
	   print(birthdays[name] + ' is the birthday of ' + name)
	else:
	   print('I do not have birthday information for ' + name)
	   print('What is their birthday?')
	   bday = input()
	   birthdays[name] = bday
	   print('Birthday database updated.')

# reverse a string
mystring = 'mystring is here'
print(mystring[::-1])
print(mystring.upper())
print(mystring.split())
print('The format {1} {0} {q}'.format('go', 'should', q='here'))
print(f'this sentense is: {mystring}')
print(mystring)


#read from a file
with open ("checkfile.txt") as my_file:
	contents = my_file.read()
print(contents)


#celcius to fahrenheit
celcius = [0, 34.5, 12, 4]

fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)
