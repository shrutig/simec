
SIMEC - SIMULATION OF ELECTRIC CIRCUITS

PROBLEM STATEMENT

The aim of this project was to create an application which would simulate electric circuits. It would provide the user with a GUI to create the required electric circuits and would possess the capability of solving for the various parameters like current, voltage, etc. through the various components.
It would also calculate the Thevenin’s Equivalent of a circuit and display the result.

Thus, such an application could be used as an educational tool and would be of immense help while checking for the correctness of circuits. It would be easier to build circuits in this software rather than implementing them in reality. 

The GUI would enable the user to enter the circuit components from a combination of resistors, capacitors, inductors, ac source, dc source, wires, etc. 

PLATFORM USED

python (version 2.7) was used for the development of this project and wxpython (version 2.8) for building the GUI of  software. In addition to these,  scipy and numpy was used for implementation of the matrix solving functionalities required for the various equations generated.


BASIC CONCEPTS
This software utilizes Kirchhoff’s Laws to solve the circuit entered by the user. This results in the creation of a matrix which is solved to find the currents in the various components of the circuit.

Kirchhoff’s Current Law 
This law is also known as Kirchhoff’s First Law or Kirchhoff’s Junction Law. It states according to the principle of conservation of electric charge that at any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node, or the algebraic sum of currents in a network of conductors meeting at a point is zero.


Kirchhoff’s Voltage Law
This law is also called Kirchhoff's second law and Kirchhoff's loop (mesh) rule. It states according to the principle of conservation of energy that the directed sum of the electrical potential differences (voltage) around any closed network is zero, or more simply, the sum of the emfs in any closed loop is equivalent to the sum of the potential drops in that loop.
Phase in AC Circuits
In alternating current (AC) , the movement of electric charge periodically reverses. In Direct Current(DC), on the other hand, current always flows in one direction. The usual waveform of AC is a sine curve. The frequency of AC sources may vary as well, generally 50 or 60 hertz.
An AC voltage can be described in the following form:
V=Vpeak.sin(wt),
Where Vpeak is the peak voltage,
w is the angular frequency.
t is the time.
When capacitors or inductors are present in an AC circuit, the current and voltage do not peak at the same time. The fraction of the period difference between the peaks expressed in degrees is said to be the phase difference. It is customary to use the angle by which the voltage leads the current. This leads to a positive phase for inductive current since current lags voltage and a negative phase for capacitive current since voltage lags current. 
Thus while applying the Kirchhoff’s Laws in AC circuits, the phase of the various components need to be taken into account. The voltages and current have complex components because of this phase difference.
The resistances, capacitors, inductors now possess impedance which is expressed in ohms which serves the same purpose as resistance in calculations.

Superposition Theorem
The superposition theorem for electrical circuits states that for a linear system the response (Voltage or Current) in any branch of a bilateral linear circuit having more than one independent source equals the algebraic sum of the responses caused by each independent source acting alone, while all other independent sources are replaced by their internal impedances.
To ascertain the contribution of each individual source, all of the other sources first must be "turned off" (set to zero) by replacing all other independent voltage sources with a short circuit (thereby eliminating difference of potential. i.e. V=0, internal impedance of ideal voltage source is zero).

Thevenin Equivalent
In circuit theory, Thévenin's theorem for linear electrical networks states that any combination of voltage sources, current sources, and resistors with two terminals is electrically equivalent to a single voltage source V and a single series resistor R. For single frequency AC systems the theorem can also be applied to general impedances, not just resistors.
In our software, we find Thevenin Equivalent across a resistor which is specified by the user.


TECHNICAL DETAILS

The software is built in python 2.7. The source code consists of the following files:
final_prj.py
classes.py
DCalgo.py
loop_law_modified.py
vovoltmeter.py
ACalgo_modified.py
ech.py

final_prj.py consists of the following:
class Frame:
This class contains functions which define the various functionalities included in the GUI. It contains the functions which are called corresponding to the buttons on the GUI such as OnResButton(), OnBatteryButton().
 It also contains the functions which take the input from the user corresponding to the component selected such as OnRes().
It contains the functions which allow the user to place the element in its’ appropriate place on the grid.
It contains the functions for removing an element (OnRemove()), refreshing the screen(OnRefresh()) and to submit the circuit(OnSubmit()) after it has been drawn by the user and to find theThevenin Equivalent of a circuit(OnThevenin()).
Whenever an element is entered by the user, its’ position(pos_dict[]) on the grid as well as other parameters are assigned to it and each element is stored in a stack.
def OnsubmitAC() and def OnSubmitDC() contain the code which is executed while solving the circuit.It calls the functions which apply Kirchhoff’s Laws and Superposition Theorem on the circuit.These are DCalogo.traverse(),  DCalgo.current_law(),  loop_law_modified.loop_law(),etc. In case 2 or more AC sources are present or AC sources are present in combination with DC sources, then the Superposition theorem is applied where one source remains active at a time and the circuit is solved by calling either DCalgo.py or ACalgo_modified.py. Then the individual currents are added up to give the final current through each component.
The ammeter button causes the user to be able to see the current through each element when the cursor passes over it or the element is clicked.
The equations[[]] generated at the end is solved using the functionality defined in ech.py which reduces it to  its’ echelon form..
The Thevenin Equivalent is found in the following manner.Resistor corresponding to Thevenin is found by placing a DC battery across the terminals where we need to find the Thevenin equivalent.Next , the current through this battery is found by short-circuiting all the other voltage sources. Res-thevenin is then found by dividing the voltage of the DC source by the current flowing through it.
Next,V-thevenin is found by placing a voltmeter between the 2 terminals across which thevenin equivalent is to be found and making the current passing through the 2 terminals 0.
class TextFrame:
This class is used to create a Dialog Box which will ask the user for the Bulb’s parameters
class TextFrame1:
 This class is used to create a Dialog Box which will ask the user for the AC voltage source’s parameters.

Classes.py is a file which has the parameters of all the components in the circuit and contains the following classes:
class Bulb ,
 class Resistor ,
 class Capacitor, 
class Inductor,
 class ACbattery, 
class DCbattery,
 class Voltmeter,
 class Ammeter,
class Wire.
Each of the above classes has the variables :
initial,final:The position of the element on the screen.
current,direction:The current flowing through the component and its’ direction.
type:The type of the element e.g.’RESISTOR’.
value:This stores the value of the element.e.g. if the element is an inductor ,this stores the inductance.
impedance: In case of a resistor, it is the same as its’ resistance. Impedance of a capacitor is 1/(wc) while that of an inductor is (wl).
DCalgo.py
It contains the functions:
traverse()
current_law()
loop_law()
traverse(): This is required to traverse the circuit entered by the user to check if it is complete and it is also the first step in solving the circuit for the required values of current in the various components. 
In this, the circuit is traversed by popping elements  from the list pos_dict[]. Then, the elements in a loop which share the same current are assigned their currents. If the circuit contains only DC sources , the capacitors and inductors are converted to their steady source state.The position of the nodes are stored in the list node_list[].

current_law(): In this, the control follows to the nodes which are popped from the list node_list[]. Then, Kirchhoff’s current law is applied at the nodes and the equations generated are stored in the double-dimension list equations[[]].

loop_law():In this, the Kirchhoff’s Loop Law is implemented. In this, every loop is traversed clockwise. During this traversal, any element encountered has the voltage across it calculated and pushed into the equations[[]] list in the position corresponding to the current through it. Whenever a node is encountered, all the possible paths are pushed into a list pos_list[] and one of the possible paths is taken. When the control follows to an element at the start of the particular loop, then control follows to the next element  left in the stack for a new equation. If a wrong loop or path is chosen, then that equation generated is removed from the equations[] list. Thus, in the end we are left with an equations[] list which needs to be solved for the current through the various components.

loop_lawmodified.py
This contains def on_wrong_entry() inside def loop_law(). This function is encountered if the element encountered has either current initialised to 0 (in case of a capacitor) or if an element is encountered twice. In this case, control follows to the next loop for new equations to be created.If all the elements have been traversed atleast once, the Kirchhoff’s Loop law has been successfully applied and all the equations are created.

vovoltmeter.py
This contains the required functions which executed when the potential difference between any 2 points is asked by the user. It finds a path between the 2 points and finds the potential difference from the currents through the various elements which have been already calculated.
ACalgo_modified.py
This contains the functions for finding the currents through the various components by using Kirchhoff’s Laws. It also takes into account the phase difference introduced in the currents due to the inductors and the capacitors.
def traverse(): It traverse the circuit and applies the same current to the elements which possess a common current.It also checks if the circuit is complete.In this , the circuit is traversed by popping elements from the list pos_dict[].The positions of the node is stored in the node_list[].
def current_law(): This applies Kirchhoff’s  current law at the various nodes which are popped from the node_list[].The equations thus generated possess complex values as well as the phase difference introduces a complex component and are stored in the double-dimension list equations[[]].
def loop_law():This applies Kirchhoff’s Loop Law to the circuit given and generates the required equations. In this, every loop is traversed clockwise. During this traversal, any element encountered has the voltage across it calculated and pushed into the equations[[]] list in the position corresponding to the current through it. Whenever a node is encountered, all the possible paths are pushed into a list pos_list[] and one of the possible paths is taken. When the control follows to an element at the start of the particular loop, then control follows to the next element left in the stack for a new equation. If a wrong loop or path is chosen, then that equation generated is removed from the equations[] list. Thus, in the end we are left with an equations[] list which needs to be solved for the current through the various components.
ech.py
It contains ToReducedRowEchelonForm() function which is used to reduce the matrix to its’ echelon form to reduce the number of equations.
USER MANUAL
The sotware consists of a window divided into 2 panels alongwith a status bar. The panel on the left contain the various elements which can be inserted in the circuit designed by the user. The panel on the right is the workspace in which the circuit is created by the user. 
The buttons on the right panel include the elements : resistor,capacitor,inductor,ac voltage source, dc voltage source,connecting wires and bulb.It also contains Submit,Refresh and Remove buttons.
The user is required to first build the required circuit. One of the circuit elements needs to be clicked after which it needs to be placed in the appropriate position in the grid on the right panel. The value of the selected element is required to be entered by the user as well.
 The resistor which can be used are either horizontal or vertical. Once a particular type of resistor is chosen, it needs to be placed in the desirable position on the grid. For example, if a horizontal resistor is  chosen , it needs to be placed on the grid by clicking between any 2 horizontal red dots. 
When the AC voltage source is clicked , the user is asked to enter the voltage as well as the phase difference. 
When the circuit is completed, the Submit button needs to be clicked. This solves the circuit for the current through the various components.


The voltmeter or ammeter button can be pressed after this. When the ammeter button is pressed, the current in the components over which the cursor hovers or the element clicked. The voltmeter button requires the user to specify 2 points across which the potential difference is to be calculated. These points correspond to the element’s ends and are shown by a change in the cursor shape.
The Refresh button clears the screen so that a new circuit may be drawn. The Remove button allows the user to remove a particular element by clicking on it.
The Thevenin Equivalent button allows the user to find the Thevenin Equivalent of a circuit across a resistor which is specified by the user. Then, the new circuit is displayed on the screen.
If the circuit include AC voltage source, then the current and voltage calculated may be complex. These values are displayed in the form of the max value followed by the phase angle.



FURTHER IMPROVEMENTS
This project could be further improved to include other elements in the circuit such as transistor, diode and transformer. It could also include AND, NOR, OR, NOT gates to form a logic circuit simulator.

REFERENCES

python download: http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi
wxpython download:
http://nchc.dl.sourceforge.net/project/wxpython/wxPython/2.8.12.1/wxPython2.8-win32-unicode-2.8.12.1-py27.exe
numpy download:
http://nchc.dl.sourceforge.net/project/numpy/NumPy/1.6.2/numpy-1.6.2-win32-superpack-python2.7.exe
scipy download:
http://nchc.dl.sourceforge.net/project/scipy/scipy/0.11.0b1/scipy-0.11.0b1-win32-superpack-python2.7.exe




Thank You.


            
