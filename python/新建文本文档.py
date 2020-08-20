from pulp import *
#import numpy as np

prob = LpProblem("test1", LpMinimize)


#LpVariablen(name(变量名),lowBound(下限),upBound(上限),cat(变量类型))
#使用None来表示无穷大（为lowBound的时候表示负无穷大，为upBound的时候为正无穷大）, 例如z <= 0应表示为LpVariable("z", None, 0)
#变量的类型默认值为LpContinuous, 整数LpInteger, 0-1变量为LpBinary.

# 自变量取值：
x11 = LpVariable("x11",0,1, 'LpBinary')
x12 = LpVariable("x12",0,1, 'LpBinary')
x13 = LpVariable("x13",0,1, 'LpBinary')
x14 = LpVariable("x14",0,1, 'LpBinary')

x21 = LpVariable("x21",0,1, 'LpBinary')
x22 = LpVariable("x22",0,1, 'LpBinary')
x23 = LpVariable("x23",0,1, 'LpBinary')
x24 = LpVariable("x24",0,1, 'LpBinary')

x31 = LpVariable("x31",0,1, 'LpBinary')
x32 = LpVariable("x32",0,1, 'LpBinary')
x33 = LpVariable("x33",0,1, 'LpBinary')
x34 = LpVariable("x34",0,1, 'LpBinary')

x41 = LpVariable("x41",0,1, 'LpBinary')
x42 = LpVariable("x42",0,1, 'LpBinary')
x43 = LpVariable("x43",0,1, 'LpBinary')
x44 = LpVariable("x44",0,1, 'LpBinary')


# 目标：
prob += 14*x11+9*x12+4*x13+15*x14 + 11*x21+7*x22+9*x23+10*x24 + 13*x31+2*x32+10*x33+5*x34 + 17*x41+9*x42+15*x43+13*x44, "obj"

# 约束条件：     约束条件名：

prob += x11+x12+x13+x14 == 1,'1'
prob += x21+x22+x23+x24 == 1,'2'
prob += x31+x32+x33+x34 == 1,'3'
prob += x41+x42+x43+x44 == 1,'4'


prob += x11+x21+x31+x41 == 1,'5'
prob += x12+x22+x32+x42 == 1,'6'
prob += x13+x23+x33+x43 == 1,'7'
prob += x14+x24+x34+x44 == 1,'8'


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
