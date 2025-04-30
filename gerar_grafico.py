# gerar_grafico.py
import matplotlib.pyplot as plt

print("Gerando gráfico...")

# Dados fictícios
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]

plt.figure(figsize=(8, 4))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Valores')
plt.title("Exemplo de Gráfico")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

# Salva o gráfico como imagem PNG
plt.savefig("grafico.png")
print("Gráfico salvo como grafico.png")