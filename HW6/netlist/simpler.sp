inverter transient response
.incl tsmc18.sp
.global vdd 
.param WDR=1u

vdd vdd 0 dc 1.8
vin in 0 pulse 0 1.8 1n 50p 50p 2n
x1 in out inv wp='2.3*WDR' wn='WDR'
cl out 0 10p

.control
*destroy all
*dc vin 0 1.8 1m
*plot v(in) v(out)
*meas dc VTH when v(out)=0.9
	
tran 0.1p 5n
plot v(in) v(out) ylimit 0 2
meas tran tphl TRIG v(in) VAL=0.9 RISE=1 TARG v(out) VAL=0.9 FALL=1
meas tran tplh TRIG v(in) VAL=0.9 FALL=1 TARG v(out) VAL=0.9 RISE=1
let delay = (tphl+tplh)/2
print delay

let pdd=-i(vdd)*v(vdd)
plot pdd
meas tran edd INTEG pdd from=0 to=5n
let eqn331=100f*1.8*1.8
print eqn331

.endc
	

.subckt inv in out wp=0.3u wn=0.3u
m1 out in vdd vdd cmosp w='wp' l=0.2u ad='wp*0.55u' as='wp*0.55u' pd='2*(wp+0.55u)' ps='2*(wp+0.55u)'
m2 out in 0 0 cmosn w='wn' l=0.2u ad='wn*0.55u' as='wn*0.55u' pd='2*(wn+0.55u)' ps='2*(wn+0.55u)'
.ends
.end