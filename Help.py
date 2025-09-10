x = "hello"
# dir() Lists all the attributes and functions (methods) associated with an object.
print(dir(x))

# help() Gives documentation about the object, including explanations of methods.
help(str)

help(x.upper)

# You can directly check the docstring of a function/class with .__doc__:
print(str.upper.__doc__)

# inspect module for more advanced digging
import inspect

print(inspect.getmembers(str, inspect.isfunction))
