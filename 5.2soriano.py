import numpy as np
import matplotlib.pyplot as plt

omega = np.linspace(-10, 10, 1000)

omega[np.isclose(omega, 1.0)] = np.nan
omega[np.isclose(omega, -1.0)] = np.nan

numerador = 2 * np.abs(np.sin(np.pi * omega))
denominador = np.abs(1 - omega**2)
F_mag = numerador / denominador

plt.figure(figsize=(10, 5))
plt.plot(omega, F_mag, label=r'$|F(\omega)|$', color='blue')
plt.title('Espectro de Amplitud de $f(t)$')
plt.xlabel(r'$\omega$')
plt.ylabel(r'$|F(\omega)|$')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.show()

