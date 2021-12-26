# Assignment 7

# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

print("\nWelcome to Program 1 of Assignment 7!\n")

# declare ng letters para icompare sa kada isang letter ng sentence
vowels = {'a', 'e', 'i', 'o' , 'u'}
consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}

def counthWords(sentence):
    return len(sentence.split())

def countVowels(sentence):
    n_vowels = 0
    for x in sentence:
        if x in vowels:
            n_vowels += 1
    return n_vowels
    
def countConsonants(sentence):
    n_consonants = 0
    for x in sentence:
        if x in consonants:
            n_consonants += 1
    return n_consonants

#------main------

sentence = str(input("Sencente: ")) 

sentence.casefold() #iconvert to lowercase para hindi masyado marami yung nakalagay sa vowels at consonants array

print("Output:")
print("Words: " + str(counthWords(sentence)))
print("Vowels: " + str(countVowels(sentence)))
print("Consonants: " + str(countConsonants(sentence)))

print("\n") #end of program 1

# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

# Tip: loop through each character of the input then process it letter by letter

print("End of Program 1\nWelcome to Program 2 of Assignment 7!")

