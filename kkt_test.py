import numpy as np
from scipy.optimize import minimize

def objective(x):
    return -((1000+141*x[0]+101*x[1]+94*x[2]+67*x[3]+157*x[4]+108*x[5])*(1+((1000+101*x[0]+141*x[1]+67*x[2]+94*x[3]+108*x[4]+157*x[5])-895)/2100*((101*x[0]+101*x[1]+67*x[2]+67*x[3]+108*x[4]+108*x[5])/1500+0.5)))

def constraint1(x):
    return -((1000+101*x[0]+141*x[1]+67*x[2]+94*x[3]+108*x[4]+157*x[5])-895)/2100 +0.8

def constraint2(x):
    return x[0]+x[1]-1

def constraint3(x):
    return x[2]+x[3]-1

def constraint4(x):
    return x[4]+x[5]-1



# initial guesses
n = 6
x0 = np.zeros(n)
#x0[0] = 1.0
#x0[1] = 0.0
#x0[2] = 1.0
#x0[3] = 0.0
#x0[4] = 1.0
#x0[5] = 0.0

# show initial objective
print('Initial SSE Objective: ' + str(objective(x0)))

# optimize
b = (0.0,1.0)
bnds = (b, b, b, b, b, b)
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'eq', 'fun': constraint2}
con3 = {'type': 'eq', 'fun': constraint3}
con4 = {'type': 'eq', 'fun': constraint4}

cons = ([con1,con2,con3,con4])
solution = minimize(objective,x0,method='SLSQP',bounds=bnds,constraints=cons)
x = solution.x

# show final objective
print('Final SSE Objective: ' + str(objective(x)))

# print solution
print('Solution')
print('x1 = ' + str(x[0]))
print('x2 = ' + str(x[1]))
print('x3 = ' + str(x[2]))
print('x4 = ' + str(x[3]))
print('x5 = ' + str(x[4]))
print('x6 = ' + str(x[5]))
