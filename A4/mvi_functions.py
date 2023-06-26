"""
The Mangrove Vegetation Index (MVI) was designed by Baloloy et al., 2020.
In this assignment, I will be showcasing the working of the MVI index using 3 functions:
(1) Loading a sentinel-2 satellite image and listing all the bands available in the .tiff file
(2) Calculating the MVI index and returning the result
(3) Plotting the results  
"""

import rasterio
import matplotlib.pyplot as plt

def load_data ():

   """"
   This function loads the Sentinel-2 image located in the mvi folder and lists all
   the bands the image has
   """

path = "/Users/lisahligono/practice-plus/A4/mvi/bolong.tif"

with rasterio.open(path) as dataset:
    band_descriptions = dataset.descriptions

for band_index, band_description in enumerate(band_descriptions):
    print(f"Band {band_index + 1}: {band_description}")

def calculated_mvi ():

    """"
    In this section MVI index is calculated using the Near-infrared (B8), Green (B3)and Short-wave infrared 1 (B11)
    The B3 and B8 are 10m while the B11 is 20m
    In this test I did not consider resampling the bands to the same resolution since it would 
    make the function complex
    """
    with rasterio.open(path) as dataset:
        B3 = dataset.read(3)  
        B8 = dataset.read(8)  
        B11 = dataset.read(11)  

    mvi = (B8 - B3) / (B11 - B3)

    return mvi

def plot_mvi(mvi):
    """
    Plots the MVI result using matplotlib.

    """
    img = plt.imshow(mvi, cmap='coolwarm')

    # Add colorbar
    cbar = plt.colorbar(img)
    cbar.set_label('MVI')

    # Set axis labels and title
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.title('Modified Vegetation Index (MVI)')

    # Show the plot
    plt.show()
