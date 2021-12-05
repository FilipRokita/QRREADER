#QRREADER
#Filip Rokita
#www.filiprokita.com

import cv2
import sys

if sys.argv[1:]:
    decoded = cv2.QRCodeDetector().detectAndDecode(cv2.imread(sys.argv[1]))
    print("aaa")
else:
    print("\n")
    print("USAGE: python3 QRREADER.py (filename)")
    print("\n")