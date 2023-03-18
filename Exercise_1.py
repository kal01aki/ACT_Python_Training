'''Q1 Write a python function that takes a list of integers
as input and returns a new list with all the even
numbers doubled and all the odd numbers replaced with -1'''

def even_doubled(numbers:list) -> list:
    new_numbers = []
    for i in numbers:
        if i%2 == 0:
            new_numbers.append(i*2)
        else:
            new_numbers.append(-1)
    return new_numbers

print(even_doubled([1, 2, 3, 4, 5, 6, 7, 8, 9]))


'''Q2 Write a function that takes a string as
input and returns a new string
with all the vowels removed.'''

def remove_vowels(letters:str) -> str:
    vowels = ('a','e','i','o','u')
    for x in letters:
        if x in vowels:
            letters = letters.replace(x, "")
    return letters

print(remove_vowels("remove vowel letters"))


'''Q3 Write a function that takes a list of 
strings as input and returns a new list 
with all the strings that have a length of 4 or greater.
'''
def string_length_checker(string_list:list)->list:

    for x in string_list:
        if len(x) < 4:
            string_list.remove(x)
    return string_list

print(string_length_checker(["pass", "pwd", "1234", "in"]))

''' Q4 Write a function that takes a list of
integers as input and returns the largest
difference between any two adjacent numbers.
'''
def q4(integer_list:list) -> int:
    pass

''' Q5 Write a function that takes a list of integers
as input and returns the second largest number in the list.'''

def second_largest(inputs:list)->int:

    inputs.sort(reverse=True)
    second_largest = inputs[1]
    return second_largest

print(second_largest([4, 5, 8, 15, 20, 23]))


'''Q6 Write a function that takes a string as input and returns
True if the string is a palindrome (reads the same forwards and backwards)
and False otherwise.'''

def palindrome_check(check_word:str) -> bool:

    word_to_list = list(check_word)

    string_format_forward = str(word_to_list)
    string_format_backward = str(word_to_list[::-1])

    if string_format_backward == string_format_forward:
        return True
    else:
        return False


print(palindrome_check("alola"))

'''Q7 Write a function that takes a list of strings
as input and returns a new list with all the strings in reverse order.'''

def revers_string(string_list:list) -> list:
    pass

'''Q8 Write a function that takes two lists as
input and returns a new list with all the elements
that are common to both lists.'''

def common_elements(first_list:list, second_list:list)->list:

    common_element = set(first_list).intersection(set(second_list))
    common_element_list = list(common_element)

    return common_element_list


print(common_elements([1,2,3,4,] , [3,4,5,6,7,]))

'''Q9 Write a function that takes a list of integers as input and
returns the sum of all the elements in the list that are divisible by 3 or 5.'''

def sum_of_elements(inputs:list)->int:
    for_sum = []
    sum=0
    for values in inputs:
        if values % 3 == 0 or values % 5 == 0:
            for_sum.append(values)
    for values in for_sum[0:len(for_sum)]:
        sum = values + sum

    return sum

print(sum_of_elements([2,4,5,9,15,-5]))

'''Q10 Write a function that takes a string as
input and returns a new string with the first letter of each word capitalized'''

def first_letter_capitalization(input:str)->str:
    updated_string = input.capitalize()
    print(updated_string)
    return updated_string

print(first_letter_capitalization("capitalize the first letter"))