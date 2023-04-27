import matplotlib.pyplot as plt
import numpy as np
import time
from prettytable import PrettyTable


def calculate_k_coefficient(f, k, n):
    a_k = (1 / n) * sum(f[i] * np.cos((2 * np.pi * k * i) / n) for i in range(n))
    b_k = - (1 / n) * sum(f[i] * np.sin((2 * np.pi * k * i) / n) for i in range(n))
    sum_amount = 2 * n
    multiplication_amount = 2 * (n + 1) + 6 * n
    return a_k, b_k, sum_amount, multiplication_amount


def calculate_all_coefficient(f, n):
    array_a = []
    array_b = []
    array_c = []
    sum_total_amount = 0
    multiplication_total_amount = 0
    start = time.time()
    for k in range(n):
        a_k, b_k, sum_amount, multiplication_amount = calculate_k_coefficient(f, k, n)
        array_a.append(a_k)
        array_b.append(b_k)
        array_c.append(a_k + 1j * b_k)
        sum_total_amount += sum_amount
        multiplication_total_amount += multiplication_amount
    end = time.time()
    return array_a, array_b, array_c, end - start, sum_total_amount, multiplication_total_amount


def print_coefficients(array_a, array_b, total_time, sum_total_amount, multiplication_total_amount, n):
    th = ['k', 'a_k', 'b_k', 'с_k']
    td = []

    for k in range(0, n):
        td.append(k)
        td.append(array_a[k])
        td.append(array_b[k])
        td.append(f"{array_a[k]} {'-' if array_b[k] < 0 else '+'} {abs(array_b[k])}j")

    columns = len(th)
    table = PrettyTable(th)

    while td:
        table.add_row(td[:columns])
        td = td[columns:]
    table.align = "l"
    print(table)
    print(f"Загальний час обчислення коефіцієнтів {total_time}")
    print(f"Загальна кількість операцій додавання {sum_total_amount}")
    print(f"Загальна кількість операцій множення {multiplication_total_amount}")


def main_func():
    n = 23
    f = np.random.uniform(-1, 1, n)
    array_a, array_b, array_c, time_array, sum_total_amount, multiplication_total_amount = \
        calculate_all_coefficient(f, n)
    print_coefficients(array_a, array_b, time_array, sum_total_amount, multiplication_total_amount, n)

    amplitude_spectrum = []
    phase_spectrum = []
    for k in range(0, n):
        amplitude_spectrum.append(np.sqrt(array_a[k]**2 + array_b[k]**2))
        phase_spectrum.append(np.angle(array_c[k]))

    # побудова графіку спектру амплітуд
    fig2, ax2 = plt.subplots(figsize=(10, 10))
    ax2.set_title('Графік спектр амплітуд', fontsize=16)
    plt.grid(True)
    for i in range(0, n):
        plt.plot(i, amplitude_spectrum[i], 'ro-')
        plt.plot([i, i], [0, amplitude_spectrum[i]], 'r-')
    plt.xlabel('k')
    plt.ylabel('|C_k|')
    plt.show()

    # побудова графіку спектру фаз
    fig2, ax2 = plt.subplots(figsize=(10, 10))
    ax2.set_title('Графік спектр фаз', fontsize=16)
    plt.grid(True)
    for i in range(0, n-1):
        plt.plot(i, phase_spectrum[i], 'ro-')
        plt.plot([i, i], [0, phase_spectrum[i]], 'r-')
    plt.xlabel('k')
    plt.ylabel('arg(C_k)')
    plt.show()
    return 0


main_func()
