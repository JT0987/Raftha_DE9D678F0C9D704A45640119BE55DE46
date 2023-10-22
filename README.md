# Raftha_DE9D678F0C9D704A45640119BE55DE4
6
f linearSearch(array, n, x):
for i in range(0, n):
if (array[i] == x):
return i return -1

array = [2, 4, 0, 1, 9]x = 1n = len(array)
result = linearSearch(array, n, x)
if (result == -1):
print("Element not found")else: print("Element found at index: ", result)


