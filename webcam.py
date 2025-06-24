# Add opencv functionality to read qr codes

import streamlit as st
import cv2
import numpy as np
import webbrowser

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # Read image from camera
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Initialize QR code detector
    detector = cv2.QRCodeDetector()

    # Detect and decode webcam frames
    data, bbox, _ = detector.detectAndDecode(cv2_img)

    # Check if there is a QR code in the frame
    if data:
        a = data
        st.write("Your decoded text: " + a)

    # Open website string
    b = webbrowser.open(str(a))
