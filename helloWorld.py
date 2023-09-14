import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

# This line is necessary to configure Kivy's windowing system
kivy.require("2.0.0")

class HideCursorApp(App):
    def build(self):
        # Create a Label widget
        label = Label(text="Cursor is hidden. Press ESC to exit.")

        # Hide the cursor
        Window.set_system_cursor("none")

        return label

if __name__ == "__main__":
    HideCursorApp().run()
