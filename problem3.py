from random import randint
import statistics

results = []

for i in range(1001):
    num1 = randint(1, 6)
    num2 = randint(1, 6)
    sum_of_two = num1 + num2
    results.append(sum_of_two)

print("--- Simulation Results (1000 rolls) ---")
print(f"{statistics.mean(results):.2f}")
print(statistics.median(results))
print(statistics.mode(results))