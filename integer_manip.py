def check_number_anagram(integer):
    """
    Write a function that gets an integer number as input and returns a boolean 
    type True or False based on whether the number when read backwards gives 
    the same number. This would be the equivalent of an anagram with strings.
    E.g. input of number 1234321 would return True.
    """
    
    flag = True

    # write you code here
    if integer in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        flag = True
    if str(integer) == str(integer)[::-1]:
        flag = True
    else:
        flag = False
    
    
    return flag
