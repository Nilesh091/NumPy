import numpy as np
a=np.array([10,20,30,40,50])
b=np.array([60,70,80,90,100])
vector_projection_on_b=(np.dot(a,b)/np.dot(b,b))*b
#projection of a on b
print(vector_projection_on_b)
#projection of b on a
vector_projection_on_a=(np.dot(a,b)/np.dot(a,a))*a
print(vector_projection_on_a)