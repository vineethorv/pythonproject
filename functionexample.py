"""
def hello(name):
    print("hello world "+ name)


hello("vineeth")


def my_function(*kids):
    print("the kid is "+kids[2])

my_function("Vineeth","Soumya","Viren")
"""

def my_function(**kids):
    print("my first kid is"+kids["kid2"])

my_function(kid1="Vineeth", kid2="Soumya")