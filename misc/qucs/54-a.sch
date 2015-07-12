<Qucs Schematic 0.0.18>
<Properties>
  <View=-59,-65,696,912,1.00774,0,0>
  <Grid=10,10,1>
  <DataSet=54-a.dat>
  <DataDisplay=54-a.dpl>
  <OpenDisplay=1>
  <Script=54-a.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Title>
  <FrameText1=Drawn By:>
  <FrameText2=Date:>
  <FrameText3=Revision:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <C C 1 320 110 -26 17 0 0 "1 nF" 1 "" 0 "neutral" 0>
  <R R1 1 220 110 -26 15 0 0 "1 kOhm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
  <VProbe PrV 1 120 50 -43 -31 1 2>
  <VProbe PrC 1 320 50 28 -31 0 0>
  <GND * 1 40 220 0 0 0 0>
  <.TR TR1 1 410 100 0 52 0 0 "lin" 1 "0" 1 "1 ms" 1 "100" 0 "Trapezoidal" 0 "2" 0 "1 ns" 0 "1e-16" 0 "150" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "26.85" 0 "1e-3" 0 "1e-6" 0 "1" 0 "CroutLU" 0 "no" 0 "yes" 0 "0" 0>
  <Vrect V1 1 120 110 -26 18 0 0 "1 V" 1 "10 ns" 1 "10 ns" 1 "1 ns" 0 "1 ns" 0 "0 ns" 0>
</Components>
<Wires>
  <350 70 350 110 "" 0 0 0 "">
  <330 70 350 70 "" 0 0 0 "">
  <290 70 290 110 "" 0 0 0 "">
  <290 70 310 70 "" 0 0 0 "">
  <250 110 290 110 "" 0 0 0 "">
  <150 110 190 110 "" 0 0 0 "">
  <130 70 150 70 "" 0 0 0 "">
  <150 70 150 110 "" 0 0 0 "">
  <90 70 90 110 "" 0 0 0 "">
  <90 70 110 70 "" 0 0 0 "">
  <350 110 380 110 "" 0 0 0 "">
  <380 110 380 220 "" 0 0 0 "">
  <40 110 90 110 "" 0 0 0 "">
  <40 110 40 220 "" 0 0 0 "">
  <40 220 380 220 "" 0 0 0 "">
</Wires>
<Diagrams>
  <Rect 60 700 609 428 3 #c0c0c0 1 00 0 0 0.0001 0.001 0 -0.1 0.2 1.1 1 -1 0.2 1 315 0 225 "Zeit [s]" "Spannung [V]" "">
	<"PrC.Vt" #0000ff 0 3 0 0 0>
	<"PrV.Vt" #ff0000 0 3 0 0 0>
  </Rect>
</Diagrams>
<Paintings>
</Paintings>
