def sent (sentence, seperators):
    if sentence [0] in seperators:
        word = sentence [0]
        sentence=sentence[1:]
        return (word, sentence)
    word = ""
    for character in sentence:
       if character.isalpha():
           word =word+character
       else :
           sentence =sentence[len(word):]


           return (word, sentence)
       if word == sentence:
            sentence = ""
    return (word,sentence)
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>#
sentence =  "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
seperators = " "
search = input("what word do you want to search")
wordposition = 0
found = False
while sentence != "":
    word,sentence = sent(sentence,seperators)
    if word not in seperators:
        wordposition =wordposition+1


    if word == search:
        found = True
        print ("The following word", search ,"is at this cordinates", wordposition)
if found == False:
    print("The word your looking for",search,"can not be found please enter a word that is in the sentence")
    
    

