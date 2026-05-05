# you can write [global [variable]] to refer to a global variable inside a funtion
# this is nessecary when we want to reassign values, specially immutable ones
# optional otherwise
#
# variables follw L-"local" - same funtion
#                 E-"Enlcosing" - enclosing the local scope (for nested fn definition, as many nested needed)
#                 G-"Global"- global scope
#                 B-"Built-in" - built-in variables for the interpreter
# order of identity
# [global [variable]] overrides this
#
# basicaly, to help the interpreter find if we are referencing a global or local variable / 
#                                        what is the scope of the variable we are referencing/
#                                        from where to pick the value/definition of that variable
# to operate on it
# works on function defintitions as well
# 

def max():
    y=0
    print(z)    #picks from global/ adding "global z" lets you operate on it
    def f1():
        x=0
        print(x)    # picks/ operates from local
        print(y)    #picks from enclosing/ adding "non-local y" lets you operate on it
        print(z)    #picks from global/ adding "global z" lets you operate on it
        print(True) #picks from built in/ incuded modules
z=0 
print(z)    #picks from global
max() #picks from global, not built in
#cannot use built in max!!