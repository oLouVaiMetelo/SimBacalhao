import random

import SimFinal

from SimFinal import simulador

import random

def calcular_gradiente(mistura_inicial, k, comp, Tfim, Tprog, Tcont, Prob, ADM,tipo_de_evento,h1,h2,h3,h4): #Propósito final de calcular o gradiente resultante da alteração de uma variável em particular

    f1=0 # Variável que guarda uma semelhança 1
    f2=0 # Variável que guarda uma semelhança 2
    if tipo_de_evento == 0: # Ou seja se for a iteração para cálculo do gradiente associado à alteração de k
        h_usar= h1 # O valor de h a utilizar será h1
        novo_k1= k  +   h1 # Soma a k de um valor h1 para criar uma variável a usar em f1
        novo_k2= k  -   h1 # Subtração a k de um valor h1 para criar uma variável a usar em f2
        f1= SimFinal.simulador(mistura_inicial, novo_k1, comp,Tfim,Tprog,Tcont,Prob,ADM)[0] # Cálculo da semelhança 1 com a alteração da variável k por novo_k1
        f2= SimFinal.simulador(mistura_inicial, novo_k2, comp,Tfim,Tprog,Tcont,Prob,ADM)[0] # Cálculo da semelhança 2 com a alteração da variável k por novo_k2

    elif tipo_de_evento == 1: # Ou seja se for a iteração para cálculo do gradiente associado à alteração de comp
        h_usar= h2 # O valor de h a utilizar será h2
        novo_comp1 = comp + h2 # Soma a comp de um valor h1 para criar uma variável a usar em f1
        novo_comp2 = comp - h2 # Subtração a comp de um valor h1 para criar uma variável a usar em f2
        f1 = SimFinal.simulador(mistura_inicial, k, novo_comp1, Tfim, Tprog, Tcont, Prob, ADM)[0] # Cálculo da semelhança 1 com a alteração da variável comp por novo_comp1
        f2 = SimFinal.simulador(mistura_inicial, k, novo_comp2, Tfim, Tprog, Tcont, Prob, ADM)[0] # Cálculo da semelhança 2 com a alteração da variável comp por novo_comp2

    elif tipo_de_evento == 2: # Ou seja se for a iteração para cálculo do gradiente associado à alteração de Tfim
        h_usar= h2 # O valor de h a utilizar será h2
        novo_tfim1 = Tfim + h2 # Soma a Tfim de um valor h1 para criar uma variável a usar em f1
        novo_tfim2 = Tfim - h2 # Subtração a Tfim de um valor h1 para criar uma variável a usar em f2
        f1 = SimFinal.simulador(mistura_inicial, k, comp, novo_tfim1, Tprog, Tcont, Prob, ADM)[0] # Cálculo da semelhança 1 com a alteração da variável Tfim por novo_tfim1
        f2 = SimFinal.simulador(mistura_inicial, k, comp, novo_tfim2, Tprog, Tcont, Prob, ADM)[0] # Cálculo da semelhança 2 com a alteração da variável Tfim por novo_tfim2

    elif tipo_de_evento == 3: # Ou seja se for a iteração para cálculo do gradiente associado à alteração de Tprob
        h_usar= h3 #O valor de h a utilizar será h3
        novo_tprog1 = Tprog + h3 # Soma a Tprog de um valor h1 para criar uma variável a usar em f1
        novo_tprog2 = Tprog - h3 # Subtração a Tprog de um valor h1 para criar uma variável a usar em f2
        f1 = SimFinal.simulador(mistura_inicial, k, comp, Tfim, novo_tprog1, Tcont, Prob, ADM)[0] # Cálculo da semelhança 1 com a alteração da variável Tprog por novo_tprog1
        f2 = SimFinal.simulador(mistura_inicial, k, comp, Tfim, novo_tprog2, Tcont, Prob, ADM)[0] # Cálculo da semelhança 2 com a alteração da variável Tprog por novo_tprog2

    elif tipo_de_evento == 4: #Ou seja se for a iteração para cálculo do gradiente associado à alteração de Tcont
        h_usar= h3#O valor de h a utilizar será h3
        novo_tcont1 = Tcont + h3 # Soma a Tcont de um valor h1 para criar uma variável a usar em f1
        novo_tcont2 = Tcont - h3 # Subtração a Tcont de um valor h1 para criar uma variável a usar em f2
        f1 = SimFinal.simulador(mistura_inicial, k, comp, Tfim, Tprog, novo_tcont1, Prob, ADM)[0] # Cálculo da semelhança 1 com a alteração da variável Tcont por novo_tcont1
        f2 = SimFinal.simulador(mistura_inicial, k, comp, Tfim, Tprog, novo_tcont2, Prob, ADM)[0] # Cálculo da semelhança 2 com a alteração da variável Tcont por novo_Tcont2

    elif tipo_de_evento == 5: #Ou seja se for a iteração para cálculo do gradiente associado à alteração de Prob
        h_usar= h4 # O valor de h a utilizar será h4
        novo_prob1 = Prob + h4 # Soma a Prob de um valor h1 para criar uma variável a usar em f1
        novo_prob2 = Prob - h4 # Subtração a Prob de um valor h1 para criar uma variável a usar em f2
        f1 = SimFinal.simulador(mistura_inicial, k, comp, Tfim, Tprog, Tcont, novo_prob1, ADM)[0] # Cálculo da semelhança 1 com a alteração da variável Prob por novo_prob1
        f2 = SimFinal.simulador(mistura_inicial, k, comp, Tfim, Tprog, Tcont, novo_prob2, ADM)[0] # Cálculo da semelhança 2 com a alteração da variável Prob por novo_prob2

    elif tipo_de_evento == 6: #Ou seja se for a iteração para cálculo do gradiente associado à alteração de ADM
        h_usar= h4 # O valor de h a utilizar será h4
        novo_adm1 = ADM + h4 # Soma a ADM de um valor h1 para criar uma variável a usar em f1
        novo_adm2 = ADM - h4 # Subtração a ADM de um valor h1 para criar uma variável a usar em f2
        f1 = SimFinal.simulador(mistura_inicial, k, comp, Tfim, Tprog, Tcont, Prob, novo_adm1)[0] # Cálculo da semelhança 1 com a alteração da variável ADM por novo_adm1
        f2 = SimFinal.simulador(mistura_inicial, k, comp, Tfim, Tprog, Tcont, Prob, novo_adm2)[0] # Cálculo da semelhança 2 com a alteração da variável ADM por novo_adm2


    return (f1 - f2)/(2*h_usar) # Cálcula do gradiente que resulta da diferença entre f1 e f2 a dividir pelo dobro do h utilizado


def descida_de_gradiente(mistura_inicial,taxa_aprendizado,num_selecoes, num_iteracoes, num_trial,h1,h2,h3,h4):#



    Aproximacao_de_cada_selecao=[] # Lista onde estarão as listas com os parâmetros aproximados e otimizados para uma melhor semelhança e melhor trança
    melhor_semelhança_atingida = 0 # Valor de melhor semelhança atingida por seleção
    melhor_tranca_atingida=[] # Trança com melhor semelhança atingida de uma seleção

    for num in range(num_selecoes): # Ir-se-à iterar um determinado número de vezes para calcular a melhor otimização de um conjunto aleatório de valores dos parâmetros (seleção)


        k= random.randint(0, 500) # Valor aleatório para parâmetro k

        comp = random.uniform(0, 100) # Valor aleatório para parâmetro comp

        Tfim = random.uniform(0, 10000) # Valor aleatório para parâmetro Tim

        Tprog = random.uniform(0, 100) # Valor aleatório para parâmetro Tprog

        Tcont = random.uniform(0, 100) # Valor aleatório para parâmetro Tcont

        Prob = random.uniform(0, 1) # Valor aleatório para parâmetro Prob

        ADM = random.uniform(0, 1) # Valor aleatório para parâmetro ADM

        parametros=[0,1,2,3,4,5,6] #Lista dos parâmetros e o indicador numérico que o determina (serve para ajudar na iteração)

        #valores lançados são [k,comp,Tfim,Tprog,Tcont,Prob,ADM]

        for iteracao in range(num_iteracoes): # Para uma determinada seleção de parâmetros iremos otimizá-la



            #Variância de Gradiente ----------------------------------------------------------------------------------------


            gradientes = [] # Lista de gradientes onde serão guaradados por ordem de que são calculados, ou seja, a ordem associada ao parâmetro que irão alterar

            for i in range(len(parametros)): # Por cada parâmetro
                gradiente=0 # Inicializa-se um gradiente igual a 0
                for t in range(num_trial): # Ir-se-à calcular um gradiente número de trial vezes para garantir que a sua média seja um valor mais exato possível

                    gradiente += calcular_gradiente(mistura_inicial, k, comp, Tfim, Tprog, Tcont, Prob, ADM, parametros[i],h1,h2,h3,h4)

                gradiente_final= (gradiente/num_trial) # Calcula-se a média dos gradientes calculados
                gradientes += [gradiente_final] # Adicona-se a média à lista de gradientes sequencialmente


            for e in range(len(parametros)): #Nesta iteração altera-se cada parâmetro consoante a diferença entre o seu respetivo gradiente e uma taxa_aprendizado

                if parametros[e] == 0: # O parâmetro a ser alterado é k

                    k = int(k - taxa_aprendizado * gradientes[e]) # Altera-se para um k inteiro pela diferença previamente referida


                if parametros[e] == 1: # O parâmetro a ser alterado é comp

                    comp = comp - taxa_aprendizado * gradientes[e] # Altera-se para um comp inteiro pela diferença previamente referida



                if parametros[e] == 2: # O parâmetro a ser alterado é Tfim

                    Tfim = Tfim - taxa_aprendizado * gradientes[e] # Altera-se para um Tfim inteiro pela diferença previamente referida


                if parametros[e] == 3: # O parâmetro a ser alterado é Tprog

                    Tprog = Tprog - taxa_aprendizado * gradientes[e] # Altera-se para um Tprog inteiro pela diferença previamente referida


                if parametros[e] == 4: # O parâmetro a ser alterado é Tcont

                    Tcont = Tcont - taxa_aprendizado * gradientes[e] # Altera-se para um Tcont inteiro pela diferença previamente referida


                if parametros[e] == 5: # O parâmetro a ser alterado é Prob

                    Prob = Prob - taxa_aprendizado * gradientes[e] # Altera-se para um Prob inteiro pela diferença previamente referida


                if parametros[e] == 6: # O parâmetro a ser alterado é ADM

                    ADM = ADM - taxa_aprendizado * gradientes[e] # Altera-se para um ADM inteiro pela diferença previamente referida




            #-------------------------------------------------------------------------------------------------------
            Resultado = SimFinal.simulador(mistura_inicial, k, comp, Tfim, Tprog, Tcont, Prob, ADM) # O resultado do cálculo de uma semelhança e trança após a melhoria dos parâmetros
            #Apesar de ser o cálculo de apenas uma simulação que não permite dissuadir o erro, é apenas utilizado para diferenciar os parâmetros otimizados com vista a distinguir valores maiores de semelhança

            if melhor_semelhança_atingida < Resultado[0]: # Se a semelhança do último resultado é maior que a última colocada esta é alterada

                melhor_semelhança_atingida = Resultado[0] #A semelhança máxima atingida é alterada
                melhor_tranca_atingida= Resultado[1] # A melhor trança atingida é alterada


        Valores_aproximado_selecao = [[k,comp,Tfim,Tprog,Tcont,Prob,ADM],melhor_semelhança_atingida,melhor_tranca_atingida] # É criada uma lista com uma lista de parâmetros otimizados da seleção, a melhor semelhança atingida e a respetiva trança
        Aproximacao_de_cada_selecao.append(Valores_aproximado_selecao) # É adicionado à lista a lista criada previamente
        if num%5 ==0: #Controlo de fase
            print(Aproximacao_de_cada_selecao)
        print(num)



    return    Aproximacao_de_cada_selecao #Retorna a lista das melhores aproximações

def repeteter(mistura_inicial): # Distribuidor das melhores aproximações pelo valor de semelhança atinginda
    a=descida_de_gradiente(mistura_inicial, 0.2, 50, 10, 3, 4, 40, 1,0.05) # Esta variável é uma lista com as melhores aproximações de cada seleção
    b01 = [] # Lista de melhores aproximações de semelhanças entre 0.0 e 0.1
    b02 = [] # Lista de melhores aproximações de semelhanças entre 0.1 e 0.2
    b03 = [] # Lista de melhores aproximações de semelhanças entre 0.2 e 0.3
    b04 = [] # Lista de melhores aproximações de semelhanças entre 0.3 e 0.4
    b05 = [] # Lista de melhores aproximações de semelhanças entre 0.4 e 0.5
    b06 = [] # Lista de melhores aproximações de semelhanças entre 0.5 e 0.6
    b07 = [] # Lista de melhores aproximações de semelhanças entre 0.6 e 0.7
    b08 = [] # Lista de melhores aproximações de semelhanças entre 0.7 e 0.8
    b09 = [] # Lista de melhores aproximações de semelhanças entre 0.8 e 0.9
    b10 = [] # Lista de melhores aproximações de semelhanças entre 0.9 e 1.0
    for i in range(len(a)): #Iterar sobre todas as listas de melhores aproximações
        if a[i][1]>=0 and a[i][1]<0.1: # Está entre 0.0 e 0.1
            b01.append(a[i])
        elif a[i][1]>=0.1 and a[i][1]<0.2: # Está entre 0.1 e 0.2
            b02.append(a[i])
        elif a[i][1]>=0.2 and a[i][1]<0.3: # Está entre 0.2 e 0.3
            b03.append(a[i])
        elif a[i][1]>=0.3 and a[i][1]<0.4: # Está entre 0.3 e 0.4
            b04.append(a[i])
        elif a[i][1]>=0.4 and a[i][1]<0.5: # Está entre 0.4 e 0.5
            b05.append(a[i])
        elif a[i][1]>=0.5 and a[i][1]<0.6: # Está entre 0.5 e 0.6
            b06.append(a[i])
        elif a[i][1]>=0.6 and a[i][1]<0.7: # Está entre 0.6 e 0.7
            b07.append(a[i])
        elif a[i][1]>=0.7 and a[i][1]<0.8: # Está entre 0.7 e 0.8
            b08.append(a[i])
        elif a[i][1]>=0.8 and a[i][1]<0.9: # Está entre 0.8 e 0.9
            b09.append(a[i])
        elif a[i][1]>=0.9 and a[i][1]<=1: # Está entre 0.9 e 1.0
            b10.append(a[i])

    return ("b01:",b01,"b02:",b02,"b03:",b03,"b04:",b04,"b05:",b05,"b06:",b06,"b07:",b07,"b08:",b08,"b09:",b09,"b10:",b10) # Retorna as aproximações distribuidas pelas respetivas listas de intervalos de valores.






if __name__ == '__main__':

    #print(repeteter([("TAT","TA"),("GTAA","CAGG"),("A","TA"),("AT","GC")]))
    #print(repeteter([("011","01"),("1","10"),("11","110")]))
    #print(repeteter([("AB","A"),("BCA","BCAB"),("BA","CAA"),("A","BCA"),("A","AB"),("BC","B"),("BAB","AB"),("BA","A")]))
    print(repeteter([("A","B"),("AB","A"),("B","BAB")]))








