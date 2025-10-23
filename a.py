import math
import time

# 1. Multiply all numbers in a list (через цикл)
numbers = [2, 3, 4, 5]
result = 1
for n in numbers:
    result *= n
print(result)

# 2. Count uppercase and lowercase letters (через цикл)
text = "Hello World!"
upper = 0
lower = 0
for c in text:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)

# 3. Check if string is palindrome (через цикл)
s = "madam"
reversed_s = ""
for i in range(len(s) - 1, -1, -1):
    reversed_s += s[i]
print(s == reversed_s)

# 4. Invoke square root function after specific milliseconds
num = 25100
ms = 2123
time.sleep(ms / 1000)
print("Square root of", num, "after", ms, "miliseconds is", math.sqrt(num))

# 5. Return True if all elements of tuple are true (через цикл)
t = (True, 1, "yes")
all_true = True
for i in t:
    if not i:
        all_true = False
        break
print(all_true)
