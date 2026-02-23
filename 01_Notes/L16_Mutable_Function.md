nonlocal

```python
a = [1, 2]
b = [3, 4]
a += b , a = a + b # they are different !
```

- nonlocal cannot be used with global variables (names defined in the global frame).
- If no nonlocal variable is found with the given name, a SyntaxError is raised.
- A name that is already local to a frame cannot be declared as nonlocal.