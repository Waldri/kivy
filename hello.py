import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from glob import glob
from os.path import dirname, join, basename
# To full screen
from kivy.core.window import Window
# Video player
from kivy.uix.videoplayer import VideoPlayer

# This line is necessary to configure Kivy's windowing system
kivy.require("2.0.0")

class HelloWorldApp(App):
    def build(self):
        # Create a layout to hold the video player
        layout = BoxLayout(orientation='vertical')
        # Create a VideoPlayer widget
        video = VideoPlayer(source='ctrl_video.mp4', state='play', options={'eos': 'loop'})
        # Add the video player to the layout
        layout.add_widget(video)

        # Create a Label widget with the text "Hello, World!"
        label = Label(text="Hello, World!")
        return layout
    def on_start(self):
        # Full screen
        Window.fullscreen = 'auto'

# Run the Kivy application
if __name__ == "__main__":
    HelloWorldApp().run()