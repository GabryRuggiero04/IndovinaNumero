import flet as ft



class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)
        self._txtNmax=ft.TextField(label= "Numero Max", value=self._controller.getNmax(),
                                  disabled=True
                                  )

        self._txtTmax=ft.TextField(label= "Tentativi max", value=self._controller.getTmax(),
                                  disabled=True
                                  )

        self._txtT=ft.TextField(label= "Tentativi rimanenti",
                               disabled=True
                               )

        self.txtInTentativo=ft.TextField(label= "Valore")
        self.btnReset=ft.ElevatedButton(text="Nuova partita", on_click=self._controller.reset)
        self.btnIndovina=ft.ElevatedButton(text="Indovina", on_click=self._controller.play)

        self._row1 = ft.Row(controls=[self._txtNmax, self.btnReset])
        self.row2 = ft.Row(controls=[self._txtT,self._txtTmax])
        self.row3=ft.Row(controls=[self.txtInTentativo,self.btnIndovina])

        self._lvOut=ft.ListView(expand=True) #Spazio per stampare il testo sotto i textfield,
                                            #contiene lista di stringhe

        self._page.add(self._row1,self.row2,self.row3, self._lvOut)
        self._page.update()

    def setController(self,controller):
        self._controller = controller

    def update(self):
        self._page.update()