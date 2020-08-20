#DEFINE
n=4

#重置棋盘与标记
def Restart(n1=n):
    L=[([1] * n1) for i in range(n1)]
    alist=[i+1 for i in range(n)]
    return L,alist
#打印棋盘1
def pr(L=[]):
    for arr1 in L:
        for arr in arr1:
            print('%3s'%arr,end='')
        print()
    print()    
#打印棋盘2
def pr2(L=[]):
    for arr1 in L:
        for arr in arr1:
            if arr==0:
                print('%3s'%arr,end='')
            else:
                print('%3s'%'',end='')
        print()
    print() 
#打印结果3
def pr3(L=[]):
    cnt=0
    for i in range(n):
        for j in range(n):
            if L[i][j]==0:
                cnt+=1
    if cnt!=n:
        return False           
    for i in range(n):
        for j in range(n):
            if L[i][j]==0:
                print(j+1,end='  ')
    print()
    
L,aList=Restart()       
#判断是否可下子
def setable(i,j):
    if L[i-1][j-1]==-1 or L[i-1][j-1]==0:
        return False
    else:
        return True
  
#下子
def aset(i,j):
    if not setable(i,j):
        return
    for ii in range(n):
         L[ii][j-1]=-1
         L[i-1][ii]=-1
         if ii-i+j>=0 and ii-i+j<=n-1:
             L[ii][ii-i+j]=-1
         if j+i-2-ii>=0 and j+i-2-ii<=n-1:    
             L[ii][j+i-2-ii]=-1
    L[i-1][j-1]=0


def k(n):
    if n==0:
        if pr3(L)!=False:
            pr(L)
        return
    for a in aList:
        if setable(n,a):
            aset(n,a)
            aList.remove(a)
            break
    k(n-1)


for i in range(1,n+1):
    aset(n,i)
    k(n-1)
    L,aList=Restart()       
    print()
