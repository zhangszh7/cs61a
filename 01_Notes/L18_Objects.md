- class(type)
- instantiate
- (instance)attribute > (class)attribute
- method

- constructor: `__init__(self, ...)`
- a dot expression: `<expression>.<name>`
- `getattr` `hasattr`

- the difference between `functions` and `bound methods`:
- Class names are conventionally written using the CapWords convention
- Method names follow the standard convention of naming functions using lowercased words separated by underscores.

- inheritance: base class and subclass, override
- multiple inheritace
- interface: share the same attribute name.

- `method` return `value` instead of the `object`, like `list.insert()` return `None` instead of the `list`.
- be careful with the `shallow copy` when using mutable objects such as the `list`.