"Mistura"
import Tranças
import random

from Tranças import desconcatenar


def novaMistura():

    return []









def randomPar(mistura):


    Par=random.sample(mistura,2)

    for tranca in Par:

        mistura.remove(tranca)

    return [Par,mistura]


def valor_não_Concatenado(Condicoes):

    return Condicoes[2]



def valor_Concatenado(Condicoes):

    return Condicoes[1]



def introduz_par_na_mistura(Condicoes):

    return [concatenacao_avancada(Condicoes[0])] + Condicoes[3]


def avaliar_concatenar_conquistar(mistura):


    Conjunto=randomPar(mistura)


    Par=Conjunto[0]


    ValorConc=Tranças.concatenar_semelhanca_uniao(Par[0], Par[1])


    ValorNaoConc= (Tranças.semelhanca_e_uniao(Par[0]) + Tranças.semelhanca_e_uniao(Par[1])) / 2



    return [Par]+[ValorConc]+[ValorNaoConc]+[Conjunto[1]]



def tamanho_minimo_Mistura(mistura):
    return len(mistura)>2


def concatenacao_avancada(Par):

    return Tranças.concatenar_tranca_com_tranca(Par[0], Par[1])






















def avalicao_mistura(mistura):

    lista_avaliada=[]

    for Tranca in mistura:

        lista_avaliada+= [[Tranças.semelhanca_e_uniao(Tranca)] + [Tranca]]

    return lista_avaliada



def iterador_de_Controlo(lista_avaliada):

    Tamanho = len(lista_avaliada)

    return Tamanho


def remove_ultima_condicoes(lista_avaliada):

    return lista_avaliada[1:]


def semelhanca_associada(lista_avaliada):

    return lista_avaliada[0][0]


def desconcatenar_e_adicionar_à_mistura(lista_avaliada, mistura):

    Lista_Mistura = novaMistura()

    Lista_Mistura += desconcatenar(lista_avaliada[0][1])
    return mistura+ Lista_Mistura


def adicionar_à_mistura(lista_avaliada,mistura):

    Lista_Mistura = novaMistura()

    Lista_Mistura += [lista_avaliada[0][1]]

    return mistura+ Lista_Mistura

def valor_update(update):
    if update==0:
        return False
    else:
        return True

def atualizar_update(update):
    return update-1








def inputToTranca(mistura):

    Nova_Mistura = novaMistura()

    for Input in mistura:

        Nova_Mistura+=[Tranças.transformador_input_em_tranca(Input)]

    return Nova_Mistura








def finalizador(mistura):

    listaFinal=[]
    for tranca in mistura:
        listaFinal+=[[Tranças.semelhanca_e_uniao(tranca),Tranças.tamanhoTranca(tranca), tranca]]

    return listaFinal
def retorna_tamanho_condicoes(Lista_final):
    return Lista_final[0][1]

def retorna_condicoes_final(Lista_final):
    return Lista_final[0][2]





if __name__ == "__main__":
    print(randomPar([[1],[2],[3]]))
    print(avaliar_concatenar_conquistar([[("a", "a")], [("a", "a"), ("ab", "a"), ("bba", "a")], [("a", "bbb")], [("a", "a")]]))


    print(len([[("",""),("",""),("","")],[("c",""),("",""),("","")],[("b",""),("",""),("","")],[("a",""),("",""),("","")]]))

    print(desconcatenar_e_adicionar_à_mistura([[0.2, [("a","a"),("a","a")]],[0.5,[("a","a")],[0.2,[("ab","a")]],[0.1,("bba","a")]],[0.1,[("a","bbb")]],[1,[("a","a")]]],[[("a","a")],[("a","a"),("ab","a"),("bba","a")],[("a","bbb")],[("a","a")]]))

    print(adicionar_à_mistura([[0.2, [("a","a")]],[0.5,[("a","a")],[0.2,[("ab","a")]],[0.1,("bba","a")]],[0.1,[("a","bbb")]],[1,[("a","a")]]],[[("a","a")],[("a","a"),("ab","a"),("bba","a")],[("a","bbb")],[("a","a")]]))


