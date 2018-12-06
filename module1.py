a_var = 'global variable'

def a_func():
    global a_var
    a_var = 'local variable'
    print(a_var, '[ a_var inside a_func() ]')
    
a_func()
print(a_var, '[ a_var outside a_func() ]')
