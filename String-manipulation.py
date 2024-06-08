import sys

def splitParagraphPerPageWidth(paragraph, pagewidth):

    line        = ""
    word        = ""
    listOfLines = []

    listOfWords  = paragraph.split(' ')

    for wordIdx in range(len(listOfWords)):
        word = (' ' if len(line) > 0 else '') + listOfWords[wordIdx]
        if (len(line) <= pagewidth) and (len(line) + len(word) <= pagewidth):
            line = line + word 
            if wordIdx == len(listOfWords) - 1:
                listOfLines.append(line)
        else:
            listOfLines.append(line)
            line = listOfWords[wordIdx]

    return listOfLines

formatedParagraph = splitParagraphPerPageWidth(sys.argv[1], int(sys.argv[2]))
print(formatedParagraph)
