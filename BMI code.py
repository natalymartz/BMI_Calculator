#App to calculate your BMI
import kivy
import kivy.app
import kivy.uix.label
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class IMC_Calc(App):
    def build(self):
        self.ventana = GridLayout()
        self.ventana.cols = 1
        self.ventana.size_hint = (0.5,0.4)
        self.ventana.pos_hint = {'center_x':0.5,'center_y':0.5}
        #insertamos imagen
        self.ventana.add_widget(Image(source='Hlogo.png'))
        #insertamos el label
        self.saludo=Label(
            text="Write your name:",
            color='#4d8cf5',
            font_size=24
            )
        self.user=TextInput(
            multiline=False,
            padding_y=(10,10),
            size_hint=(1,0.9)
        )
        self.button = Button(
            text='Next->',
            size_hint=(1,0.9),
            bold=True,
            background_color = '#4d8cf5'
        )
        self.ventana.add_widget(self.saludo)
        self.ventana.add_widget(self.user)
        self.button.bind(on_press = self.user_data)
        self.ventana.add_widget(self.button)
        return self.ventana
    def user_data(self,x):
        self.ventana.remove_widget(self.user)
        self.ventana.remove_widget(self.button)
        self.saludo.text = 'Hello ' + self.user.text + " let's get your BMI "
        self.data1=Label(
            text="Enter your weight (kg):",
            color='#4d8cf5',
            font_size=24
            )
        self.weight=TextInput(
            multiline=False,
            padding_y=(10,10),
            size_hint=(1,0.9)
        )
        self.data2 = Label(
            text="Enter your height (m):",
            color='#4d8cf5',
            font_size=24
        )
        self.height = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(1, 0.9)
        )
        self.IMC=Button(
            text='Calculate BMI',
            size_hint=(1, 0.9),
            bold=True,
            background_color='#4d8cf5'
        )
        self.end=Button(
            text='END',
            size_hint=(1, 1),
            bold=True,
            background_color='#4d8cf5'
        )
        self.save=Button( #esto es nuevo
            text="Guardar IMC",
            size_hint=(1,1),
            bold=True,
            background_color='#4d8cf5'
        )
        self.ventana.add_widget(self.data1)
        self.ventana.add_widget(self.weight)
        self.ventana.add_widget(self.data2)
        self.ventana.add_widget(self.height)
        self.ventana.add_widget(self.IMC)
        self.IMC.bind(on_press = self.IMC_FINAL)


    def IMC_FINAL(self,x):
        self.ventana.remove_widget(self.data1)
        self.ventana.remove_widget(self.data2)
        self.ventana.remove_widget(self.weight)
        self.ventana.remove_widget(self.height)
        self.ventana.remove_widget(self.IMC)
        resultado=0
        while resultado==0:
            weight=str(self.weight.text)
            height=str(self.height.text)
            weight=float(weight)
            height=float(height)
            height=height**2
            resultado=weight/height
            resultado=round(resultado,2)
            resultado=str(resultado)
            user=str(self.user.text)
            self.saludo.text=f"The Body Mass Index (BMI) of {user} is {resultado}"
            self.ventana.add_widget(self.end)
            self.end.bind(on_press=self.stop_program)
            return resultado
    def stop_program(self,x):
        App.get_running_app().stop()
#puedo agregar si esta en el promedio segun su edad y asi ...
#cada resultado que me salga lo puedo guardar en un excel si el usuario quiere guardarlo o no

if __name__=="__main__":
    IMC_Calc().run()
