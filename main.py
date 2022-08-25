from scipy.optimize import linprog
obj = ['-25', '-27', '-27', '980']
lhs_ineq = [
    [1, 1, 1, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [-1, -1, -1, 0]
]
rhs_ineq = [
    20,
    10,
    20,
    15,
    -5
]
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,)
print(opt)
