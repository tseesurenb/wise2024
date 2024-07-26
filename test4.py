
#%%
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
 
 
sg = simpleGeneratorFun() 
# Driver code to check above generator function
for value in enumerate(sg):
    print(value)
# %%
