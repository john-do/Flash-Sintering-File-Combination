from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QComboBox
import sys

class SetUp(QtGui.QWidget):
    
    def __init__(self):
        super(self.__class__,self).__init__()
        ## Operating vars
        test = True
        self.delimiter = ','
        
        #Files
        self.t_file = ''
        self.v_file = ''
        self.i_file = ''
        self.save_file = ''
        
        if test == True:
            self.t_file = './test_files/T.log'
            self.v_file = './test_files/V.csv'
            self.i_file = './test_files/I.csv'
            self.save_file = './test_files/out.txt'
        
        #Vars
        self.last_location = None
        
        ##Window Properties
        self.setWindowTitle("Flash Combination")
        self.resize(300,450)
        ## Build Layout
        grid = QtGui.QGridLayout(self)
        grid.setSpacing(20)
        t_lbl = QtGui.QLabel('Temperature File', self)
        v_lbl = QtGui.QLabel('Voltage File', self)
        i_lbl = QtGui.QLabel('Current File', self)
        save_lbl = QtGui.QLabel('Save Location', self)
        delimiter_lbl = QtGui.QLabel('Delimiter', self)
        
        self.t_btn = QtGui.QPushButton('Select File',self)
        self.v_btn = QtGui.QPushButton('Select File', self)
        self.i_btn = QtGui.QPushButton('Select File', self)
        self.save_btn = QtGui.QPushButton('Select File', self)
        run_btn = QtGui.QPushButton('Run',self)
        """
        self.delimiter_select = QComboBox(self)
        #delimiter_select.addItem('')
        self.delimiter_select.addItem(",")
        self.delimiter_select.addItem("tab")
        """
        self.comma_radio = QtGui.QRadioButton("comma")
        self.comma_radio.setChecked(True)
        self.comma_radio.toggled.connect(lambda:self.delimiter_select_radio(self.comma_radio))
        
        self.tab_radio = QtGui.QRadioButton("tab")
        self.tab_radio.toggled.connect(lambda:self.delimiter_select_radio(self.tab_radio))
        
        self.radio_layout =QtGui.QVBoxLayout()
        self.radio_layout.addWidget(self.comma_radio)
        self.radio_layout.addWidget(self.tab_radio)
        
        self.progress = QtGui.QProgressBar(self)
        
        grid.addWidget(t_lbl, 0,0)
        grid.addWidget(self.t_btn,0,1)
        grid.addWidget(v_lbl, 1,0)
        grid.addWidget(self.v_btn,1,1)
        grid.addWidget(i_lbl,2,0)
        grid.addWidget(self.i_btn,2,1)
        grid.addWidget(delimiter_lbl,3,0)
        #grid.addWidget(self.delimiter_select,)
        grid.addLayout(self.radio_layout,3,1)
        grid.addWidget(save_lbl,4,0)
        grid.addWidget(self.save_btn,4,1)
        grid.addWidget(self.progress,5,0,1,2)
        grid.addWidget(run_btn,6,1)
        
        self.setLayout(grid)
            
        ## Build Connections:
        self.t_btn.clicked.connect(self.get_tfile)
        self.v_btn.clicked.connect(self.get_vfile)
        self.i_btn.clicked.connect(self.get_ifile)
        #self.delimiter_select.activated[str].connect(self.delimiter_select_set)
        self.save_btn.clicked.connect(self.get_outfile)
        run_btn.clicked.connect(self.run_matching)
    
    def get_tfile(self):
        self.t_file = QtGui.QFileDialog.getOpenFileName(self,'Open File', ""," (*.txt *.csv *.log)")
        self.t_btn.setText('Done')
    
    def get_vfile(self):
        self.v_file = QtGui.QFileDialog.getOpenFileName(self,'Open File', ""," (*.txt *.csv *.log)")
        self.v_btn.setText('Done')
        
    def get_ifile(self):
        self.i_file = QtGui.QFileDialog.getOpenFileName(self,'Open File', ""," (*.txt *.csv *.log)")
        self.i_btn.setText('Done')
    
    def get_outfile(self):
        self.save_file = QtGui.QFileDialog.getSaveFileName(self)
        self.save_btn.setText('Done')
        
    def delimiter_select_set(self, text):
        print(text)
        
        if text == ",":
            self.delimiter = ","
            
        elif text == "tab":
            self.delimiter = "\t"
        #print('delimiter set as ', self.delimiter)
    
    def delimiter_select_radio(self, b):
        if b.text() == 'tab':
            self.delimiter = "\t"
            print(self.delimiter)
        elif b.text() =='comma':
            self.delimiter = ","
            print(self.delimiter)
    def run_matching(self):
        #print('Matching!')
        #print(self.t_file)
        #print(self.v_file)
        #print(self.i_file)
        #print(self.save_file)
        #self.delimiter = str(self.delimiter_select.currentText())
        print(self.delimiter)
        
        if self.t_file and self.v_file and self.i_file and self.save_file:
            
            ##Get values for progress bar
            f =open(self.t_file,'r',encoding='utf-8')
            progress_length = sum(1 for line in f)
            #print(progress_length)
            f.close() 
            
            
            ## Open Files
            tFile = open(self.t_file,'r',encoding='utf-8')
            vFile = open(self.v_file,'r',encoding='utf-8')
            iFile = open(self.i_file,'r',encoding='utf-8')
            outFile = open(self.save_file,'w',encoding='utf-8')

            tline = tFile.read().split("\n")
            iline   = iFile.read().split("\n")
            vline = vFile.read().split("\n")


            #print data
            frow = 0    #Count in temperature file
            lastv=0		#line where last measurement was taken from the voltage file 
            lasti= 0 	#line where last measurement was taken from the current file 

            for line in tline:
                frow=frow+1
                vrow = 0
                irow = 0
        
                if frow < 9:
                    pass  #skip header, 8 lines
                elif frow == 9:
                    #Hack to write header line 
                    outFile.write("Time\tTemperature [C]\tVoltage [V]\tCurrent [A]\n")
                else:
                    V= "" # V and I are given empty spaces if not found for that time
                    I= ""
                    t = line.split()[0]
                    T = line.split()[1]

                    ct = 0 # last row counter
                    for vrow in vline:
                        ct = ct +1 
                        if ct-1 < lastv:
                            pass
                        elif vrow.split(self.delimiter)[0][:8] == t:
                        
                            V = vrow.split(self.delimiter)[1]
                            lastv= ct
                            break
                        else:
                            pass
                        
                    ct = 0	# last row counter
                    
                    for irow in iline:
                        ct = ct +1 
                        if ct-1 < lasti:
                            pass
                        elif irow.split(self.delimiter)[0][:8] == t:

                            I = irow.split(self.delimiter)[1]
                            lasti= ct
                            break
                        else:
                            pass
                    #print(    "%s\t%s\t%s\t%s\n" % (t, T, V, I))
                    
                    outFile.write("%s\t%s\t%s\t%s\n" % (t, T, V, I))
                
                completed = frow/progress_length*100
                self.progress.setValue(completed)

            #Close files
            tFile.close()
            iFile.close()
            vFile.close()
            outFile.close()
        
        else:
            QtGui.QMessageBox.critical(self, "File Selection",
                                           "One or more files is missing",
                                       QtGui.QMessageBox.Ok)

            
def main():
    app = QtGui.QApplication(sys.argv)
    form = SetUp()
    form.show()
    sys.exit(app.exec_())
    
    

if __name__ == '__main__':
    main()
