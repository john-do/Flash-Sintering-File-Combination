# Flash-Sintering-File-Combination
User friendly version to combine flash sintering measurement files

## Use
UI used to combine the multiple files collected while taking flash sintering measurements. 

## Measurement File Expectations
* Temperature files are the .log file recorded with the NI thermocouple reader.  This file is the frame for matching the other data files because it is the most consistent data.  

* _Temperature recording must be started before and ended after all other measurments to ensure complete data_

* Current measurements and Voltage measurements files are the exported .csv or .txt files from the Agilent and  Keithly Excel plugins.
* _Both files should be in the same .csv or .txt format_

## Freeze and .exe
A .exe has been created using cx_Freeze to run on Windows 7 (Ok on Win10) without the requirement of Python
To run freeze, run setup.py
