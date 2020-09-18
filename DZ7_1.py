from copy import deepcopy


class Matrix:
    def __init__(self, digits):
        self.data = digits

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        result = deepcopy(self.data)
        i = 0
        for other_i in other.data:
            j = 0
            for other_j in other_i:
                result[i][j] += other_j
                j += 1
            i += 1
        return Matrix(result)


numbers = [[1, 2, 3], [4, 5, 6]]
my_mat = Matrix(numbers)
numbers2 = [[1, 1, 1], [2, 2, 2]]
my_mat2 = Matrix(numbers2)
print(my_mat + my_mat2)

