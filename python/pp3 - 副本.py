from pulp import *
#import numpy as np

prob = LpProblem("test1", LpMinimize)


#LpVariablen(name(变量名),lowBound(下限),upBound(上限),cat(变量类型))
#使用None来表示无穷大（为lowBound的时候表示负无穷大，为upBound的时候为正无穷大）, 例如z <= 0应表示为LpVariable("z", None, 0)
#变量的类型默认值为LpContinuous, 整数LpInteger, 0-1变量为LpBinary.

# 自变量取值：
x1 = LpVariable("x1",0,None,cat='Integer')
x2 = LpVariable("x2",0,None,cat='Integer')
x3 = LpVariable("x3",0,None,cat='Integer')
x4 = LpVariable("x4",0,None,cat='Integer')
x5 = LpVariable("x5",0,None,cat='Integer')
x6 = LpVariable("x6",0,None,cat='Integer')



# 目标：
prob += x1+x2+x3+x4+x5+x6, "obj"

# 约束条件：     约束条件名：

prob += 2*x1+x2 >= 15,'1'
prob += x2+3*x3+2*x4+x5 >= 20,'2'
prob += x2+x4+3*x5+4*x6 >= 50,'3'


#求解问题
prob.solve()
# 打印出已经求解问题的状态
print("Status:", LpStatus[prob.status])
# 打印出最优解
for v in prob.variables():
    print(v.name, "=", v.varValue,end='  ')
#换行
print()
# 打印最优目标函数值
print("objective=", value(prob.objective))
