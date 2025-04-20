import CAP
import Eventos
import obsrand



def simulador(mistura_inicial, k, comp, Tfim, Tprog, Tcont, Prob, ADM):
    Tempo = 0
    EventoAdd1 = Eventos.eventoTT(Tempo + obsrand.exprandom(Tprog),"prog")
    EventoAdd2 = Eventos.eventoTT(Tempo + obsrand.exprandom(Tcont),"control")

    Agenda = CAP.novaAgenda()
    Agenda = CAP.adicionaEvento(Agenda,EventoAdd1)
    Agenda = CAP.adicionaEvento(Agenda, EventoAdd2)

    EventoAtual = Eventos.eventoTT(0, "prog")
    Tipo = Eventos.tipoEvento(EventoAtual)
    mistura = Eventos.multiplicadorInput(mistura_inicial, k)
    while Tempo <= Tfim:

        if Tempo == 0:
            mistura = Eventos.process(EventoAtual, mistura, Prob, ADM)

        else:
            mistura = Eventos.process(EventoAtual, mistura, Prob, ADM)
            Agenda = CAP.tiraEvento(Agenda)

            if Tipo == "prog":
                Agenda = CAP.adicionaEvento(Agenda, EventoAdd1)
            else:
                Agenda = CAP.adicionaEvento(Agenda, EventoAdd2)


        EventoAtual = CAP.seguinteEvento(Agenda)

        Tempo = Eventos.tempoEvento(EventoAtual)
        Tipo = Eventos.tipoEvento(EventoAtual)

        EventoAdd1 = Eventos.eventoTT(Tempo + obsrand.exprandom(Tprog),"prog")
        EventoAdd2 = Eventos.eventoTT(Tempo + obsrand.exprandom(Tcont),"control")









    return Eventos.Terminar(mistura, comp)




