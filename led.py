from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import ListProperty, OptionProperty, BooleanProperty, NumericProperty, StringProperty

class Led(Image):
    state = OptionProperty("off", options=["on", "off"])
    type = OptionProperty('color',options=['color','source','both'])
    color_on = ListProperty([0.22,0.79,1,1])
    color_off = ListProperty([0.05,0.175,0.225,1])
    source_on = StringProperty('')
    source_off = StringProperty('')
    auto_off=BooleanProperty(False)
    auto_off_delay=NumericProperty(0.2)
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.on_state(None,'off')
        
    def toggle_state(self):
        if self.state == 'on':
            self.state = 'off'
        else:
            self.state = 'on'
    
    def on_state(self,instance,state):
        if state=='on':
            if self.type == 'color' or self.type == 'both':
                self.color=self.color_on
            if self.type == 'source' or self.type == 'both':
                self.source=self.source_on
            if self.auto_off:
                Clock.schedule_once(lambda dt: self.set_off(),self.auto_off_delay)
        else: # state==off
            if self.type == 'source' or self.type == 'both':
                self.source=self.source_off
            if self.type == 'color' or self.type == 'both':
                self.color=self.color_off
            
    def set_off(self):
        self.state='off'
    
    def on_source_on(self,instance,src):
        if self.state == 'on' and (self.type == 'source' or self.type == 'both'):
            self.source=self.source_on
            
    def on_source_off(self,instance,src):
        if self.state == 'off' and (self.type == 'source' or self.type == 'both'):
            self.source=self.source_off
            
    def on_color_on(self,instance,clr):
        if self.state == 'on' and (self.type == 'color' or self.type == 'both'):
            self.color=self.color_on
            
    def on_color_off(self,instance,clr):
        if self.state == 'off' and (self.type == 'color' or self.type == 'both'):
            self.color=self.color_off
            
    def on_type(self, instance, tp):
        if tp == 'source':
            self.color = [1,1,1,1]
            
if __name__ == '__main__':
    from kivy.app import App
    from kivy.clock import Clock
    from kivy.lang.builder import Builder
    from kivy.uix.boxlayout import BoxLayout
    kvstr="""
BoxLayout:
    orientation: 'vertical'
    padding: 20
    Label:
        text: 'shapes'
    BoxLayout:
        orientation: 'horizontal'
        spacing: 20
        padding: 30
        Led:
            id: led_basicdisc
            source: 'shapes/basic_disc.png'
        Led:
            id: led_basicsquare
            source: 'shapes/basic_square.png'
        Led:
            id: led_basicsquarerounded
            source: 'shapes/basic_squarerounded.png'
        Led:
            id: led_contourdisc
            source: 'shapes/contour_disc.png'
        Led:
            id: led_contoursquare
            source: 'shapes/contour_square.png'
        Led:
            id: led_contoursquarerounded
            source: 'shapes/contour_squarerounded.png'
    Label:
        text: 'features'
    BoxLayout:
        orientation: 'horizontal'
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'type=color (default)'
            Led:
                id: led_typecolor
                source: 'shapes/basic_disc.png'
                color_off: [1,0,0,1]
                color_on: [0,1,0,1]
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'type=source'
            Led:
                id: led_typesource
                type: 'source'
                source_on: 'media/yes.png'
                source_off: 'media/no.png'
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'type=both'
            Led:
                id: led_typeboth
                type: 'both'
                source_on: 'shapes/basic_disc.png'
                source_off: 'shapes/basic_square.png'
                color_off: [1,0,0,1]
                color_on: [0,1,0,1]
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'auto_off=True'
            Led:
                id: led_autooff
                type: 'color'
                source: 'shapes/basic_disc.png'
                auto_off: True
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'with animated image'
            Led:
                id: led_animated
                type: 'both'
                source_on: 'media/fan.zip'
                source_off: 'media/fan.png'"""
        
    
    class LedApp(App):
        def build(self):
            Clock.schedule_interval(lambda dt: self.toggle_led(),3)
            w=Builder.load_string(kvstr)
            return w
            
        def toggle_led(self):
            for k in self.root.ids:
                if "led_" in k:
                    self.root.ids[k].toggle_state()
           
    LedApp().run()