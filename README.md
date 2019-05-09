# Private Function Decorator
A decorator that makes a function private by executing a replacement function or a function that returns None (DEFAULT) when other class tries to access the function.

- Example,returns None (Default option):
```
@private
def foo():
  print("Private!")
```  
- Example 2, returns a replacement function:
```
def replace():
  print("You tried to access a private function.")
  
@private(replacement_function=replace)
def foo():
  print("Private!")
```
