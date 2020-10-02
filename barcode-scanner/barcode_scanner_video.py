# USAGE
# python barcode_scanner_video.py

# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
from scipy.spatial import distance
import math 
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
help="path to output CSV file containing barcodes")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
# vs = VideoStream(src=0).start()
vs = VideoStream(0).start()
time.sleep(2.0)

# open the output CSV file for writing and initialize the set of
# barcodes found thus far
#csv = open(args["output"], "w")
#found = set()

# loop over the frames from the video stream
while True:
# grab the frame from the threaded video stream and resize it to
# have a maximum width of 400 pixels
        frame = vs.read()

        #frame = imutils.resize(frame, width=800)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # find the barcodes in the frame and decode each of the barcodes
        barcodes = pyzbar.decode(frame)
        cv2.circle(frame,(320,240),2,(0,0,255),8)
        #cv2.circle(frame,(320,240),2,(0,0,255),4)
        #loop over the detected barcodes
        for barcode in barcodes:
                # extract the bounding box location of the barcode and draw
                # the bounding box surrounding the barcode on the image
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # the barcode data is a bytes object so if we want to draw it
                # on our output image we need to convert it to a string first
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type

                if(barcodeData == 'ROBOCON VIIT'):
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        c1=int((x+x+w)/2)
                        c2=int((y+y+h)/2)
                        cv2.circle(frame,(c1,c2),2,(0,0,255),8)
                        #x_dist = int(distance.euclidean((c1,c2), (320,240)))
                        x_dist = int(320 - c1)                                  #to get signed values instead of absolute
                        cv2.putText(frame, f"distance: {x_dist}",(20,50),cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 2 ,5)
                        # draw the barcode data and barcode type on the image
                        #print(f"dtype:{type(x_dist)}, dist = {x_dist}")
                        text = "{} ({})".format(barcodeData, barcodeType)
                        cv2.putText(frame, text, (x, y - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                        # if the barcode text is currently not in our CSV file, write
                        # the timestamp + barcode to disk and update the set
                        '''if barcodeData not in found:
                        csv.write("{},{}\n".format(datetime.datetime.now(),
                                barcodeData))
                        csv.flush()
                        found.add(barcodeData)'''

        # show the output frame
        cv2.imshow("Barcode Scanner", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break

# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
#csv.close()
#vs.release()
cv2.destroyAllWindows()
vs.stop()
