import numpy as np
a = np.array([['A', 'B', 'C', 'D', 'E'],
           ['F', 'G', 'H', 'I', 'J'],
           ['K', 'L', 'M', 'N', 'O'],
           ['P', 'Q', 'R', 'S', 'T'],
           ['U', 'V', 'W', 'X', 'Y']])

rows = np.array([0,2,1])
cols = np.array([2])

ix = np.broadcast(rows, cols)
print(ix.shape)
print(*ix)

print('changing rows and cols')
rows = np.array([4,3,1])
cols = np.array([2,4,0])

# Expanding the dimension of rows
# Application 1
print(rows[:,np.newaxis])
print(np.expand_dims(rows, axis=0))
print(np.expand_dims(rows, axis=1))

print(a[rows[:,None], cols])
print(a[np.ix_(rows, cols)])

# Changing cols
# Application 2
cols = [[3,4], [0,2], [0,1], [1,2], [3,3]]
rows = np.arange(a.shape[0]) #0,1,2,3,4
rows = rows[:, None]
ix = np.broadcast(rows, cols)
print(*ix)
print(a[rows, cols])
      
