# Import s (a string) and decode & encode (functions)
from this import s
from codecs import decode, encode
​
# Decode s and assign to a variable called zen
zen = decode(s, "rot13")
# Rot13 decoding is synonymous with rot13 encoding,
# therefore we can use either encode or decode
zen = encode(s, "rot13")
​
# Explore string methods
zen.upper()
zen.lower()
zen.title()
zen.swapcase()
​
# Obtain lists of words and lines from zen
word_list = zen.split()
line_list = zen.splitlines()
​
# Count characters, words, and lines
len(zen)
len(word_list)
len(line_list)
​
# Count a specific word (better) in zen 
zen.count("better")
word_list.count("better")
​
# Find the first occurence of the word "better"
zen.index("better")
word_list.index("better")
​
# Method chaining
# Convert to uppercase, get the word list, then
# Count a specific word (better) in zen 
zen.upper().split().count("BETTER")
​
(zen
 .upper()
 .split()
 .count("BETTER")
)
​
# Indexing (get one thing)
# First character
zen[0]
# First word
word_list[0]
# Last character
zen[-1]
# Last word
word_list[-1]
​
# Slicing (get a series of things)
# First 10 characters
zen[:10]
# First 4 words
word_list[:4]
# Last 10 characters
zen[-10:]
# Last 5 words
word_list[-5:]
# Get 3 (7 minus 4) characters
zen[4:7]
# Get 3 (4 minus 1) words
word_list[1:4]
# Reverse a string
zen[::-1]
# Reverse a list
word_list[::-1]
# Get a midpoint
midpoint = len(word_list) // 2
# Use the midpoint to split a list
# First half
word_list[:midpoint]
# Second half
word_list[midpoint:]
​
word_list[-10:]
zen.index("better")
​
# Arithmetic operators
# Plus sign (+)
# Addition for int, float, bool
3 + 2
4 + 4.5
True + False + True
# Concatenation for str, tuple, list
'3' + '2'
'abc' + 'def'
list('abc') + list('def')
tuple('abc') + tuple('def')
# Asterisk (*)
# Multiplication for int, float, bool
3 * 2
4 * 4.5
False * 9
True * 3
# Duplication and concatenation for str, tuple, list
'3' * 4
'abc' * 2
list('abc') * 3
tuple('abc') * 5
# Comparison operators (>, <, >=, <=, ==, !=)
"Python" < "R"
"Python" > "JavaScript"
# Modulo (%) divides by right-hand-side
# and returns the remainder
8 % 2 == 0
5 % 2 != 0
# Check if everything is True using and
True and True and True
True and False and True
# Check if at least one thing is True using or
True or True or True
True or False or True
​
# Turn number into character
chr(97)
# Turn character into number
ord("A")
​
# Functions
# In the case of binary results, return True or False
def is_odd(x):
    if x % 2 == 0:
        return False
    return True
​
# For non-binary results, return strings
def hi_mid_lo(x):
    if x > 7:
        return "hi"
    if x > 4:
        return "mid"
    return "lo"
​
# Without a return statement, functions return None
def myfunc(x):
    x
​
is_odd(5)
is_odd(8)
hi_mid_lo(3)
hi_mid_lo(5)
hi_mid_lo(8)
type(myfunc(5))
​
# List comprehensions
# Uppercase_alphabet 
[chr(x) for x in range(65, 91)]
# Lowercase_alphabet 
[chr(x) for x in range(97, 123)]
# Lowercase_alphabet 
[chr(x) for x in range(97, 123)]
# Odd numbers
[x for x in range(9) if is_odd(x)]
[x for x in range(9) if x % 2 != 0]
# Even numbers
[x for x in range(9) if x % 2 == 0]
# Square even numbers
[x**2 for x in range(9) if x % 2 == 0]
# Even numbers greater than 4
[x for x in range(9) if x % 2 == 0 if x > 4]
[x for x in range(9) if x % 2 == 0 and x > 4]
# Get a numbers if it is even OR greater than 4
[x for x in range(9) if x % 2 == 0 or x > 4]
​
# Boolean values (bools)
bools = True, False, True
# Count how many times True occur
sum(bools)
# Count the proportion of True
sum(bools) / len(bools)
# Count the percentage of True
sum(bools) / len(bools) * 100
​
from pathlib import Path
​
# Save zen to a text file
Path("zen.txt").write_text(zen)
# Read in the zen text file and assign to a variable
python_poem = Path("zen.txt").read_text()
print(python_poem)
​
import joblib
​
# Save zen to a zip file with joblib
joblib.dump(zen, "zen.zip")

# Read in the zen zip file and assign to a variable with joblib
python_poem2 = joblib.load("zen.zip")

print(python_poem2)ß