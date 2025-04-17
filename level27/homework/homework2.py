sentence = input("Enter Something Here: ")
word = input("Enter What Word You Need To Find: ")

position = sentence.find(word)

if position != -1:
    print("Your Word Was Found At Position:", position)
else:
    print("The Word Was Not Found.")