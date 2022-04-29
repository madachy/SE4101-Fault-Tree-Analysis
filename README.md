# SE4101-Fault-Tree-Analysis

Artifacts for fault tree analysis using PyML.  The file _fault_tree_example.py_ shows how to create a fault tree diagram.  The spreadsheets are also used to define fault trees and read into PyML using the following conventions.

![Alt text](fault tree spreadsheet example.png)

![fault tree spreadsheet example.png]

The top event must be in the first row, but all other events can be in any order.  They may be grouped by their event paths or by hierarchical levels as convenient.   Event types can be conditional "and"s, conditional "or"s, or basic events (leaves).  The following are valid designations for event types:

|Event Type | Acceptable Spellings |
|:-|:-|
|And | "And" "and" "AND" |
|Or | "Or" "or" "OR" |
|Basic | "Basic" "basic" "BASIC"
