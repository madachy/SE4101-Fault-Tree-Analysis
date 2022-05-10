import pyml

lamp_circuit_fault_tree = [("Missing Indication", "and", ["Resistor Fails", "Capacitor Fails", "Both Lamps Out"]),
           ('Both Lamps Out', 'or', ['Lamp 1 Fails', 'Lamp 2 Fails', 'Lamp 3 Fails']),
           ('Resistor Fails', 'basic', []),
           ('Capacitor Fails', 'basic', []),
           ('Lamp 1 Fails', 'BASIC', []),
           ('Lamp 2 Fails', 'basic', []),
           ('Lamp 3 Fails', 'basic', []),]

pyml.fault_tree_diagram(lamp_circuit_fault_tree, filename="lamp_circuit_fault_tree", format='png')
