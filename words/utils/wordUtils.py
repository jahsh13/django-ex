import itertools
from words.models import Words

def parse_word(word):
    encoded_word = [0] * 26

    try:
        for letter in list(word.strip()):
            encoded_word[ord(letter.upper()) - ord('A')] += 1
    except Exception as e:
        encoded_word = [0] * 26

    return encoded_word

def generateCharPerms(char_list):
    char_list_hashes = []
    charlist = []
    i = 1
    # convert char_list to a list of characters
    chars = list(char_list.strip())
    # generate permutations
    while i <= len(chars):
        for perms in list(itertools.permutations(chars, i)):
            charlist.append(perms)
        i += 1

    # encode each permutation and store to char_list_hashes
    for perm in charlist:
        perm_word = ''.join(str(e) for e in perm)
        char_list_hashes.append(parse_word(perm_word.upper()))

    return char_list_hashes

def get_word_list(letters):
    word_list = []

    char_list_hashes = generateCharPerms(letters)
    query_list = []

    for encoded_word in char_list_hashes:
        hashed_word = ''.join(str(e) for e in encoded_word)
        query_list.append(hashed_word)

    instances = Words.objects.filter(hashed_word__in=query_list,word_length__gt=2).order_by('word_length','word').values_list('word',flat=True)

    if instances:
        for word in instances:
            word.strip().upper()


            if word not in word_list:
                word_list.append(word)

    return word_list