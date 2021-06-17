import tkinter
from PIL import ImageTk
from PIL import Image

class Frames:
    xAxis = 0
    yAxis = 0
    MainWindow = 0
    MainObj = 0
    winFrame = object()
    btnClose = object()
    btnView = object()
    image = object()
    method = object()
    callingObj = object()
    labelImg = 0

    def __init__(self, mainObj, MainWin, wWidth, wHeight, function, Object, xAxis=10, yAxis=10):
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.MainWindow = MainWin
        self.MainObj = mainObj
        self.MainWindow.title("Tumour  Detection")
        if (self.callingObj != 0):
            self.callingObj = Object

        if (function != 0):
            self.method = function

        global winFrame
        self.winFrame = tkinter.Frame(self.MainWindow, width=wWidth, height=wHeight)
        self.winFrame['borderwidth'] = 5
        self.winFrame['relief'] = 'ridge'
        self.winFrame.place(x=xAxis, y=yAxis)

        self.btnClose = tkinter.Button(self.winFrame, text="Close", width=8,
                                      command=lambda: self.quitProgram(self.MainWindow))
        self.btnClose.place(x=1020, y=600)
        self.btnView = tkinter.Button(self.winFrame, text="View", width=8, command=lambda: self.NextWindow(self.method))
        self.btnView.place(x=900, y=600)


    def setCallObject(self, obj):
        self.callingObj = obj


    def setMethod(self, function):
        self.method = function


    def quitProgram(self, window):
        global MainWindow
        self.MainWindow.destroy()


    def getFrames(self):
        global winFrame
        return self.winFrame


    def unhide(self):
        self.winFrame.place(x=self.xAxis, y=self.yAxis)


    def hide(self):
        self.winFrame.place_forget()


    def NextWindow(self, methodToExecute):
        listWF = list(self.MainObj.listOfWinFrame)

        if (self.method == 0 or self.callingObj == 0):
            print("Calling Method or the Object from which Method is called is 0")
            return

        if (self.method != 1):
            methodToExecute()
        if (self.callingObj == self.MainObj.DT):
            img = self.MainObj.DT.getImage()
        else:
            print("Error: No specified object for getImage() function")

        jpgImg = Image.fromarray(img)
        current = 0

        for i in range(len(listWF)):
            listWF[i].hide()
            if (listWF[i] == self):
                current = i

        if (current == len(listWF) - 1):
            listWF[current].unhide()
            listWF[current].readImage(jpgImg)
            listWF[current].displayImage()
            self.btnView['state'] = 'disable'
        else:
            listWF[current + 1].unhide()
            listWF[current + 1].readImage(jpgImg)
            listWF[current + 1].displayImage()

        print("Step 22Extraction complete")
        print("\nTreatment ")
        print("\nTreatment for a brain tumor depends on the type,size and location of the tumor, as well as your overall health and your preferences")
        print("\nSurgery")
        print("\nIf the brain tumor is located in a place that makes it accessible for an operation, your surgeon will work to remove as much of the brain tumor as possible.")
              
        print("\nRadiation therapy")
        print("\nRadiation therapy uses high-energy beams, such as X-rays or protons, to kill tumor cells.")
        print("Radiation therapy can come from a machine outside your body (external beam radiation), or, in very rare cases, radiation can be placed inside your body close to your brain tumor (brachytherapy) ")
        print("\nChemotherapy")
        print("\nChemotherapy uses drugs to kill tumor cells.")
        print("\nChemotherapy drugs can be taken orally in pill form or injected into a vein (intravenously).")
        print("\nThe chemotherapy drug used most often to treat brain tumors is temozolomide (Temodar), which is taken as a pill.")
        print("\nMany other chemotherapy drugs are available and may be used depending on the type of cancer.Chemotherapy side effects depend on the type and dose of drugs you receive. Chemotherapy can cause nausea, vomiting and hair loss.Tests of your brain tumor cells can determine whether chemotherapy will be helpful for you. The type of brain tumor you have also is helpful in determining whether to recommend chemotherapy.")
        print("\nRadiosurgery")
        print("\nStereotactic radiosurgery is not a form of surgery in the traditional sense. Instead, radiosurgery uses multiple beams of radiation to give a highly focused form of radiation treatment to kill the tumor cells in a very small area.")
        print("\nEach beam of radiation isn't particularly powerful, but the point where all the beams meet — at the brain tumor — receives a very large dose of radiation to kill the tumor cells.")
        print("\nThere are different types of technology used in radiosurgery to deliver radiation to treat brain tumors, such as a Gamma Knife or linear accelerator.")
        print("\nRadiosurgery is typically done in one treatment, and in most cases you can go home the same day.")
        print("\nTargeted drug therapy")
        print("\nTargeted drug treatments focus on specific abnormalities present within cancer cells. By blocking these abnormalities, targeted drug treatments can cause cancer cells to die.Targeted therapy drugs are available for certain types of brain tumors, and many more are being studied in clinical trials. Many different forms of targeted therapy are being developed.")
        print("\nRehabilitation after treatment :")
        print("\nPhysical therapy to help you regain lost motor skills or muscle strength")
        print("\nOccupational therapy to help you get back to your normal daily activities, including work, after a brain tumor or other illness")
        print("\nSpeech therapy with specialists in speech difficulties (speech pathologists) to help if you have difficulty speaking")
        print("\nTutoring for school-age children to help kids cope with changes in their memory and thinking after a brain tumor")

        

    def removeComponent(self):
        self.btnClose.destroy()
        self.btnView.destroy()


    def readImage(self, img):
        self.image = img


    def displayImage(self):
        imgTk = self.image.resize((250, 250), Image.ANTIALIAS)
        imgTk = ImageTk.PhotoImage(image=imgTk)
        self.image = imgTk
        self.labelImg = tkinter.Label(self.winFrame, image=self.image)
        self.labelImg.place(x=700, y=150)

        
