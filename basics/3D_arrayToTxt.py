import numpy as np
arr = np.array([[[1, 2],[3, 4]],[[5, 6], [7, 8]]])
file = open('3D_array.txt', 'x')
file.close()

file = open('3D_array.txt', 'w')
for row in arr:
    np.savetxt('3D_array.txt', row)

file.close()
