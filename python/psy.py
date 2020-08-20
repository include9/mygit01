def build(x, y):
    return lambda: x * x + y * y
f=build(4,5)
print(f)


#导入pyplot模块，并用plt作为它的名字
import matplotlib.pyplot as plt
def count(interest=5,year=10):
    print("--------interest:",interest,"%---------")
    interest=interest/100+1
    list=[]
    for i in range(1,year+1):
        list.append(interest**i)
        print("After",i,"year(s),value:",interest**i)



def fuli(year=10,interest=42):
    print("--------interest:",interest,"---------")
    interest=interest/100+1
    for i in range(1,year+1):
        li=(1-interest**(i+1))/(1-interest)
        print("After",i,"year(s),value(times):",li)
        print("                                                                             :",interest**(i))


if __name__=="__main__": 
    for i in range(22,41):
        fuli(year=28,interest=i)
        
        
        
        
        
