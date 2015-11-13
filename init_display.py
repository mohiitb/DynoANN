from headers import *


class TabPanel(wx.Panel):
    
    '''Declare Variables here'''
    filename="No file selected"
    
    setSlider, hiddenLayers, hiddenNeuron, maxError, activationFunc, biasCB, filenamelabel, trainingRate, momentumRate, maxIterations, normalizeData = (None,)*11
    gsetSlider, ghiddenLayers, ghiddenNeuron, gmaxError, gactivationFunc, gbiasCB, gfilenamelabel, gtrainingRate, gmomentumRate, gmaxIterations, gnormalizeData = (None,)*11
    raisedError 		= None
    graisedError 		= "None"
    transportData 		= []
    trainingInputData   = []
    trainingTargetData  = []
    testingInputData    = []
    testingTargetData   = []
    
    mlpNetwork = None
    hLayers = []
    
    # initialize the display
    def __init__(self, parent, option):
        
        self.dirname = ""
        self.parenting = parent
        
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        
        # in sizer 11
        self.filenamelabel  = wx.StaticText(self, 0, label=self.filename, size=(250, 18))
        self.filenamelabel.SetFont(font)
        uploadButton        = wx.Button(self, 1, "Upload")
        ratioLabel  		= wx.StaticText(self, 0, label="TrainingSet : TestingSet Ratio", size=(250, 18))
        self.setSlider 		= wx.Slider(self, -1, minValue=50, maxValue=100, size=(250, -1),style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        self.setSlider.SetTickFreq(5, 1)
        
        # in sizer 12
        hiddenLayerslabel   = wx.StaticText(self, 0, 'No. of Hidden Layers: ', size=(250,18))
        self.hiddenLayers   = wx.SpinCtrl(self, wx.ID_ANY, "Hidden Layers", min=0, max=50)
        hiddenNeuronlabel   = wx.StaticText(self, 0, 'No. of neurons in each Hidden Layer: ', size=(250,18))
        self.hiddenNeuron   = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=512)
        
        # in sizer 13
        maxErrorlabel       = wx.StaticText(self, 0, 'Maximum Error allowed: ', size=(250,18))
        self.maxError       = wx.TextCtrl(self, wx.ID_ANY, "")
        maxIterationsLabel  = wx.StaticText(self, 0, 'Maximum Iterations allowed: ', size=(250,18))
        self.maxIterations 	= wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=1000000)
        
        # in sizer 14
        biasLabel           = wx.StaticText(self, 0, 'You want bias or not? ', size=(250,18))
        self.biasCB         = wx.ComboBox(self, wx.ID_ANY, choices=["Yes","No"])
        activationFunclabel = wx.StaticText(self, 0, 'Activation Function: ', size=(250,18))
        self.activationFunc = wx.ComboBox(self, wx.ID_ANY, choices=["Sigmoid","Softmax","Tanh"])
        
        # in sizer 15
        trainingRateLabel   = wx.StaticText(self, 0, 'Training Rate: ', size=(250,18))
        self.trainingRate   = wx.TextCtrl(self, wx.ID_ANY, "")
        momentumRateLable   = wx.StaticText(self, 0, 'Momentum Rate: ', size=(250,18))
        self.momentumRate   = wx.TextCtrl(self, wx.ID_ANY, "")
        
        # in sizer 16
        normalizeDataLabel  = wx.StaticText(self, 0, 'Normalize Data? ', size=(250,18))
        self.normalizeData 	= wx.ComboBox(self, wx.ID_ANY, choices=["Yes","No"])
        compareButton       = wx.Button(self, 2, "Start Network")
        resetButton         = wx.Button(self, 3, "Reset")
        
        # in sizer 17
        self.raisedError  	= wx.StaticText(self, 0, " Error Raise: None", size=(250,18))

        sizer1  = wx.BoxSizer(wx.VERTICAL)
        sizer11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer17 = wx.BoxSizer(wx.HORIZONTAL)
        
        sizer11.Add(self.filenamelabel, wx.ALL, 5)
        sizer11.Add(uploadButton, wx.ALL, 5)
        sizer11.AddSpacer(40)
        sizer11.Add(ratioLabel, wx.ALL, 5)
        sizer11.Add(self.setSlider, wx.ALL, 5)

        sizer12.Add(hiddenLayerslabel, wx.ALL, 5)
        sizer12.Add(self.hiddenLayers, wx.ALL, 5)
        sizer12.AddSpacer(40)
        sizer12.Add(hiddenNeuronlabel, wx.ALL, 5)
        sizer12.Add(self.hiddenNeuron, wx.ALL, 5)

        sizer13.Add(maxErrorlabel, wx.ALL, 5)
        sizer13.Add(self.maxError, wx.ALL, 5)
        sizer13.AddSpacer(40)
        sizer13.Add(maxIterationsLabel, wx.ALL, 5)
        sizer13.Add(self.maxIterations, wx.ALL, 5)
        
        sizer14.Add(biasLabel, wx.ALL, 5)
        sizer14.Add(self.biasCB, wx.ALL, 5)
        sizer14.AddSpacer(40)
        sizer14.Add(activationFunclabel, wx.ALL, 5)
        sizer14.Add(self.activationFunc, wx.ALL, 5)


        sizer15.Add(trainingRateLabel, wx.ALL, 5)
        sizer15.Add(self.trainingRate, wx.ALL, 5)
        sizer15.AddSpacer(40)
        sizer15.Add(momentumRateLable, wx.ALL, 5)
        sizer15.Add(self.momentumRate, wx.ALL, 5)

        sizer16.Add(normalizeDataLabel, wx.ALL, 5)
        sizer16.Add(self.normalizeData, wx.ALL, 5)
        sizer16.AddSpacer(40)
        sizer16.Add(compareButton, wx.ALL, 5)
        sizer16.Add(resetButton, wx.ALL, 5)

        sizer17.Add(self.raisedError, wx.ALL, 50)

        sizer1.Add(sizer11, 0, wx.ALL, 5)
        sizer1.Add(sizer12, 0, wx.ALL, 5)
        sizer1.Add(sizer13, 0, wx.ALL, 5)
        sizer1.Add(sizer14, 0, wx.ALL, 5)
        sizer1.Add(sizer15, 0, wx.ALL, 5)
        sizer1.Add(sizer16, 0, wx.ALL, 5)
        sizer1.Add(sizer17, 0, wx.ALL, 5)

        self.Bind(wx.EVT_BUTTON, self.UploadData, id=1)
        self.Bind(wx.EVT_BUTTON, self.Comparisons, id=2)
        self.Bind(wx.EVT_BUTTON, self.ResetButton, id=3)
        self.SetSizer(sizer1)

        # initialize the parameters
        self.initParameters()

    def initParameters(self):
        # initialize each parameter as following:
		self.filenamelabel.SetLabel("No file selected")
		font = wx.Font(10, wx.DECORATIVE, wx.BOLD, wx.NORMAL)
		self.filenamelabel.SetFont(font)
		self.setSlider.SetValue(50)
		self.hiddenLayers.SetValue(0)
		self.hiddenNeuron.SetValue(0)
		self.maxError.SetValue("1e-6")
		self.maxIterations.SetValue(1000000000)
		self.biasCB.SetValue("No")
		self.activationFunc.SetValue("Sigmoid")
		self.trainingRate.SetValue("0.3")
		self.momentumRate.SetValue("0.9")
		self.normalizeData.SetValue("No")
		self.raisedError.SetLabel("Error Raised:	None")
		self.raisedError.SetForegroundColour((0,0,255))

    def UploadData(self, e):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "","*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            try:
                self.readFile(os.path.join(dlg.GetDirectory(), dlg.GetFilename()))
                self.filenamelabel.SetLabel(dlg.GetFilename()+" Successfully Uploaded")
                self.filename = dlg.GetFilename()+" Successfully Uploaded"
                font = wx.Font(10, wx.DECORATIVE, wx.BOLD, wx.NORMAL)
                self.filenamelabel.SetFont(font)
            except:
                self.filenamelabel.SetLabel("File not uploaded")
                font = wx.Font(10, wx.DECORATIVE, wx.BOLD, wx.NORMAL)
                self.filenamelabel.SetFont(font)

    def Comparisons(self, e):
        try:
	        self.gfilename       = self.filename
	        self.gsetSlider 	 = int(self.setSlider.GetValue())
	        self.gHiddenlayers   = int(self.hiddenLayers.GetValue())
	        self.gHiddenneurons  = int(self.hiddenNeuron.GetValue())
	        self.gmaxError       = float(self.maxError.GetValue())
	        self.gmaxIterations  = int(self.maxIterations.GetValue())
	        if self.biasCB.GetValue()=="Yes":
	            self.gbiasCB     = True
	        else:
	            self.gbiasCB     = False
	        self.gactivationFunc = self.activationFunc.GetValue()
        
	        self.gtrainingRate   = float(self.trainingRate.GetValue())
	        self.gmomentumRate   = float(self.momentumRate.GetValue())
	    	self.gnormalizeData  = self.normalizeData.GetValue()
	        # format the input data
	        self.setData()
	        # create the MPL Network
	        self.createNetwork()
        except:
    		self.raisedError.SetLabel("Error Raised:\t\t\t\t\t\t\t   " + str(sys.exc_info()[0]))
    		self.raisedError.SetForegroundColour((255,0,0))
        
    # reset the parameters    
    def ResetButton(self, e):
        self.initParameters()

    # read the input file
    def readFile(self, nameFile):
        self.transportData = []
        with open(nameFile, 'r') as csvfile:
		    alldata = csv.reader(csvfile)
		    for row in alldata:
		        self.transportData.append(map(float,row))

    # separate data into input & target parts and normalize the data
    def setData(self):
    	ratio = int(self.setSlider.GetValue())
    	ratio = int(float(ratio)/100*len(self.transportData))
        self.transportData  = np.array(self.transportData)
        trainingData   = self.transportData[:ratio+1]
        testingData    = self.transportData[ratio+1:]
        cols = []
        for i in range(len(trainingData[0])-1):
        	cols.append(i)
        
        if self.gnormalizeData == "No":
	        self.trainingInputData 	= trainingData[:,cols]
	        self.trainingTargetData = trainingData[:,len(trainingData[0])-1]
	        self.testingInputData   = testingData[:,cols]
	        self.testingTargetData  = testingData[:,len(testingData[0])-1]
        else:
        	self.trainingInputData 	= preprocessing.scale(trainingData[:,cols])
	        self.trainingTargetData = preprocessing.scale(trainingData[:,len(trainingData[0])-1])
	        self.testingInputData   = preprocessing.scale(testingData[:,cols])
	        self.testingTargetData  = preprocessing.scale(testingData[:,len(testingData[0])-1])

    # create network here
    def createNetwork(self):
        # create network
        self.mlpNetwork     = FeedForwardNetwork()
        if self.gactivationFunc == "Sigmoid":
            self.inputLayer      = SigmoidLayer(len(self.testingInputData[0]))
            self.outputLayer     = SigmoidLayer(1)
            for i in range(self.gHiddenlayers):
                self.hLayers.append(SigmoidLayer(self.gHiddenneurons))

        elif self.gactivationFunc == "Softmax":
            self.inputLayer      = SoftmaxLayer(len(self.testingInputData[0]))
            self.outputLayer     = SoftmaxLayer(1)
            for i in range(self.gHiddenlayers):
                self.hLayers.append(SoftmaxLayer(self.gHiddenneurons))

        elif self.gactivationFunc == "Tanh":
        	print self.gactivationFunc
        	self.inputLayer      = TanhLayer(len(self.testingInputData[0]))
        	self.outputLayer     = TanhLayer(1)
        	for i in range(self.gHiddenlayers):
				self.hLayers.append(TanhLayer(self.gHiddenneurons))
        # add modules
        self.mlpNetwork.addInputModule(self.inputLayer)
        self.mlpNetwork.addOutputModule(self.outputLayer)
        for i in range(self.gHiddenlayers):
	            self.mlpNetwork.addModule(self.hLayers[i])
        if self.gHiddenlayers == 0:
			self.mlpNetwork.addConnection(FullConnection(self.inputLayer, self.outputLayer))
        else:
	        # create connections
            self.mlpNetwork.addConnection(FullConnection(self.inputLayer, self.hLayers[0]))
            for i in range(self.gHiddenlayers-1):
            	self.mlpNetwork.addConnection(FullConnection(self.hLayers[i], self.hLayers[i+1]))
            self.mlpNetwork.addConnection(FullConnection(self.hLayers[self.gHiddenlayers-1], self.outputLayer))	
            if self.gbiasCB == True:
                bias = BiasUnit('bias')
                self.mlpNetwork.addModule(bias)
		    	# add bias to all hidden layers
                for i in range(self.gHiddenlayers):
					self.mlpNetwork.addConnection(FullConnection(bias, self.hLayers[i]))
                self.mlpNetwork.addConnection(FullConnection(bias, self.outputLayer))
        self.mlpNetwork.sortModules()
        self.createDataset()
	    	
    def createDataset(self):
    	ds = SupervisedDataSet(len(self.trainingInputData[0]),1)
    	# add samples
    	for i in range(len(self.trainingTargetData)):
    		ds.addSample(tuple(self.trainingInputData[i]), (self.trainingTargetData[i],))
    	if self.gtrainingRate==0:
    		self.gtrainingRate = 0.3
    	trainer = BackpropTrainer(self.mlpNetwork, ds, learningrate= self.gtrainingRate, momentum=self.gmomentumRate)
    	if self.gmaxError==0 and self.gmaxIterations==0:
    		trainer.trainUntilConvergence()	
    	else:
    		sTime = time.time()
    		for i in range(self.gmaxIterations):
    			if i%10==9:
    				print float(i)*100 /self.gmaxIterations,"% completed", time.time()-sTime
    			trainer.trainEpochs(1)	
        errSum = 0.0
        for i in range(len(self.testingInputData)):
        	    output = self.mlpNetwork.activate(self.testingInputData[i])
        	    errSum+=(output-self.testingTargetData[i])**2
        print "Accuracy: " + str(errSum/len(self.testingInputData))	    
class NotebookApp(wx.Notebook):

    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style= wx.BK_DEFAULT)
 
        # Create the tab and add it to the notebook
        onlyTab = TabPanel(self, 1)
        self.AddPage(onlyTab, "Artificial Neural Networks Implementation")

 
 
class AppFrame(wx.Frame):

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY,"ANN Implementation Comparisons",size=(600,400))
        panel = wx.Panel(self)
 
        notebook = NotebookApp(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 10)
        panel.SetSizer(sizer)
        self.Layout()
        self.Show()

def main():
    app = wx.PySimpleApp()
    frame = AppFrame()
    app.MainLoop()    

if __name__ == '__main__':
    main()
    
