# Step 1: Imort reuqired libraries
import cv2
import list #?? changed
import int# ?? changed
import numpy as np 
import types

#Change to original code which didn't work 
path = r'\roisin\Steganography\Arnie.jpeg'

image = cv2.imread(path)

window_name = 'image'

cv2.imshow(window_name, image)

cv2.waitKey(0)

cv2.destroyAllWindows()


def messageToBinary(message):
    if type(message) == str:
        return ''.join([ format(ord(i), "08b") for i in message ])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [ format(i, "08b") for i in message ]
    elif type(message) == int or type(message) == np.unit8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")


# Step 3: Function to hide secret message into the image by altering the LSB(Least significant bite)

def hideData(image, secret_message):

    # Calculate the maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print("Maximun bytes to encode:", n_bytes)

    # Check if the number of bytes to encode is less than the maximum bytes in the image
    if len(secret_message) > n_bytes:
        raise ValueError("Error encountered insufficient bytes, need bigger image or less data!")

    secret_message += "#####" # You can use any string as the delimeter

    data_index = 0
    # Convert input data to binary format using messageToBinary() function
    binary_secret_msg = messageToBinary(secret_message)

    data_len = len(binary_secret_msg) # Find the lenght of data that needs to be hidden
    for values in image:
        for pixel in values:
            # Convert RGB values to binary format
            r, g, b = messageToBinary(pixel)
            # Modify the last significant bit only if there is still data to store
            if data_index < data_len:
                # Hide the data into least significant bit of red pixel
                pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1

            if data_index < data_len:
                # Hide the data into least significant bit of green pixel
                pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1

            if data_index < data_len:
                # Hide the data into least significant bit of blue pixel
                pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1

            # If data is encoded, just break out of the loop
            if data_index >= data_len:
                break

    return image


# Step 4: Define a function to decoded the hidden message from the stego image

def showData(image):
    binary_data = " "
    for values in image:
        for pixel in values:
            r, g, b = messageToBinary(pixel) # Convert the red, green and blue values into binary format
            binary_data += r[-1] # Extracting data from the least significant bit of red pixel
            binary_data += g[-1] # Extracting data from the least significant bit of green pixel
            binary_data += b[-1] # Extracting data from the least significant bit of blue pixel

    # split by 8-bits
    all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
    # Convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####": # Check if we have reached the delimeter which is "#####"
            break
    
    # Print(decoded_data)
    return decoded_data[:-5] # Remove the delimeter to show the original hidden message

    # Step 5: Function that takes the input image name and secret message as input from
    # user and calls hideDate() to encode the message

# Encode data into image
def encode_text():
    image_name = input("Enter image name(with extension):")
    image = cv2.imread(image_name) # Read the input image using OpenCV-Python.
    # It is a library of python bindings designed to solve computer vision problems.

    # Details of the image
    print("The shape of the image is:",image.shape) #check the shape of the image to calculate the number of bytes in it
    print("The original image is as shown below:")
    resized_image = cv2.resized(image, (500, 500)) # Resize the image as per your requirment
    cv2_imshow(resized_image) #display the image

    data = input("Enter data to be encoded :")
    if (len(data) == 0):
        raise ValueError('Data is empty')

    filename = input("Enter the name of new encoded image(withextension):")
    encoded_image = hideData(image, data) # Call the hideData function to hide the secret message into the selected image
    cv2_imwrite(filename, encoded_image)


# Step 6: Creat a function to ask user to enter the name of the image that needs to be decoded and 
# call the showData() function to return the decoded message.

# Decoded the data in the image
def decode_text():
    # Read the image that contains the hidden message
    image_name = input("Enter the name of the steganograph image that you wish to decode (with extention): ")
    image = cv2.imread(image_name) # Reas the image using cv2.imread()

    print("The steganograph image is as shown below:")
    resized_image = cv2.resize(image, (500, 500))  # Resize the original image as per your requirment
    cv2_imshow(resized_image) # Display the steganograph image

    text = showData(image)
    return text

    # Step 7: Main Function()

#Image steganography
def Steganography():
    a = input("Image Steganography \n 1. Encode the data \n 2. Decode the data \n Your input is: ")
    userinput = int(a)
    if (userinput == 1):
        print("\nEncoding....")
        encode_text()

    elif (userinput == 2):
        print("\nDecoding....")
        print("Decoded message is " + decoded_text())
    else:
        raise Exception("Enter correct input")

Steganography() #encoded image

