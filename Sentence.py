# Take  sentence from the user , split it into words and store them in a list. print the longest word.
sentence = input("Enter a sentence: ")
words = sentence.split()
print("The words in the sentence are:", words)
longest_word = max(words, key=len)
print("The longest word in the sentence is:", longest_word)
