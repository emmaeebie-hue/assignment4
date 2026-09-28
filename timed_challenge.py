# Question 13: Balanced Symbols
# Given a string containing brackets (), {}, and [], determine whether the brackets
# are balanced. Return True if they are balanced and False otherwise.
# Example:
# "{[()]}" → True
# "{[(])}" → False

def balanced_symbols(text):
    if not isinstance(text, str):
        return False
    
    stack = []

    matching = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            if stack[-1] != matching[char]:
                return False
            stack.pop()
    return len(stack) == 0

#Timed Challenge Response:
# For my timed challenge, I chose the Balanced Symbols problem because it seemed like one of 
# the problems I understand well and could complete within the 30-minute time limit. I used a
# stack because I needed to keep track of the opening brackets and make sure each closing bracket 
# matched the correct one. The stack allowed me to check the most recent opening bracket first.

# I finished the problem in under 30 minutes. The time limit honestly did not make a huge 
# difference for me because I did not find the problem too difficult once I understood what I 
# was supposed to do. The part that took the longest was double-checking myself and remembering 
# the correct code. I knew what I wanted the program to do, but I had to think about the exact 
# syntax and make sure I was writing each part correctly. I also spent time testing different 
# examples to make sure I did not miss anything.

# I used a Python list as my stack instead of making a separate stack class. This made the 
# solution simpler and quicker to write. I also added a check for an incorrect data type after 
# testing the function with a list instead of a string. I tested balanced brackets, mismatched 
# brackets, an empty string, and a wrong data type. Overall, this challenge was pretty manageable
# once I figured out that a stack was the right structure to use.