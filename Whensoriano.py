import numpy as np
import matplotlib.pyplot as plt

def a_n(n):
    pi = np.pi
    return (32 * (-1)**n - 16 * n * pi * (-1)**n + 4 * n**2 * pi**2) / (n * pi)**3

def fourier_series(t, N):
    result = 4/3  # a_0
    for n in range(1, N+1):
        result += a_n(n) * np.cos(n * np.pi/2 * t)
    return result

t = np.linspace(-4, 4, 1000)
f_t = t**2  # función original
approx = fourier_series(t, 10)  # usar 10 términos

plt.plot(t, f_t, label="f(t) = t^2")
plt.plot(t, approx, label="Serie de Fourier", linestyle='--')
plt.legend()
plt.grid()
plt.title("Aproximación de la serie de Fourier de t^2")
plt.show()