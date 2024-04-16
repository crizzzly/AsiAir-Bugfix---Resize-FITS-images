#!/usr/bin/env python3.11
# Workaround for AsiAir FITS files changing image sizes during latest update.
# script reads images in pasted folder and removes the last row.
# Saves images as copy
# Christina Rost 15.04.2024
# https://github.com/crizzzly

from astropy.io import fits
import os

path = os.path.dirname(os.path.dirname(__file__))

print("remove column in multiple fits files.")
# TODO: offer to remove first or last row


def resize_files():
    print("paste directory with fits file: ")
    working_directory = input()
    dir_path = working_directory
    os.chdir(working_directory)
    print(f"Working directory: {working_directory} ")

    # Loop through all files in the directory
    for filename in os.listdir(dir_path):
        if filename.endswith(".fit"):
            # Open the FITS file

            try:
                with fits.open(filename) as hdul:
                    # Access the data and header
                    data = hdul[0].data
                    header = hdul[0].header

                    # Remove the last row from the data
                    modified_data = data[:-1, :]
            except OSError as e:
                print(f"Error reading file {filename}: {e}")
            else:

                # Update the header to reflect the new size
                header['NAXIS2'] = modified_data.shape[0]

                # new_name = filename.split(".")[0] + "_s.fit"
                # Write the modified data and header to a new FITS file
                fits.writeto("s_"+filename, modified_data, header, overwrite=True)


    print("resize more files? (y/n)")
    answer = input()
    if answer == "y":
        resize_files()
    else:
        print("done")


if __name__ == "__main__":
    resize_files()



