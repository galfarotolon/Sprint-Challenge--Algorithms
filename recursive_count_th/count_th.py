'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # set a counter for each 'th' occurrence in the word
    count = 0

    # check for base  case

    # if the word is smaller than 2, then count does not apply
    
    if len(word) < 2:
        # would return 0
        return 0
    
    # Do a recursion, if the word is 2 or longer

    else: 
        # check first two characters of the word
        if word[0:2] == 'th':
            # increase the  count by 1
            count += 1
            # here it does a recursion if the first 2 letters are 'th'
            return count + count_th(word[2:])
        else:
            # if they are not, then check for the next pair(kind of like bubble sort)
            # checks from the second letter instead of the third
            return count + count_th(word[1:])

print(count_th('pythonmathematics')) # prints 2: correct!   
print(count_th('thathethithothu')) # prints 5: correct!   
print(count_th('themasterthinksthatthisisthusnothat')) # prints 6: correct!   