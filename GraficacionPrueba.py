import numpy as np
import matplotlib.pyplot as plt

# Parámetros
T = 4
omega = 2 * np.pi / T
pi = np.pi

# Coeficientes c_n (corregido para manejar n negativos)
def c_n(n):
    if n == 0:
        return 4/3
    n_abs = abs(n)
    signo = (-1.0)**n_abs  # usar float para evitar error
    return (16 * signo - 8 * n_abs * pi * signo + 2 * n_abs**2 * pi**2) / (n_abs * pi)**3

# Rango de n
n_vals = np.arange(-10, 11)
c_vals = [c_n(n) for n in n_vals]
amplitudes = [abs(c) for c in c_vals]
fases = [np.angle(c) for c in c_vals]

# Gráfico
plt.figure(figsize=(12, 5))

# Amplitud
plt.subplot(1, 2, 1)
plt.stem(n_vals, amplitudes, use_line_collection=True)
plt.title("Espectro de Amplitud |cₙ|")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid(True)

# Fase
plt.subplot(1, 2, 2)
plt.stem(n_vals, fases, use_line_collection=True)
plt.title("Espectro de Fase arg(cₙ)")
plt.xlabel("n")
plt.ylabel("Fase (radianes)")
plt.grid(True)

plt.tight_layout()
plt.show()
