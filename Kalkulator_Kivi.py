from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


class PaymentCalculatorApp(App):
    def build(self):
        self.cenik = {"pivo": 3, "kofola": 2, "pizza": 12, "polievka": 1}

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.lidi_input = TextInput(hint_text="Kolik lidí se účastní platby", multiline=False)
        layout.add_widget(Label(text="Kolik lidí se účastní platby?"))
        layout.add_widget(self.lidi_input)

        self.pivo_input = TextInput(hint_text="Kolik piv?", multiline=False)
        layout.add_widget(Label(text="Kolik piv?"))
        layout.add_widget(self.pivo_input)

        self.kofola_input = TextInput(hint_text="Kolik kofol?", multiline=False)
        layout.add_widget(Label(text="Kolik kofol?"))
        layout.add_widget(self.kofola_input)

        self.pizza_input = TextInput(hint_text="Kolik pizz?", multiline=False)
        layout.add_widget(Label(text="Kolik pizz?"))
        layout.add_widget(self.pizza_input)

        self.polievka_input = TextInput(hint_text="Kolik polévek?", multiline=False)
        layout.add_widget(Label(text="Kolik polévek?"))
        layout.add_widget(self.polievka_input)

        self.spropitne_input = TextInput(hint_text="Spropitné (%)?", multiline=False)
        layout.add_widget(Label(text="Spropitné (%)?"))
        layout.add_widget(self.spropitne_input)

        calculate_button = Button(text="Vypočítat")
        calculate_button.bind(on_press=self.calculate_payment)
        layout.add_widget(calculate_button)

        self.result_table = TextInput(hint_text="Výsledky se zobrazí zde.", multiline=True, readonly=True)
        layout.add_widget(ScrollView(size_hint=(1, None), size=(400, 200), do_scroll_x=False, do_scroll_y=True))
        layout.add_widget(self.result_table)

        self.result_label = Label(text="Celková částka bude zobrazena zde.")
        layout.add_widget(self.result_label)

        return layout

    def calculate_payment(self, instance):
        try:
            lidi = int(self.lidi_input.text)
            piva = int(self.pivo_input.text) if self.pivo_input.text else 0
            kofola = int(self.kofola_input.text) if self.kofola_input.text else 0
            pizza = int(self.pizza_input.text) if self.pizza_input.text else 0
            polievka = int(self.polievka_input.text) if self.polievka_input.text else 0
            spropitne = int(self.spropitne_input.text) if self.spropitne_input.text else 0

            celkova_cena = (piva * self.cenik["pivo"] +
                            kofola * self.cenik["kofola"] +
                            pizza * self.cenik["pizza"] +
                            polievka * self.cenik["polievka"])

            celkova_cena_spropitne = celkova_cena + (celkova_cena * spropitne / 100)

            self.result_table.text = ""

            castka_na_osobu = celkova_cena / lidi
            for i in range(1, lidi + 1):
                self.result_table.text += f"Osoba {i} zaplatí bez spropitného: {castka_na_osobu:.2f} €\n"

            self.result_label.text = f"Celková částka bez spropitného: {celkova_cena:.2f} €\n" \
                                      f"Celková částka se spropitným: {celkova_cena_spropitne:.2f} €"
        except ValueError:
            self.result_label.text = "Zadejte platné hodnoty."

if __name__ == "__main__":
    PaymentCalculatorApp().run()