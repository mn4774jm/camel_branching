import re
pattern = re.compile(r'\W')
def main():

    sentence = input('Please enter a sentence. Any sentence at all: ')
    outputs = camelCase(sentence)
    print(outputs)


def camelCase(sentence):
    wordSplit = sentence.split(' ')
    variableName = ''
    for i in range(len(wordSplit)):
        if i == 0:
            variableName += wordSplit[i].lower()
        else:
            variableName += wordSplit[i].capitalize()
    mo = pattern.search(variableName)
    if mo is not None:
        return f'\nWarning: There may be an issue in created variable name "{variableName}"'
    else:
        return variableName



main()