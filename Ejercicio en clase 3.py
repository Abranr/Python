import random
import math

def simulate_pi_approximation(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    pi_approximation = (points_inside_circle / num_points) * 4
    return pi_approximation

# Cantidades de puntos a simular
point_counts = [10, 50, 100, 1000]

# Resultados de la simulación
approximations = {count: simulate_pi_approximation(count) for count in point_counts}

for count, approximation in approximations.items():
    print(f"Aproximación de π con {count} puntos: {approximation}")
