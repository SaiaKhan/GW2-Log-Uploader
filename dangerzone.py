import numpy as np
from scipy.optimize import minimize
from stats import stats

def objective(x):
    return -((1000+stats.get_stats("helmet_3")[0]*x[0]\
            +stats.get_stats("helmet_3")[1]*x[1]\
            +stats.get_stats("shoulder_3")[0]*x[2]\
            +stats.get_stats("shoulder_3")[1]*x[3]\
            +stats.get_stats("chest_3")[0]*x[4]\
            +stats.get_stats("chest_3")[1]*x[5]\
            +stats.get_stats("gloves_3")[0]*x[6]\
            +stats.get_stats("gloves_3")[1]*x[7]\
            +stats.get_stats("legs_3")[0]*x[8]\
            +stats.get_stats("legs_3")[1]*x[9]\
            +stats.get_stats("boots_3")[0]*x[10]\
            +stats.get_stats("boots_3")[1]*x[11]\
            +stats.get_stats("amulet_3")[0]*x[12]\
            +stats.get_stats("amulet_3")[1]*x[13]\
            +stats.get_stats("ring_3")[0]*x[14]\
            +stats.get_stats("ring_3")[1]*x[15]\
            +stats.get_stats("ring_3")[0]*x[16]\
            +stats.get_stats("ring_3")[1]*x[17]\
            +stats.get_stats("earring_3")[0]*x[18]\
            +stats.get_stats("earring_3")[1]*x[19]\
            +stats.get_stats("earring_3")[0]*x[20]\
            +stats.get_stats("earring_3")[1]*x[21]\
            +stats.get_stats("backpiece_3")[0]*x[22]\
            +stats.get_stats("backpiece_3")[1]*x[23]\
            +stats.get_stats("2h_weap_3")[0]*x[24]\
            +stats.get_stats("2h_weap_3")[1]*x[25]\
            )*(1+((1000\
            +stats.get_stats("helmet_3")[1]*x[0]\
            +stats.get_stats("helmet_3")[0]*x[1]\
            +stats.get_stats("shoulder_3")[1]*x[2]\
            +stats.get_stats("shoulder_3")[0]*x[3]\
            +stats.get_stats("chest_3")[1]*x[4]\
            +stats.get_stats("chest_3")[0]*x[5]\
            +stats.get_stats("gloves_3")[1]*x[6]\
            +stats.get_stats("gloves_3")[0]*x[7]\
            +stats.get_stats("legs_3")[1]*x[8]\
            +stats.get_stats("legs_3")[0]*x[9]\
            +stats.get_stats("boots_3")[1]*x[10]\
            +stats.get_stats("boots_3")[0]*x[11]\
            +stats.get_stats("amulet_3")[1]*x[12]\
            +stats.get_stats("amulet_3")[0]*x[13]\
            +stats.get_stats("ring_3")[1]*x[14]\
            +stats.get_stats("ring_3")[0]*x[15]\
            +stats.get_stats("ring_3")[1]*x[16]\
            +stats.get_stats("ring_3")[0]*x[17]\
            +stats.get_stats("earring_3")[1]*x[18]\
            +stats.get_stats("earring_3")[0]*x[19]\
            +stats.get_stats("earring_3")[1]*x[20]\
            +stats.get_stats("earring_3")[0]*x[21]\
            +stats.get_stats("backpiece_3")[1]*x[22]\
            +stats.get_stats("backpiece_3")[0]*x[23]\
            +stats.get_stats("2h_weap_3")[1]*x[24]\
            +stats.get_stats("2h_weap_3")[0]*x[25]\
            )-895)/2100\
            *((+stats.get_stats("helmet_3")[2]*x[0]\
            +stats.get_stats("helmet_3")[2]*x[1]\
            +stats.get_stats("shoulder_3")[2]*x[2]\
            +stats.get_stats("shoulder_3")[2]*x[3]\
            +stats.get_stats("chest_3")[2]*x[4]\
            +stats.get_stats("chest_3")[2]*x[5]\
            +stats.get_stats("gloves_3")[2]*x[6]\
            +stats.get_stats("gloves_3")[2]*x[7]\
            +stats.get_stats("legs_3")[2]*x[8]\
            +stats.get_stats("legs_3")[2]*x[9]\
            +stats.get_stats("boots_3")[2]*x[10]\
            +stats.get_stats("boots_3")[2]*x[11]\
            +stats.get_stats("amulet_3")[2]*x[12]\
            +stats.get_stats("amulet_3")[2]*x[13]\
            +stats.get_stats("ring_3")[2]*x[14]\
            +stats.get_stats("ring_3")[2]*x[15]\
            +stats.get_stats("ring_3")[2]*x[16]\
            +stats.get_stats("ring_3")[2]*x[17]\
            +stats.get_stats("earring_3")[2]*x[18]\
            +stats.get_stats("earring_3")[2]*x[19]\
            +stats.get_stats("earring_3")[2]*x[20]\
            +stats.get_stats("earring_3")[2]*x[21]\
            +stats.get_stats("backpiece_3")[2]*x[22]\
            +stats.get_stats("backpiece_3")[2]*x[23]\
            +stats.get_stats("2h_weap_3")[2]*x[24]\
            +stats.get_stats("2h_weap_3")[2]*x[25]\
            )/1500+0.5)))

def constraint1(x):
    """This is the crit chance constraint"""
    return -((1000\
    +stats.get_stats("helmet_3")[1]*x[0]\
    +stats.get_stats("helmet_3")[0]*x[1]\
    +stats.get_stats("shoulder_3")[1]*x[2]\
    +stats.get_stats("shoulder_3")[0]*x[3]\
    +stats.get_stats("chest_3")[1]*x[4]\
    +stats.get_stats("chest_3")[0]*x[5]\
    +stats.get_stats("gloves_3")[1]*x[6]\
    +stats.get_stats("gloves_3")[0]*x[7]\
    +stats.get_stats("legs_3")[1]*x[8]\
    +stats.get_stats("legs_3")[0]*x[9]\
    +stats.get_stats("boots_3")[1]*x[10]\
    +stats.get_stats("boots_3")[0]*x[11]\
    +stats.get_stats("amulet_3")[1]*x[12]\
    +stats.get_stats("amulet_3")[0]*x[13]\
    +stats.get_stats("ring_3")[1]*x[14]\
    +stats.get_stats("ring_3")[0]*x[15]\
    +stats.get_stats("ring_3")[1]*x[16]\
    +stats.get_stats("ring_3")[0]*x[17]\
    +stats.get_stats("earring_3")[1]*x[18]\
    +stats.get_stats("earring_3")[0]*x[19]\
    +stats.get_stats("earring_3")[1]*x[20]\
    +stats.get_stats("earring_3")[0]*x[21]\
    +stats.get_stats("backpiece_3")[1]*x[22]\
    +stats.get_stats("backpiece_3")[0]*x[23]\
    +stats.get_stats("2h_weap_3")[1]*x[24]\
    +stats.get_stats("2h_weap_3")[0]*x[25])-895)/2100 +0.8

def constraint2(x):
    """Constraint for the choice of the helmet"""
    return x[0]+x[1]-1

def constraint3(x):
    """Constraint for the choice of the shoulders"""
    return x[2]+x[3]-1

def constraint4(x):
    """Constraint for the choice of the chest"""
    return x[4]+x[5]-1

def constraint5(x):
    """Constraint for the choice of the gloves"""
    return x[6]+x[7]-1

def constraint6(x):
    """Constraint for the choice of the legs"""
    return x[8]+x[9]-1

def constraint7(x):
    """Constraint for the choice of the boots"""
    return x[10]+x[11]-1

def constraint8(x):
    """Constraint for the choice of the amulet"""
    return x[12]+x[13]-1

def constraint9(x):
    """Constraint for the choice of the ring 1"""
    return x[14]+x[15]-1

def constraint10(x):
    """Constraint for the choice of the ring 2"""
    return x[16]+x[17]-1

def constraint11(x):
    """Constraint for the choice of the earring 1"""
    return x[18]+x[19]-1

def constraint12(x):
    """Constraint for the choice of the earring 2"""
    return x[20]+x[21]-1

def constraint13(x):
    """Constraint for the choice of the backpiece"""
    return x[22]+x[23]-1

def constraint14(x):
    """Constraint for the choice of the weapon"""
    return x[24]+x[25]-1



# initial guesses
n = 26
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
bnds = (b, b, b, b, b, b, b, b, b, b, b, b, b)
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'eq', 'fun': constraint2}
con3 = {'type': 'eq', 'fun': constraint3}
con4 = {'type': 'eq', 'fun': constraint4}
con5 = {'type': 'eq', 'fun': constraint5}
con6 = {'type': 'eq', 'fun': constraint6}
con7 = {'type': 'eq', 'fun': constraint7}
con8 = {'type': 'eq', 'fun': constraint8}
con9 = {'type': 'eq', 'fun': constraint9}
con10 = {'type': 'eq', 'fun': constraint10}
con11 = {'type': 'eq', 'fun': constraint11}
con12 = {'type': 'eq', 'fun': constraint12}
con13 = {'type': 'eq', 'fun': constraint13}
con14 = {'type': 'eq', 'fun': constraint14}

cons = ([con1,con2,con3,con4,con5,con6,con7,con8,con9,con10,con11,con12,con13,con14])
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
