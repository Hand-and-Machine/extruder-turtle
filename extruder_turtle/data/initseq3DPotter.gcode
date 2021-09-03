; 3D POTTER INITIALIZATION SEQUENCE
; for 5mm nozzle
; layer height = 3mm
; extrude rate = 3mm
M82                             ; absolute extrusion mode
G28                             ; Home all axes
G92 E0                          ; Reset Extruder
G1 E3000 F40000                 ; Prime Extruder
G92 E0
G92 E0
G92 E0
;M208 X0 Y0 Z0 S1               ; set axis minima
;M208 X415 Y405 Z500 S0         ; set axis maxima 
;G1 X207.5 Y202.5 Z20 F10000     ; Move X and Y to center, Z to 20mmhigh    
G0 F1800 X209.083 Y140.009 Z1.5 ; go to the starting position
G1 F500                         ; set the feedrate
M83                             ; Relative extrusion
G91                             ; relative coordinates for X,Y,Z axes??