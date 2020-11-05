from threading import Thread, Semaphore
import cv2
import numpy as np

#global
clipName = 'clip.mp4'
frameQueue = impQueue()
grayScaleQueue = impQueue()

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

def Extract(Thread):
    return

def GrayscaleConversion():
    return

def Display():
    return

def main():
    extractThread = Extract()
    extractThread.start()

    grayScaleThread = GrayScaleConversion()
    grayScaleThread.start()

    displayThread = Display()
    displayThread.start()
    
if __name__ == "__main__":
    main()
