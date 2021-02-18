"""
Practice problems with recursion.

Based off of this practice sheet:
https://www.cs.cornell.edu/courses/cs2110/2014fa/L07-Recursion/recursion_practice.pdf
"""

# Compute the factorial of a number n
# factorial(3) = 3 * 2 * 1 = 6
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# factorial = n * n - 1...


def factorial(n):
    """Compute factorial of a number n recursively."""
    if n == 1:
        return 1
    # Do you understand why n needed to be outside the function call?
    # Computing inside the args leads to stackOverflow bc it never reaches 1
    return n * factorial(n - 1)


print(f"Factorial 3: {factorial(3)}")  # output 6
print(f"Factorial 5: {factorial(5)}")  # output 120

# Compute the sum of natural numbers until n
# sum(5) = 5 + 4 + 3 + 2 + 1
# sum(3) = 3 + 2 + 1


def sum(n):
    """Compute sum of natural numbers until n."""
    if n == 1:
        return n
    return n + sum(n - 1)


print(f"Sum 5: {sum(5)}")  # output 15
print(f"Sum 3: {sum(3)}")  # output 6

# Write a function for multiply (a, b) where a and b are both positive integers
# but you can only use + or - operators
# multiply(5, 2) = 5 + 5
# multiply(6, 3) = 6 + 6 + 6


def multiply(a, b):
    """Multiply positive integers using only + or - operators."""
    if a == 1:
        return b
    if b == 1:
        return a
    if a == 1 and b == 1:
        return 1
    # a + a b times and subtract 1 from b each time
    return a + multiply(a, b - 1)


print(f"Multiply 6 and 2: {multiply(6, 2)}")  # output 12
print(f"Multiply 5 and 3: {multiply(5, 3)}")  # output 15

# Find greatest common divisor of two numbers using recursion
# For example, gcd(8, 12) = 4
# gcd(6, 9) = 3
# The below solution uses the Euclidean algorithm, but there are other ways to
# calculate GCD. I was
# unfamiliar with GCD, so I used some internet help.


def gcd(a, b):
    """Find greatest common divisor of two numbers a and b."""
    # Everything divides by 0
    if a == 0:
        return b
    # Everything divides by 0
    if b == 0:
        return a
    # if a and b are equal:
    if a == b:
        return a
    # if a is greater than b:
    if a > b:
        return gcd(a - b, b)
    # otherwise:
    return gcd(a, b - a)


# Let's test it!

print(f"GCD 12 and 18: {gcd(12, 18)}")
print(f"GCD 64 and 48: {gcd(64, 48)}")


# Write a recursive function to reverse a string.
# reverse("hello") -> "olleh"
# reverse("hi there!") -> "!ereht ih"

def reverse(word):
    """
    Reverse a string using recursion.

    Typically, I'd use [:-1], but I want to
    try to challenge myself.
    """
    reversed = []
    # Base case - if our str length is one, we
    # were either given a short string or we're done.
    if len(word) == 1:
        print("Word == 1")
        reversed.append(word)
        return "".join(reversed)
    if len(word) == 0:
        print("Word == 0")
        return None
    reversed.append(word[-1])
    print(f"Reversed: {reversed}")
    return reverse(word)


# Let's test it!
print(f"Reversed hello: {reverse('hello')}")
print(f"Reversed hey there!: {reverse('hey there!')}")
