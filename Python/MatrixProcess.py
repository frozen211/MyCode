# Assumes that the matrix is non-empty
matrix = [[1,2],[3,4]]

# create a zero matrix
zero_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
print(zero_matrix)

# copy the matrix
copied_matrix = [row[:] for row in matrix]
print(copied_matrix)

# transpose the matrix
# Zip returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. 
# * operator shatters the matrix into independent rows like a[0], a[1], a[2]
# together, zip will extract the ith value from each row, and put them into a tuple, then return an iterable object
transposed_matrix = list(map(list,zip(*matrix)))
print(transposed_matrix)