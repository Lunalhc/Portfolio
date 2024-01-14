from sympy.functions.combinatorial.factorials import subfactorial
from sympy.calculus.euler import euler_equations
import math
import numpy as np
from scipy.optimize import fsolve
import sympy as sp
import random
from fractions import Fraction
from sympy import symbols, Eq, solve
from itertools import product



# question #1

# solve the system using a multivariate root finder
# r_1(x,y,z,d): sqrt( (x-A1)^2 + (y-B1)^2 + (z-C1)^2 ) - c(t1-d) = 0
# r_2((x,y,z,d): sqrt( (x-A2)^2 + (y-B2)^2 + (z-C2)^2 ) - C(t2-d) = 0
# r_3(x,y,z,d): sqrt( (x-A3)^2 + (y-B3)^2 + (z-C3)^2 ) - c(t3-d) = 0
# r_4 =(x,y,z,d) sqrt( (x-A4)^2 + (y-B4)^2 + (z-C4)^2 ) - c(t4-d) = 0

# fine the receiver position (x,y,z) near earth and time correction d
# location of 4 satellites (A,B,C) =  (15600, 7540, 20140),(18760, 2750, 18610),(17610, 14630, 13480),(19170, 610, 18390) in km
# measured time intervals (t) 0.07074, 0.07220, 0.07690, 0.07242 in seconds, respectively
# set the initial vector to be (x0, y0, z0, d0) = (0, 0, 6370, 0)

# As a check, the answer (x,y,z) = (−41.77271,−16.78919, 6370.0596), d = -3.201566*10^-3 seconds


c = 299792.458
ABCs = np.array([[15600, 7540, 20140],
               [18760, 2750, 18610],
               [17610, 14630, 13480],
               [19170, 610, 18390]])

ts = np.array([0.07074, 0.07220, 0.07690, 0.07242])


def equations(variables):

    x, y, z, d = variables
    eq1 = np.sqrt((x - ABCs[0, 0])**2 + (y - ABCs[0, 1])**2 + (z - ABCs[0, 2])**2) - c * (ts[0] - d)
    eq2 = np.sqrt((x - ABCs[1, 0])**2 + (y - ABCs[1, 1])**2 + (z - ABCs[1, 2])**2) - c * (ts[1] - d)
    eq3 = np.sqrt((x - ABCs[2, 0])**2 + (y - ABCs[2, 1])**2 + (z - ABCs[2, 2])**2) - c * (ts[2] - d)
    eq4 = np.sqrt((x - ABCs[3, 0])**2 + (y - ABCs[3, 1])**2 + (z - ABCs[3, 2])**2) - c * (ts[3] - d)

    return [eq1, eq2, eq3, eq4]


initial_guess = [0, 0, 6370, 0]

result = fsolve(equations, initial_guess)

print("Solution (x, y, z, d):", result)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# question #2

# carry out the solution via the quadratic formula
# By Subtracting the last three equations of (4.37) from the first
# yield to three linear equations in 4 unknowns
# x*u_x + y*u_y + z*u_z + d*u_d + w = 0  expressed in vector form
# A formula for x in terms of d :
# 0 = det[u_y | u_z | x*u_x + y*u_y + z*u_z + d*u_d + w]
# we can arrive at formulas for y and z respectively in terms of d, that can be subsituted in the first quadratic equation of (4.3.7) to make it an equation in 1 variable


A1, B1, C1, t1, A2, B2, C2,t2, A3, B3, C3, t3, A4, B4, C4, t4 = sp.symbols('A1 B1 C1 t1 A2 B2 C2 t2 A3 B3 C3 t3 A4 B4 C4 t4')
x, y, z, d, c = sp.symbols('x y z d c')


eq1 = (x - A1)**2 + (y - B1)**2 + (z - C1)**2 - c**2 * (t1 - d)**2
eq2 = (x - A2)**2 + (y - B2)**2 + (z - C2)**2 - c**2 * (t2 - d)**2
eq3 = (x - A3)**2+ (y - B3)**2 + (z - C3)**2 - c**2 * (t3 - d)**2
eq4 = (x - A4)**2 + (y - B4)**2 + (z - C4)**2 - c**2 * (t4 - d)**2

subtract_equations = [eq1 - eq2, eq1 - eq3, eq1 - eq4]


expanded_equations = [sp.expand(eq) for eq in subtract_equations]

factored_equations = [sp.collect(eq, [x, y, z, d]) for eq in expanded_equations]

for i, eq in enumerate(factored_equations, 1):
    print(f"Equation {i}: {eq}")


u_x = np.array([-2 * A1 + 2 * A2, -2 * A1 + 2 * A3, -2 * A1 + 2 * A4])
u_y = np.array([-2 * B1 + 2 * B2, -2 * B1 + 2 * B3, -2 * B1 + 2 * B4])
u_z = np.array([-2 * C1 + 2 * C2, -2 * C1 + 2 * C3, -2 * C1 + 2 * C4])
u_d = np.array([2 * c**2 * t1 - 2 * c**2 * t2, 2 * c**2 * t1 - 2 * c**2 * t3, 2 * c**2 * t1 - 2 * c**2 * t4])
w = np.array([
    A1**2 - A2**2 + B1**2 - B2**2 + C1**2 - C2**2 - c**2 * t1**2 + c**2 * t2**2,
    A1**2 - A3**2 + B1**2 - B3**2 + C1**2 - C3**2 - c**2 * t1**2 + c**2 * t3**2,
    A1**2 - A4**2 + B1**2 - B4**2 + C1**2 - C4**2 - c**2 * t1**2 + c**2 * t4**2
])


print("u_x =", u_x)
print("u_y =", u_y)
print("u_z =", u_z)
print("u_d =", u_d)
print("w =", w)

matrix = np.vstack((u_y, u_z, x * u_x + y * u_y + z * u_z + d * u_d + w))
print(matrix)


determinant = sp.det(sp.Matrix(matrix))
print(f"determinant:{determinant}")

solution_x = sp.solve(determinant, x)
solution_y = sp.solve(sp.det(sp.Matrix(np.vstack((u_x, u_z, y * u_y + z * u_z + d * u_d + w)))), y)
solution_z = sp.solve(sp.det(sp.Matrix(np.vstack((u_x, u_y, z * u_z + d * u_d + w)))), z)


print("Solution for x in terms of d:")
print(solution_x)

print("Solution for y in terms of d:")
print(solution_y)

print("\nSolution for z in terms of d:")
print(solution_z)


values = {
    A1: 15600, B1: 7540, C1: 20140,
    A2: 18760, B2: 2750, C2: 18610,
    A3: 17610, B3: 14630, C3: 13480,
    A4: 19170, B4: 610, C4: 18390,
    t1: 0.07074, t2: 0.0722, t3: 0.0769, t4: 0.07242,
    c: 299792.458,
}

result_x = solution_x[0].evalf(subs=values)
result_y = solution_y[0].evalf(subs=values)
result_z = solution_z[0].evalf(subs=values)

print("Result for x in terms of d:")
print(result_x)

print("\nResult for y in terms of d:")
print(result_y)

print("\nResult for z in terms of d:")
print(result_z)

x_expr = 10.7491778824478 * d - 41.738295370189
y_expr = -623.677195294295 * d - 18.7859377037094
z_expr = -83788.8071424887 * d + 6101.80417737353

eq1_substituted_values_d = eq1.subs({x: x_expr, y: y_expr, z: z_expr, A1: 15600, B1: 7540, C1: 20140, t1: 0.07074, c: 299792.458})

eq1_simplified_values_d = sp.simplify(eq1_substituted_values_d)

solutions_for_d_values = sp.solve(eq1_simplified_values_d, d)

print("Solutions for d with substituted values:", solutions_for_d_values)



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# question 4

# set up a test of the conditioning of the GPS problem.

# Define satellite positions (A_i, B_i, C_i) from spherical coordinates (rou, phi_i, theta_i) as
# A_i = rou * cos(phi_i) * cos(theta_i)
# B_i = rou * cos(phi_i) * sin(theta_i)
# C_i = rou * sin(phi_i)

# rou = 26570 is fixed, 0 <= phi_i <= pi/2, 0 <= theta_i <= 2pi are chosen arbitrarily for i = 1,...,4
# phi coordinate is restricted so that the four satellites are in the upper hemisphere

# set x=0, y=0, z=6370, d=0.0001
# calculate the corresponding ranges R_i = sqrt((A_i)^2 + (B_i)^2 + (C_i-6370)^2) and travel time t_i = d + R_i/c



rou = 26570
d = 0.0001
c = 299792.458
num_satellites = 4

t_i_values = []
A_values = []
B_values = []
C_values = []
R_values = []

phi_values = [0.2,0.5,0.9,1.2]
theta_values = [0.1,0.9,1.8,2.6]

for i in range(num_satellites):
    phi_i = phi_values[i]
    theta_i = theta_values[i]

    A_i = rou * math.cos(phi_i) * math.cos(theta_i)
    B_i = rou * math.cos(phi_i) * math.sin(theta_i)
    C_i = rou * math.sin(phi_i)

    R_i = math.sqrt(A_i**2 + B_i**2 + (C_i - 6370)**2)
    t_i = d + R_i / c
    t_i_values.append(t_i)
    A_values.append(A_i)
    B_values.append(B_i)
    C_values.append(C_i)
    R_values.append(R_i)

print("phi_i values:", phi_values)
print("theta_i values:", theta_values)
print("t_i values:", t_i_values)
print("A_i values:", A_values)
print("B_i values:", B_values)
print("C_i values:", C_values)
print("R_i values:", R_values)



# define an error magnification factor specially tailored to the situation.
# atomic clockes aboard the satellites are correct up to about 10 nanoseconds (10^-8 second).

# let the backward error(input error) be the input change in meters.
# At the speed of light, delta-t_i = 10^-8 second corresponds to 10^-8c ~= 3 meters
# let the forward error(output error) be the change in position inifinity-norm(delta-x, delta-y, delta-z), caused by such a change t_i, in meters.
# Then we can define the dimensionless error maginfication factor = (infinity-norm(delta-x, delta-y, delta-z)) / (c * infinity-norm(delta_t_1,...,delta-t_m))
# the condition number of the problem to be the maximum error magification factor for ll small delta-t_i(say 10^-8 or less)
# change each t_i defined in the forgoing by delta-t_i = +10^-8 or -10^8, not all the same
# denote the new solution of the equations by (x_bar, y_bar, z_bar, d_bar)
# and compute the difference in position  infinity-norm(delta-x, delta-y, delta-z) and the error magnification factor.

deltat_i = 10**-8

matrix_of_variations = [
    [t_i_values[0] + deltat_i, t_i_values[1] - deltat_i, t_i_values[2] - deltat_i, t_i_values[3] - deltat_i],
    [t_i_values[0] - deltat_i, t_i_values[1] + deltat_i, t_i_values[2] - deltat_i, t_i_values[3] - deltat_i],
    [t_i_values[0] - deltat_i, t_i_values[1] - deltat_i, t_i_values[2] + deltat_i, t_i_values[3] - deltat_i],
    [t_i_values[0] - deltat_i, t_i_values[1] - deltat_i, t_i_values[2] - deltat_i, t_i_values[3] + deltat_i],
    [t_i_values[0] + deltat_i, t_i_values[1] + deltat_i, t_i_values[2] - deltat_i, t_i_values[3] - deltat_i],
    [t_i_values[0] + deltat_i, t_i_values[1] - deltat_i, t_i_values[2] + deltat_i, t_i_values[3] - deltat_i],
    [t_i_values[0] + deltat_i, t_i_values[1] - deltat_i, t_i_values[2] - deltat_i, t_i_values[3] + deltat_i],
    [t_i_values[0] - deltat_i, t_i_values[1] + deltat_i, t_i_values[2] + deltat_i, t_i_values[3] - deltat_i],
    [t_i_values[0] - deltat_i, t_i_values[1] - deltat_i, t_i_values[2] - deltat_i, t_i_values[3] + deltat_i],
    [t_i_values[0] - deltat_i, t_i_values[1] + deltat_i, t_i_values[2] + deltat_i, t_i_values[3] + deltat_i],
    [t_i_values[0] + deltat_i, t_i_values[1] + deltat_i, t_i_values[2] + deltat_i, t_i_values[3] - deltat_i],
    [t_i_values[0] + deltat_i, t_i_values[1] + deltat_i, t_i_values[2] - deltat_i, t_i_values[3] + deltat_i],
    [t_i_values[0] + deltat_i, t_i_values[1] - deltat_i, t_i_values[2] + deltat_i, t_i_values[3] + deltat_i],
    [t_i_values[0] - deltat_i, t_i_values[1] + deltat_i, t_i_values[2] + deltat_i, t_i_values[3] + deltat_i],
    [t_i_values[0] + deltat_i, t_i_values[1] + deltat_i, t_i_values[2] + deltat_i, t_i_values[3] + deltat_i],
    [t_i_values[0] - deltat_i, t_i_values[1] - deltat_i, t_i_values[2] - deltat_i, t_i_values[3] - deltat_i]
]


def numerical_eq1(x, y, z, d, t1):
    c = 299792.458
    return (x - 25910.275593752252)**2 + (y - 2599.6990053427844)**2 + (z - 5278.644119224777)**2 - c**2 * (t1 - d)**2

def numerical_eq2(x, y, z, d, t2):
    c = 299792.458
    return (x - 14494.308798758027)**2 + (y - 18265.12234046712)**2 + (z - 12738.336560713673)**2 - c**2 * (t2 - d)**2

def numerical_eq3(x, y, z, d, t3):
    c = 299792.458
    return (x - 3752.5099782208804)**2 + (y - 16084.239703307543)**2 + (z - 20812.995988802235)**2 - c**2 * (t3 - d)**2

def numerical_eq4(x, y, z, d, t4):
    c = 299792.458
    return (x - 8249.992559353326)**2 + (y - 4963.167581722671)**2 + (z - 24764.278514149202)**2 - c**2 * (t4 - d)**2


def solve_system(t_values):

    def system_equations(vars):
        x, y, z, d = vars
        return [
            numerical_eq1(x, y, z, d, t_values[0]),
            numerical_eq2(x, y, z, d, t_values[1]),
            numerical_eq3(x, y, z, d, t_values[2]),
            numerical_eq4(x, y, z, d, t_values[3])
        ]


    initial_guess = [0, 0, 6370, 0]

    solution = fsolve(system_equations, initial_guess)

    return solution

for i, row in enumerate(matrix_of_variations, 1):

    solution = solve_system(row)
    print(f"Solution {i}: {solution}")


original_solution = np.array([-4.17727096e+01, -1.67891941e+01, 6.37005956e+03, -3.20156583e-03])

solutions_with_variations = [
    [1.18289150e-02, 5.36396210e-03, 6.37002340e+03, 1.00047742e-04],
    [-3.05267970e-02, -6.65406222e-03, 6.36995522e+03, 9.98928120e-05],
    [3.52566322e-02, -3.66605031e-03, 6.37005342e+03, 1.00098231e-04],
    [-1.65588588e-02, 4.95614654e-03, 6.36996796e+03, 9.99412138e-05],
    [-1.86978469e-02, -1.29008902e-03, 6.36997861e+03, 9.99505545e-05],
    [4.70855046e-02, 1.69790763e-03, 6.37007682e+03, 1.00155973e-04],
    [-4.72992335e-03, 1.03201078e-02, 6.36999136e+03, 9.99989561e-05],
    [4.72992311e-03, -1.03201076e-02, 6.37000864e+03, 1.00001044e-04],
    [-1.65588588e-02, 4.95614654e-03, 6.36996796e+03, 9.99412138e-05],
    [-1.18289280e-02, -5.36396815e-03, 6.36997660e+03, 9.99522577e-05],
    [1.65588306e-02, -4.95613854e-03, 6.37003204e+03, 1.00058786e-04],
    [-3.52567270e-02, 3.66605904e-03, 6.36994657e+03, 9.99017681e-05],
    [3.05267158e-02, 6.65404376e-03, 6.37004478e+03, 1.00107187e-04],
    [-1.18289280e-02, -5.36396815e-03, 6.36997660e+03, 9.99522577e-05],
    [2.7414399e-11, -3.0978283e-12, 6.3700000e+03, 1.0001000e-04],
    [6.84823649e-12, -6.26371677e-12, 6.37000000e+03, 9.99900000e-05]
]


solutions = np.array([solution[:3] for solution in solutions_with_variations])

delta_xyz = np.abs(solutions - original_solution[:3])

infinity_norms = np.max(delta_xyz, axis=1)

for i, norm in enumerate(infinity_norms, 1):
    print(f"Infinity Norm for Row {i}: {norm}")

print("the max of position error is 41.8197951046")
print("the condition number is 13949.58212")



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# question 5

# Now repeat Step 4 with a more tightly grouped set of satellites.
# Choose all phi_i within 5 percent of one another and all theta_i within 5 percent of one another
# Solve with and without the same input error as in Step 4.
# Find the maximum position error and error magnification factor.
# Compare the conditioning of the GPS problem when the satellites are tightly or loosely bunched.

base_phi = 0.2
base_theta = 0.1

variation_range_phi = 0.05 * base_phi
variation_range_theta = 0.05 * base_theta


phi_values_new = np.linspace(base_phi - variation_range_phi, base_phi + variation_range_phi, num=num_satellites)

theta_values_new = np.linspace(base_theta - variation_range_theta, base_theta + variation_range_theta, num=num_satellites)

print(f"new phi:{phi_values_new}")
print(f"new theta:{theta_values_new}")

t_is_new = []
A_new = []
B_new = []
C_new = []
R_new = []

for i in range(num_satellites):
    phi_i_new = phi_values_new[i]
    theta_i_new = theta_values_new[i]

    A_i_new = rou * math.cos(phi_i_new) * math.cos(theta_i_new)
    B_i_new = rou * math.cos(phi_i_new) * math.sin(theta_i_new)
    C_i_new = rou * math.sin(phi_i_new)

    R_i_new = math.sqrt(A_i_new**2 + B_i_new**2 + (C_i_new - 6370)**2)
    t_i_new = 0.0001 + R_i_new / c
    t_is_new.append(t_i_new)
    A_new.append(A_i_new)
    B_new.append(B_i_new)
    C_new.append(C_i_new)
    R_new.append(R_i_new)


print("new t_i :", t_is_new)
print("new A_i :", A_new)
print("new B_i :", B_new)
print("new C_i :", C_new)
print("new R_i :", R_new)

def numerical_eq1_new(x, y, z, d, t1):
    c = 299792.458
    return (x - 25974.20156580701)**2 + (y - 2474.9992551478877)**2 + (z - 5017.9808395256205)**2 - c**2 * (t1 - d)**2

def numerical_eq2_new(x, y, z, d, t2):
    c = 299792.458
    return (x - 25931.938914458908)**2 + (y - 2558.2248511642224)**2 + (z - 5191.813724283392)**2 - c**2 * (t2 - d)**2

def numerical_eq3_new(x, y, z, d, t3):
    c = 299792.458
    return (x - 25888.25826416606)**2 + (y - 2641.078694206724)**2 + (z - 5365.415862619145)**2 - c**2 * (t3 - d)**2

def numerical_eq4_new(x, y, z, d, t4):
    c = 299792.458
    return (x - 25843.163589986983)**2 + (y - 2723.548582367)**2 + (z - 5538.779538910866)**2 - c**2 * (t4 - d)**2

def solve_system_new(t_values_new):

    def system_equations_new(vars):
        x, y, z, d = vars
        return [
            numerical_eq1_new(x, y, z, d, t_values_new[0]),
            numerical_eq2_new(x, y, z, d, t_values_new[1]),
            numerical_eq3_new(x, y, z, d, t_values_new[2]),
            numerical_eq4_new(x, y, z, d, t_values_new[3])
        ]


    initial_guess = [0, 0, 6370, 0]

    solution = fsolve(system_equations_new, initial_guess)

    return solution

solution = solve_system(t_is_new)
print(f"Solution without variation: {solution}")

matrix_of_variations_new = [
    [t_is_new[0] + deltat_i, t_is_new[1] - deltat_i, t_is_new[2] - deltat_i, t_is_new[3] - deltat_i],
    [t_is_new[0] - deltat_i, t_is_new[1] + deltat_i, t_is_new[2] - deltat_i, t_is_new[3] - deltat_i],
    [t_is_new[0] - deltat_i, t_is_new[1] - deltat_i, t_is_new[2] + deltat_i, t_is_new[3] - deltat_i],
    [t_is_new[0] - deltat_i, t_is_new[1] - deltat_i, t_is_new[2] - deltat_i, t_is_new[3] + deltat_i],
    [t_is_new[0] + deltat_i, t_is_new[1] + deltat_i, t_is_new[2] - deltat_i, t_is_new[3] - deltat_i],
    [t_is_new[0] + deltat_i, t_is_new[1] - deltat_i, t_is_new[2] + deltat_i, t_is_new[3] - deltat_i],
    [t_is_new[0] + deltat_i, t_is_new[1] - deltat_i, t_is_new[2] - deltat_i, t_is_new[3] + deltat_i],
    [t_is_new[0] - deltat_i, t_is_new[1] + deltat_i, t_is_new[2] + deltat_i, t_is_new[3] - deltat_i],
    [t_is_new[0] - deltat_i, t_is_new[1] - deltat_i, t_is_new[2] - deltat_i, t_is_new[3] + deltat_i],
    [t_is_new[0] - deltat_i, t_is_new[1] + deltat_i, t_is_new[2] + deltat_i, t_is_new[3] + deltat_i],
    [t_is_new[0] + deltat_i, t_is_new[1] + deltat_i, t_is_new[2] + deltat_i, t_is_new[3] - deltat_i],
    [t_is_new[0] + deltat_i, t_is_new[1] + deltat_i, t_is_new[2] - deltat_i, t_is_new[3] + deltat_i],
    [t_is_new[0] + deltat_i, t_is_new[1] - deltat_i, t_is_new[2] + deltat_i, t_is_new[3] + deltat_i],
    [t_is_new[0] - deltat_i, t_is_new[1] + deltat_i, t_is_new[2] + deltat_i, t_is_new[3] + deltat_i],
    [t_is_new[0] + deltat_i, t_is_new[1] + deltat_i, t_is_new[2] + deltat_i, t_is_new[3] + deltat_i],
    [t_is_new[0] - deltat_i, t_is_new[1] - deltat_i, t_is_new[2] - deltat_i, t_is_new[3] - deltat_i]
]

def solve_system_new_vari(t_values_new_vari):

    def system_equations(vars):
        x, y, z, d = vars
        return [
            numerical_eq1_new(x, y, z, d, t_values_new_vari[0]),
            numerical_eq2_new(x, y, z, d, t_values_new_vari[1]),
            numerical_eq3_new(x, y, z, d, t_values_new_vari[2]),
            numerical_eq4_new(x, y, z, d, t_values_new_vari[3])
        ]


    initial_guess = [0, 0, 6370, 0]

    solution = fsolve(system_equations, initial_guess)

    return solution

for i, row in enumerate(matrix_of_variations_new, 1):

    solution = solve_system_new_vari(row)
    print(f"Solution {i}: {solution}")


original_solution_new = np.array([ 6.95808931e+01, 1.07793944e+01, 2.34154784e+02, -9.96066821e-04])

solutions_with_variations_new = [
    [4.05977180e+01, 2.60817203e+00, 6.36930644e+03, 2.35579557e-04],
    [-8.11623005e+00, -1.56589638e+01, 6.37799337e+03, 6.67382234e-05],
    [-8.45043596e+01, -8.87752315e+01, 6.41420914e+03, -2.16437990e-04],
    [6.53507900e+01, 3.23652456e+01, 6.35393774e+03, 3.29652964e-04],
    [2.70045897e+01, 8.29942225e+00, 6.36639387e+03, 1.92808456e-04],
    [-5.16575908e+01, -3.07057417e+01, 6.38527137e+03, -8.36946001e-05],
    [1.20453322e+02, -5.36755247e+01, 6.39828187e+03, 4.77264263e-04],
    [-1.21633073e+02, 5.47676355e+01, 6.34120619e+03, -2.81441773e-04],
    [6.53507900e+01, 3.23652456e+01, 6.35393774e+03, 3.29652964e-04],
    [-3.94860565e+01, -9.06125331e+00, 6.37399071e+03, -3.45028976e-05],
    [-5.43542331e+01, -8.45820631e+01, 6.41269102e+03, -1.14832085e-04],
    [7.91497229e+01, 9.75070304e+01, 6.32138872e+03, 4.01052572e-04],
    [3.72027775e+00, 3.64798372e+01, 6.35126899e+03, 1.26989848e-04],
    [-3.94860565e+01, -9.06125331e+00, 6.37399071e+03, -3.45028976e-05],
    [1.32376724e-05, -7.19067342e-05, 6.37000004e+03, 1.00010015e-04],
    [2.63215245e-05, -1.43052099e-04, 6.37000007e+03, 9.99900295e-05]
]

solutions = np.array([solution[:3] for solution in solutions_with_variations_new])

delta_xyz_new = np.abs(solutions - original_solution_new[:3])

infinity_norms_new = np.max(delta_xyz_new, axis=1)

for i, norm in enumerate(infinity_norms_new, 1):
    print(f"new Infinity Norm for Row {i}: {norm}")


print("the max of position error is 6180.054356.")
print("the condition number is 2061444.24")
