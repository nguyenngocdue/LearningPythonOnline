# Property in Python

---

The `property()` function is used to define properties in the Python class.

The `property()` method in Python provides an interface to instance attributes. It encapsulates instance attributes and provides a property, same as Java and C#.

The `property()` method takes the get, set and delete methods as arguments and returns an object of the `property` class.

It is recommended to use the [property decorator](https://www.tutorialsteacher.com/python/property-decorator) instead of the `property()` method.



```python
class person:
    def __init__(self):
        self.__name=''
    def setname(self, name):
        print('setname() called')
        self.__name=name
    def getname(self):
        print('getname() called')
        return self.__name
    name=property(getname, setname)
```

```python
class person:
    def __init__(self, name):
        self.__name=name
    def setname(self, name):
        print('setname() called')
        self.__name=name
    def getname(self):
        print('getname() called')
        return self.__name
    def delname(self):
        print('delname() called')
        del self.__name
    # Set property to use get_name, set_name
    # and del_name methods
    name=property(getname, setname, delname)
```

https://www.tutorialsteacher.com/python/property-function

https://en.wikipedia.org/wiki/Property_(programming)

