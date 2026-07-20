def outer_function(name):
    def inner_function():
        print (f"Hello {name}")
    inner_function()
    
print(outer_function("Shankar"))