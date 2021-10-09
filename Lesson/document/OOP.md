# Object - Oriented Programming (OOP)

---

![](C:\Users\admin\OneDrive\05_Learning Python Online\LearningPythonOnline\Lesson\document\image OOP\java-oops.png)

---

**Object**

> + is a basic unit of OOP.
> + Representing real life entities like computers, cars, tables, etc.
> + When create a class, Object can be defined as an instance of that class.
> + When we define an object, it contains an address and takes up space in memory.
>
> > Object have identity, behavior, and state. 
> >
> > For example, a dog object then name of the dog is identity, age, color, the breed are dog's sate. The dog can eat, sleep and bark which are dog behaviors.

**Class**

> + is a user-defined blueprint or prototype.
>
> + A class contains a logical part of the code in the form of methods. 
>
> + We create objects for t he class to access this logic of class.
>
>   ***Point to Remember:*** Class doesn't consume any space, Objects do.

**Method**

> + Writing inside the class.
> + is a collection of statements that perform some specific task. 



<u>**4 Pillar of Object-oriented programming**</u>

> **4 Pillars**
>
> > Encapsulation _*[encapsulation]*
> >
> > Abstraction _*[æbˈstræk.ʃən]*
> >
> > Inheritance _*[ɪnˈher.ɪ.təns]*
> >
> > Polymorphism_*[ˌpɑː.liˈmɔːr.fɪ.zəm]*
> >
> > ---
>
> [**Encapsulation**]()
>
> > + ***Binding of data into single entity***
> >
> > + Encapsulation is a concept of *** bundling of data*** related variables, properties and method in one class.
> >
> > + It is approach for restricting direct access to some of the data structure elements (fields, properties, method, etc).
> >
> > ![](C:\Users\admin\OneDrive\05_Learning Python Online\LearningPythonOnline\Lesson\document\image OOP\encap.JPG)
> >
> > We can see that variables can't see as its private and methods are visible as its public. So binding of these variables and methods into class (entity) is called as Encapsulation. 
> >
> > ***Advantages of Encapsulation:***
> >
> > * Achieve Security.
> > * Enhancement become very easy.
> > * Improve maintenance of application.
> > * provide flexibility.
> >
> > ***Disadvantages:***
> >
> > + Code length may increase.
>
> [**Abstraction**]()
>
> >+ Only essential detail are displayed to the user.
> >
> >+ Non-essential details are hidden to the user.
> >
> >  " Hiding internal detail and show functionality."
> >
> >  > For example: 
> >  >
> >  > - [ ] ​	A car, the user sees a car as a car rather than its individual components.
> >  > - [ ]  Assume a remote controller of a television. The use does not need to know about the internal circuitry of the controller to use it. 
> >  >
> >  > in Java, Abstraction is achieved by abstract class and interface.
> >
> >***Abstract Class***
> >
> >>
> >>
> >>![](C:\Users\admin\OneDrive\05_Learning Python Online\LearningPythonOnline\Lesson\document\image OOP\Difference-Between-Encapsulation-and-Abstraction-in-C_Figure-2.jpg)
> >>
> >>​															Figure: C# Program with an Abstract class.
> >
> >***Interface***
> >
> >>https://pediaa.com/what-is-the-difference-between-encapsulation-and-abstraction-in-c/
> >>
> >>![](C:\Users\admin\OneDrive\05_Learning Python Online\LearningPythonOnline\Lesson\\image OOP\Difference-Between-Encapsulation-and-Abstraction-in-C_Figure-3.jpg)
> >>
> >>​										Figure: C# programing with an Interface.
>
> **[Inheritance]()**
>
> > +  Allows us to define a class that inherits all methods and properties from another class.
> >
> > + Representing the IS-A relationship, also known as a parent-child relationship. 
> >
> >   + **Parent class** is the class being inherited from, also called base class.
> >
> >   + **Child class** is the class inherits from another class, also called derived class.
> >   + **Reusability**: Using inheritance will reuse the code of the fields and method of the existing class when you create a new class.
> >
> > ![](C:\Users\admin\OneDrive\05_Learning Python Online\LearningPythonOnline\Lesson\document\image OOP\types-of-inheritance-c-sharp.png)
> >
> > ***Single***
> >
> > >+ If a child inherits the features of only one superclass is know as single inheritance.
> > >
> > >  ![](C:\Users\admin\OneDrive\05_Learning Python Online\LearningPythonOnline\Lesson\document\image OOP\inheritance11.png)
> > >
> > >```python
> > ># Python program to demonstrate
> > ># single inheritance
> > > 
> > ># Base class
> > >class Parent:
> > >     def func1(self):
> > >            print("This function is in parent class.")
> > > # Derived class
> > >class Child(Parent):
> > >     def func2(self):
> > >        print("This function is in child class.")
> > > # Driver's code
> > >object = Child()
> > >object.func1()
> > >object.func2()
> > >```
> > >
> > >Output:
> > >
> > >```txt
> > >This function is in parent class.
> > >This function is in child class.
> > >```
> >
> > ***Multiple***
> >
> > >+ When a class can be derived from more than one base class.
> > >
> > >+ All the features of the base classes are inherited into derived class.
> > >
> > >  ![](C:\Users\admin\OneDrive\05_Learning Python Online\LearningPythonOnline\Lesson\document\image OOP\multiple-inheritance1.png)
> > >
> > >  ```python
> > >  # Python program to demonstrate
> > >  # multiple inheritance
> > >   
> > >      # Base class1
> > >  class Mother:
> > >      mothername = ""
> > >      def mother(self):
> > >          print(self.mothername)
> > >  # Base class2
> > >  class Father:
> > >      fathername = ""
> > >      def father(self):
> > >          print(self.fathername)
> > >  # Derived class
> > >  class Son(Mother, Father):
> > >      def parents(self):
> > >          print("Father :", self.fathername)
> > >          print("Mother :", self.mothername)
> > >  # Driver's code
> > >  s1 = Son()
> > >  s1.fathername = "RAM"
> > >  s1.mothername = "SITA"
> > >  s1.parents()
> > >  ```
> > >
> > >  Output:
> > >
> > >  ```txt
> > >  Father : RAM
> > >  Mother : SITA
> > >  ```
> >
> > ***Multilevel***
> >
> > >+ Features of the base class and the derived class are further inherited into the new derived class.
> > >
> > >+ This is similar to a relationship representing a child and grandfather.
> > >
> > >  ![](C:\Users\admin\OneDrive\05_Learning Python Online\LearningPythonOnline\Lesson\document\image OOP\Multilevel-inheritance1.png)
> > >
> > >  ```python
> > >  # Python program to demonstrate
> > >  # multilevel inheritance
> > >   
> > >  # Base class
> > >  class Grandfather:
> > >      def __init__(self, grandfathername):
> > >          self.grandfathername = grandfathername
> > >          
> > >   # Intermediate class
> > >  class Father(Grandfather):
> > >      def __init__(self, fathername, grandfathername):
> > >          self.fathername = fathername
> > >          
> > >   # invoking constructor of Grandfather class
> > >          Grandfather.__init__(self, grandfathername)
> > >   # Derived class
> > >  class Son(Father):
> > >      def __init__(self,sonname, fathername, grandfathername):
> > >          self.sonname = sonname
> > >          
> > >   # invoking constructor of Father class
> > >          Father.__init__(self, fathername, grandfathername)
> > >    	def print_name(self):
> > >          print('Grandfather name :', self.grandfathername)
> > >          print("Father name :", self.fathername)
> > >          print("Son name :", self.sonname)
> > >  #  Driver code
> > >  s1 = Son('Prince', 'Rampal', 'Lal mani')
> > >  print(s1.grandfathername)
> > >  s1.print_name()
> > >  ```
> > >
> > >  Output:
> > >
> > >  ```txt
> > >  Lal mani
> > >  Grandfather name : Lal mani
> > >  Father name : Rampal
> > >  Son name : Prince
> > >  ```
> >
> > ***Hierarchical***
> >
> > >+ When more than one derived classes are created from single base.
> > >
> > >  In this program, we have a parent (base) class and two child (derived) classes.
> > >
> > >  ![](C:\Users\admin\OneDrive\05_Learning Python Online\LearningPythonOnline\Lesson\document\image OOP\Hierarchical-inheritance1.png)
> > >
> > >  ```python
> > >  
> > >  # Python program to demonstrate
> > >  # Hierarchical inheritance
> > >   
> > >   # Base class
> > >  class Parent:
> > >        def func1(self):
> > >          print("This function is in parent class.")
> > >   # Derived class1
> > >  class Child1(Parent):
> > >        def func2(self):
> > >          print("This function is in child 1.")
> > >   # Derivied class2
> > >  class Child2(Parent):
> > >        def func3(self):
> > >          print("This function is in child 2.")
> > >  # Driver's code
> > >  object1 = Child1()
> > >  object2 = Child2()
> > >  object1.func1()
> > >  object1.func2()
> > >  object2.func1()
> > >  object2.func3()
> > >  ```
> > >
> > >  Output:
> > >
> > >  ```txt
> > >  This function is in parent class.
> > >  This function is in child 1.
> > >  This function is in parent class.
> > >  This function is in child 2.
> > >  ```
> >
> > ***Hybrid***
> >
> > > + Inheritance consisting of multiple types of inheritance.
> > >
> > >   ```python
> > >    Python program to demonstrate
> > >   # hybrid inheritance
> > >        
> > >   class School:
> > >        def func1(self):
> > >           print("This function is in school.")
> > >   class Student1(School):
> > >        def func2(self):
> > >           print("This function is in student 1. ")
> > >   class Student2(School):
> > >        def func3(self):
> > >           print("This function is in student 2.")
> > >   class Student3(Student1, School):
> > >        def func4(self):
> > >           print("This function is in student 3.")
> > >   # Driver's code
> > >   object = Student3()
> > >   object.func1()
> > >   object.func2()
> > >   ```
> > >
> > >   Output:
> > >
> > >   ```txt
> > >   This function is in school.
> > >   This function is in student 1.
> > >   ```
>
> [**Polymorphism**]()
>
> >+ is the occurrence of two or more clearly different morphs or forms.
> >
> >+ It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.
> >
> >  > *Polymorphism in addition operator.*
> >
> >  ```python
> >  #Example 1: Polymorphism in addition operator
> >  num1 = 1
> >  num2 = 2
> >  print(num1+num2)
> >  
> >  str1 = "Python"
> >  str2 = "Programming"
> >  print(str1+" "+str2)
> >  
> >  """
> >  here, we can see that a single perator + have been used to carry out different operations for distinct data types. This is one of the most simple occurrences of polymorshism in Python.
> >  """
> >  ```
> >
> >  > Function Polymorphism
> >  >
> >  > > There are some functions in python which can compatible to run multiple data types.
> >  > >
> >  > > One such function is the len() function. It can run with many types in Python.
> >  > >
> >  > > ```python
> >  > > #Example 2: Polymorphic len() function
> >  > > print(len("Programiz"))
> >  > > print(len(["Python", "Java", "C"]))
> >  > > print(len({"Name": "John", "Address": "Nepal"}))
> >  > > Output:
> >  > >     9
> >  > >     3
> >  > >     2
> >  > > 
> >  > > """
> >  > > Explanation: you can see that many data types such as string, list, tuple, set, and dictionary can work with len() funtion. However, we can see that it returns specific information about specific data types. 
> >  > > """
> >  > > ```
> >  > >
> >  > > ![](C:\Users\admin\OneDrive\05_Learning Python Online\LearningPythonOnline\Lesson\document\image OOP\polymorphism_function.png)
> >  >
> >  > Class Polymorphism
> >  >
> >  > >Can use the concept of polymorphism while creating class methods as Python allows different classes to have methods with same name.
> >  > >
> >  > >```python
> >  > >class Cat:
> >  > >    def __init__(self, name, age):
> >  > >        self.name = name
> >  > >        self.age = age
> >  > >
> >  > >    def info(self):
> >  > >        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
> >  > >
> >  > >    def make_sound(self):
> >  > >        print("Meow")
> >  > >
> >  > >
> >  > >class Dog:
> >  > >    def __init__(self, name, age):
> >  > >        self.name = name
> >  > >        self.age = age
> >  > >
> >  > >    def info(self):
> >  > >        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
> >  > >
> >  > >    def make_sound(self):
> >  > >        print("Bark")
> >  > >
> >  > >
> >  > >cat1 = Cat("Kitty", 2.5)
> >  > >dog1 = Dog("Fluffy", 4)
> >  > >
> >  > >for animal in (cat1, dog1):
> >  > >    animal.make_sound()
> >  > >    animal.info()
> >  > >    animal.make_sound()
> >  > >```
> >  > >
> >  > >Output:
> >  > >
> >  > >```txt
> >  > >Meow
> >  > >I am a cat. My name is Kitty. I am 2.5 years old.
> >  > >Meow
> >  > >
> >  > >Bark
> >  > >I am a dog. My name is Fluffy. I am 4 years old.
> >  > >Bark
> >  > >```
> >
> >  [Polymorphism and Inheritance]()
> >
> >  > **Method Overriding**
> >  >
> >  > >+ When the child classes inherited method and attributes from the parent class. We can redefine certain methods and attributes specifically to fit the child class.
> >  > >
> >  > >+ Allow us to access these overridden methods and attributes that have the same name as the parent class.
> >  > >
> >  > >  ```python
> >  > >  from math import pi
> >  > >  
> >  > >  
> >  > >  class Shape:
> >  > >      def __init__(self, name):
> >  > >          self.name = name
> >  > >  
> >  > >      def area(self):
> >  > >          pass
> >  > >  
> >  > >      def fact(self):
> >  > >          return "I am a two-dimensional shape."
> >  > >  
> >  > >      def __str__(self):
> >  > >          return self.name
> >  > >  
> >  > >  
> >  > >  class Square(Shape):
> >  > >      def __init__(self, length):
> >  > >          super().__init__("Square")
> >  > >          self.length = length
> >  > >  
> >  > >      def area(self):
> >  > >          return self.length**2
> >  > >  
> >  > >      def fact(self):
> >  > >          return "Squares have each angle equal to 90 degrees."
> >  > >  
> >  > >  
> >  > >  class Circle(Shape):
> >  > >      def __init__(self, radius):
> >  > >          super().__init__("Circle")
> >  > >          self.radius = radius
> >  > >  
> >  > >      def area(self):
> >  > >          return pi*self.radius**2
> >  > >  
> >  > >  
> >  > >  a = Square(4)
> >  > >  b = Circle(7)
> >  > >  print(b)
> >  > >  print(b.fact())
> >  > >  print(a.fact())
> >  > >  print(b.area())
> >  > >  ```
> >  > >
> >  > >  Output:
> >  > >
> >  > >  ```txt
> >  > >  Circle
> >  > >  I am a two-dimensional shape.
> >  > >  Squares have each angle equal to 90 degrees.
> >  > >  153.93804002589985
> >  > >  ```
> >  > >
> >  > >  ![](C:\Users\admin\OneDrive\05_Learning Python Online\LearningPythonOnline\Lesson\document\image OOP\polymorphism_overriting.png)
> >  >
> >  > **Method Overloading**:
> >  >
> >  > > A way to create multiple methods with the same but different arguments, ***is not possible in Python.***
> >  >
> >  > 
> >
> >  
>
> ---
>
> Reference link:
>
> 1. https://www.programiz.com/python-programming/polymorphism
> 2. https://pediaa.com/category/technology/it/programming/
> 3. https://www.thecodingshala.com/2019/07/java-inheritance-coding-shala.html
> 4. https://www.geeksforgeeks.org/types-of-inheritance-python/

