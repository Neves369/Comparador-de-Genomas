import matplotlib.pyplot as plt

def generateChart(filename1, filename2):
    entrada1 = open("data\\" + filename1).read()
    entrada2 = open("data\\" + filename2).read()

    
    count1 = {}
    count2 = {}

    # Inicializa os dicionários com valor zero
    for i in ['A', 'T', 'C', 'G']:
        for j in ['A', 'T', 'C', 'G']:
            count1[i+j] = 0
            count2[i+j] = 0


    # Remove quebra de linha dos arquivos
    entrada1 = entrada1.replace("\n", "")
    entrada2 = entrada2.replace("\n", "")

    # --- Faz a contagem das sequências de nucleotídeos ---
    for k in range(len(entrada1) - 1):
        count1[entrada1[k]+entrada1[k+1]] += 1

    for k in range(len(entrada2) - 1):
        count2[entrada2[k]+entrada2[k+1]] += 1
    # -----------------------------------------------------

    plt.style.use('seaborn')  # to get seaborn scatter plot

    # eixos
    plt.ylabel('Quantidade')
    plt.xlabel('Pares Nitrogenados')

    plt.scatter(count1.keys(), count1.values(), label=filename1.split('.')[0], s=50, alpha=0.6, c='blue', edgecolor='black', linewidth=1)
    plt.scatter(count2.keys(), count2.values(), label=filename2.split('.')[0], s=50, alpha=0.6, c='red', edgecolor='black', linewidth=1)
    plt.legend()
    plt.savefig('output/densityChart.png', dpi=900)    