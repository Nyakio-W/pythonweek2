list_a = [1,2,3,4,5]
#index    0,1,2,3,4
print(list_a[2])
print(list_a)
list_a[0] = 10
print(list_a)

print(len(list_a))

list_a.insert(len(list_a),6)
list_a.append(7)
list_a.extend([8,9])
list_a.pop(8) #deletes the index
del list_a[7] #deletes the index
print(list_a)

for item in list_a:
    print(item)

print(list_a[2:5]) #prints index 2-4
print(list_a[5:])

list_b = [1, 'today', True, 3.0]

list_c = ["skinny", 'Ahmad', 'Mutemi']

list_d = [1,2,3,[4,5],6,7]

list_e =[]

numbers = [number*number for number in range (1,6)]
print(numbers)

#setssss

student_id = {112,114,116,118,115}
print('student ID:' ,student_id)

vowel_letters={'a','e','i','o','u'}
print('vowel letters:',vowel_letters)

mixed_set = {'hello', 101, -2, 'bye'}
print('set of mixed data types:', mixed_set)

emptySet = set()
print(emptySet)

emptyDictionary = {}
print(emptyDictionary)

numbers = {21,34,54,12}
print('Initial set:' ,numbers)
numbers.add(66)
print('updated set',numbers)

companies = {'lactose', 'ralph lauren'}
tech_companies = ['apple','google','apple']

companies.update(tech_companies)
print(companies)

companies.discard('apple')
print(companies)

fruits = {'apple','peach','mango'}

for fruit in fruits:
    print(fruits)

print(len(fruits))

#union of sets - trying to create a set that has elements of both a and b

A = {1,3,5}
B= {0,2,4}
print('union using|:',A|B)
print('union using union():',A.union(B))

#itersection using &, intersection using .intersection()
#difference using A-B , or .difference() - showsyou which elements are not in the other set
#symmetric difference using ^ A^B, OR, A.symmetricdifference(B)

C = {1,3,5}
D = {3,5,1}
if C==D:
    print('set c and d are equal')
else: 
    print('set c and d are not equal')


#tupulessss

#dictionarriessss
capital_city = {"nepal":"kathmandu", 'italy':'rome','england':'london'}
print('initial dictionary',capital_city.keys())

capital_city['nepal'] = 'newcapital'
capital_city[55] = 66
print('updated dictionary:',capital_city)

print(capital_city['england'])

print('england' not in capital_city) #membership test

for i in capital_city:
    print(capital_city[i])

#stringsssss
greet = 'hello'
print (greet[1])
print (greet[-2])
print(greet[1:4])

message = """
never gonna give you up
never gonna let you down
"""
print (message)

result = greet + message
print(result)

for letter in greet:
    print(letter)

print(len(greet))
print(greet.index('l'))

example = 'he said, \'what\'s there?\'' #escape sequences
print(example)

name = 'ahmed'
country = 'rwanda'
print({name},'is from',{country})