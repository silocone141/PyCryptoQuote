from random import shuffle


def scramble_text(text):
    # Make all text lowercase
    text = text.lower()

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']
    masterAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y', 'z']

    # Generate scrambled alphabet list where no letter is in its original
    # position
    i = 0
    while i < 26:
        if alphabet[i] == masterAlphabet[i]:
            shuffle(alphabet)
            i = 0
        else:
            i += 1

    # Find a the new position of letter
    indexList = [alphabet.index(masterAlphabet[i]) for i in range(26)]

    # Create a list of all characters of text
    characterList = list(text)

    # Get the alphabet index of all elements of the character list
    j = 0
    translationList = []
    while j < len(characterList):
        try:
            item = masterAlphabet.index(characterList[j])
            cipherItem = masterAlphabet[indexList[item]]
            translationList.append(cipherItem)

        except ValueError:
            item = characterList[j]
            translationList.append(item)

        j += 1

    # Create cipher text string from translationList
    cipherText = ''.join(translationList)

    return cipherText
