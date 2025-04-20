

import Mistura
import random
from Mistura import iterador_de_Controlo, semelhanca_associada, remove_ultima_condicoes, valor_update, atualizar_update, retorna_tamanho_condicoes, retorna_condicoes_final


def progresso(mistura,Prob):


    Mistura_a_alterar = Mistura.novaMistura()

    Mistura_a_alterar = mistura

    if Mistura.tamanho_minimo_Mistura(Mistura_a_alterar):

        Mistura_alterada = Mistura.avaliar_concatenar_conquistar(Mistura_a_alterar)

        if Mistura.valor_Concatenado(Mistura_alterada) < Mistura.valor_não_Concatenado(Mistura_alterada):

            if random.random() <= Prob:

                return Mistura.introduz_par_na_mistura(Mistura_alterada)

            else:
                return mistura

        else:

            return  Mistura.introduz_par_na_mistura(Mistura_alterada)
    else:
        return mistura




def controlo(mistura,Adm):

    Mistura_Avaliada = Mistura.avalicao_mistura(mistura)

    Update= iterador_de_Controlo(Mistura_Avaliada)

    Mistura_Nova= Mistura.novaMistura()

    while valor_update(Update):


        if semelhanca_associada(Mistura_Avaliada)>Adm:

            Mistura_Nova = Mistura.adicionar_à_mistura(Mistura_Avaliada,Mistura_Nova)

        else:

            Mistura_Nova = Mistura.desconcatenar_e_adicionar_à_mistura(Mistura_Avaliada, Mistura_Nova)

        Mistura_Avaliada= remove_ultima_condicoes(Mistura_Avaliada)

        Update=atualizar_update(Update)

    return Mistura_Nova




def novoEvento():

    return [0,""]


def eventoTT(tempo,string):

    Evento = novoEvento()

    Evento[0] = tempo

    Evento[1] = string

    return Evento


def tipoEvento(Evento):
    return Evento[1]



def tempoEvento(Evento):
    return Evento[0]


def multiplicadorInput(mistura,k):

    Mistura_mult = Mistura.novaMistura()

    Mistura_mult = (Mistura.inputToTranca(mistura))*k

    return Mistura_mult


def Terminar(misturafinal,comp):

    Lista_nova = Mistura.finalizador(misturafinal)


    Resultado_final=[0,""]

    update = iterador_de_Controlo(Lista_nova)

    while Mistura.valor_update(update):

        if semelhanca_associada(Lista_nova) > Resultado_final[0] and retorna_tamanho_condicoes(Lista_nova)<= comp:

            Resultado_final=[semelhanca_associada(Lista_nova),retorna_condicoes_final(Lista_nova)]

        Lista_nova= remove_ultima_condicoes(Lista_nova)

        update = atualizar_update(update)

    return Resultado_final


def process(evento, mistura, prob, adm):

    if tipoEvento(evento) == "prog":

        return progresso(mistura, prob)

    elif tipoEvento(evento) == "control":

        return controlo(mistura, adm)
    else:

        return mistura

if __name__ == "__main__":

    print(progresso([[("1","1")] ,  [("11","11"),("2","2"),("222","222")]  ,  [("3","3")],[("33","33")]],0.2))

    print(controlo([[("3","3"),("22","22")] ,  [("2","2"),("11","11"),("222","222")]  ,  [("1","1")],[("33","33")]],0.6))