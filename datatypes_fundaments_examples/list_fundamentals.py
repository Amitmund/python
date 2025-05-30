
# List
languages = [ "python","c","javascript","java"]
print(languages)
print(languages[0])
print(languages[2].title())
print(languages[-1]) #return the last object

print(f"My first language was {languages[1]}")





# Lists are mutable, which mean you can update the list.
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)
bikes[0] = 'hero' # Update the index 0th place.
print(bikes)

bikes.append('ducati') # append at the end.
print(bike)




# Creating empty list[] and later adding the value
bikes[]
bikes.append('Honda')
bikes.append('Yamaha')
bikes.append('suzuki')
print(bikes)




# Removing item from list[]
del bikes[0]
del bikes[-1]
# With delete, you will not know the value removed.




# pop() method.
# The pop() method, removed the last item from the list, but also allowed you to work on it.
bikes = ['honda', 'yamaha', 'hero']
poped_bike = bikes.pop()
print(poped_bike) # hero

# pop(0)
print(bikes)
my_first_bike = bikes.pop(0) # 0th index. It will also update the bike[]
print(bikes)
print(f"My first bike was {my_first_bike}.title()")





# Removing items by value from list[]
bikes = ['honda', 'yamaha', 'hero', 'x']
print(bikes)
bikes.remove("hero")
print(bikes)
# remove(), remove only the first occurance.






# list methods()
bikes = ['hero', 'honda', 'yamaha', 'suzuki']
bikes.sort() # permanent change # if sort is a method, it should be Caps S in sort.
bikes.sort(reverse=True)

print(sorted(bikes)) # temp changes of the order.

bikes.reverse()
print(bikes)
len(bikes)



















