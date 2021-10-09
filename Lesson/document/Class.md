# Python Classes / Objects

---

Python has been an object-oriented language since it existed. Because of this, creating and using classes and objects are downright easy. 

> in Python:
>
> > An object oriented programing language (OOP)
> >
> > Almost everything is an object, with its properties and methods.
> >
> > A class is like an object constructor, or a 'blueprint' for creating objects.

**Overview of OOP Terminology**

> **Class:**
>
> > - A user-defined prototype for an object that the define a set of attributes that characterizes any object of the class.
> > - The attributes are dats members ( class variables and instance variables) and methods, accessed via dot notation.
>
> **Class variable:**
>
> > + A variable that s shared by all instance of a class.
> > + It is defined with a class but outside any of the class's methods.
> > + It is not used as frequently as instance variable are.
>
> **Data member:**
>
> > - A class variable or instance variable that holds associated  with a class and its objects.
> >
> >   May be private or public
> >
> >   
>
> **Function overloading:**
>
> > + The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or argument involved. 
>
> **Instance variable:**
>
> > + A variable that is defined inside a method and belongs only to the current instance of a class.
> >
> >   ```c++
> >   class Animal{
> >     public:
> >     		static int a; // Stactic Variable
> >     		int b; // instance variable
> >     public:
> >     func()
> >     {
> >     		int c; // local varibale  
> >     }
> >   }
> >   ```
> >
> >   
>
> **Inheritance:** 
>
> > * Transfer of the characteristics of a class to other classes that are derived from it.
> >
> >   ```python
> >   #Create a Parent Class
> >   #Create a class named Person, with firstname and lastname properties, and a printname method:
> >   class Person:
> >       def __init__(self, fname, lname):
> >           self.firstname = fname
> >           self.lastname = lname
> >          def printname(self):
> >       	print(self.firstname, self.lastname)
> >    #Use the Person class to create an object, and then execute the printname method:
> >   x = Person("John", "Doe")
> >   x.printname()
> >   
> >      #Create a Child Class
> >   #Create a class named Student, which will inherit the properties and methods from the Person class:
> >   class Student(Person):
> >       pass
> >   x = Student("Mike", "Olsen")
> >   x.printname()
> >   
> >      #OUT = Mike Olse
> >   
> >      ```
>
> **Instance:**
>
> > + An  individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.
> >
> >   
>
> **Instantiation:**
>
> > + The creation of an instance of a class.
>
> **Method:**
>
> > + A special kind of function that is defined in a class definition.
> >
> >   ![](C:\Users\admin\OneDrive\05_Learning Python Online\LearningPythonOnline\Lesson\document\image\instancemethod.png)
> >
> >   
>
> **Object:**
>
> > + A unique instance of data structure that's defined by its class. Ad object comprises both data members ( class variables and instance variables) and methods.
> >
> >
>
> **Operator overloading:**
>
> > + The assignment of more than more one function to a particular operator.
> >
> >   We can change the way operations work for user-defined types like objects and structures. This is known as ***operator overloading***.
>
> **Constructor**:
>
> > + is a special type of subroutine called to create an object.
> >
> > + Preparing the new object for use, often accepting arguments that constructor uses to set required member variables.
> >
> > + A constructor resembles an instance method, but it has no explicit return type, it is implicitly inherited and it usually has different rules for scope modifilers. 
> >
> >   ```C#
> >   public class MyClass
> >   {
> >       private int a;
> >       private string b;
> >   
> >       // Constructor
> >       public MyClass() : this(42, "string")
> >       {
> >       }
> >   
> >       // Overloading a constructor
> >       public MyClass(int a, string b)
> >       {
> >           this.a = a;
> >           this.b = b;
> >       }
> >   }
> >   ```
> >
> >   
>
> **Member variable:**
>
> >+ member variable (sometimes called a member field) is a variable that is associated with a specific object, and accessible for all its methods (member functions).
> >
> >```c++
> >class Foo {
> >    int bar; // Member variable
> >  public:
> >    void setBar(const int newBar) { 
> >      bar = newBar;
> >    }
> >};
> >
> >int main () {
> >  Foo rect; // Local variable
> >
> >  return 0;
> >}
> >```
> >
> >

---

#Class

**Creating Classes**

The class statement creates a new class definition. > Keyword : "class' followed by a colon as follows:

```python
class ClassName:
   #'Optional class documentation string'
   class_suite
```

- [ ] The class has a documentation string, which can be accessed via ClassName._________doc_____.

- [ ] The class_suite consists of all the component statement defining class members, data attributes and functions.

**Terminology in Class**

>**______init__()** 
>
>> + is a special method, which is called class constructor or initialization method.
>
>> + is called automatically every time the class is being used to create a new object.
>
>>   ```python
>>   #constructor synonym with initialization
>>   class Animal():
>>   def __init__(self):
>>        pass
>>   ```
>
>>   ```python
>>   Example:
>>   #Create a class named Animal, use the __init__() function to assign values for name and shout:
>>   class Animal:
>>   def __init__(self, name, shout):
>>        self.name = name
>>        self.shout = shout
>>   def greeting(self, para):
>>     	return "Hello guys! My name is " + self.name + para
>
>>   animal1 = Animal('dog', 'gaugau') #-> this is called an instance or object which will occur for Class self -> animal1 , name -> dog, shout -> gaugau 
>
>>   print(animal1.name)
>>   print(animal1.shout)
>>   print(animal1.gretting(" Pug"))
>>
>>   ```
>
>>   ```python
>>   dog
>>   gaugau
>>   Hello guys! My name is dog Pug
>>   ```
>
>
>
>**self**
>
>> + it represents the instance of the class.
>> + By using the 'self' key word --> can access the attributes and methods of the class. (It binds the attributes with the given argument).
>> + It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class.
>
>> ***What reason do you need to use self?***
>
>> + Python does not use the @syntax to refer to instance attributes.
>> + Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically. 
>
>> > > ***Self is always pointing to Current Object.***
>> >
>> > ```python
>> > #it is clearly seen that self and obj is referring to the same object
>> > class check:
>> > def init(self):
>> >     print("Address of self = ",id(self))
>> > 
>> > obj = check()
>> > print("Address of class object = ",id(obj))
>> > ```
>> >
>> > ```python
>> > Address of self =  140124194801032
>> > Address of class object =  140124194801032
>> > ```
>> >
>> > Another example of using Self:
>> >
>> > ```python
>> > class car():
>> >  #init method or constructor
>> > 	def init(self, model, color):
>> >         self.model = model
>> >         self.color = color
>> > 
>> > 	def show(self):
>> >     	print("Model is", self.model )
>> >      	print("color is", self.color )
>> > 
>> > #both objects have different self which
>> > #contain their attributes
>> > audi = car("audi a4", "blue")
>> > ferrari = car("ferrari 488", "green")
>> > 
>> > audi.show()     # same output as car.show(audi)
>> > ferrari.show()  # same output as car.show(ferrari)
>> > 
>> > #Behind the scene, in every instance method
>> > #call, python sends the instances also with
>> > #that method call like car.show(audi)
>> > ```
>> >
>> > Output
>> >
>> > ```python
>> > Model is audi a4
>> > color is blue
>> > Model is ferrari 488
>> > color is green
>> > ```
>> >
>> > > ***Self is the first argument to be passed in Constructor and Instance Method.***
>> >
>> > self must be provided as a First parameter to the Instance method and constructor. If you don't provide it, it will cause an error. 
>> >
>> > ```python
>> > # Self is always required as the first argument
>> > class check:
>> > def __init__():
>> >     print("This is Constructor")
>> > object = check()
>> > print("Worked fine")
>> > 
>> > """
>> > Following Error is produced if Self is not passed as an argument
>> > Traceback (most recent call last):
>> > File "/home/c736b5fad311dd1eb3cd2e280260e7dd.py", line 6, in <module>
>> > object = check()
>> > TypeError: init() takes 0 positional arguments but 1 was given
>> > ```
>> >
>> > > ***Self is a convention and not a Python keyword .***
>> >
>> > ```python
>> > # Write Python3 code here
>> > class this_is_class:
>> > def __init__(in_place_of_self):
>> >     print("we have used another "
>> >     "parameter name in place of self"
>> >     "It means that you can change any words you want")
>> > object = this_is_class()
>> > ```
>
>

---

# Class Inheritance

Instead of starting from scratch, you can create a class by deriving it from a preexisting class by listing the parent class in parentheses after the new class name.

The child class inherits the attributes of its parent class. 

You can use those attributes as if they were defined in the child class. 

A child class can also override data members and methods from the parent.



---

# Object Methods

Objects can also contain methods. Methods in objects are functions that belong to the object.

Example:

```python
#Insert a function that prints a greeting, and execute it on the p1 object:
class Animal:
    def __init__(self, name, food):
    	self.name = name
    	self.food = food
    def myfunc(self):
    	print("Hello my name is " + self.name)

p1 = Person("Dog", 36)
p1.myfunc()
```

Output

```
Hello my name is Dog
```

