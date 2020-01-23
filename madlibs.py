#! python3
# This program reads text files and allows the user to replace ADJECTIVE, NOUN,
# ADVERB, or VERB with a word of their choice.

# Prompt user to enter file name
filename = input("Please enter name of file (including extension):")

# Open, load, then close file
textFile = open(filename)
text = textFile.read()
textFile.close()

# Split string to allow for easier manipulation
text = text.split()

# If-else branch to replace specific keywords
for count, word in enumerate(text):
    if "ADJECTIVE" in word:
        text[count] = input("Enter an adjective: ") + text[count][9:]
    elif "NOUN" in word:
        text[count] = input("Enter a noun: ") + text[count][4:]
    elif "ADVERB" in word:
        text[count] = input("Enter an adverb: ") + text[count][6:]
    elif "VERB" in word:
        text[count] = input("Enter a verb: ") + text[count][4:]

# Open, write, and close new text file
newTextFile = open(filename[:-4] + "!.txt", 'w')
newTextFile.write(' '.join(text))
newTextFile.close()
