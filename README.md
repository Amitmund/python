# Python Notes

Notes from multiple learning sources. Thank you all.

## Ref links:

<details>

- [Chai aur python](https://github.com/hiteshchoudhary/chai-aur-python)
- [Google IT Automation with Python Certificate](https://www.youtube.com/watch?v=UYU_ki7likk&list=PLTZYG7bZ1u6oJu7Imgx8FTOjyDNwesrm5&index=1)
  
</details>

<!-- comment in markdown. -->


<!-- -------------------------------------------------------------------------------------------------------------------------- -->
<!-- -------------------------------------------------------------------------------------------------------------------------- -->


## Few of the best python book:

<details>

- Python Crash Course [ref youtube link](https://www.youtube.com/watch?v=MqywbqLmjp4)
- Python Programming By John Zelle
- Algorithms Illuminated - Path1: The Basics - By Tim Roughgarden (Not in python, but fir Algo.
- Python Tools for Scientiest.
- Effective Panda
  
</details>



<!-- -------------------------------------------------------------------------------------------------------------------------- -->
<!-- -------------------------------------------------------------------------------------------------------------------------- -->



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

<!-- -------------------------------------------------------------------------------------------------------------------------- -->
<!-- -------------------------------------------------------------------------------------------------------------------------- -->


## Knowing what are the functions, variables  with in a module

<details>

* import myModule
* dir(myModule)

* you can also use as `from myModule import aGivenFunction`
  
</details>


<!-- -------------------------------------------------------------------------------------------------------------------------- -->
<!-- -------------------------------------------------------------------------------------------------------------------------- -->



## Note: 001

<details>
  
```
print("Hello"+"Python") # output: HelloPython (No space when we use +)
print("Hello", "Python") #Output: Hello Python (When we use , it add a space in between these two string.)
```

</details>


<!-- -------------------------------------------------------------------------------------------------------------------------- -->
<!-- -------------------------------------------------------------------------------------------------------------------------- -->



## Note: 002

<details>
  
  ```
print("My age is" , 36) # This will work. As we are not doing any concanitation. ( So, good to use , ) 

print("My age is " + 36)  # This will give you error: "TypeError: must be str, not int"  # + expect both to be string.
```

```
Using + works for combining two strings — it concatenates them. It also works for two numbers — it adds the numbers together.

But, it can't join a string and a number.
```

- This both will work. In comma, we don't need to add space.
- In the second one we are using +, but giveing a space at the end of is, and using "27" as string.
```
print("My age is" , 27)
print("My age is " + "27")
```

```
print("Our combined age is 27" + "32") # output: Our combined age is 2732
```
![Python Concatenation example!](/images/0001_python_image.png "Python Concatenation example")

</details>


<!-- -------------------------------------------------------------------------------------------------------------------------- -->
<!-- -------------------------------------------------------------------------------------------------------------------------- -->



## Note: 003

<details>

```
seconds = 14926

hours = seconds//3600

minutes = (seconds - hours * 3600)//60

final_seconds = seconds%60

print(str(seconds) , "seconds is the same as")
print(str(hours) , "hours," , minutes  , "minutes, and" , final_seconds , "seconds")

```


```
seconds = 14926

hours = seconds // 3600

leftover_seconds = seconds % 3600

minutes = leftover_seconds // 60

final_seconds = leftover_seconds % 60

print(str(seconds) , "seconds is the same as")
print(str(hours) , "hours," , minutes  , "minutes, and" , final_seconds , "seconds")

```

  
</details>




<!-- -------------------------------------------------------------------------------------------------------------------------- -->
<!-- -------------------------------------------------------------------------------------------------------------------------- -->




## Note: 004

<details>

### Naming convention

- Class names start with an Uppercase
- Other identifiers start with lowercase
- starting with single _ : private identifier
- starting with double __ : strongly private
- start and end with double __ : language defined special name.


  
</details>



<!-- -------------------------------------------------------------------------------------------------------------------------- -->
<!-- -------------------------------------------------------------------------------------------------------------------------- -->


## Note: 005 : set

<details>

Example of set: 
set_a = {1,2,3}
print(set_a) # output: {1,2,3}

set_b = {1,2,2,4}
print(set_b) # output: {1,2,4}


  
</details>




<!-- -------------------------------------------------------------------------------------------------------------------------- -->
<!-- -------------------------------------------------------------------------------------------------------------------------- -->


## Note: 006 : Arithmetic Operators

<details>

  - Addition: a + b
  - Subtraction: a - b
  - Multiplication: a * b
  - Division: a / b 
  - Modulus: a % b
  - Exponent: a ** b
  - Floor Division: a // b
</details>


![Python Assignment example!](/images/0002_python_image.png "Python Assignemnt example")



<!-- -------------------------------------------------------------------------------------------------------------------------- -->
<!-- -------------------------------------------------------------------------------------------------------------------------- -->





  
