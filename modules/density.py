

def generateDensityView(filename1, filename2):
    entrada1 = open("data\\" + filename1).read()
    entrada2 = open("data\\" + filename2).read()
    saida = open("output/density.html", "w")


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
    # ------------------------------------------------------


    # Gera uma página em html para exibição dos dados

    saida.write("<div style='display: flex; flex-direction: row; align-items: center; justify-content: space-evenly;'>")


    # primeiro genoma
    # div do primeiro genoma
    saida.write("<div>")
    saida.write("<h2>"+filename1.split('.')[0]+"</h2>")
    i = 1
    for k in count1:
        transparencia = count1[k]/max(count1.values())
        saida.write(
            "<div style='width: 100px; border:1px solid #111; height: 100px; float:left; color:#fff; background-color:rgba(0, 0, 0, "+str(transparencia)+")'>"+ k + " = " + str(count1[k]) + "</div> ")
        if i % 4 == 0:
            saida.write("<div style='clear:both'></div>")
        i += 1
    saida.write("</div>")

    # segundo genoma
    # div do segundo genoma
    saida.write("<div>")
    saida.write("<h2>"+filename2.split('.')[0]+"</h2>")
    i = 1
    for k in count2:
        transparencia = count2[k]/max(count2.values())
        saida.write(
            "<div style='width: 100px; border:1px solid #111; height: 100px; float:left; color:#fff; background-color:rgba(0, 0, 0, "+str(transparencia)+")'>"+ k + " = " + str(count2[k]) + "</div> ")
        if i % 4 == 0:
            saida.write("<div style='clear:both'></div>")
        i += 1
    saida.write("</div>")

    # div da legenda
    saida.write("<div style='display: flex; flex-direction: column;'>")
    saida.write("<div>")
    saida.write("<div style='width: 30px; border:1px solid #111; height: 30px; float:left; color:#000; background-color:rgba(0, 0, 0, 0); border-radius: 15px;'></div>")
    saida.write("<div style='width: 100px; height: 30px; color:#000; margin: 5px'>"+" min value "+"</div></div>")
    saida.write("<div style='margin-top: 15px'>")
    saida.write("<div style='width: 30px; border:1px solid #111; height: 30px; float:left; color:#fff; background-color:rgba(0, 0, 0, 1); border-radius: 15px;'></div>")
    saida.write("<div style='width: 100px; height: 50px; color:#000;  margin: 5px'>"+" max value "+"</div></div>")
    saida.write("</div>")



    saida.write("</div>")

    saida.close()
