import obsrand
import random as jorge


# Funções úteis para realizar esta merda:
def concatenar(u, v):
    # Parte fácil
    return u + v
    # Concatena(junta) duas tranças :)


def listmaker(mistura):
    # Temos de emendar a necessidade desta função :(
    mistura_nova = []
    for Trança in mistura:
        mistura_nova += [[Trança]]
    return mistura_nova


def randomPar(mistura):
    a = 1
    b = 1
    while a == b:
        a = jorge.randint(0, len(mistura) - 1)
        b = jorge.randint(0, len(mistura) - 1)
        if a != b:
            return [mistura[a], mistura[b]]
    # Escolhe um par aleatório de tranças da mistura


def juntar(Trança):
    Nova_Trança = ["", ""]
    for peça in Trança:
        Nova_Trança[0] += peça[0]
        Nova_Trança[1] += peça[1]
    return Nova_Trança
    # Junta as peças de uma trança para se poder calcular a semelhança


def semelhança(u):
    # Fator determinístico do algoritmo
    min_len = len(u[0])
    max_len = len(u[1])
    igualdade = 0
    if len(u[0]) >= len(u[1]):
        min_len = len(u[1])
        max_len = len(u[0])
    for i in range(min_len):
        if u[0][i] == u[1][i]:
            igualdade += 1
    return igualdade / max_len
    # Determina a proporção de algarismos/símbolos iguais na parte superior e inferior da Trança


# Funções evento:
def evento_prog(mistura, Prob):
    # Neste evento vamos buscar tranças da nossa mistura para: ou criar uma nova trança
    # e colocá-la na mistura de tranças se tiver semelhança elevada ou se averiguarmos que a nova trança
    # tem semelhança inferior à esperada, mantemos a mistura igual/sob uma probabilidade podemos colcá-la na nova mistura

    if len(mistura) < 2:
        return mistura
    # Basicamente é impossível juntar duas tranças se só existe uma trança

    Trança1 = (randomPar(mistura)[0])
    Trança2 = (randomPar(mistura)[1])
    TrançaConc = concatenar(Trança1, Trança2)
    # Primeira parte: tirar as tranças que queremos usar e criar uma nova trança a partir delas(concatená-la),
    # é preciso que a nova Trança tenha um comprimento menor que comp

    Potencial = semelhança(juntar(Trança1)) + semelhança(juntar(Trança2)) / 2
    SemConc = semelhança(juntar(TrançaConc))
    # Segunda parte: calcular a semelhança da nova trança e o potencial(média aritmética das semelhanças)
    # das tranças que a formam

    if Potencial > SemConc and jorge.random() < Prob:
        mistura.append(TrançaConc)
    else:
        mistura.append(TrançaConc)
    # Terceira parte: se a semelhança da nova trança for maior que o potencial ela é colocada na mistura,
    # doutra forma sobre uma probabilidade (Prob) é colocada ou não na mistura

    return mistura
    # Retornamos a mistura com o update devido


def evento_cont(mistura, ADM):
    # Neste evento vamos criar uma nova mistura que vai resultar da filtração de tranças pelo seu valor de semelhança.
    # Se a semelhança for abaixo de ADM, fragmentamos a trança em peças e juntamos as peças à nossa mistura
    nova_mistura = mistura
    for lista in mistura:
        if semelhança(juntar(lista)) < ADM:
            nova_mistura.remove(lista)
            for peça in lista:
                nova_mistura.append([peça])
    return mistura
    # Retornamos a mistura com o update devido


def simulador(mistura_inicial, k, comp, Tfim, Tprog, Tcont, Prob, ADM):
    # Agora no simulador definimos de imediato uma agenda de eventos e um tempo inicial

    tempo_atual = 0
    Progresso = 0
    Controlo = 1
    evento_agendado = [0]
    mistura_atual = (listmaker(mistura_inicial)) * k
    Trança_final = []
    Valor_semelhança_FINAL = 0

    while tempo_atual <= Tfim:
        # Naturalmente quando o tempo de simulação acabar devolvemos os resultados a uma função final

        if evento_agendado == [] or evento_agendado[0] == Progresso:
            # Neste caso o evento a realizar é o de Progresso
            mistura_atual = evento_prog(mistura_atual, Prob)
            evento_agendado += [jorge.randint(0, 1)]
            tempo_atual += obsrand.exprandom(Tprog)
            evento_agendado = evento_agendado[1:]

        else:
            # Neste caso o evento a realizar é o de Controlo
            mistura_atual = evento_cont(mistura_atual, ADM)
            evento_agendado += [0]
            tempo_atual += obsrand.exprandom(Tcont)
            evento_agendado = evento_agendado[1:]

    for Trança in mistura_atual:
        # Só falta encontrar a Trança com o melhor teor de semelhança
        Semelhança_atual = semelhança(juntar(Trança))

        if Semelhança_atual > Valor_semelhança_FINAL and len(Trança) < comp:
            Valor_semelhança_FINAL = Semelhança_atual
            Trança_final = Trança

    # E finalmente...
    return juntar(Trança_final)


if __name__ == "__main__":
    print(simulador([("A","BAA"),("AB","AA"),("BBA","BB")],500,100,10000,50,80,0.8,0.5))


