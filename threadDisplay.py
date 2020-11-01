from threading import Thread, Semaphore
import cv2
import numpy as np

#global 
clipName = 'clip.mp4'
frameQueue = []
grayScaleQueue = []

def Extract():        
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
