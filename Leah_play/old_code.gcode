 ; ############### begin header ############## 
G92 E0 ; Reset Extruder 
G28 ; Home all axes
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
G90 ; Absolute positioning
M83 ; Relative extrustion
; ###############  end header  ############## 

 ; ############### begin shape ############## 
G1 F300 Z2.0 ; Move Z Axis up 2mm 
G1 F1000 X50.00 Y50.00 ; Move to starting location 
G1 F300 Z0.00 
G1 F300 E3 ; Extrude to get ready
G1 F1000 X50.000 Y0.000 Z0.000 E1.000
G1 F1000 X62.856 Y0.000 Z0.000 E1.000
G1 F1000 X82.552 Y0.000 Z0.000 E1.000
G1 F1000 X99.872 Y0.000 Z0.000 E1.000
G1 F1000 X106.713 Y0.000 Z0.000 E1.000
G1 F1000 X99.872 Y0.000 Z0.000 E1.000
G1 F1000 X82.552 Y0.000 Z0.000 E1.000
G1 F1000 X62.856 Y0.000 Z0.000 E1.000
G1 F1000 X50.000 Y0.000 Z0.000 E1.000
G1 F1000 X50.000 Y0.200 Z0.200 E0.010
G1 F1000 X50.000 Y0.200 Z0.200 E1.000
G1 F1000 X62.856 Y0.200 Z0.200 E1.000
G1 F1000 X82.552 Y0.200 Z0.200 E1.000
G1 F1000 X99.872 Y0.200 Z0.200 E1.000
G1 F1000 X106.713 Y0.200 Z0.200 E1.000
G1 F1000 X99.872 Y0.200 Z0.200 E1.000
G1 F1000 X82.552 Y0.200 Z0.200 E1.000
G1 F1000 X62.856 Y0.200 Z0.200 E1.000
G1 F1000 X50.000 Y0.200 Z0.200 E1.000
 ; ############### end shape ############## 
 ; ############### begin footer ############## 
G1 E-3 ; Extrude backwards to prevent blob 
G1 Z20.0 F300 ; Move Z axis up to 2mm above bed
G1 F9000 X0 Y0 ; Return to 0,0
M104 S0 ; Set extruder temperature to 0
M140 S0 ; Set bed temperature to 0 
 ; ############### end footer ############## 
