# Python Scanned Image Cropper
# This program is designed to crop scanned images saved as jpg/jpeg of photos, crop them and save them in a new folder.

import os
import cv2
import numpy as np

# Specify the input and output folders
input_folder = 'input_images'
output_folder = 'output_images_cropped'

# Variables to store the ANSI escape codes for text colors and styles
CFC_text_red = "\033[31m"
CFC_text_yellow = "\033[33m"
CFC_text_green = "\033[32m"
CFC_text_blue = "\033[34m"
CFC_highlight_green = "\033[42m"
CFC_highlight_white = "\033[47m"
CFC_text_bold = "\033[1m"
CFC_text_dim = "\033[2m"  
CFC_reset = "\033[0m"

def print_error(error_message):
    print(f"{CFC_text_red}{CFC_text_bold}{error_message}{CFC_reset}")

def initalise_folders():
    # Ensure both the folders exist, if they don't create them
    try:
        if not os.path.exists(input_folder):
            os.makedirs(input_folder)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
    except OSError as e:
        print_error(f"An error occurred while creating directories: {e}")

def ask_user_input():
    # Ask the user for the number of border pixels to crop around the content, default is 8
    # The reason for this is becuse some scanners may include a border around the scaned area

    print(f"Woud you like to crop the images with a border around the content?\nThis is useful if the scanned images have a border around the content, as some scanners may include a border around the scanned area.")
    while True:
        input_border_pixels = input(f"Please enter the number of border pixels to crop around the content (if left blank, the default will be 8): ")

        # Check if the user has entered a value
        if input_border_pixels == "":
            border_pixels = 8
            break
        else:
            try:
                border_pixels = int(input_border_pixels)
                if border_pixels < 0:
                    print_error("Please enter a number that is 0 or higher.")
                else:
                    break
            except ValueError:
                print_error("Please enter a valid number.")
    
    # return the border pixels
    return border_pixels

def files_in_folder(folder):
    # Get all image filenames in the input folder that are jpg or jpeg
    image_files = [f for f in os.listdir(folder) if f.endswith('.jpg') or f.endswith('.jpeg')]
    return image_files

def crop_image_with_border(image_path, border_pixels):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale for easier thresholding
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to smooth the image (to remove noise)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Use adaptive thresholding to separate the background (white) from the content
    _, thresholded = cv2.threshold(blurred, 240, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Get the bounding box of the largest contour (which should correspond to the content)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        
        # Adjust the bounding box to crop a border of 0.25 cm (8 pixels) around the content
        x = max(x - border_pixels, 0)
        y = max(y - border_pixels, 0)
        w = min(w + 2 * border_pixels, image.shape[1] - x)
        h = min(h + 2 * border_pixels, image.shape[0] - y)
        
        # Crop the image using the adjusted bounding box
        cropped_image = image[y:y+h, x:x+w]
        return cropped_image
    else:
        return None  # In case no contours are found

def main():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
    initalise_folders()

    print(f"{CFC_text_blue}{CFC_text_bold}Python Scanned Image Cropper{CFC_reset}")
    print(f"{CFC_text_dim}This program is designed to crop scanned images saved as jpg/jpeg of photos, crop them and save them in a new folder.{CFC_reset}")
    print(f"{CFC_text_dim}==================================================================================================={CFC_reset}")
    print("")

    print(f"{CFC_text_yellow}{CFC_text_bold}Step:{CFC_reset}")
    print(f"1. Place all the scanned images in the 'input_images' folder.")
    print(f"2. Input the number of border pixels to crop around the conten, if needed.")
    print(f"3. The cropped images will be saved in the 'output_images_cropped' folder as their original names.")
    print("")

    input("Press Enter to continue to step 1...")
    print("")

    print(f"{CFC_text_yellow}{CFC_text_bold}step 1{CFC_reset}")
    print(f"Place all the scanned images in the 'input_images' folder in the same directory as this program.")

    input("Press Enter to continue to step 2...")
    print("")

    print(f"{CFC_text_yellow}{CFC_text_bold}step 2{CFC_reset}")
    border_pixels = ask_user_input()

    input("Press Enter to continue to step 3...")
    print("")

    print(f"{CFC_text_yellow}{CFC_text_bold}step 3{CFC_reset}")
    input("Press Enter to start processing the images...")

    # Get all image filenames in the input folder
    image_files = files_in_folder(input_folder)

    # No images found in the input folder
    if not image_files:
        print(f"{CFC_text_red}Error: No images found in the input folder.{CFC_reset}")
        return
    
    # List holding failed images
    failed_images = []

    # Process the images
    for index, image_file in enumerate(image_files, start=1):
        # Print the processing status "i/n: image.jpg"
        print(f"{index}/{len(image_files)}: {image_file}")

        image_path = os.path.join(input_folder, image_file)
        
        # Crop the image with a border around the content
        cropped_image = crop_image_with_border(image_path, border_pixels)
        
        if cropped_image is not None:
            # Generate the output filename in the format
            output_filename = f"{image_file}"
            output_path = os.path.join(output_folder, output_filename)
            
            # Save the cropped image
            cv2.imwrite(output_path, cropped_image)
            print(f"{CFC_text_green}Cropped image saved as {output_filename}.{CFC_reset}")
        else:
            print(f"{CFC_text_red}Error: Could not crop the image.{CFC_reset}")

    print(f"\n============\n{CFC_text_green}All images have been processed.{CFC_reset}")
    if failed_images:
        print(f"{CFC_text_red}{len(failed_images)}/{len(image_files)} images could not be processed:{CFC_reset}")
        for failed_image in failed_images:
            print(failed_image)
    print(f"{CFC_text_green}{len(image_files) - len(failed_images)}/{len(image_files)} images have been successfully processed.{CFC_reset}")
              
main()