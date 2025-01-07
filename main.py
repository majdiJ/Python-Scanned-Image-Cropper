# Python Scanned Image Cropper
# This program is designed to crop scanned images saved as jpg/jpeg of photos, crop them and save them in a new folder.

import os

# Variables to store the ANSI escape codes for text colors and styles
CFC_text_red = "\033[31m"
CFC_text_yellow = "\033[33m"
CFC_text_blue = "\033[34m"
CFC_highlight_green = "\033[42m"
CFC_highlight_white = "\033[47m"
CFC_text_bold = "\033[1m"
CFC_text_dim = "\033[2m"  
CFC_reset = "\033[0m"

def print_error(error_message):
    print(f"{CFC_text_red}{CFC_text_bold}{error_message}{CFC_reset}")

def initalise_folders():
    # Specify the input and output folders
    input_folder = 'input_images'
    output_folder = 'output_images_cropped'

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
        input_border_pixels = input(f"Please enter the number of border pixels to crop around the content (default is 8): ")

        # Check if the user has entered a value
        if input_border_pixels == "":
            border_pixels = 8
        else:
            try:
                border_pixels = int(input_border_pixels)
            except ValueError:
                print_error(f"Please enter a valid number for the border pixels.")
                border_pixels = 8

main()