"listaUsage"

def concatenar(u,v):
    #Parte fácil
    return u+v
    #Concatena(junta) duas tranças :)

def listmaker(mistura):
    #Temos de emendar a necessidade desta função :(
    mistura_nova=[]
    for Trança in mistura:
        mistura_nova+= [[Trança]]
    return mistura_nova

def juntar(Trança):
    Nova_Trança=["",""]
    for peça in Trança:
        Nova_Trança[0]+= peça[0]
        Nova_Trança[1]+= peça[1]
    return Nova_Trança  
    #Junta as peças de uma trança para se poder calcular a semelhança
def semelhança(u):
    #Fator determinístico do algoritmo
    min_len=len(u[0])
    max_len=len(u[1])  
    igualdade= 0
    if len(u[0])>=len(u[1]):
        min_len=len(u[1])
        max_len=len(u[0])   
    for i in range(min_len):
        if u[0][i]==u[1][i]:
            igualdade+=1
    return igualdade/max_len 
    #Determina a proporção de algarismos/símbolos iguais na parte superior e inferior da Trança
def semjunt(trança):
    valor=semelhança(juntar(trança))
    return valor
    #Junta as funções de juntar e semelhança



