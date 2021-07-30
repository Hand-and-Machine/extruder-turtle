 ; ############### begin header ############## 
G92 E0 ; Reset Extruder 
G28 ; Home all axes
G90 ; Absolute coordinates for X,Y,Z   
M190 S60 ; Set bed temperature and wait 
M109 S205 ; Set extruder temperature and wait 
G1 Z2.0 F3000 ; Move Z to 2mm above bed 
G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position
G1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line
G1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little
G1 X0.4 Y20 Z0.3 F1500.0 E30 ; Draw the second line
G92 E0 ; Reset Extruder
G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed 
G1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish 
G92 E0 ; Reset extruder position to zero 
G1 F300 E-3 
G1 F1000
G1 0 0 .3
; ###############  end header  ############## 

G1 X100 Y100 Z0       ; go to the starting positionG1 
F300 E3                 ; Extrude to get ready
G1 F1000			; set the feedrate
M83 					; Relative extrustion
G91                     ; relative coordinates for X,Y,Z axes

G1 F1000
G1 X50.0 Y0.0 Z0.0 E2.5
G1 X0.0 Y50.0 Z0.0 E2.5
G1 Z0.2
G1 X-0.0 Y-50.0 Z-0.0 E2.5
G1 X-50.0 Y-0.0 Z-0.0 E2.5
G1 Z0.2
G1 X50.0 Y0.0 Z0.0 E2.5
G1 X0.0 Y50.0 Z0.0 E2.5
G1 Z0.2
G1 X-0.0 Y-50.0 Z-0.0 E2.5
G1 X-50.0 Y-0.0 Z-0.0 E2.5
G1 Z0.2
G1 X50.0 Y0.0 Z0.0 E2.5
G1 X0.0 Y50.0 Z0.0 E2.5
G1 Z0.2
G1 X-0.0 Y-50.0 Z-0.0 E2.5
G1 X-50.0 Y-0.0 Z-0.0 E2.5
G1 Z0.2
G1 X50.0 Y0.0 Z0.0 E2.5
G1 X0.0 Y50.0 Z0.0 E2.5
G1 Z0.2
G1 X-0.0 Y-50.0 Z-0.0 E2.5
G1 X-50.0 Y-0.0 Z-0.0 E2.5
G1 Z0.2
G1 X50.0 Y0.0 Z0.0 E2.5
G1 X0.0 Y50.0 Z0.0 E2.5
G1 Z0.2
G1 X-0.0 Y-50.0 Z-0.0 E2.5
G1 X-50.0 Y-0.0 Z-0.0 E2.5
G1 Z0.2
G1 F300
G1 X50.0 Y5.0 Z0.0 E2.51246890528
G1 X0.0 Y5.0 Z0.0 E0.25
G4 P1000
G1 Z0.01
G1 X-45.0 Y-10.0 Z0.0 E2.30488611432
G1 X5.0 Y0.0 Z0.0 E0.25
G1 Z0.01
G1 X40.0 Y15.0 Z0.0 E2.13600093633
G1 X0.0 Y5.0 Z0.0 E0.25
G4 P1000
G1 Z0.01
G1 X-35.0 Y-20.0 Z0.0 E2.01556443707
G1 X5.0 Y0.0 Z0.0 E0.25
G1 Z0.01
G1 X30.0 Y25.0 Z0.0 E1.95256241898
G1 X0.0 Y5.0 Z0.0 E0.25
G4 P1000
G1 Z0.01
G1 X-25.0 Y-30.0 Z0.0 E1.95256241898
G1 X5.0 Y0.0 Z0.0 E0.25
G1 Z0.01
G1 X20.0 Y35.0 Z0.0 E2.01556443707
G1 X0.0 Y5.0 Z0.0 E0.25
G4 P1000
G1 Z0.01
G1 X-15.0 Y-40.0 Z0.0 E2.13600093633
G1 X5.0 Y0.0 Z0.0 E0.25
G1 Z0.01
G1 X10.0 Y45.0 Z0.0 E2.30488611432
G1 X0.0 Y5.0 Z0.0 E0.25
G4 P1000
G1 Z0.01
G1 X-5.0 Y-50.0 Z0.0 E2.51246890528
G1 X5.0 Y0.0 Z0.0 E0.25
G1 Z0.01
G1 E-3
G1 X-50.0 Y-0.0 Z-0.0
G1 E3
G1 F1000
G1 X50.0 Y0.0 Z0.0 E2.5
G1 X0.0 Y50.0 Z0.0 E2.5
G1 Z0.2
G1 X-0.0 Y-50.0 Z-0.0 E2.5
G1 X-50.0 Y-0.0 Z-0.0 E2.5
G1 Z0.2
G1 X50.0 Y0.0 Z0.0 E2.5
G1 X0.0 Y50.0 Z0.0 E2.5
G1 Z0.2
G1 X-0.0 Y-50.0 Z-0.0 E2.5
G1 X-50.0 Y-0.0 Z-0.0 E2.5
G1 Z0.2
G1 E-3
G1 X-50.0 Y-0.0 Z-0.0
G1 E3

; FINALIZATION SEQUENCE
M104 S0                 ; cool down hotend
M140 S0                 ; cool down bed
M107                    ; turn off fan
G1 Z100                 ; move extruder above print
M84                     ; disable motors

