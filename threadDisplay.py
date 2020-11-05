import threading
from threading import Semaphore
import cv2
import numpy as np

class impQueue:

    def __init__(self):
        self.queue = []
        self.capacity = threading.Semaphore(10) #max 10 frames
        self.remaining = threading.Semaphore(0) #used
        self.lock = threading.Lock()

    def enqueue(self, frame):
        self.capacity.acquire()
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.remaining.release()

    def dequeue(self):
        self.remaining.acquire()
        self.lock.acquire()
        self.queue.pop(item)
        self.lock.release()
        self.capacity.release()
        return frame

#global
clipName = 'clip.mp4'
frameQueue = impQueue()
grayScaleQueue = impQueue()
    
def Extract():
    return

def GrayScaleConversion():
    return

def Display():
    return

def main():

    extractThread = threading.Thread(target = Extract)
    convertThread = threading.Thread(target = GrayScaleConversion)
    displayThread = threading.Thread(target = Display)

    extractThread.start()
    convertThread.start()
    displayThread.start()
    
if __name__ == "__main__":
    main()
