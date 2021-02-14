.title JUST_FOR_TEST

Vin in 0 DC 1
V1 vp1 0 DC 1
V2 0 vp2 DC 1
CL out 0 1p 
MNM1 in vp1 out vp2 n18 W=1u L=200n
MNM2 out vp2 vin vp1 p18 W=1u L=200n

.op
.dc Vin -4 4 0.1
.probe dc v(out) i(out)

.temp 27
.option post accurate probe
.lib '.\models\ms018.lib' tt

.end

