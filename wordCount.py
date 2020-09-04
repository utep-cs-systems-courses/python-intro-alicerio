# Intro to Python Lab
# Operating Systems
# Created by: Alan Licerio
# Last modified: 09-03-20

def countWords(fileName, numWords, listWords):
    file = open(fileName,'r')
    for line in file:
        # Replaces special punctuation with whitespace.
        line = line.replace("\n", " ").replace(";", " ").replace(".", " ").replace(", ", " ").replace("-", " ").replace('"', " ")
        word = line.split() # Splits a line into words.
        for i in range(len(word)):
            word[i] = word[i].lower() # Passes the word into lowercase.
            # If the word is already on the list, it adds a one everytime it is found. 
            # Otherwise it adds the word to the list.
            if(word[i] in numWords):
                numWords[word[i]] +=1
            else:
                listWords.append(word[i])
                numWords[word[i]] = 1
    
def writeFile(numWords, listWords):
    file = open("output.txt",'w')
    for i in range(len(listWords)):
        file.write((listWords[i] + " " + str(numWords[listWords[i]]) + "\n"))


if __name__ == "__main__":
    numWords = {}
    listWords = []
    fileName = input("Enter name of file that will be read:\n")
    countWords(fileName, numWords, listWords)
    listWords = sorted(listWords) # Sorts the list of words.
    writeFile(numWords, listWords)
