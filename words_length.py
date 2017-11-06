# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:51:51 2017

@author: Padam Singh
"""

def words_length(list_of_words) :
    "This function returns list having lenght of list_of_words passed as parameter."
    iter = map(len, list_of_words)
    result = []
    for item in iter :
        result.append(item)
    return result

def main():
    words = input("Please enter list of words (use comma separater between two words) : ").split(',')
    
    output = words_length(words)
    
    print("\nMapping of list of words into length of words are : \n{} - {}".format(words,output))
 
if __name__ == '__main__':
    main()