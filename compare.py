import os
from modules import density, densityChart, animationLoading
import inquirer

def main():

  # os.system('cls')

  print("""
     ____________________________________________________________________
    |--------------------------------------------------------------------|
    |      ██╗    ███████████╗     ██████╗██████╗███╗   ██████████╗      |
    |      ██║    ████╔════██║    ██╔════██╔═══██████╗ ██████╔════╝      |
    |      ██║ █╗ ███████╗ ██║    ██║    ██║   ████╔████╔███████╗        |
    |      ██║███╗████╔══╝ ██║    ██║    ██║   ████║╚██╔╝████╔══╝        |
    |      ╚███╔███╔██████████████╚██████╚██████╔██║ ╚═╝ █████████╗      |
    |       ╚══╝╚══╝╚══════╚══════╝╚═════╝╚═════╝╚═╝     ╚═╚══════╝      |
    |                                                                    |
    |-------------------------COMPARADOR DE GENOMAS----------------------|
    |--Informe os arquivos a serem comparados                            |
    |--depois selecione as opções de saída                               |
    |                                                                    |
    |--------------------------------------------------------------------|
    |____________________________________________________________________| 
  """) 



  # listar arquivos da pasta data
  caminhos = [os.path.join("data", nome) for nome in os.listdir("data")]
  arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
  fasta = [arq[5:] for arq in arquivos if arq.lower().endswith(".fasta")]


  questions = [
    inquirer.List(
      'filename1',
      message="Selecione o primeiro arquivo: ",
      choices=fasta,
    ),
    inquirer.List(
     'filename2',
      message="Selecione o segundo arquivo: ",
      choices=fasta,
    ),
    inquirer.Confirm(
      'gerarHtml',
      message="Deseja gerar o arquivo de comparação visual?" ,
      default=True),
    inquirer.Confirm(
      'gerarGrafico',
      message="Deseja gerar o gráfico de dispersão?" ,
      default=True),
    
  ]

  answers = inquirer.prompt(questions)
  filename1 =  answers["filename1"]
  filename2 =  answers["filename2"]

  
  if (os.path.exists('output') == False):
    try:
      os.mkdir('output')
    except:
      print("Não foi possível criar diretório") 

  if(answers['gerarHtml']):
    density.generateDensityView(filename1=filename1, filename2=filename2)
  if(answers['gerarGrafico']):  
    densityChart.generateChart(filename1=filename1, filename2=filename2)

  animationLoading.load_animation()
  os.system('cls')


  print("""
  -------------------------------------------------------------------

   ██████╗██████╗███╗   █████████╗██╗    ██████████████████████╗
  ██╔════██╔═══██████╗ ██████╔══████║    ██╔════╚══██╔══██╔════╝
  ██║    ██║   ████╔████╔████████╔██║    █████╗    ██║  █████╗  
  ██║    ██║   ████║╚██╔╝████╔═══╝██║    ██╔══╝    ██║  ██╔══╝  
  ╚██████╚██████╔██║ ╚═╝ ████║    ██████████████╗  ██║  ███████╗
  ╚═════╝╚═════╝╚═╝     ╚═╚═╝    ╚══════╚══════╝  ╚═╝  ╚══════╝

  -------------GERADOS ARQUIVOS DE VISUALIZAÇÃO----------------------
                  --confira a pasta output--
  """) 

  confirm = {
    inquirer.Confirm(
      'confirmed',
      message="Deseja sair?" ,
      default=True),
  }
  confirmation = inquirer.prompt(confirm)

  if(confirmation["confirmed"]):
    quit()


if __name__ == '__main__':
  while True:
    main()