
#numbers = input("Enter a list of integers separated by spaces: ")
#total_sum = sum(numbers)

# print('the sum of the integers is:', total_sum)

# Create a tuple containing the names of five favorite books
favorite_books = ("To Kill a Mockingbird", "1984", "The Great Gatsby", "Pride and Prejudice", "Harry Potter and the Sorcerer's Stone")

# Use a for loop to print each book name on a separate line
for book in favorite_books:
    print(book)

# Create an empty dictionary to store person's information
person_info = {}

# Ask the user for input and store the information in the dictionary
name = raw_input("Enter your name: ")
age = raw_input("Enter your age: ")
favorite_color = raw_input("Enter your favorite color: ")

# Store the information in the dictionary
person_info['name'] = name
person_info['age'] = age
person_info['favorite_color'] = favorite_color

# Print the dictionary to the console
print("Person's information:")
print(person_info)


set1 = raw_input('enter set of integers')
set2 = raw_input('enter set of integers')
delimiter = ','
set1 = set(map(int, set1.split(delimiter)))
set2 = set(map(int, set2.split(delimiter)))


common_elements = set1.intersection(set2)
print('common elements in both sets',common_elements)

list = ['black', 'yellow', 'mango', 'chew']
odd_length_words = [word for word in list if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)