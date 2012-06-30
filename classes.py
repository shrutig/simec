from math import pi
import numpy

class Resistor:
    def __init__(self, value = 0, initial = (0,0), final = (0,0)):
        self.value = value
        self.initial = initial
        self.final = final
        self.current = [0]
        self.initial_v = 0
        self.final_v = 0
        self.type = 'RESISTOR'
        self.flag = 0
        self.impedance = value
        self.direction = (0,0)
        self.displaycurrent = [0]
    def getfinalpos(self):
        self.final = (self.initial[0]+44, self.initial[1])
        self.impedance = self.value
    def getfinalpos1(self):
        self.final = (self.initial[0], self.initial[1]+44)
        self.impedance = self.value
    def currentdirection(self, x,y):
        self.direction = (x,y)
    

class Bulb:
    def __init__(self, value = 0, initial = (0,0), final = (0,0)):
        self.value = value
        self.initial = initial
        self.final = final
        self.current = [0]
        self.initial_v = 0
        self.final_v = 0
        self.voltage = 0
        self.power = 0
        self.type = 'BULB'
        self.flag = 0
        self.direction = (0,0)
        self.access = 'NO'
        self.displaycurrent = [0]
    def getfinalpos(self):
        self.final = (self.initial[0]+44, self.initial[1])
        self.value = 1.0*self.voltage**2/self.power
        self.impedance = self.value
    def currentdirection(self, x,y):
        self.direction = (x,y)
            

class Wire:
    def __init__(self, initial = (0,0), final = (0,0)):
        self.initial = initial
        self.final = final
        self.type = 'WIRE'
        self.current = [0]
        self.flag = 0
        self.value = 0
        self.impedance = 0
        self.direction = (0,0)
        self.displaycurrent = [0]
    def currentdirection(self, x,y):
        self.direction = (x,y)

class Voltmeter:
    def __init__(self, initial = (0,0), final = (0,0)):
        self.initial = initial
        self.final = final
        self.type = 'VOLTMETER'
        self.current = [0]
        self.flag = 0
        self.value = 0
        self.impedance = 0
        self.direction = (0,0)
        self.displaycurrent = [0]
    def currentdirection(self, x,y):
        self.direction = (x,y)
        
        
class Dcbattery:
    def __init__(self, countdc = 0,EMF = 0, initial = (0,0), final = (0,0)):
        self.ID = countdc
        self.initial = initial
        self.final = final
        self.value =EMF
        self.valuer = EMF
        self.positive = (0,0)
        self.negative = (0,0)
        self.type = 'DCBATTERY'
        self.current = [0]
        self.flag = 0
        self.direction = (0,0)
        self.impedance = 0
        self.displaycurrent = [0]
    def getfinalpos(self):
        self.final = (self.initial[0]+44, self.initial[1])
        self.positive = self.initial
        self.negative = self.final
    def getfinalpos1(self):
        self.final = (self.initial[0], self.initial[1]+44)
        self.positive = self.initial
        self.negative = self.final
    def getfinalpos2(self):
        self.final = (self.initial[0]+44, self.initial[1])
        self.positive = self.final
        self.negative = self.initial
    def getfinalpos3(self):
        self.final = (self.initial[0], self.initial[1]+44)
        self.positive = self.final
        self.negative = self.initial
    def currentdirection(self, x,y):
        self.direction = (x,y)
            
        
        


class Acbattery:
    def __init__(self, countAC = 0,EMF = 0, initial = (0,0), final = (0,0)):
        self.ID = countAC
        self.initial = initial
        self.final = final
        self.value =EMF
        self.valuer = EMF
        self.type = 'ACBATTERY'
        self.current = [0]
        self.flag = 0
        self.freq = 50
        self.access = 'NO'
        self.direction = (0,0)
        self.phase = 0
        self.impedance = 0
        self.displaycurrent = [0]
    def getfinalpos(self):
        
        self.final = (self.initial[0]+44, self.initial[1])
        self.positive = self.initial
        self.negative = self.final
        x = self.phase
        print x
        print self.phase
        self.value = self.value*numpy.cos(x*pi/180) + self.value*numpy.sin(x*pi/180)*(1j)
        print self.value
    def getfinalpos1(self):
        self.final = (self.initial[0], self.initial[1]+44)
        self.positive = self.initial
        self.negative = self.final
        x = self.phase
        print x
        print self.phase
        self.value = self.value*numpy.cos(x*pi/180) + self.value*numpy.sin(x*pi/180)*(1j)
        print self.value
        print self.type
    def currentdirection(self, x,y):
        self.direction = (x,y)
        

class Capacitor:
    def __init__(self, capacitance = 0, initial =(0,0), final = (0,0)):
        
        self.initial = initial
        self.final = final
        self.value = capacitance
        self.type = 'CAPACITOR'
        self.current = [0]
        self.Xc = 0
        self.freq = 50
        self.flag = 0
        self.impedance = -1j*(self.Xc)
        self.direction = (0,0)
        self.displaycurrent = [0]
    def currentdirection(self, x,y):
        self.direction = (x,y)
    def getfinalpos(self):
        self.final = (self.initial[0]+44, self.initial[1])
        self.Xc = 1000.0/(2*pi*self.freq*self.value)
        self.impedance = -1j*(self.Xc)
    
        

class Inductor:
    def __init__(self, inductance = 0, initial =(0,0), final = (0,0)):
        self.initial = initial
        self.final = final
        self.value = inductance
        self.type = 'INDUCTOR'
        self.current = [0]
        self.Xl = 0
        self.freq = 50
        self.flag = 0
        self.impedance = 1j*(self.Xl)
        self.direction = (0,0)
        self.displaycurrent = [0]
    def getfinalpos(self):
        self.Xl = 2.0*pi*self.freq*self.value
        self.impedance = 1j*(self.Xl)
        self.final = (self.initial[0]+44, self.initial[1])
    def currentdirection(self, x,y):
        self.direction = (x,y)
   
        