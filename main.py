from kivy.app import App
import json
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
class AddLocationForm(BoxLayout):
    input_text=ObjectProperty()
    search_results=ObjectProperty()
    def search_location(self):
        link="http://api.openweathermap.org/data/2.5/find?q={}&type=like"
        url=link.format(self.input_text.text)
        request=UrlRequest(url,self.found_location)
        
        #print(self.input_text.text)
    
    def found_location(self,request,data):
        data=json.loads(data.decode()) if not isinstance(data,dict) else data
        cities=["{}({})".format(d['name'],d['sys']['country'])
                for d in data['list']]
        self.search_results.item_strings=cities
        print("\n".join(cities))
class WeatherApp(App):
    pass
if __name__=='__main__':
    WeatherApp().run()
