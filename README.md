# Comparador-de-Genomas
Algoritmo em python que recebe duas cadeias de bases nitrogenadas, faz a montagem dos nucleotideos e gera uma comparação visual entre elas.

## Primeira versão
Esta versão recebe dois arquivos em formato .fasta contendo as cadeias a serem comparadas e gera um arquivo em html contendo a representação visual das duas cadeias bem como a ocorrência dos nucleotideos presentes nelas.

Para que o mesmo funcione é preciso que os arquivos .fasta estejam no mesmo nível de acesso que o arquivo main.py

## Teoria
>DNA é uma molécula presente em todos os seres vivos, que é responsável por armazenar as características hereditárias. Ela é composta por sequências de nucleotídeos, que podem de quatro tipos: adenina, timina, citosina ou guanina.
>"Computacionalmente" falando podemos representá-los através de 4 letras: A, T, C ou G.

## Estudo de caso
Usando as sequências human_18s_rRNA_gene.fasta e escherichia_coli_strain_U_5_41_16S_rRNA_partial.fasta,
presentes na pasta data, podemos avaliar se estruturas com funções parecidas (estamos usando sequências de RNA ribossomal) de organismos diferentes têm diferenças. Para isso vamos avaliar a quantidade de pares de nucleotídeos.




