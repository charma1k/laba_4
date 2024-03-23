# Вариант 15
# Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество чисел, больших К в четных столбцах больше, чем сумма чисел в нечетных строках, то поменять местами С и Е симметрично, иначе В и С поменять местами несимметрично. 
# При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*A^T – K * F^Т, иначе вычисляется выражение (A^Т +G^(-1)-F^(-1))*K, где G-нижняя треугольная матрица, полученная из А. 
# Выводятся по мере формирования А, F и все матричные операции последовательно.


import numpy as np
import matplotlib.pyplot as plt

def generate_matrix(N):
    return np.random.randint(-10, 11, size=(N, N))

def count_greater_than_K(matrix, K):
    return np.sum(matrix > K)

def plot_matrix(matrix, title):
    plt.imshow(matrix, cmap='viridis')
    plt.title(title)
    plt.colorbar()
    plt.show()

def main():
    K = int(input("Введите значение K: "))
    N = int(input("Введите размер матрицы N: "))

    A = generate_matrix(N)
    print("Матрица A:")
    print(A)

    F = np.copy(A)

    even_columns_count = np.sum(F[:, 1::2] > K)
    odd_rows_sum = np.sum(F[::2, :])

    if even_columns_count > odd_rows_sum:
        F[:, [1, 3]] = F[:, [3, 1]]
    else:
        F[[0, 1], 1] = F[[1, 0], 1]

    print("Матрица F:")
    print(F)

    det_A = np.linalg.det(A)
    diagonal_sum_F = np.trace(F)

    if det_A > diagonal_sum_F:
        G = np.tril(A)
        result = np.dot(A, A.T) - K * F.T
    else:
        G_inv = np.linalg.inv(np.tril(A))
        F_inv = np.linalg.inv(F)
        result = np.dot(np.dot(A.T, G_inv) + G_inv - F_inv, K)

    print("Результат вычислений:")
    print(result)

    plot_matrix(A, "Матрица A")
    plot_matrix(F, "Матрица F")

if __name__ == "__main__":
    main()
