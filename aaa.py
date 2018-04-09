def my_cons():
    res = []
    for i in range(0, 5, 2):
        def _temp(x):
            return x[i] * x[i+1]
        res.append(_temp)
    return res

def make_func():
    def _function(x,i):
        #print(x[i] + x[i+1] - 1)
        return x[i] + x[i+1] -1
    return _function

print(make_func())
# my_functions = [make_func(i) for i in range(4)]
# i=0
# for each in my_functions:
#     each([0,1,2,3,4,5,6,7],i)
#     i+=2
