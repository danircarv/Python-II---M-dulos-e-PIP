import statistics

# 1 - Aplicar a média
print(statistics.mean([3,2,3,8,9]))

# 2 - Aplicar a mediana
print(statistics.median([1, 2, 3, 4, 5, 6, 7]))
print(statistics.median([1, 2, 3, 4, 5, 6, 7, 8]))

# 3 -  Aplicar a moda
print(statistics.mode([2, 3, 4, 5, 6, 2, 2, 5, 6, 8, 5]))

# 4 - Desvio padrão
"""
- Quanto mais próximo de 0 for o desvio padrão, significa que os dados do conjunto estão menos dispersos
"""

print(statistics.stdev([1, 1.1, 1.111, 1.11111, 1.2]))