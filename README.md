# GeoSpatial_BigData
 Geospatial science combines aspects of geography, cartography, remote sensing, geodesy, and spatial statistics to analyze and interpret geospatial data using programing languages like python and its spatial libraries

<p> This repository showcases my geospatial analysis portfolio in Python, which includes code completed as part of my academic work. The code reflects the current real-time data and was developed while I was taking Geog 573 during the Spring 2023 semester. The course was taught by <a href = "https://geography.wisc.edu/staff/gao-song/"> Professor Song Gao</a>, a renowned expert in the geospatial data science field and the director of the <a href = "https://geography.wisc.edu/geods/">GeoDS Lab</a> in the Geography department at the <a href = "https://wisc.edu/">University of Wisconsin Madison</a>. </p>

## 1. <a href = "https://github.com/gangaraju09/GeoSpatial_BigData/tree/main/DaneCounty_Covid_19">  Dane County Covid 19</a>
<ul>
<p> In this project, I developed a visualization of COVID-19 cases in Dane County, Wisconsin, by monitoring dynamic human mobility changes and travel flow patterns at various geographic scales. Understanding human behavior changes during the pandemic is crucial, and this project involved collecting both spatial and non-spatial structured data from the Dane County region, as well as related COVID-19 data. To process the data, I used Python libraries, specifically geopandas, to convert the data into the GeoJSON data format.<br><br> For visualization of number of cases, I aggregated census tract information with ZCTA (Zip Code Tabular Areas) and appended COVID-19 information to this zip code information. <p> 

<img src = "https://github.com/gangaraju09/GeoSpatial_BigData/blob/main/DaneCounty_Covid_19/New%20folder/covid_daneCounty.png?raw=true" alt="Number of cases on feb 13 2021 during the COVID-19 pandemic">
</ul>

<ul>
<p>  For visualization of Human mobility from one zipcode location data in Dane county is converted into source & desitnation's latitude and longitude by performing google geocoding method using google maps api and kepler spatial data visualization tool <p> 

<img src = "https://github.com/gangaraju09/GeoSpatial_BigData/blob/main/DaneCounty_Covid_19/New%20folder/visitor_flows_53508.png?raw=true" alt="Visitor flows in zip code 53508 during the COVID-19 pandemic">
</ul>

## 2. <a href = "https://github.com/gangaraju09/GeoSpatial_BigData/tree/main/Vector_processing">  Flicker Photo Distribution in a Orange County Using Vector Analysis</a>
<ul>
<p> In this project, geospatial analysis techniques were employed to investigate the distribution and clustering of geotagged photos taken within the vicinity of Disney Land in Orange County, by utilizing the Flickr API. Firstly, the Orange County shapefile was converted into a geopandas object and Geoseries is used to create spatial boundaries and to enable spatial analysis. Spatial information on Flickr photos was then collected by webscrapping of data with Flickr api, and a spatial within analysis was performed to establish the number of photos taken within a specific spatial boundary. since Flickr photos are in point form, the K-means clustering method was used to group similar photos based on their spatial location, enabling the identification of spatial clusters of photos.

Overall, this project demonstrated the effectiveness of geospatial analysis techniques in webscrapping, examining the distribution and clustering of photos taken within a particular area. The combination of geopandas, GeoSeries, Shapely and K-means clustering proved useful for analyzing and visualizing geospatial data.  <p> 

<img src = " https://github.com/gangaraju09/GeoSpatial_BigData/blob/main/Vector_processing/images/Orange_county.png?raw=true" alt="">

<img src = " https://github.com/gangaraju09/GeoSpatial_BigData/blob/main/Vector_processing/images/flickr_image_points.png?raw=true" alt="">

<img src = " https://github.com/gangaraju09/GeoSpatial_BigData/blob/main/Vector_processing/images/no_spatial_within.png?raw=true" alt="">

<img src = " https://github.com/gangaraju09/GeoSpatial_BigData/blob/main/Vector_processing/images/with_spatial_within.png?raw=true" alt="">

<img src = " https://github.com/gangaraju09/GeoSpatial_BigData/blob/main/Vector_processing/images/cluster.png?raw=true" alt="">

</ul>

## 3  <a href = "https://github.com/gangaraju09/GeoSpatial_BigData/tree/main/Google_Earth_Engine">  Google Earth Engine (GEE MAP).</a>
<ul>
<p> Google Earth is a virtual globe platform that provides users with access to a range of geospatial data, including satellite imagery, maps, terrain, and 3D buildings. It allows users to explore and learn about different parts of the world.

On the other hand, Earth Engine is a tool designed specifically for analyzing geospatial data. It provides a data catalog that is different from the Google Earth data catalog, and not all the data available in Google Earth is available for analysis in Earth Engine. Similarly, not all the data in Earth Engine is currently available for visualization in Google Earth. Earth Engine is primarily focused on analyzing and processing geospatial data, whereas Google Earth is focused on visualizing and exploring geospatial data.

To generate two-period maps of land cover-land use in Dane County using Dynamic World data on Google Earth Engine, I tool the data for the years 2016 and 2022, filtered the data to include only Dane County, visualized parameters to display land cover-land use classes in different colors, created two separate maps, and compare them side by side to identify any changes in land use over the six-year period. This data can inform decision-making processes and future land use planning in the county.
  <p> 
    <img src = " https://github.com/gangaraju09/GeoSpatial_BigData/blob/main/Google_Earth_Engine/output_files/landcover.png?raw=true" alt="">  

  <p> To analyze the vegetation cover in a study area, I used Landsat 8 remote sensing images and Google Earth Engine to compute the Normalized Difference Vegetation Index (NDVI) values. This involves filtering the data to the time period of interest, calculating NDVI values using Landsat 8 data and the appropriate formula, setting visualization parameters to display NDVI values in different colors, and creating a map of the study area with the NDVI values overlaid on it. This information can help identify areas requiring additional vegetation management or restoration efforts and monitor changes in vegetation cover over time.</p>

  <p>To create a Landsat timelapse animation GIF file, I used Google Earth Engine to filter Landsat data for a specific area and time period, set visualization parameters, and export the animation as a GIF file. This can provide valuable insights into land use and environmental changes over time, which can be used for monitoring, analysis, and public education purposes. The resulting timelapse animation is a dynamic and engaging way to show environmental changes and human impacts on the planet. </p>
<br>
  <img src = " https://github.com/gangaraju09/GeoSpatial_BigData/blob/main/Google_Earth_Engine/output_files/Aral_sea_ts.gif?raw=true" alt="">   
  <br>
  <img src = "https://github.com/gangaraju09/GeoSpatial_BigData/blob/main/Google_Earth_Engine/output_files/Denver_ts.gif?raw=true" alt="">
</ul>

## 4  <a href = "https://github.com/gangaraju09/GeoSpatial_BigData/tree/main/Network_Analysis">  Network Analysis</a>
<ul>
<p>For my Network Analysis project, I utilized two Python libraries, OSMnx and NetworkX, to analyze complex road networks. OSMnx enables users to access and analyze OpenStreetMap (OSM) data, and visualize street networks on interactive maps. NetworkX is a comprehensive Python package that provides tools for creating, manipulating, and studying intricate networks. By combining the capabilities of these two packages, users can conduct various network analysis tasks on street networks, such as identifying the shortest paths between nodes, detecting the centrality of nodes, and recognizing communities within the network.

In this project, I applied network analysis techniques to Madison, Wisconsin. Initially, I extracted the network dataset and saved it as a shapefile. I then computed edge_centrality_closeness, which enables us to determine the areas of the network with high or low closeness centrality. Next, I calculated Betweenness centrality, which measures the frequency of shortest paths between node pairs passing through a particular node. Finally, I computed Degree centrality, which indicates the number of edges that connect to a node in a network. These analyses allowed me to study the structure, dynamics, and functions of complex road networks in Madison, Wisconsin.
  <p> 

## 5  <a href = "https://github.com/gangaraju09/GeoSpatial_BigData/tree/main/Spatial_Autocorrelation_and_Regression"> Spatial Auto Correlation and Regression</a>
<ul>
<p> Through the application of Moran's I and Geographic Weighted Regression (GWR) using PySAL geospatial analysis library, several observations were made regarding the distribution of wasted votes for Democrats during the 2020 presidential election in Madison, WI. The image below depicts the distribution of these wasted votes, which are defined as votes cast for a candidate that did not win, and therefore did not contribute to the candidate's victory<sup><a href = "https://ballotpedia.org/Efficiency_gap"> Ballotpedia</a></sup>.

The analysis using Moran's I revealed hotspots with a high concentration of wasted votes in certain regions of Madison, indicating a strong spatial autocorrelation. On the other hand, coldspots showed a weak spatial correlation of wasted votes. Additionally, the GWR results demonstrated that the relationship between wasted votes and key predictors, such as race and education, varied geographically, indicating the need for targeted strategies to address this issue in specific areas. This information can be useful for improving the efficiency and fairness of the election process in Madison, WI.

<img src = "https://github.com/gangaraju09/GeoSpatial_BigData/blob/main/Spatial_Autocorrelation_and_Regression/images/Coldspots.png?raw=true" alt="">

Here I took Airbnb raw data and analysed the Airbnb median price variation in Austin, Texas based on mean bedrooms and review score values was generated using Geographic Weighted Regression (GWR). GWR is a spatial regression technique that allows the relationship between variables to vary geographically, enabling the identification of local variations in the relationship between the variables of interest. The snapshot reveals the median price variation of Airbnb listings in different areas of Austin, Texas, highlighting the impact of mean bedrooms and review score values on the pricing of Airbnb listings. This information can be useful for both hosts and guests in making informed decisions regarding pricing and rental choices in Austin, Texas.

<img src = "https://github.com/gangaraju09/GeoSpatial_BigData/blob/main/Spatial_Autocorrelation_and_Regression/images/GWR.png?raw=true" alt="">

</ul>
  </p> 


