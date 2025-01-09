# Python Scanned Image Cropper

## Overview
Python Scanned Image Cropper is a tool designed to automate the cropping of scanned images, particularly useful for handling photos scanned as part of a larger sheet (e.g., A4 size). This program was created to simplify the process of digitizing and cropping physical photos, such as old family photographs, for safekeeping and easier access.

Many traditional scanners scan photos as part of an A4-sized image, leaving unnecessary white or black borders around the photos. Since the photos can vary in size, manual cropping can be tedious. This tool automatically detects the content area and crops the image accordingly.

## Features
- **Automatic Content Detection:** Identifies the main content of scanned images, regardless of varying photo sizes.
- **Customizable Border Cropping:** Allows you to specify the number of pixels to include around the detected content.
- **Batch Processing:** Processes all images in the input folder at once.
- **Preserves Original Names:** Saves the cropped images with their original names in the output folder.

## Prerequisites
- Python 3.x
- Required Python libraries: 
  - `opencv-python`
  - `numpy`

Install the required libraries using pip:

```bash
pip install opencv-python numpy
```

## How It Works
1. Place all your scanned images (in JPG/JPEG format) in the `input_images` folder.
2. Run the script.
3. Enter the number of border pixels to crop around the content (default is 8 pixels). This is useful for preserving a small margin around the photo if desired.
4. The cropped images will be saved in the `output_images_cropped` folder.

## Folder Structure
The program uses the following folder structure:
- `input_images`: Place your scanned images here.
- `output_images_cropped`: The cropped images will be saved here.

These folders will be created automatically if they don't already exist.

## Usage
1. Clone the repository or download the script.
2. Place your scanned images in the `input_images` folder.
3. Run the script:
   ```bash
   python scanned_image_cropper.py
   ```
4. Follow the on-screen instructions to specify the border crop size.
5. The cropped images will be saved in the `output_images_cropped` folder.

## Example
### Scenario
You have scanned old family photos using a scanner, resulting in A4-sized images with each photo surrounded by unwanted borders. This tool will:
- Detect the actual photo within each scanned image.
- Crop the photo while removing the borders.
- Save the cropped photo in the output folder.

### Input
A scanned image of an A4 sheet with a small photo in the center.

### Output
The photo, cropped to its actual size, with optional borders removed or preserved based on your input.

## Error Handling
- If no images are found in the `input_images` folder, the program will display an error message.
- If an image cannot be processed, it will be skipped, and the program will continue with the next image. A list of failed images will be displayed at the end.

## Notes
- The script uses adaptive thresholding to detect the content in scanned images.
- Gaussian blur is applied to reduce noise before detecting contours.
- This tool is designed specifically for scanned images in JPG or JPEG format.
