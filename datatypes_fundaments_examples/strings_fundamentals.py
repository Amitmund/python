
# Using of a variable in python.
message = "Welcome to Python!"
print(message)




# .title() is a method
# A method is an action that python can perform on a piece of data

name = "amit mund"
print(name.title())
print(name.upper())
print(name.lower())





# f (Formatted) string in python
first_name = "amit"
last_name = "mund"
full_name = f "{first_name} {last_name}"
print(fullname.title())
print(f"Hello, {full_name.title()}!")





# r-string ("raw string")
# Tell the python interpreter to treat backslashes \ as literal characters.

print("Hello \t World")
print(r"Hello \t World")

valid_raw_string = r"C:\path\to\folder" + "\\"
print(valid_raw_string) # Output: C:\path\to\folder\

valid_raw_string = r"C:\path\to\folder" + "\\"
print(valid_raw_string) # Output: C:\path\to\folder\

valid_raw_string = r"C:\path\to\folder" + "\\"
print(valid_raw_string) # Output: C:\path\to\folder\





# Not learned yet. Need to explore a lot more.

# IMP
# t-strings in python 3.14
# Its not the string type, but its template type

name = "amit mund"
message = t"Hello,{name}!"
print(message)
message = t"Hello,{name}.title()!"
print(message)




# Managing white spaces:
text.rstrip()
text.lstrip()
text.strip() # remove white space from both the side.





# Removing the prefixs:
my_url = 'https://sretoolkit.com'
print(my_url.removeprefix('https://'))



