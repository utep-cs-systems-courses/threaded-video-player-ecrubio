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
        self.queue.append(frame)
        self.lock.release()
        self.remaining.release()

    def dequeue(self):
        self.remaining.acquire()
        self.lock.acquire()
        frame = self.queue.pop()
        self.lock.release()
        self.capacity.release()
        return frame

#global
clipName = 'clip.mp4'
frameQueue = impQueue()
grayScaleQueue = impQueue()
    
def Extract():

    # Initialize frame count 
    count = 0
    # open video file
    vidcap = cv2.VideoCapture(clipName)
    # read first image
    success, frame = vidcap.read()
    print(f'Reading frame {count} {success}')

    while success:
        frameQueue.enqueue(frame)
        success, frame = vidcap.read()
        print(f'Reading frame {count} {success}')
        count += 1

    frameQueue.enqueue([])

def GrayScaleConversion():

    count = 0
    while True:
        print(f'Converting frame {count}')

        colorFrame = frameQueue.dequeue()
        if colorFrame == []:
            break

        # convert the image to grayscale
        grayscaleFrame = cv2.cvtColor(colorFrame, cv2.COLOR_BGR2GRAY)
        grayScaleQueue.enqueue(grayscaleFrame)
        count += 1
    grayScaleQueue.enqueue([])

def Display():

    count = 0
    while True:
        grayFrame = grayScaleQueue.dequeue()
        if grayFrame == []:
            break

        print(f'Displaying frame {count}')        

        # display the image in a window called "video" and wait 42ms
        # before displaying the next frame
        cv2.imshow('Video', grayFrame)
        if cv2.waitKey(42) and 0xFF == ord("q"):
            break

        count += 1

    print('Finished displaying all frames')
    # cleanup the windows
    cv2.destroyAllWindows()

def main():

    extractThread = threading.Thread(target = Extract)
    convertThread = threading.Thread(target = GrayScaleConversion)
    displayThread = threading.Thread(target = Display)

    extractThread.start()
    convertThread.start()
    displayThread.start()
    
if __name__ == "__main__":
    main()
