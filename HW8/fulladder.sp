* 1-bit Full Adder SPICE Netlist
.include '45nm_HP.pm' * Include the technology file

* Supply voltage
Vdd vdd gnd 1.1

* Input voltage sources
va A 0 pulse(0 1.8 8n 50p 50p 8n 16n)
vb B 0 pulse(0 1.8 4.05n 50p 50p 4n 8.0n)
vcin Cin 0 pulse(0 1.8 2n 50p 50p 2n 4n)

* CMOS Transmission Gate based Full Adder
* Correct Shannon decomposition for Cout:
* Cout = Cin·(A·~B + ~A·B + A·B) + ~Cin·A·B
* [Your detailed circuit implementation would go here]
* This is a placeholder for the actual transistor-level implementation

* Analysis commands
.tran 1p 16n
.plot v(Cin) v(B)+2 v(A)+4 v(S)+6 v(Cout)+8
.end 