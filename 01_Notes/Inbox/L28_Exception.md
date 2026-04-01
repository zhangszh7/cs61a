
# Exception

An exception(object instance) belongs to a class wich inherits directly or indirectly from the `BaseException` class.
The statement `raise` constructs an exception and raises it.

**try:**
An exception can be handled by a `try` statement.
For example:
```python
try:
    rasie ValueError()
except ValueError as e:
    print(e)
```