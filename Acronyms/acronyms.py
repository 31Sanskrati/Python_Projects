#simple python project to generate acronyms from phrases

# request a phrase from the user
phrase = str(input("Enter you phrase:"))

# split up the text into individual words 
# assigns each word an index number, starting with 0.
text = phrase.split()

# initialize x with an empty string
x = " "

# loop through all of the words, adding a capital letter for each one 
# until it reaches the end of string (the last character).
for i in text:
    x = x+str(i[0]).upper()
    
print(x)
