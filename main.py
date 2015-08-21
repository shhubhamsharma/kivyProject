from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class AddLocationForm(BoxLayout):
    input_text=ObjectProperty()
    def search_location(self):
        print(self.input_text.text)
    
class WeatherApp(App):
    pass
if __name__=='__main__':
    WeatherApp().run()
