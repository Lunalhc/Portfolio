import nltk   # import a data structure containing enlish words
nltk.download('words')
from nltk.corpus import words

import string

english_words = set(word.upper() for word in words.words())  # grab the words from data and convert to uppercase

possible_original_text = []  # initialize a list to store possible answers


def decoder (cipher_text):   # decoder function with parameter cipher text

    original_text = ""    # initialize original text

    for n in range(26):   # use shift n from 0 to 26

        decoding_dic = {}  # initialize decoding dictionary

        for i in range(26):   # iterate each letter
        
            letter = string.ascii_uppercase[i]  # grad lettes
            new_letter = string.ascii_uppercase[(i+n) %26]   # grab the letters after the shift

            decoding_dic[new_letter] = letter   # assign values for letters
            
        subsitution_table = decoding_dic   # store the dictionary as subsitution table

        for letter_ in cipher_text:    # iterate each letter in cipher text

            original_text += subsitution_table[letter_]   # find the assigned value in subsitution table

        print(f"{original_text} with shift {n}")  # print out the original text with n shift
        
        possible_original_text.append(original_text)  # put possible answers in the list

        original_text = ""   # restore the original text so that it's ready for next iteration
    
    return original_text


def count_words(combination):  # count how many possible words we can grab from the combination
    
    word_count = 0   # initialize the number of words

    for start_letter_index in range(len(combination)):  # start from the first letter, then second, third...

        for end_letter_index in range(start_letter_index + 1, len(combination) + 1): # end at the second letter, third,...

            substring = combination[start_letter_index:end_letter_index]  # store each possibility as a substring

            if substring in english_words:  # check if the sunstring is in the data set
                
                word_count += 1   # count how many words is in the combination


    return word_count


# test 
if __name__ == "__main__":

    input_text = input("what's the cipher text?")   # ask user the cipher text input

    decoder(input_text)  # find all the potential original text

    max_number = 0    # initialize the max number of words found
    number_of_words_list = []   # create an empty list for all the numbers counted

    for combination in possible_original_text:   # iterate each possible original text

        number_of_words = count_words(combination)   # count how many words we can found in that possibility

        shiftn = possible_original_text.index(combination)   # track the index of each combination, whihc is also the shift number
        print(f" {number_of_words} in total with shift {shiftn}")  # print out the number of words found paired with shift number

        number_of_words_list.append(number_of_words)  # put the number of words found in the list

        if number_of_words > max_number:  # check if this number of words found is greater than the previous one

            max_number = number_of_words  # if so, it becomes the new max number
    
    
    max_shift_appear = [index for index, number in enumerate(number_of_words_list) if number == max_number]   # find all the index of element where the max shift appear in the list
    print(f"the most words count appears in shift {max_shift_appear}.")   # print out the most possibile shift number
