#playing with lists, use ctrl +/ to comment and uncomment multiple lines

vehicles = ['BMW', "Audi", 'Honda', 'Mercedes']
print("the length of vehicles list is {}".format(len(vehicles)))
print(vehicles[1])
vehicles.pop(0)
print(vehicles)
vehicles.insert(0, 'Ambassador')
print(vehicles)
vehicles.insert(-1, 'Suzuki')
print(vehicles)
vehicles.append("BMW")
print(vehicles)
fruits = ['Banana', 'Orange', 'Apple', 'Strawberry']
vehicles.extend(fruits)
print(vehicles)
vehicles.sort(reverse=True)
print(vehicles)

sample ='Chrome'
print(set(sample))
