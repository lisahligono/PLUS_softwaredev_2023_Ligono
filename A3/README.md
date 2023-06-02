<h1>Network and Distance Analysis</h1>

<b>Geopy</b> is a python library that simplifies the calculation of geographic distances between points. It makes it easier for developers to retrieve coordinates of various locations using third-party geocoders, as well as other data sources.

Supporting libraries and packages also used here are:

<b>Folium</b> is a python library that makes it easier to visualize spatial data in python on an interactive online leaflet map. 

<b>Osmnx</b> is a python package that lets you download geospatial data from OpenStreetMap and model, project, visualize, and analyze real-world street networks and any other geospatial geometries. 

<h2>Content</h2>
<h2>Introduction</h2> 
My group’s final semester project will involve routing by emergency responders during rescue operations. Therefore, for the A3, I will be exploring the geopy library in order to learn how distances between two geographic coordinates are calculated using python.

Additionally, I will explore network analysis using the osmnx package which is essential for routing applications and further visualize these datasets with the help of folium.

<i>NB: The ipynb notebook file provided will not load the maps created by the folium library. Therefore, I recommend following the steps in the <b>installation stage</b> in order to replicate and run the script on your local machine</i>

<h2>Installation</h2> 
To replicate this example, the package can be installed through source using the conda environment with the library itself and all the dependencies installed using the provided a3geopyenv.yml file

git clone https://github.com/lisahligono/PLUS_softwaredev_2023_Ligono.git

cd A3

conda env create -f a3geopyenv.yml

conda activate A3

<h2>Contribution</h2>
Contributions of any kind are welcome 

<h2>Acknowledgement</h2> 
This example is developed as part of the Practice: Software development in python course

<h2>Documentation</h2> 
More documentation can be found in the links below: 

Geopy: https://geopy.readthedocs.io/en/latest/ 

Osmnx: https://osmnx.readthedocs.io/en/stable/

Folium: https://python-visualization.github.io/folium/ 

