#!/usr/bin/env python
# coding: utf-8

# In[1]:


def customreduce(anyfunc, sequence):
  result = sequence[0]
  for item in sequence[1:]:
   result = anyfunc(result, item)
  return result

def sum(x,y): return x + y

print ("Sum on list [4,6,7,8] using custom reduce function "   + str(customreduce(sum, [4,6,7,8])) )


# In[7]:


def customfilter(boolpre, iterable):
    result = []
    for item in iterable:
      if boolpre(item):
       result.append(item)
    return result

def ispositive(x):
 if (x <= 0): 
  return False 
 else: 
  return True

print ("Filter only positive Integers on list [1,2,-3,4,5,6] using custom filter function"  + str(customfilter(ispositive, [0,1,-2,3,4,5])))


# In[8]:



#########
word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print ("ACADGILD => " + str(alphabet_list))

#########
input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))

#########
input_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_list  ]
print("['x','y','z'] => " +   str(result))

#########
input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))

#########
input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))

#########
input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))

########


# In[11]:


def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["iNeuron", "Assignment", "CodeWorkout"]))

