# AsiAir Bugfix for DSLR Image Size Bug in v2.1.4
With the latest update of the AsiAir images created with DSLR are saved in a different resolution which leads to processing errors in some stacking software.

Image resolution differs by 1 pixel in the width, so the easiest way to solve this is by resizing the older, bigger images to the new resolution by removing the rightmost column of pixels 

## Usage
1. **Download Script**: Save the provided script file in any folder on your computer.


2. **Set File Permissions**:
Ensure the script file has permission to execute. You can do this by right-clicking on the file, selecting "Properties," and under the "Permissions" tab, checking the box that allows executing the file as a program.


3. **Organize Images**:
Place the images you need to resize in a separate folder on your computer. It's important to keep these images separate because the script will resize every image in the folder.


4. **Run the Script**:
Double-click the script file to run it. Alternatively, open a terminal, navigate to the folder where the script is located, and execute it.


5. **Provide Folder Path**:
The script will prompt you to paste the absolute path to the folder containing the images you want to resize. Paste the path and hit enter.


6. **Wait for Completion**:
The script will automatically resize all the images in the specified folder. Depending on the number of images and their sizes, this may take some time. Please be patient and wait for the process to complete.


7. **Repeat if Necessary**:
After the script finishes resizing the images, you'll be asked if you want to resize another batch of images. If you have more images to resize, follow steps 3 to 6 again. Otherwise, you can close the terminal or exit the script.