
string = input()


balencedStrings = []  
newString = ""  

for char in string:
    newString += char

    
    if newString.count('L') == newString.count('R'):
        balencedStrings.append(newString)
        newString = ""


print(len(balencedStrings))
for i in balencedStrings:
    print(i)



"""
solve by python
Given a balanced string 𝑆
 consists of ['R', 'L'] characters. Split it into maximum number of strings such that the new strings are also balanced.

Note:

Balanced strings are those who have equal quantities of 'L' and 'R' characters.
You can not remove or reorder the characters while making the new strings.
Input
Only one line contains a string 𝑆
 (2≤|𝑆|≤1000)
 where |S| is the length of the string.

It's guaranteed that 𝑆
 consists of only ['L', 'R'] letters, 𝑆
 is balanced and |𝑆|
 is even.

Output
Print maximum number of balanced strings then the balanced strings in any order.

Examples
input:
LLRRLLLRRR

output:
2
LLRR
LLLRRR

"""