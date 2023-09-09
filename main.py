from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton


Builder.load_string("""
<ScreenOne>:
    id: screen1
    Label:
        text: 'Salary related Calculator(Ethiopia)'
        font_size: '20sp'  # Change the font size
        halign: 'center'  # Center-align the text
        text_size: (None, None)
        size_hint_y: None  # Disable automatic size_hint
        pos_hint: {'center_y': 0.95}
        background_color: (73/255, 147/255, 150/255, 1)
		canvas.before:
			Color:
				rgba: self.background_color
			Rectangle:
				size: self.size
				pos: self.pos
    Label:
        text: '©2023 Developed by Geda Siraj'
        halign: 'center'
        size_hint_y: None  # Disable automatic size_hint
        background_color: (73/255, 147/255, 150/255, 1)
        height: 50
		canvas.before:
			Color:
				rgba: self.background_color
			Rectangle:
				size: self.size
				pos: self.pos
        
    Button:
        text: 'Calculate net salary'
        pos_hint: {'center_x': 0.5, 'center_y': 0.70}
        font_size: '27sp'
        size_hint: None, None  # Disable automatic size_hint
        size: "350dp", "80dp"  # Set the button size in density-independent pixels (dp)
        on_press:
            root.manager.current = 'screen2'
    Button:
        text: 'Calculate gross salary'
        pos_hint: {'center_x': 0.5, 'center_y': 0.52}
        font_size: '27sp'
        size_hint: None, None  # Disable automatic size_hint
        size: "350dp", "80dp"  # Set the button size in density-independent pixels (dp)
        on_press:
            root.manager.current = 'screen3'
    Button:
        text: 'Calculate duty'
        pos_hint: {'center_x': 0.5, 'center_y': 0.36}
        font_size: '27sp'
        size_hint: None, None  # Disable automatic size_hint
        size: "350dp", "80dp"  # Set the button size in density-independent pixels (dp)
        on_press:
            root.manager.current = 'screen4'

    Button:
        text: 'Exit'
        pos_hint: {'center_x': 0.5, 'center_y': 0.20}
        font_size: '20sp'
        background_color: (0.8, 0.2, 0, 1)
        size_hint: None, None  # Disable automatic size_hint
        size: "100dp", "50dp"  # Set the button size in density-independent pixels (dp)
        on_release:
            app.stop()
            #root.manager.current = 'screen1'

<ScreenTwo>:
    id: screen2
    Label:
        text: 'Gross to Net Salary'
        font_size: '20sp'  # Change the font size
        halign: 'center'  # Center-align the text
        text_size: (None, None)
        size_hint_y: None  # Disable automatic size_hint
        pos_hint: {'center_y': 0.95}
        background_color: (73/255, 147/255, 150/255, 1)
		canvas.before:
			Color:
				rgba: self.background_color
			Rectangle:
				size: self.size
				pos: self.pos
    Label:
        text: '©2023 Developed by Geda Siraj'
        halign: 'center'
        size_hint_y: None  # Disable automatic size_hint
        background_color: (73/255, 147/255, 150/255, 1)
        height: 50
		canvas.before:
			Color:
				rgba: self.background_color
			Rectangle:
				size: self.size
				pos: self.pos
    Button:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.20}
        font_size: '20sp'
        background_color: (0.8, 0.2, 0, 1)
        size_hint: None, None  # Disable automatic size_hint
        size: "100dp", "50dp"  # Set the button size in density-independent pixels (dp)
        on_press:
            root.manager.current = 'screen1'
<ScreenThree>:
    id: screen3
    Label:
        text: 'Net to Gross Salary'
        font_size: '20sp'  # Change the font size
        halign: 'center'  # Center-align the text
        text_size: (None, None)
        size_hint_y: None  # Disable automatic size_hint
        pos_hint: {'center_y': 0.95}
        background_color: (73/255, 147/255, 150/255, 1)
		canvas.before:
			Color:
				rgba: self.background_color
			Rectangle:
				size: self.size
				pos: self.pos
    Label:
        text: '©2023 Developed by Geda Siraj'
        halign: 'center'
        size_hint_y: None  # Disable automatic size_hint
        background_color: (73/255, 147/255, 150/255, 1)
        height: 50
		canvas.before:
			Color:
				rgba: self.background_color
			Rectangle:
				size: self.size
				pos: self.pos
    Button:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.20}
        font_size: '20sp'
        background_color: (0.8, 0.2, 0, 1)
        size_hint: None, None  # Disable automatic size_hint
        size: "100dp", "50dp"  # Set the button size in density-independent pixels (dp)
        on_press:
            root.manager.current = 'screen1'
<ScreenFour>:
    id: screen4
    Label:
        text: 'Duty Calculator'
        font_size: '20sp'  # Change the font size
        halign: 'center'  # Center-align the text
        text_size: (None, None)
        size_hint_y: None  # Disable automatic size_hint
        pos_hint: {'center_y': 0.95}
        background_color: (73/255, 147/255, 150/255, 1)
		canvas.before:
			Color:
				rgba: self.background_color
			Rectangle:
				size: self.size
				pos: self.pos
    Label:
        text: '©2023 Developed by Geda Siraj'
        halign: 'center'
        size_hint_y: None  # Disable automatic size_hint
        background_color: (73/255, 147/255, 150/255, 1)
        height: 50
		canvas.before:
			Color:
				rgba: self.background_color
			Rectangle:
				size: self.size
				pos: self.pos
    
    TextInput:
        id: input1
        hint_text: 'Enter gross salary'
        size_hint: (None, None)  # Disable automatic sizing
        width: 300               # Set width
        height: 50                # Set height
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
    TextInput:
        id: input2
        hint_text: 'Enter total hrs'
        size_hint: (None, None)  # Disable automatic sizing
        width: 300               # Set width
        height: 50                # Set height
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    Button:
        text: 'Submit'
        pos_hint: {'center_x': 0.5, 'center_y': 0.50}
        font_size: '20sp'
        #background_color: (0.2, 0.2, 0, 1)
        size_hint: None, None  # Disable automatic size_hint
        size: "100dp", "50dp"  # Set the button size in density-independent pixels (dp)
        
        on_release:
            app.error_check(input1.text, input2.text)
            input1.text = ""
            input2.text = ""
            
    Button:
        text: 'Back'
        pos_hint: {'center_x': 0.8, 'center_y': 0.20}
        font_size: '20sp'
        background_color: (0.8, 0.2, 0, 1)
        size_hint: None, None  # Disable automatic size_hint
        size: "100dp", "50dp"  # Set the button size in density-independent pixels (dp)
        on_press:
            root.manager.current = 'screen1'
""")
screen_manager = ScreenManager()

class ScreenOne(Screen):
    pass
  
class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class ScreenFour(Screen):
    pass

screen_manager.add_widget(ScreenOne(name="screen1"))
screen_manager.add_widget(ScreenTwo(name="screen2"))
screen_manager.add_widget(ScreenThree(name="screen3"))
screen_manager.add_widget(ScreenFour(name="screen4"))

class MainApp(MDApp):
    def build(self):
        return screen_manager

    def calc_duty(self, salar, hrs):
       salar = salar
       hrs = hrs
       
       result = round(((float(salar)/240) * float(hrs)), 2)
       result_text = " {}".format(result)
       self.show_result(result_text)
       
    def error_check(self, salar, hrs):
        self.salar = salar
        self.hrs = hrs
        if self.salar and self.hrs:
            if (self.salar.isdigit() and self.hrs.isdigit()):
                self.calc_duty(self.salar, self.hrs)
            else:
                err = "please input valid number only!"
                self.show_error(err)
        else:
            err = "please input valid number only!"
            self.show_error(err)
            
    def show_error(self, err):
        self.dialog = MDDialog(title="Error!!",
                               text=err,
                               buttons=[
                                   MDRaisedButton(
                                       text="OK", 
                                       on_release=self.close_dialog)])
        self.dialog.open()
    
    def show_result(self, result_text):
        self.dialog = MDDialog(title="potential duty pay",
                               text=result_text + " birr",
                               buttons=[
                                   MDRaisedButton(
                                       text="OK", 
                                       on_release=self.close_dialog)])
        self.dialog.open()
    
    def close_dialog(self, instance):
        self.dialog.dismiss()
        
    
if __name__ == '__main__':
    app = MainApp()
    app.run()
