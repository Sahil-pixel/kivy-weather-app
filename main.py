 

from kivy.app import*
from kivy.uix.textinput import TextInput
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button




class MyApp(App):
	def f(self,x):
		BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
		CITY = x
		API_KEY ="put your own api key"
		URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
		response=UrlRequest(URL,self.got_json)
		print(response)
	def got_json(self,req, result):
		self.t2.text=str(result)
	def build(self):
		self.box=BoxLayout(orientation='vertical')
		self.t=TextInput(hint_text='Enter City Name')
		self.t2=TextInput()
		self.box.add_widget(self.t)
		self.box.add_widget(self.t2)
		self.box.add_widget(Button(on_release=self.callback))
		return self.box
	def callback(self,obj):
		self.f(self.t.text)

    
MyApp().run()
