# Python Notes

Notes from multiple learning sources. Thank you all.

- [Chai aur python](https://github.com/hiteshchoudhary/chai-aur-python)
- [Google IT Automation with Python Certificate](https://www.youtube.com/watch?v=UYU_ki7likk&list=PLTZYG7bZ1u6oJu7Imgx8FTOjyDNwesrm5&index=1)


## Few of the best python book:
- Python Crash Course [ref youtube link](https://www.youtube.com/watch?v=MqywbqLmjp4)
- Python Programming By John Zelle
- Algorithms Illuminated - Path1: The Basics - By Tim Roughgarden (Not in python, but fir Algo.
- Python Tools for Scientiest.
- Effective Panda
---

# Chapter1


## hello_chai.py
<details>
  <summary>
    Creating a function, that can be used from a different file.
  </summary>

  ```
print("chai aur python")

def chai(n):
    print(n)

chai("lemon tea")

chai_one = "lemon tea"
chai_two = "ginger tea"
chai_three = "masala chai"
  ```
</details>

## chai.py

<details>
  <summary>
    Calling a function from anoher file
  </summary>
  
  ```
from hello_chai import chai

chai("ginger tea")

# this is comment
  ```
</details>


## Knowing what are the functions, variables  with in a module
* import myModule
* dir(myModule)

* you can also use as `from myModule import aGivenFunction`

---

## Note: 001

```
print("Hello"+"Python") # output: HelloPython (No space when we use +)
print("Hello", "Python") #Output: Hello Python (When we use , it add a space in between these two string.)
```

---

## Note: 002

```
print("My age is " , 36) # This will work. As we are not doing any concanitation. ( So, good to use , ) 

print("My age is" + 36)  # This will give you error: "TypeError: must be str, not int"  # + expect both to be string.
```

```
Using + works for combining two strings — it concatenates them. It also works for two numbers — it adds the numbers together.

But, it can't join a string and a number.
```


---



