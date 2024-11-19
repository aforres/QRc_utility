# PC_QRc_utility.py 20230829 aforres
import streamlit as st
import qrtools as qr
import numpy as np

def QRcode_generator(example_data, output_filename):

    # instantiate QRCode object
    qr = QRCode(version=1, box_size=10, border=4)
    # add data to the QR code
    qr.add_data(example_data)
    # compile the data into a QR code array
    qr.make()
    # print the image shape
    st.write("The shape of the QR image:", np.array(qr.get_matrix()).shape)
    # transfer the array into an actual image
    # img = qr.make_image(fill_color="white", back_color="black")
    img = qr.make_image(fill_color="black", back_color="white")
    # output: The shape of the QR image: (37, 37)
    img.save(output_filename)
    st.image(output_filename)
        
if __name__ == "__main__":
    st.header('Test: PC_QRc_utility ver:001 20241119')
    example_data = "https://brython.info/"
    output_filename = "./myoutput.png"
    QRcode_generator(example_data, output_filename)
    

