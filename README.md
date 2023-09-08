# Comparador-de-Genomas
Algoritmo em python que recebe duas cadeias de bases nitrogenadas, faz a montagem dos nucleotideos e gera uma comparação visual entre elas.

## Segunda versão
Esta versão recebe dois arquivos em formato .fasta contendo as cadeias a serem comparadas e gera um arquivo em html contendo a representação visual das duas cadeias bem como a ocorrência dos nucleotideos presentes nelas.
Também gera um gráfico de dispersão dessas duas cadeias.

Para que o mesmo funcione é preciso que os arquivos .fasta estejam dentro da pasta data

### modo de uso
>Coloque os arquivos .fasta na pasta data
>xecute o arquivo compare.exe ou abra o prompt de comando no diretório raiz do projeto
>execute o comando python compare.py
>selecione os arquivos e as opções de saídas desejadas 

"Caso não exista o programa vai criar uma pasta chamada output onde estarão o arquivo de saída" 

## Teoria
>DNA é uma molécula presente em todos os seres vivos, que é responsável por armazenar as características hereditárias. Ela é composta por sequências de nucleotídeos, que podem de quatro tipos: adenina, timina, citosina ou guanina.
>
![image](https://github.com/Neves369/Comparador-de-Genomas/assets/63128431/cbebb21e-00ca-46bd-9a62-47f9fa43c687)
>Estrutura do DNA. Fonte: https://se.wikipedia.org/wiki/Fiila:Dna-base-flipping.svg
>
>"Computacionalmente" falando podemos representá-los através de 4 letras: A, T, C ou G.

## Estudo de caso
Usando as sequências human_18s_rRNA_gene.fasta e escherichia_coli_strain_U_5_41_16S_rRNA_partial.fasta,
presentes na pasta data, podemos avaliar se estruturas com funções parecidas (estamos usando sequências de RNA ribossomal) de organismos diferentes têm diferenças. Para isso vamos avaliar a quantidade de pares de nucleotídeos.

### Resultado

![image](https://github.com/Neves369/Comparador-de-Genomas/assets/63128431/34c93e58-d89b-40f1-a119-9b03444be7ae)
![densityChart](https://github.com/Neves369/Comparador-de-Genomas/assets/63128431/e9f52084-bae1-4b18-8061-231608344d8f)




