

import sys
import os
from modules import density


def main():
  if len(sys.argv) != 3:
    print ('usage: ./compare.py  file1 file2')
    sys.exit(1)

  filename1 =  sys.argv[1]
  filename2 =  sys.argv[2]

  
  if (os.path.exists('output') == False):
    try:
      os.mkdir('output')
    except:
      print("Não foi possível criar diretório") 

  density.generateDensityView(filename1=filename1, filename2=filename2)

  



if __name__ == '__main__':
  main()