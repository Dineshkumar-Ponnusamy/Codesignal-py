#Your friend is an experienced coder who just started learning Python. Since she is already proficient in Java and C++, she decided to write all of her snippets in all three languages, in order to ensure the Python code was working as expected. Here's the very first function your friend wrote in Python and Java (the C++ version is the same as Java one):

#Python:
def division(x, y):
    return x // y
#Java:
int division(int x, int y) {
    return x / y;
}

#You noticed that the functions aren't quite the same: they won't produce the same result for some valid values of x and y. For which of the following example inputs would these two versions produce different outputs?

#Answer is: x = 15, y = -4. Reason: In Java, 15/-4 = -3. In Python, floor division returns, -4.
# More Info, https://www.cs.umd.edu/~clin/MoreJava/Intro/expr-int-div.html#:~:text=Java%20does%20integer%20division%2C%20which,can%20come%20in%20very%20handy.
# https://python-reference.readthedocs.io/en/latest/docs/operators/floor_division.html
