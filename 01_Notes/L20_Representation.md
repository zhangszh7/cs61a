
# Lecture 20

## Topic

Three techniques to make a **generic** function:
- shared interface 
- type dispatching
- type coercion

Certain functions should apply to multiple data types.
 
In Python, functions are **first-class** objects. 
What does **first-class** mean in the context of Python?

**representation:**
- `repr()`
- `str` is a **class**.
By default, the result of `str()` is the same as what `repr()` returns, unless `__str__` is explicily defined.

**interface:**
Different classes share the special identical attribute name .

**type dispatch:**
`isinstance()`: to estimate if the object is belong to the specified class(or any subclasses inherited from it).
`type()`: to return the exact **type** of the object.

**type coercion:**
To transform an object of one type into an equivalent object of another type. 