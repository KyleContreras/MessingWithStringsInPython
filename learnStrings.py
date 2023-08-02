# Capitalize the first letter of a sentence, in a two sentence string.


#Entry point of program. Print fixed sentence here
def Main():
    sentence = input("Type your sentence: ")

    sentenceList = PushToList(sentence)
    fixedSentence = WorkOnSentences(sentenceList)

    #return the corrected user input back to the user.
    print('Corrected sentence: ' + fixedSentence)

    return Main()

# This function will go through each item in the string and put each into
# the sentenceList, list
def PushToList(userInput):
    # will contain the user's sentence
    sentence = userInput
    # convert the string to a list. Each item being an indexed entry in
    # sentenceList
    sentenceList = []

    for letter in sentence:
        sentenceList.append(letter)

    return sentenceList

# This function will be the driver of turning our list into the fixed sentence
# to be returned back to the user
def WorkOnSentences(theList):
    # user sentence converted to a list
    sentenceList = theList

    for letter in sentenceList:
        # find the first '.' and separate the two sentences
        if letter == '.':
            findIndex = sentenceList.index(letter)
            # we want to go 1 past the '.' index, so we include the '.' in the
            # first sentence
            sliceHere = findIndex + 1

            # slice the first sentence and store in 'firstSentence'
            # only the endpoint is required as an arg for slice
            firstSlice = slice(sliceHere)
            firstSentence = sentenceList[firstSlice]

            # slice the second sentence and store in 'secondSentence'
            # get the length of the entire list, so we know a stopping point
            endOfList = len(sentenceList)
            # since this slice will be in the middle of the list, we need to
            # designate a starting point and end point
            secondSlice = slice(sliceHere, endOfList)
            secondSentence = sentenceList[secondSlice]

            # send both sentences to 'MakeUpper' to get the first letters
            # capitalized
            firstSentence = MakeUpper(firstSentence)
            secondSentence = MakeUpper(secondSentence)

            #join the two lists back together
            joinSentence = firstSentence + secondSentence

            # Convert the list back into a string
            fixedSentence = MakeNewString(joinSentence)

            break

    return fixedSentence

# This function will capitalize the first letters of each sentence
def MakeUpper(sentence):
    sentenceList = sentence
    count = 0

    while True:
        # The second slice will contain empty strings first, so we want to make
        # sure we iterate until we find that first letter.
        if sentenceList[count] != ' ':
            letter = sentenceList[count]
            upperLetter = letter.upper()
            sentenceList[count] = upperLetter

            break
        else:
            count = count + 1

    return sentenceList

# This function will concatenate each item of listSentence into a new string.
def MakeNewString(list):
    listSentence = list
    newSentence = ''

    # join each entry in the corrected list back into a string
    # This is done by concatenating each item to the empty string
    # 'newSentence'
    for item in listSentence:
        newSentence = newSentence + item

    return newSentence

Main()














