#Buổi 8: Function

#Python Functions

> A function if a block of code which only runs when it is called.
>
> You can pass data, known as parameters, into a function.
>
> A function can return data as a result.

Creating a Function

​    A function is defined using the "def" keyword:

​    Example: 

​        def my_functionName():

​            print('Hello from a function')

Calling a Function

​    def my_functionName():

​        print('Hello world')

​    

​    my_functionName()

Arguments:

​    Information can be passed into functions ad arguments.

​    Arguments are specified after the function name, insdie the parentheses. You can add as many arguments as you want, just separate them with a comma.

Arbitrary Arguments, *args

​    If you do not know how many arguments that will be passed into your function, add a *  before the parameter name in the function definition.

​    This way the function will receive a tuple of arguments, and can accsess the items accordingly:

Example:

​    If the number of arguments is unknow, add a * before the parameter name:

​        def my_functionName(*kids):

​            print('The youngest child is' + kids[2])

​        

​        my_funtionname('Email', 'Tobias', 'Linus')

​    # Arbitary Arguments are often shortened to *args in Python documentations.

Keyword Arguments:

Arbitrary Keyword Arguments, **kwargs

​    If you do not know how many keyword arguments that will be passed into your function, add two astersk: ** before the parameter name in the function definition.

​    This way the function will receive a dictionary of arguments, and can access the items accordingly:

Example:

​    If the number of keyword arguments is unknown, add a double ** before the parameter name:

​    

​        def my_functionName(**kid):

​            print('My name name is' + kid['1name])

​        my_functionName(fname = 'Tobias', 1lame = 'Redsnes')

Fefault argument must to at the end of arguments

Don't allow 2 arguments do packing => (*arg, *arg)=> wrong

You have to use keyword behind packing argument => (*arg, key = 'sample value')

When you use dictionary, the function only out "key" of value. => using unpacking (*dic)

you have key in argument of function to get Key:val ==> def functionName(name, member) with name and member are key in dictionary.

you can also use packing (**kargs) to get key:val

Rule: Positional Argument before Keyword Argument

=>> def best_function_ever(*args, **kwargs)

print nhận bao nhiêu argument cũng được ?

nhờ packing argument đôi khi bạn sẽ không biết trước được pass vào bao nhiêu argument => control that thing impossible

Packing argument đồng nghĩa với việc nhờ 1 biến đi gói tất cả các giá trị truyền vào cho hàm bằng positional argument thành một tuple, nếu không có gì để gói bạn không truyền vào bất kỳ cái gì bạn sẽ nhận được một tuple rỗng.

Để giao nhiệm vụ cho một biến làm công việc này bạn bắt đầu trước nó bởi 1 dấu * (astersk)



Vấn đề lập trình tuần tự: nó nhai đi nhai lại nhiều lần của một nhiệm vụ. Code không có hệ thống cùng một cách tính thống nhất. (một bài toán nhiều cách giải á).



