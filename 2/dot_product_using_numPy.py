import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
first_dot_result=np.dot(a,b)
print(first_dot_result)
#Cheak Commutative Property of dot product
second_dot_result=np.dot(b,a)
if first_dot_result==second_dot_result:
    print("Dot Product is commutative")
else:
    print("Dot product is not commutative")
#Yeeeh It is working
#Lets cheak Distributive property of dot product
c=np.array([11,12,13,14,15])
first_result=np.dot(a,(b+c))
second_result=np.dot(a,b)+np.dot(a,c)
if first_result==second_result:
    print("Dot Product is distributive")
else:
    print("dot Product is not distributive")