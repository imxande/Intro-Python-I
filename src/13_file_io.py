"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
fiLe1 = open("foo.txt", "r")
print(fiLe1.read())
fiLe1.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
fiLe2 = open("bar.text", "w")
fiLe2.write("Last name Ever, first name Greatest\nLike a sprained ankle\nBoy I ain't nothing to play with, Drake!")
fiLe2.close()