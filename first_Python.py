#convert ~Frame to Time(~min~sec)

import tkinter as tk
import math as m


frameSet = set()
window = tk.Tk()
window.title("Frame To Time")
window.geometry ("500x500")


def showFrameList():
    print("----- Frame list ------")
    for elements in frameSet:
        print(elements)

def viewResult (result) :
    text2 = tk.Label(window, text=result, name="text2")
    text2.pack_forget()
    text2.pack()
    
def frameCalc(FPS,Frame) :
    totalSecond = m.floor(int(Frame) / int(FPS))
    minute = m.floor(totalSecond / 60)
    second = totalSecond - (minute*60)
    result = str(minute) + "min" + str(second) + "sec"
    viewResult(result)
    frameSet.add(result)
    
def main ():

    explainText = tk.Label(window, text="This app is convertion Frame to Time", width=50, height=10)
    explainText.pack()

    inputFPS = tk.Entry()
    text1 = tk.Label(window, text="Input FPS")
    inputFrame = tk.Entry()
    convertButton = tk.Button(window, text="Start convert", command=lambda: frameCalc(inputFPS.get(), inputFrame.get()))
    drawFrameList = tk.Button(window, text="Show frame list", command=showFrameList)

    drawFrameList.pack()
    inputFPS.pack()
    text1.pack()
    inputFrame.pack()
    convertButton.pack()

    window.mainloop()

main()