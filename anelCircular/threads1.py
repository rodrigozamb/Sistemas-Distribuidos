#!/usr/bin/python

import threading
import time

ActiveThread = 0
TotalThreads = 30
globalstring = "Hello Word"

strings = [
    "I have brought peace, freedom, justice, and security to my new empire. Your new empire? Don´t make me kill you.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque quis libero eget nisi condimentum dictum."
]

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter


    def run(self):
        self.executeTask(self.name)


    def executeTask(self,threadName):
        global ActiveThread
        global TotalThreads
        global globalstring

        while True:

            if self.checkCompleteTask():
                break


            if ActiveThread == self.threadID:
                # Se é a vez dessa thread fazer a tarefa, ela executará
                for i in range(0,len(globalstring)):
                    if globalstring[i].islower():
                        if i != 0 and i != (len(globalstring)-1):
                            globalstring = globalstring[0:i:]+globalstring[i].upper()+globalstring[i+1::]
                        elif i == 0:
                            globalstring = globalstring[0].upper()+globalstring[1::]
                        else:
                            globalstring = globalstring[:len(globalstring)-1:]+globalstring[i].upper()
                        print("thread "+str(self.threadID)+" modificou : ")
                        print(globalstring)
                        print()
                        time.sleep(1)
                        ActiveThread = (ActiveThread+1) % TotalThreads
                        break


    def checkCompleteTask(self):
        global globalstring
        for i in globalstring:
            if i.islower():
                return False
        return True

# Create new threads
thread0 = myThread(0, "Thread-0", 0)
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)
thread4 = myThread(4, "Thread-4", 4)
thread5 = myThread(5, "Thread-5", 5)
thread6 = myThread(6, "Thread-6", 6)
thread7 = myThread(7, "Thread-7", 7)
thread8 = myThread(8, "Thread-8", 8)
thread9 = myThread(9, "Thread-9", 9)
thread10 = myThread(10, "Thread-10", 10)
thread11 = myThread(11, "Thread-11", 11)
thread12 = myThread(12, "Thread-12", 12)
thread13 = myThread(13, "Thread-13", 13)
thread14 = myThread(14, "Thread-14", 14)
thread15 = myThread(15, "Thread-15", 15)
thread16 = myThread(16, "Thread-16", 16)
thread17 = myThread(17, "Thread-17", 17)
thread18 = myThread(18, "Thread-18", 18)
thread19 = myThread(19, "Thread-19", 19)
thread20 = myThread(20, "Thread-20", 20)
thread21 = myThread(21, "Thread-21", 21)
thread22 = myThread(22, "Thread-22", 22)
thread23 = myThread(23, "Thread-23", 23)
thread24 = myThread(24, "Thread-24", 24)
thread25 = myThread(25, "Thread-25", 25)
thread26 = myThread(26, "Thread-26", 26)
thread27 = myThread(27, "Thread-27", 27)
thread28 = myThread(28, "Thread-28", 28)
thread29 = myThread(29, "Thread-29", 29)

globalstring = strings[0]

# Start new Threads

thread0.start()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()
thread15.start()
thread16.start()
thread17.start()
thread18.start()
thread19.start()
thread20.start()
thread21.start()
thread22.start()
thread23.start()
thread24.start()
thread25.start()
thread26.start()
thread27.start()
thread28.start()
thread29.start()

while True:
    if thread0.is_alive() == False:
        time.sleep(1)
        print("String foi completamente transformada : ")
        print(globalstring)
        break