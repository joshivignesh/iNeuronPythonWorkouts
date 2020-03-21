#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Parent:

 def __init__(self, n):
     self.number_of_sides = n

 def print_num_sides(self):
     '''a quick, informational print statement'''
     print('There are ' + str(self.number_of_sides) + ' sides.')
     

class Triangle(Parent):
 def __init__(self, lengths_of_sides):
     Parent.__init__(self, 3)
     self.lengths_of_sides = lengths_of_sides  # list of three numbers

 def get_area(self):
     '''return the area of the triangle using the semi-perimeter method'''
     a, b, c = self.lengths_of_sides

     # calculate the semi-perimeter
     s = (a + b + c) / 2
     return (s*(s-a)*(s-b)*(s-c)) ** 0.5

 p = Parent(9)
 
 tri = Triangle([3, 4, 5])
 print(tri.get_area())


# In[13]:


def longwords(wordlist, length):
    return (word for word in wordlist if len(word) >= length)

def main():
    words = input("Enter words, separated by spaces: ").split()
    length = int(input("Minimum length of words to keep: "))
    print("Words longer than {} are {}.".format(length,
          ', '.join(longwords(words, length))))

main()


# In[34]:


def find_length_of_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n)))
    word_len.sort()
    return word_len

print(find_length_of_word(["ab", "cde", "erty"]))


# In[35]:


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('d'))
print(is_vowel('e'))

