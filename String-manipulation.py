import sys

def splitParagraphPerPageWidth(paragraph, pagewidth):

    line        = ""
    word        = ""
    listOfLines = []

    listOfWords = paragraph.split(' ')

    for wordIdx in range(len(listOfWords)):
        word = (' ' if len(line) > 0 else '') + listOfWords[wordIdx]
        if (len(line) <= pagewidth) and (len(line) + len(word) <= pagewidth):
            line = line + word 
            if wordIdx == len(listOfWords) - 1:
                listOfLines.append(line)
        else:
            listOfLines.append(line)
            line = listOfWords[wordIdx]
            if wordIdx == len(listOfWords) - 1:
                listOfLines.append(line)
    return listOfLines

def lrJustified(listOfParagraphLines, pagewidth):

    listOfLines = []
    listOfWords = []

    for lineIdx in range(len(listOfParagraphLines)):

        line                    = listOfParagraphLines[lineIdx]
        newline                 = ""
        totalSpacesToFill       = pagewidth - len(line)
        totalWordsInALine       = 0
        totalSpaceToFillBtwWord = 0

        listOfWords             = line.split(' ')
        totalWordsInALine       = (len(listOfWords) - 1)

        # When there is only 1 word in a line, it is simply left justified
        if totalWordsInALine == 0:
            newline = line
        # When atleast 1 space to be added between words    
        elif (totalSpacesToFill // totalWordsInALine > 0):
            
            totalSpaceToFillBtwWord = totalSpacesToFill // totalWordsInALine

            if totalSpacesToFill % totalWordsInALine > 0:
                for wordIdx in range(len(listOfWords)):
                    word = listOfWords[wordIdx]
                    if wordIdx == len(listOfWords) - 1:
                        newline = newline + (' ' if len(newline) > 0 else '') + word.rjust(len(word) + totalSpaceToFillBtwWord)
                    else:
                        newline = newline + (' ' if len(newline) > 0 else '') + word.ljust(len(word) + totalSpaceToFillBtwWord)    
            else:
                for wordIdx in range(len(listOfWords)):
                    word = listOfWords[wordIdx]
                    if wordIdx == len(listOfWords) - 1:
                        newline = newline + (' ' if len(newline) > 0 else '') + word.rjust(len(word))
                    else:    
                        newline = newline + (' ' if len(newline) > 0 else '') + word.ljust(len(word) + totalSpaceToFillBtwWord)
        else:
            for wordIdx in range(len(listOfWords)):
                word = listOfWords[wordIdx]
                if wordIdx == len(listOfWords) - 1:
                    newline = newline + (' ' if len(newline) > 0 else '') + word.rjust(len(word) + totalSpacesToFill)
                else:    
                    newline = newline + (' ' if len(newline) > 0 else '') + word.ljust(len(word))

        listOfLines.append(newline)

    return listOfLines

def validateInputArguments():
    errMsg            = f"Usage: python {sys.argv[0]} 'This is a sample paragraph text that need to be left and right justified by the script as per page width provided.' 20"
    expectedArguments = 2

    if len(sys.argv) != expectedArguments + 1:
        print(f"Error: Expected {expectedArguments} parameters!")
        print(errMsg)
        sys.exit(1)
    else:
        paragraph = sys.argv[1]
        pagewidth = sys.argv[2]

        if not paragraph or not pagewidth:
            print(f"Error: Paragraph text or page width is empty!")
            print(errMsg)
            sys.exit(1)
        elif not pagewidth.isnumeric():
            print(f"Error: Page width can only be numeric integer!")
            print(errMsg)
            sys.exit(1)
    return None

validateInputArguments()
splittedParagraph = splitParagraphPerPageWidth(sys.argv[1], int(sys.argv[2]))
if len(splittedParagraph) > 0:
    formatedParagraph = lrJustified(splittedParagraph, int(sys.argv[2]))
    print()
    for lineIdx in range(len(formatedParagraph)):
        print(formatedParagraph[lineIdx])