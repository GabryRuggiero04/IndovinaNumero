import random

class Model(object):
    def __init__(self):
        self._Nmax=100
        self._Tmax=6
        self._T=self._Tmax
        self._segreto=None

    def reset(self):
        #Questo metodo resetta lo stato del gioco.
        # Imposta il numero segreto a un numero randomico fra 0 e Nmax e
        # ripristina il numero di tentativi rimanenti
        # return: niente, il segreto in fase di test#
        self._segreto=random.randint(0,self._Nmax)
        self._T=self._Tmax
        print(self._segreto)


    def play(self, tentativo):
        #Questo metodo riceve come argomento un valore intero,
        # il tentativo del giocatore, e lo confronta il
        # numero segreto randomico
        # return:  1 se il tentativo è più piccolo del segreto
        #          0 se il tentativo è uguale al segreto
        #         -1 se il tentativo è maggiore del segreto
        #          2 se non ho più tentativi disponibili#
        self._T-=1
        if tentativo == self._segreto:
            #ho vinto
            return 0

        if self._T == 0:
            #ho finito le vite, non posso più giocare
            return 2

        if tentativo > self._segreto:
            #il tentativo dell'utente è più grande del segreto
            return -1
        else:
            #tentativo è più piccolo del segreto
            return 1

    @property
    def Nmax(self):
        return self._Nmax

    @property
    def Tmax(self):
        return self._Tmax

    @property
    def T (self):
        return self._T

    @property
    def segreto(self):
        return self._segreto

if __name__ == "__main__":
    m=Model()
    m.reset()
    print(m.play(50))
    print(m.play(30))
    print(m.play(20))
    print(m.play(32))
    print(m.play(20))
    print(m.play(57))