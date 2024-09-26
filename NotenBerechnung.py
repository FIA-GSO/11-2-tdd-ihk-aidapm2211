def berechne_prozentwert(erreichte_punkte, maximale_punkte):
    if maximale_punkte <= 0 or erreichte_punkte < 0:
        raise ValueError("Ungültige Punktzahl")
    return (erreichte_punkte / maximale_punkte) * 100


def ermittle_note(prozentwert):
    if prozentwert < 0 or prozentwert > 100:
        raise ValueError("Ungültiger Prozentwert")

    if prozentwert >= 92:
        return "sehr gut"
    elif prozentwert >= 81:
        return "gut"
    elif prozentwert >= 67:
        return "befriedigend"
    elif prozentwert >= 50:
        return "ausreichend"
    else:
        return "ungenügend"
