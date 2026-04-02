from cgitb import reset

from view import View
from model import Model
import flet as ft

class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNmax(self):
        return self._model.Nmax

    def getTmax(self):
        return self._model.Tmax

    # tutti i metodi del controller generati da un pulsante devono avere argomento e
    def reset(self, e):
        self._model.reset() #resetto lo stato del gioco lato modello!!
        self._view.btnIndovina.disabled = False
        self._view._txtT.value=self._model.T #il text field dell'interfaccia prende il valore del T del model
        self._view._lvOut.controls.clear() #stiamo dicendo di svuotare la lista di controlli di lvOut
        self._view._lvOut.controls.append(
            ft.Text("Inizia il gioco! Indovina a quale numero sto pensando", color="blue")
        )
        # ogni volta che finiamo di fare delle modifiche dobbiamo dire di aggiornare
        # la pagina della finestra per visualizzarle,
        # in questo caso ci appoggiamo a un metodo presente in view:
        # def update(self):
        #         self._page.update()
        self._view.update()

    def play(self, e):
        tentativoStr=self._view.txtInTentativo.value #il tentativo=valore inserito nel textfield
        try:
            tentativoIntero=int(tentativoStr) #trasforno la stringa in intero, se è un numero ok, altrimenti gestisco l'errore
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Errore, devi inserire un numero intero")
            )
            self._view.update()
            return #return se si scatena l'errore

        confronto=self._model.play(tentativoIntero)

        if confronto==0:
            self._view._lvOut.controls.append(
                ft.Text(f"Grande, il numero segreto è: {tentativoIntero}", color="green"))
            self._view.btnIndovina.disabled = True
            self._view.update()
            return

        if confronto==2:
            self._view._txtT.value = self._model.T
            self._view._lvOut.controls.append(
                ft.Text(f"Nope! Hai perso!! Il numero segreto era: {self._model.segreto} ", color="red"))
            self._view.btnIndovina.disabled = True
            self._view.update()
            return

        if confronto==-1:
            self._view._txtT.value = self._model.T
            self._view._lvOut.controls.append(
                ft.Text(f"Nope! Il numero segreto è minore di: {tentativoIntero}"))
            self._view.update()
            return

        if confronto==1:
            self._view._txtT.value = self._model.T
            self._view._lvOut.controls.append(
                ft.Text(f"Nope! Il numero segreto è maggiore di: {tentativoIntero}"))
            self._view.update()
            return
