"""
# print  ("Hello World!")

# type of variable


b = 10
print(type(b))

# unpack a list

fruits = ['apple', 'banana', 'orange']
[x, y, z] = fruits
print(x)
print(y)
print(z)


a= 'Vineeth'
txt = "fifth character is {}"
print (txt.format(a[5]))


import random

print(random.randrange(1, 10))


fruit = 'straw berry'
print(len(fruit))

for x in fruit:
    print(x)

print(fruit[2:])
print(fruit[:3])
print(fruit[::2])
print(fruit.upper())
print(fruit.strip())
print(fruit.replace('n', 'k'))
print(fruit.split(' '))


# Lists
# Tuples
# Sets
# Dictionaries
# Functions

# Pandas
# import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index=['x', 'y', 'z'])

print(myvar)
print(myvar[2])

import pandas as pd

mydata = {"day1": 125, "day2": 130, "day3": 135}
print(pd.Series(mydata, index=["day1", "day2"]))



# dataframes

import pandas as pd

mydata = {"names": ['Vineeth', 'Soumya', 'Viren'],
          "marks": [98, 99, 100]}

myresults = pd.DataFrame(mydata, index=["me", "wife", "kid"])

print(myresults)
print(myresults.loc["kid"])

import pandas as pd

df = pd.read_csv(r'C:\Users\vinee\Desktop\sampletest.csv')

print (df.to_string())
print(df.head(1))
print(df.tail(3))
print(df.info())


new_df = df.dropna()
print(new_df)

x = df["Marks"].mean()
df.fillna(x, inplace=True)
df.loc[0, "Marks"] = 0
print(df)


import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)


import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('2nd element on 1st row: ', arr1[1, 2])

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)


l = ['banana', 2, 3, 4, 5]

print(len(l))
l.insert(2,7)
print(l)
l.pop()
print(l)
l.remove(7)
print(l)



thislist = ["apple", "banana", "cherry"]
for x in thislist:
    if x == "apple":
        print("I love apple")
    elif x == "banana":
        print("I love banana")
    else:
        print("I love cherry")
print(x)


thisdict = {
    "car1" : "BMW",
    "car2" : "Audi",
    "car3" : "Ford"
}
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
print(thisdict["car1"])
thisdict.update({"car4":"Ambassador"})
print(thisdict.items())

for x in thisdict.values():
    print (x)

print([x for x in thisdict.keys() if "car1" in x])


"""


vehicles = ['BMW',"Audi",'Honda','Mercedes']
print ("Length of vehicles list is"+ len(vehicles))
