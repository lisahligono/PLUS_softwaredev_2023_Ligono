<h1>Bintang Bolong, The Gambia: Mangrove Vegetation Index (MVI)</h1>

<b>Bintang Bolong Location</b>

<img width="286" alt="image" src="https://github.com/lisahligono/PLUS_softwaredev_2023_Ligono/assets/72496335/3971518e-fe03-4c81-ae02-7aade7afcc43">


<h2>Introduction</h2>

This project focuses on the analysis of mangrove coverage in Bintang Bolong, a beautiful and ecologically significant area located in The Gambia. Mangroves play a vital role in coastal ecosystems, providing various ecological and socioeconomic benefits. The Mangrove Vegetation Index (MVI) is an important tool for quantifying and monitoring mangrove coverage, and this project demonstrates the calculation and analysis of MVI using satellite imagery.

<h2>Bintang Bolong</h2>

Bintang Bolong is a stunning mangrove-rich estuary located in the southern part of The Gambia. It is known for its diverse mangrove species and serves as a crucial habitat for a wide range of flora and fauna. The region is not only ecologically significant but also of great importance to the local communities that rely on mangroves for sustenance and livelihoods.

<h2>Mangrove Vegetation Index (MVI)</h2>

The Mangrove Vegetation Index (MVI) is a specialized index designed to assess and quantify the extent of mangrove coverage in satellite imagery. It utilizes specific bands from remote sensing data to calculate the index, providing a measure of the relative density and health of mangrove vegetation.

<h2>Project Workflow</h2>

This project consists of the following steps:

Loading the Satellite Image: The load_data() function loads the Sentinel-2 satellite image of Bintang Bolong and lists all available bands within the image.
Calculating the MVI: The calculated_mvi() function calculates the Mangrove Vegetation Index (MVI) using specific bands, such as the Near-infrared (B8), Green (B3), and Short-wave infrared 1 (B11). The index is calculated based on the formula (B8 - B3) / (B11 - B3).
Plotting the Results: The plot_mvi() function visualizes the MVI results using a colormap. 

<h2>Getting Started</h2>

To replicate this project and perform MVI analysis for Bintang Bolong in The Gambia, follow these steps:

Clone the project repository: git clone (https://github.com/lisahligono/PLUS_softwaredev_2023_Ligono.git)
Install the mvi.yml file provided 
Update the file paths in the code to match your local environment.
Run the notebook or script to execute the MVI analysis and generate the results.
Explore and interpret the MVI analysis results to gain insights into the mangrove coverage in Bintang Bolong.
