def find_vowels_consonants(string):
    """
    Write a function that takes a string in English as input 
    and returns the number of vowels and consonants.
    For example:
    If the string is 'The cat is sleeping', 
    then the function should return : (6, 10)
    """
    
    number_vowels = 0
    number_consonants = 0
    # write your code here
    all_consonants = 'BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz'
    all_of_vowels = 'AEIOUYaeiouy'
    for letter in string:
        if letter in all_consonants:
            number_consonants+= 1
        if letter in all_of_vowels:
            number_vowels+=1
    
    
    
    return number_vowels, number_consonants
