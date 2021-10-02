""" Ví Dụ: """
my_tuple = 1, 2, 3, 'a', 'b'
out = (100,)+ my_tuple[1:] # slicing tuple
print(out)

out = 100, *my_tuple[1:] #packing --> unpacking tuple
print(out)

my_tuple = 1, 2, 3, 4 ['a', 'b', 1]
out = my_tuple[-1].append(100,)
print(out)

#immutable data type

print({})
print(1)