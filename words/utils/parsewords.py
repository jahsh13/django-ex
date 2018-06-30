#!/usr/bin/env python3

import sys
import os
import sqlite3

def parse_word(word):
    encoded_word = [0] * 26

    try:
        for letter in list(word.strip()):
            encoded_word[ord(letter.upper()) - ord('A')]+=1
    except Exception as e:
        encoded_word = [0] * 26

    return encoded_word

def initializeDB(db, cursor):
    try:
        cursor.execute('''
        create table words (hashed_word text, word text, word_length int)
        ''')
        db.commit()
    except sqlite3.OperationalError:
        pass


def storeWords(parsed_words, db, cursor):
    i = 0
    for hashed_word in parsed_words.keys():
        for word in parsed_words[hashed_word]:
            try:
                word_length = len(word)
                cursor.execute('''
                insert into words_words(hashed_word, word,word_length)
                values(?,?,?)''', (hashed_word, word, word_length))
                db.commit()
            except sqlite3.IntegrityError:
                print('Record %s %s already exists' % (hashed_word, word))
            except Exception as e:
                print('Error occurred for %s %s' % (hashed_word, word))
        #if ((i % 1000) == 0):
        #    print('Committed %s %s' % (hashed_word, word))

def main(words_file):
    parsed_words = {}
    print('Connecting to app_data.db')
    db = sqlite3.connect('../../data/app_data.db')
    cursor = db.cursor()
    print('Initializing the database')
    #initializeDB(db, cursor)

    print('Opening the word file %s' % words_file)
    f = open(words_file,'r')

    print ('Parsing the words')
    all_zeros = [0] * 26
    allzeros = ''.join(str(e) for e in all_zeros)

    for line in f:
        encoded_word = parse_word(line)
        hashed_word = ''.join(str(e) for e in encoded_word)
        if hashed_word == allzeros:
            pass
        else:
            if hashed_word in parsed_words:
                parsed_words[hashed_word].append(line.strip())
            else:
                parsed_words[hashed_word] = []
                parsed_words[hashed_word].append(line.strip())

    print('parsed_words.keys() = %s' % len(parsed_words.keys()))
    print('Storing the parsed words into the database')
    storeWords(parsed_words, db, cursor)
    db.close()
    print('Done')

if __name__ == '__main__':
    main(sys.argv[1])
