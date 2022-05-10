# SE4101-Fault-Tree-Analysis

This repository contains resources for fault tree analysis using [PyML](https://github.com/madachy/PyML).  The file _fault_tree_example.py_ shows an example creation of a fault tree diagram for the lamp circuit fault tree example shown below.  

## Spreadsheet Instructions
A fault tree can be defined in a spreadsheet and then read with PyML for analysis and visualization. The top event must be in the first row, but all other events can be in any order.  They may be grouped by their event paths or by hierarchical levels as convenient.   Event types can be conditional "and"s, conditional "or"s, or basic events (leaves).  The following are valid designations for event types:

|Event Type | Acceptable Spellings |
|:-|:-|
|And | "And" "and" "AND" |
|Or | "Or" "or" "OR" |
|Basic | "Basic" "basic" "BASIC"

## Spreadsheet Instructions
The template provided can be modified.


The example fault tree below is specified using the provided template file 'fault tree example.xls' shown underneath.

![lamp_circuit_fault_tree](lamp_circuit_fault_tree.png)



The spreadsheets are also used to define fault trees and read into PyML using the following conventions.

![fault tree example](fault%20tree%20example.png)


