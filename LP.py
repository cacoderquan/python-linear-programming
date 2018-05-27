from pulp import *

prob = LpProblem("",LpMinimize)

# It has four parameters, the first is the arbitrary name of what this variable represents, 
# the second is the lower bound on this variable, 
# the third is the upper bound, 
# and the fourth is essentially the type of data (discrete or continuous). The options for the fourth parameter are LpContinuous or LpInteger, with the default as LpContinuous.
x_1=LpVariable("Equities",0, 500, LpInteger)
x_2=LpVariable("Equities",0, 1000, LpInteger)
y=LpVariable("Goverment bond",0, LpInteger)
z=LpVariable("Cash",0)



# The objective function is added to 'prob' first
prob += 0.0005 * x + 0.0007 * y + 0.001 * z, "opportunity cost"

# The margin constraints are entered
prob += 0.6 * x + 0.8 * y + z >= 100000, "Margin constraint"

prob += x_1 <= 500
prob += x_2 <= 1000


# The problem data is written to an .lp file
#prob.writeLP("ACUO.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)
    
    
   

