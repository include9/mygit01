from pulp import *
import numpy as np

prob = LpProblem("test1", LpMinimize)


#LpVariablen(name(变量名),lowBound(下限),upBound(上限),cat(变量类型))
#使用None来表示无穷大（为lowBound的时候表示负无穷大，为upBound的时候为正无穷大）, 例如z <= 0应表示为LpVariable("z", None, 0)
#变量的类型默认值为LpContinuous, 整数LpInteger, 0-1变量为LpBinary.

# 自变量取值：
x = LpVariable("x", 0, None)

y = LpVariable("y", 0, None)

z = LpVariable("z", 0, None)

# 目标：
prob += 5*x + 5*y + 4*z, "obj"

# 约束条件：     约束条件名：

prob += 4*x + 4*y + -8*z >= 12, "c1"
prob += 2*x + -2*y + -6*z >= 7,  "c2"
#prob += 3*x + 1*y + 1*z <= 10,  "c3"



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


            
            



'''
a=np.array([[1,1,-1,1,0,0,10],
           [-1,2,1,0,1,0,12],
           [1,3,2,0,0,1,20]])
b=np.array([[0,1,1],
           [1,2,-1],
           [0,3,1]])
print(np.linalg.inv(b))

'''
            

'''
print(np.linalg.inv(b).dot(a).astype(np.int64))
'''


'''初等行变换
a=np.array([[1,1,-1,1,0,0,10],
           [-1,2,1,0,1,0,12],
           [1,3,2,0,0,1,20]])
b=np.array([[1,0,0],
           [1,1,0],
           [0,0,1]])
print(b.dot(a).astype(np.int64))
'''

