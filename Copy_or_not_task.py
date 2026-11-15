a = [1,2,3,4]
b = a
c = a.copy()
c.append(5)
print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]
print(c)  # Output: [1, 2, 3, 4, 5]
#This code demonstrates the difference between assignment and copying in Python.
# When you use assignment (b = a), both variables point to the same object in memory.
# When you use copying (c = a.copy()), a new object is created with the same values.