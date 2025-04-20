

def criar_peca_Nula():

    return ("","")

def fusao_peca(Peca1, Peca2):

    Nova_peca = criar_peca_Nula()



    Nova_peca=(Peca1[0] + Peca2[0], Peca1[1] + Peca2[1])



    return Nova_peca

def transformador_de_input_em_peca(input):



    Peca_criada = criar_peca_Nula()



    Peca_criada = fusao_peca(input, Peca_criada)


    return Peca_criada

def comparador_semelhanca_peca_unida(Peca):

    String_superior = Peca[0]

    String_inferior = Peca[1]

    Igualdade=0

    if len(String_superior)>len(String_inferior):

        Min_len = len(String_inferior)

        Max_len = len(String_superior)

    else:
        Min_len = len(String_superior)

        Max_len = len(String_inferior)


    for caracter in range(Min_len):

        if String_inferior[caracter] == String_superior[caracter]:

            Igualdade += 1

    return Igualdade / Max_len

if __name__ == "__main__":
    print(comparador_semelhanca_peca_unida(("aaab","aab")))
    print(fusao_peca(("aaab","aab"),("","")))
    print(transformador_de_input_em_peca(("aaab","aab")))

