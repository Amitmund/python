
# List
languages = [ "python","c","javascript","java"]
print(languages)
print(languages[0])
print(languages[2].title())
print(languages[-1]) #return the last object

print(f"My first language was {languages[1]}")





# Lists are mutable, which mean you can update the list.
bike = ['honda', 'yamaha', 'suzuki']
print(bike)
bike[0] = 'hero' # Update the index 0th place.
print(bike)

bike.append('ducati') # append at the end.
print(bike)




# Creating empty list[] and later adding the value
bike[]
bike.append('Honda')
bike.append('Yamaha')
bike.append('suzuki')
print(bike)




# Removing item from list[]
del bike[0]
del bike[-1]
# With delete, you will not know the value removed.




# pop() method.
# The pop() method, removed the last item from the list, but also allowed you to work on it.
bike = ['honda', 'yamaha', 'hero']
poped_bike = bike.pop()
print(poped_bike) # hero

# pop(0)
print(bike)
my_first_bike = bike.pop(0) # 0th index. It will also update the bike[]
print(bike)
print(f"My first bike was {my_first_bike}.title()")





# Removing items by value from list[]
bike = ['honda', 'yamaha', 'hero', 'x']
print(bike)
bike.remove("hero")
print(bike)
# remove(), remove only the first occurance.






# list methods()
bike = ['hero', 'honda', 'yamaha', 'suzuki']
bike.sort() # permanent change # if sort is a method, it should be Caps S in sort.
bke.sort(reverse=True)

print(sorted(bike)) # temp changes of the order.

bike.reverse()
print(bike)
len(bike)















