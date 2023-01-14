from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from numpy import size
from kivy.core.window import Window

Window.size=(350,600)


helper_string = """
ScreenManager:
    Hello:
    bye:
    admin:
    Createuser:
    Submit:
    Leave:
    AdminPage:
    Id:

<Hello>:
    name:'hello'
    md_bg_color:1,1,1,1
    MDToolbar:
        id:'MDTopAppBar'
        text_color:0,0,0,1
        title:'Welcome to Attandance App'
        left_action_items:[["menu"]]
        elevation:10
        pos_hint:{'top':1}
        md_bg_color:184/255,11/255,16/255,1

    Image:
        source:'logo.jpg'
        pos_hint:{'center_x':0.5,'center_y':0.59}
        size_hint:.60,.60

    MDLabel:
        text:'WELCOME TO'
        icon:'Android'
        pos_hint:{'center_x':.85,'center_y':.30}
        theme_text_color:'Custom'

    MDLabel:
        text:'SANJIVANI GROUP OF INSTITUTE'
        pos_hint:{'center_x':.70,'center_y':.25}
        theme_text_color:'Custom'

    MDRoundFlatButton:
        text:'LOGIN AS RECTOR'
        icon:'Android'
        user_font_size:'100sp'
        pos_hint:{'center_x':0.52,'center_y':0.14}
        md_bg_color:app.theme_cls.primary_dark
        on_release:root.manager.current = 'Admin'
    MDRoundFlatButton:
        text:'LOGIN AS STUDENT'
        user_font_size:'100sp'
        md_bg_color:app.theme_cls.primary_dark
        # size_hint:.16,.06
        pos_hint:{'center_x':0.52,'center_y':0.05}
        on_release:root.manager.current = 'Bye'

<bye>:
    name:'Bye'
    MDToolbar:
        id:'MDTopAppBar'
        title:'Welcome to Attandance App'
        left_action_items:[["menu"]]
        elevation:10
        pos_hint:{'top':1}
        md_bg_color:184/255,11/255,16/255,1
    Image:
        source:'logo.jpg'
        pos_hint:{'center_x':0.5,'center_y':0.68}
        size_hint:.50,.50
    MDTextFieldRound:
        hint_text:'Hostel'
        multiline:False
        mode:'rectangle'
        pos_hint:{'center_x':.5,'center_y':.42}
        size_hint:.40,.05
        icon_left:'home'

    MDTextFieldRound:
        hint_text:'username'
        multiline:False
        mode:'rectangle'
        pos_hint:{'center_x':.5,'center_y':.34}
        size_hint:.40,.05
        icon_left:'account'

    MDTextFieldRound:
        hint_text:'Password'
        password:True
        icon_left:'key-variant'
        icon_right:'eye-off'
        mode:'rectangle'
        pos_hint:{'center_x':.5,'center_y':.26}
        size_hint:.40,.05
    MDRoundFlatButton:
        text:'Create user'
        pos_hint:{'center_x':.47,'center_y':.11}
        size_hint:.10,.05
        on_release:root.manager.current = 'create user'
    MDRoundFlatButton:
        text:'LOGIN'
        pos_hint:{'center_x':.47,'center_y':.18}
        size_hint:.10,.05
        on_release:root.manager.current = 'attandance'

    MDRoundFlatButton:
        text:'Forgot password'
        
        pos_hint:{'center_x':.47,'center_y':.04}
        size_hint:.35,.05
    MDIconButton:
        # text:'Back'
        icon:'arrow-left'
        # user_font_size:'100sp'
        # md_bg_color:app.theme_cls.primary_dark
        pos_hint:{'center_x':.1,'center_y':.83}
        # size_hint:.08,.05
        on_release:root.manager.current = 'hello'

<admin>:
    name:'Admin'
    MDToolbar:
        id:'MDTopAppBar'
        title:'Welcome to Attandance App'
        left_action_items:[["menu"]]
        elevation:10
        pos_hint:{'top':1}
        md_bg_color:184/255,11/255,16/255,1
    Image:
        source:'logo.jpg'
        pos_hint:{'center_x':.5,'center_y':.59}
        size_hint:.60,.60

    MDTextFieldRound:
        icon_left:'home'
        hint_text:'username'
        mode:'rectangle'

        pos_hint:{'center_x':.5,'center_y':.30}
        size_hint:.36,.06
    MDTextFieldRound:
        hint_text:'password'
        password:True
        icon_left:'key-variant'
        icon_right:'eye-off'
        mode:'rectangle'
        pos_hint:{'center_x':.5,'center_y':.20}
        size_hint:.36,.06

    MDRoundFlatButton:
        text:'LOGIN'
        pos_hint:{'center_x':.45,'center_y':.10}
        size_hint:.08,.05
        on_release:root.manager.current='Adminpage'

    MDIconButton:
        # text:'Back'
        icon:'arrow-left'
        # user_font_size:'100sp'
        # md_bg_color:app.theme_cls.primary_dark
        pos_hint:{'center_x':.1,'center_y':.85}
        size_hint:.08,.05
        on_release:root.manager.current = 'hello'  
                
<AdminPage>:
    name:'Adminpage'
    MDToolbar:
        id:'MDTopAppBar'
        title:'Welcome to Attandance App'
        left_action_items:[["menu"]]
        elevation:10
        pos_hint:{'top':1}
        md_bg_color:184/255,11/255,16/255,1
    Image:
        source:'logo.jpg'
        size_hint:.60,.60
        pos_hint:{'center_x':.5,'center_y':.59} 
    MDRectangleFlatButton:
        text:'Today Attandance'
        pos_hint:{'center_x':.5,'center_y':.30}
        size_hint:.40,.06
        
    MDRectangleFlatButton:
        text:'Monthly Attandance'
        pos_hint:{'center_x':.5,'center_y':.20}
        size_hint:.40,.06
        
    MDRectangleFlatButton:
        text:'Applications of Leave'
        pos_hint:{'center_x':.5,'center_y':.10}
        size_hint:.40,.06
        
    MDIconButton:
        # text:'Back'
        icon:'arrow-left'
        # user_font_size:'100sp'
        # md_bg_color:app.theme_cls.primary_dark
        pos_hint:{'center_x':.1,'center_y':.85}
        size_hint:.08,.05
        on_release:root.manager.current = 'Admin'   
        
<Createuser>:
    name:'create user'
    MDToolbar:
        id:'MDTopAppBar'
        title:'Welcome to Attandance App'
        left_action_items:[["menu"]]
        elevation:10
        pos_hint:{'top':1}
        md_bg_color:184/255,11/255,16/255,1
    Image:
        source:'logo.jpg'
        size_hint:.50,.50
        pos_hint:{'center_x':.5,'center_y':.68}
    
    MDTextFieldRect:
        hint_text:'Name Of Student'
        multiline:False
        pos_hint:{'center_x':.50,'center_y':.43}
        size_hint:.50,.05
        
    MDTextFieldRect:
        hint_text:'Alloted Room'
        multiline:False
        pos_hint:{'center_x':.50,'center_y':.35}
        size_hint:.50,.05

    MDTextFieldRect:
        hint_text:'E-mail ID'
        multiline:False
        pos_hint:{'center_x':.50,'center_y':.27}
        size_hint:.50,.05

    MDTextFieldRect:
        hint_text:'Mobile Number'
        multiline:False
        pos_hint:{'center_x':.50,'center_y':.19}
        size_hint:.50,.05

    MDTextFieldRect:
        hint_text:'College'
        multiline:False
        pos_hint:{'center_x':.50,'center_y':.11}
        size_hint:.50,.05

    MDIconButton:
        # text:'Back'
        icon:'arrow-left'
        # user_font_size:'100sp'
        # md_bg_color:app.theme_cls.primary_dark
        pos_hint:{'center_x':.12,'center_y':.83}
        # size_hint:.08,.05
        on_release:root.manager.current = 'Bye'
    MDRectangleFlatButton:
        text:'Submit'
        pos_hint:{'center_x':.47,'center_y':.04}
        size_hint:.08,.05
        on_release:root.manager.current='id'
        
        
<Id>:
    name:'id'
    MDToolbar:
        id:'MDTopAppBar'
        title:'Welcome to Attandance App'
        left_action_items:[["menu"]]
        elevation:10
        pos_hint:{'top':1}
        md_bg_color:184/255,11/255,16/255,1
    Image:
        source:'logo.jpg'
        size_hint:.60,.60
        pos_hint:{'center_x':.5,'center_y':.59}
        
    MDTextFieldRound:
        hint_text:'username'
        icon_left:'home'
        pos_hint:{'center_x':.5,'center_y':.3}
        size_hint:.36,.06    
        
    MDTextFieldRound:
        hint_text:'Password'
        pos_hint:{'center_x':.5,'center_y':.2}
        size_hint:.36,.06   
        icon_left:'key-variant'
        icon_right:'eye-off'
    MDRectangleFlatButton:
        text:'Submit'
        icon:'Andorid'
        user_font_size:'100sp'
        md_bg_color:app.theme_cls.primary_dark
        pos_hint:{'center_x':.50,'center_y':.10}
        size_hint:.08,.05
        # on_release:root.manager.current = 'create user'    
        
    MDIconButton:
        # text:'Back'
        icon:'arrow-left'
        # user_font_size:'100sp'
        # md_bg_color:app.theme_cls.primary_dark
        pos_hint:{'center_x':.11,'center_y':.84}
        size_hint:.06,.05
        on_release:root.manager.current = 'create user'         
<Submit>:
    name:'attandance'
    MDToolbar:
        id:'MDTopAppBar'
        title:'Welcome to Attandance App'
        left_action_items:[["menu"]]
        elevation:10
        pos_hint:{'top':1}
        md_bg_color:184/255,11/255,16/255,1
    Image:
        source:'logo.jpg'
        pos_hint:{'center_x':.5,'center_y':.59}
        size_hint:.60,.60
    MDLabel:
        text:'Submit Your Attandance'
        pos_hint:{'center_x':.79,'center_y':.32}
    MDRectangleFlatButton:
        text:'Submit'
        pos_hint:{'center_x':.5,'center_y':.25}
        size_hint:.18,.06

    MDRectangleFlatButton:
        text:'Apply for Leave'
        pos_hint:{'center_x':.5,'center_y':.15}
        size_hint:.30,.06
        on_release:root.manager.current ='leave'

    MDIconButton:
        # text:'Back'
        icon:'arrow-left'
        pos_hint:{'center_x':.11,'center_y':.85}
        size_hint:.08,.05
        on_release:root.manager.current='Bye'

<Leave>:
    name:'leave'
    MDToolbar:
        id:'MDTopAppBar'
        title:'Welcome to Attandance App'
        left_action_items:[["menu"]]
        elevation:10
        pos_hint:{'top':1}
        md_bg_color:184/255,11/255,16/255,1
    Image:
        source:'logo.jpg'
        pos_hint:{'center_x':.5,'center_y':.68}
        size_hint:.50,.50

    MDTextFieldRect:
        hint_text:'From'
        multiline:False
        pos_hint:{'center_x':.5,'center_y':.4}
        size_hint:.45,.06

    MDTextFieldRect:
        hint_text:'To'
        multiline:False
        pos_hint:{'center_x':.5,'center_y':.3}
        size_hint:.45,.06

    MDTextFieldRect:
        hint_text:'Reason'
        multiline:True
        pos_hint:{'center_x':.5,'center_y':.2}
        size_hint:.45,.06

    MDRectangleFlatButton:
        text:'Submit'
        pos_hint:{'center_x':.5,'center_y':.1}
        size_hint:.10,.06

    MDIconButton:
        # background_color:0,0,1,1
        # text:'Back'
        icon:'arrow-left'
        pos_hint:{'center_x':.13,'center_y':.83}
        size_hint:.07,.05
        on_release:root.manager.current='attandance'


"""


class Hello(Screen):
    pass

class bye(Screen):
    pass

class good(Screen):
    pass

class admin(Screen):
    pass

class Createuser(Screen):
    pass

class Submit(Screen):
    pass

class Leave(Screen):
    pass

class AdminPage(Screen):
    pass

class Id(Screen):
    pass

sm = ScreenManager()

sm.add_widget(Hello(name='hello'))
sm.add_widget(bye(name='Bye'))
sm.add_widget(admin(name='Admin'))
sm.add_widget(Createuser(name='create user'))
sm.add_widget(Submit(name='attandance'))
sm.add_widget(Leave(name='leave'))
sm.add_widget(AdminPage(name='Adminpage'))
sm.add_widget(Id(name='id'))


class SanjivaniGroupOfInstitute(MDApp):
    def build(self):
        self.icon="logo.jpg"
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Red'
        screen = Screen()
        help_str = Builder.load_string(helper_string)
        screen.add_widget(help_str)
        return screen


SanjivaniGroupOfInstitute().run()