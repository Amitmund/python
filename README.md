# Python Notes

Notes from multiple learning sources. Thank you all.

- https://github.com/hiteshchoudhary/chai-aur-python


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


