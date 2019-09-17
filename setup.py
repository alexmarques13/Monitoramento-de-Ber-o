import time
import datetime
import os 

from temperatura.py import temperatura
from Temp_Bebe.py import temp_bebe
from timelapse.py import timelapse
from peso.py import peso



bb_berco=True

tentativas = 0
conexao = False

while tentativa < 5:
    try:
        conexao = (os.system('nc -z 8.8.8.8 53')==0)
        break

    except:
        tentativas +=1
        

if conexao == True:

    #Chama Rotina que Verifica o bb no berco
    
    while bb_berco = True:
        #inicia Stream

        timelapse()
        peso()
        temperatura()
        temp_bebe()
        

else
    #Seria Chamar a rotina de conexao
    print "Sem Conexao"
