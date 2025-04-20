
import Peças
from Peças import transformador_de_input_em_peca


def criar_tranca_Nula():
    return []


def transformador_input_em_tranca(input):

    tranca_criada=criar_tranca_Nula()

    tranca_criada=[transformador_de_input_em_peca(input)]

    return tranca_criada



def concatenar_tranca_com_tranca(Tranca1, Tranca2):

    return Tranca1+Tranca2



def uniao_de_Pecas_de_Tranca(Tranca):

    Tranca_com_peca_singular= criar_tranca_Nula()
    for Peca in Tranca:

        if Tranca_com_peca_singular == []:

            Tranca_com_peca_singular = [Peças.fusao_peca(Peças.criar_peca_Nula(), Peca)]

        else:

            Tranca_com_peca_singular = [Peças.fusao_peca(Tranca_com_peca_singular[0], Peca)]

    return Tranca_com_peca_singular



def semelhanca_e_uniao(Tranca):

    Tranca_com_peca_singular=uniao_de_Pecas_de_Tranca(Tranca)

    Valor_semelhanca_tranca=Peças.comparador_semelhanca_peca_unida(Tranca_com_peca_singular[0])

    return Valor_semelhanca_tranca





def concatenar_semelhanca_uniao(Tranca1, Tranca2):

    valor=semelhanca_e_uniao(concatenar_tranca_com_tranca(Tranca1, Tranca2))

    return valor

def desconcatenar(Tranca):

    Novas_Trancas=[]

    for peca in Tranca:


        Novas_Trancas+=[[peca]]



    return Novas_Trancas

def tamanhoTranca(Tranca):

    return len(Tranca)


if __name__ == "__main__":

    print(desconcatenar([("aab", "ab"), ("aa", "bb")]))
    print(uniao_de_Pecas_de_Tranca([("aab", "ab"), ("aa", "bb"),("bbb","ab")]))






    