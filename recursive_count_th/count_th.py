'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

"""
Inside the `recursive_count_th` directory you'll find the `count_th.py` file. In this file, please add your recursive implementation to the `count_th()` method following these rules:

* Your function should take in a signle parameter (a string `word`)
* Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
* Your function must utilize recursion. 
  * It cannot contain any loops.

Run `python test_count_th.py` to run the tests for your `count_th()` function to ensure that your implementation is correct.
"""

"""
I need to go through each 2 letters of the sequence
If those letters are not 'th', I need do the same function, but
one index forward

I need a way to keep track of the number

I tried a count =, but remembered the rabbit example for earlier,
I forgot you could just return the number + the function
"""
def count_th(word):
    # Creating a base case. if there are fewer than 2 letters
    # They they can't be 'th'
    if len(word) < 2:
        return 0
    # If they are 'th' add 1 to the count, like the bunny example
    if word[0:2] == 'th':
        # then use recursion on the whole word, but one index forward
        return 1 + count_th(word[1:])
    else:
        # Otherwise, I still need to return the recursion,
        # but without adding 1 
        return count_th(word[1:])
