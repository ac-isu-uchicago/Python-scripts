import mymodule

print(mymodule.foo)
print(mymodule.hello())

from mymodule import foo # this statement import only foo variable from mymodule
print(foo)

dir(module_name)