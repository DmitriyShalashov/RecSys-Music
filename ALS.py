import pandas as pd
import numpy as np
import time


# Сгенерировано из CF.py
items=[2, 3, 9, 11, 13, 14, 15, 17, 18, 19, 22, 24, 27,
        30, 33, 35, 36, 38, 39, 42, 43, 48, 49, 51, 52, 54, 55, 57, 59, 60, 62, 63,
        65, 66, 67, 68, 72, 73, 87, 90, 91, 92, 98, 99]

users_size=11
# Взяли из CF.py
user=[1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1,
 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1,
 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1,
 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1,
 1, 1, 0, 0,]

items_size=len(items)
d=100
start_time=time.time()

def sigma(x):
    return 1/(1+np.exp(-x))


def calc_derivation_cost(X,y,weights,b):
    return sigma(np.dot(X,weights)+b)-y


def calc_grad_batch(X_batch, y_batch,weights,bias):
    batch_size=len(X_batch)
    grad=np.zeros(d+1)
    for j in range(d+1):
        for i in range(batch_size):
            grad[j]+=calc_derivation_cost(X_batch[i], y_batch[i],weights,bias)
            if j!=d:
                grad[j]*=X_batch[i][j]
        grad[j]/=batch_size

    return grad

def gradient_descent(users, items ,r, lr=0.1, batch_size=3, iters=100):
    P=users
    Q=items
    for i in range(iters):
        if i%2==0:
            for j in range(len(Q)):
                weights=Q[j]
                bias=bias_i[j]
                
                batch_index=np.random.choice(users_size,batch_size)
                X=P[batch_index]
                y=np.rot90(r,3)[j][batch_index]

                new_weigths=calc_grad_batch(X,y,weights,bias)
                new_bias=new_weigths[-1]
                weights-=lr*new_weigths[:-1]
                bias-=lr*new_bias

                bias_i[j]=bias
                Q[j]=weights
        else:
            for j in range(len(P)):
                weights=P[j]
                bias=bias_u[j]

                batch_index=np.random.choice(users_size,batch_size)
                X=Q[batch_index]
                y=r[j][batch_index]
                
                new_weigths=calc_grad_batch(X,y,weights,bias)
                new_bias=new_weigths[-1]
                weights-=lr*new_weigths[:-1]
                bias-=lr*new_bias

                bias_u[j]=bias
                P[j]=weights  
    
    res=np.dot(P,Q.T)
    for i in range(users_size):
        for j in range(items_size):
            res[i][j]+=bias_i[j]+bias_u[i]
    return  res



X_users=np.random.random((users_size,d))
X_users[0]=user
X_items=np.random.random((items_size,d))
matrix=np.random.random((users_size,items_size))

user=X_users[0]


for i in range(users_size):
    for j in range(items_size):
        matrix[i][j]=np.around(matrix[i][j])

bias_u=np.random.random(users_size)
bias_i=np.random.random(items_size)

res_matrix=gradient_descent(X_users, X_items,matrix)

arr_mat=[]
arr_res=[]


for i in range(users_size):
    for j in range(items_size):
        res_matrix[i][j]=sigma(res_matrix[i][j])
print({"data":np.around(res_matrix,2)})

res=list(res_matrix[0])

for i in range(users_size):
    for j in range(items_size):
        res_matrix[i][j]=np.around(res_matrix[i][j])



arr_res=res_matrix[0]
arr_mat=matrix[0]

def accuracy():
    cnt=0
    for i in range(users_size):
        for j in range(items_size):
            cnt+=(res_matrix[i][j]==matrix[i][j])
    return cnt/(items_size*users_size)


def DCG(y):
    index=range(len(y))
    arr=[x for x in zip(index,y)]
    arr.sort(key=lambda x:x[1])
    arr=list(reversed(arr))
    return sum([np.around(x[1])/np.log2(x[0]+2) for x in arr])

def IDCG(y):
    y.sort()
    y=list(reversed(y))
    return sum([np.around(y[i])/np.log2(i+2) for i in range(len(y))])

def nDCG(y):
    return DCG(y)/IDCG(y)

# print(matrix)
# print(res_matrix)


print(nDCG(res))
print(time.time()-start_time)

