import matplotlib.pyplot as plt
import numpy as np

# Vetores u e v no R^2
u = np.array([2, 1])
v = np.array([1, 2])

# Soma e subtração dos vetores
u_plus_v = u + v
u_minus_v = u - v

# Origem
origin = np.array([0, 0])

# Plotando os vetores
plt.figure(figsize=(8, 8))
plt.quiver(*origin, *u, angles='xy', scale_units='xy', scale=1, color='blue', label='u')
plt.quiver(*origin, *v, angles='xy', scale_units='xy', scale=1, color='green', label='v')
plt.quiver(*origin, *u_plus_v, angles='xy', scale_units='xy', scale=1, color='red', label='u + v')
plt.quiver(*origin, *u_minus_v, angles='xy', scale_units='xy', scale=1, color='orange', label='u - v')

# Ajustes do gráfico
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Vetores u, v, u + v e u - v em R²")
plt.show()
