import pandas as pd
import numpy as np
array1 = np.array([[10, 20, 30], [40, 50, 50], [70, 80, 90]])
print(array1)

zero_arr1 = np.zeros(5)
print(zero_arr1)
print('\n**********************************')

zero_arr2= np.zeros((4,4))
print(zero_arr2)

print("\n********************************")
one_arr1= np.ones(4)
print(one_arr1)
print("\n****************************")

one_arr2 = np.ones((3,2), dtype= int)
print(one_arr2)

print("\n**************************")

rand_arr = np.random.rand(5,4)
print(rand_arr)

print("\n**************************")


iden_arr1 = np.eye(4)
print(iden_arr1)

print("\n**************************")


iden_arr2= np.eye(2, dtype= int)
print(iden_arr2)

print("\n**************************")

a = np.arange(12).reshape(3, 4)
print(a)

rows = np.array([False, True, True])
a=a[rows, : ]
print(a)

em= pd.DataFrame({"weight": pd.Series([60, 80, 100], index=["Ram", "Sam", "Max"]), "dob": pd.Series([1990,1970,1991], index=["Ram", "Max", "Sam"], name="year"), "hobby": pd.Series(["Reading", "Singing"], index=["Ram ", "Max"])})
print(em)