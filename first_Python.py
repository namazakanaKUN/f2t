#convert ~Frame to Time(~min~sec)

import tkinter as tk
import math as m

frameList = []
window = tk.Tk()
window.title("Frame To Time")
window.geometry ("500x500")


def showFrameList(x):
    frameSet = set(frameList)
    print("----- Time list ------")
    for elements in frameSet:
        print(elements + "  " + str(x) + "FPS")

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
    frameList.append(result)
    
def main ():

    explainText = tk.Label(window, text="This app is convertion Frame to Time", width=50, height=10)
    explainText.pack()

    inputFPS = tk.Entry()
    text1 = tk.Label(window, text="Input FPS")
    inputFrame = tk.Entry()
    text2 = tk.Label(text="Input Frame")
    convertButton = tk.Button(window, text="Start convert", command=lambda: frameCalc(inputFPS.get(), inputFrame.get()))
    drawFrameList = tk.Button(window, text="Show time list", command=lambda :showFrameList(inputFPS.get()))

    drawFrameList.pack()
    text1.pack()
    inputFPS.pack()
    text2.pack()
    inputFrame.pack()
    convertButton.pack()

    window.mainloop()

main()