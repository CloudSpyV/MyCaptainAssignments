dict1={}
str1=input("Enter The String: ")
str2=str1.lower()
for letter in str2:
    dict1[letter]=str2.count(letter)

#unsorted dictionary
print("The Unsorted dictionary is : \n",dict1)

#Fetching The sorted Values and keys from the list <dict_name>.items() since it returns a list of tuples.
#storing the Sorted List In dict2 , sorted wrt values thus interchanged keys and values in the statement
dict2=sorted((value,key) for (key,value) in dict1.items())

#converting the sorted list into a dictionary again.
dict3=dict([(key,value) for (value,key) in dict2])


#printing the sorted dictionary wrt to occurence of letters in the word. In descending order.


for x in reversed(dict3):
    print(x,'=',dict3[x])
