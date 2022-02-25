def adder(x, y):
    """adds two numbers together """
    
    print("INSIDE OF ADDER")
    return x + y 

#assert - expects a condition to be true, and if its not true, it will raise an error.  it looks  like this 

# if not condition: 
#     raise AssertionError

assert adder(2,5) == 7 , ' scenario A '
# assert adder(2,7) == 10, ' scenario B '
assert adder(2,8) == 10, 'scenario c '

# Assert is used mostly if you are anticipating a bug to happen in your code block and you want to raise an exception immediately.   You are testing conditions.  Exception messages are displayed if the expression is False.   This can help identify bugs.   


print (" Hello World!!! ")