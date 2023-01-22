#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

"""There are several ways to traverse a list in Python 3:

	Using a for loop:
	Copy code
	my_list = [1, 2, 3, 4, 5]
	for item in my_list:
    	print(item)

	Using the range() function:
	Copy code
	my_list = [1, 2, 3, 4, 5]
	for i in range(len(my_list)):
    	print(my_list[i])

	Using a while loop:
	Copy code
	my_list = [1, 2, 3, 4, 5]
	i = 0
	while i < len(my_list):
    	print(my_list[i])
    	i += 1

	Using the enumerate() function :
	Copy code
	my_list = [1, 2, 3, 4, 5]
	for i, item in enumerate(my_list):
    	print(i, item)

	Using List comprehension
	Copy code
	my_list = [1, 2, 3, 4, 5]
	[print(i) for i in my_list]

	It depends on what you want to do with the elements of the list, and what is the most readable and efficient way for you."""
