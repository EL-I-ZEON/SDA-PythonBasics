from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        # Nastavení hlavního okna aplikace
        self.window = GridLayout()
        self.window.cols = 4

        # Vstupní pole
        self.result = TextInput(
            font_size=40,
            halign="right",
            readonly=True,
            multiline=False
        )
        self.window.add_widget(self.result)

        # Přidání tlačítek čísel
        for i in range(1, 10):
            self.window.add_widget(Button(
                text=str(i),
                font_size=32,
                on_press=self.on_button_press
            ))

        # Tlačítko 0
        self.window.add_widget(Button(
            text='0',
            font_size=32,
            on_press=self.on_button_press
        ))

        # Přidání tlačítek operací
        operations = ['+', '-', '*', '/']
        for op in operations:
            self.window.add_widget(Button(
                text=op,
                font_size=32,
                on_press=self.on_button_press
            ))

        # Tlačítko =
        self.window.add_widget(Button(
            text='=',
            font_size=32,
            on_press=self.on_equal_press
        ))

        # Tlačítko C (clear)
        self.window.add_widget(Button(
            text='C',
            font_size=32,
            on_press=self.clear_result
        ))

        # Připojení klávesových zkratek
        Window.bind(on_key_down=self.on_key_down)

        return self.window

    def on_button_press(self, instance):
        # Přidání textu tlačítka do vstupního pole
        self.result.text += instance.text

    def on_equal_press(self, instance):
        try:
            # Vyhodnocení matematického výrazu
            self.result.text = str(eval(self.result.text))
        except Exception:
            self.result.text = "Error"

    def clear_result(self, instance):
        # Vymazání vstupního pole
        self.result.text = ""

    def on_key_down(self, window, key, scancode, codepoint, modifier):
        # Ovládání kalkulačky klávesnicí
        if codepoint in '0123456789+-*/':
            self.result.text += codepoint
        elif key == 13:  # Enter klávesa
            self.on_equal_press(None)
        elif key == 8:  # Backspace klávesa
            self.result.text = self.result.text[:-1]
        elif key == 27:  # Escape klávesa pro vymazání
            self.clear_result(None)

# Spuštění aplikace
if __name__ == "__main__":
    CalculatorApp().run()
