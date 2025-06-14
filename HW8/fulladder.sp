* 1-bit Full Adder SPICE Netlist
.include tsmc18.sp

* parameters
.param Lall=0.18u
.param Wn=0.3u
.param Wp=0.8u


* Input voltage sources
va A 0 pulse(0 1.8 8n 50p 50p 8n 16n)
vb B 0 pulse(0 1.8 4.05n 50p 50p 4n 8.0n)
vcin Cin 0 pulse(0 1.8 2n 50p 50p 2n 4n)

xa va van inv
xb vb vbn inv
xc vcin vcinn inv

M1 vcin va 1 1 cmosn W={Wn} L={Lall}
M2 vcin van 1 1 cmosp W={Wp} L={Lall}

M3 1 vb s s cmosn W={Wn} L={Lall}
M4 1 vbn s s cmosp W={Wp} L={Lall}

M5 vcin van 2 2 cmosn W={Wn} L={Lall}
M6 vcin va 2 2 cmosp W={Wp} L={Lall}

M7 2 vbn s s cmosn W={Wn} L={Lall}
M8 2 vb s s cmosp W={Wp} L={Lall}

M9 vcinn van 3 3 cmosn W={Wn} L={Lall}
M10 vcinn va 3 3 cmosp W={Wp} L={Lall}

M11 3 vb s s cmosn W={Wn} L={Lall}
M12 3 vbn s s cmosp W={Wp} L={Lall}

M13 vcinn va 4 4 cmosn W={Wn} L={Lall}
M14 vcinn van 4 4 cmosp W={Wp} L={Lall}

M15 4 vbn s s cmosn W={Wn} L={Lall}
M16 vcinn vb s s cmosp W={Wp} L={Lall}

.subckt inv in out wp=0.8u wn=0.3u
m1 out in vdd vdd cmosp w='wp' l=0.2u ad='wp*0.55u' as='wp*0.55u' pd='2*(wp+0.55u)' ps='2*(wp+0.55u)'
m2 out in 0 0 cmosn w='wn' l=0.2u ad='wn*0.55u' as='wn*0.55u' pd='2*(wn+0.55u)' ps='2*(wn+0.55u)'
.ends

.control
* Analysis part
tran 1p 16n
plot v(s)
*.plot v(Cin) v(B)+2 v(A)+4 v(S)+6 v(Cout)+8
.endc
.end 