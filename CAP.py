import Eventos



def novaAgenda():
    return []


def adicionaEvento(Agenda,EventoNovo):
    return [ev for ev in Agenda if Eventos.tempoEvento(ev)< Eventos.tempoEvento(EventoNovo)] + [EventoNovo]+\
           [ev for ev in Agenda if Eventos.tempoEvento(ev)> Eventos.tempoEvento(EventoNovo)]


def tiraEvento(Agenda):

    if len(Agenda) > 0:
        return Agenda[1:]

    else:
        print("Alguma coisa não correu bem, não existe evento para retirar")


def seguinteEvento(Agenda):

    if len(Agenda) > 0:
        return Agenda[0]

    else:
        print("Alguma coisa não correu bem, não existe evento seguinte")