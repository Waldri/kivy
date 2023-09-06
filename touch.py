from kivy.app import App
from kivy.uix.label import Label

class TouchScreenApp(App):
    def build(self):
        return Label(text="Toque na tela!")

    def on_touch_down(self, touch):
        # Quando ocorre um toque na tela
        self.root.text = f"Toque na tela em {touch.x}, {touch.y}"

    def on_touch_move(self, touch):
        # Quando o dedo é arrastado na tela
        self.root.text = f"Arrastando em {touch.x}, {touch.y}"

    def on_touch_up(self, touch):
        # Quando o dedo é retirado da tela
        self.root.text = "Toque na tela!"

if __name__ == "__main__":
    TouchScreenApp().run()
