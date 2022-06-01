def sentence5 (sentence6,seperators):
    if sentence6 [0] in seperators:
        word = sentence6 [0]
        sentence6 = sentence6[1:]
        return (word, sentence6)
    word = ""
    for character in sentence6:
        if character.isalpha():
            word =word+character
        else :
            sentence6 =sentence6[len(word):]
    
            return (word, sentence6)
        if word == sentence6 :
            sentence6 = ""
    return (word, sentence6)
###################################################################################################################################
sentence6 = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU WHAT YOU CAN DO FOR YOUR COUNTRY"
seperators = " "
searchword = input("What word would you like to search: ")
wordposition = 0
found = False
while sentence6 != "":
    word,sentence6 = sentence5(sentence6,seperators)
    if word not in seperators:
        wordposition =wordposition+1

    if word == searchword:
        found = True
        print ("The word", searchword , "is in position", wordposition)
if found == False:
    print(searchword, "Not found")
    
    
    


