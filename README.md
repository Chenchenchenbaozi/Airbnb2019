# Airbnb2019 (python + Power BI)
The data of analysing is from airbnb official website, which shows the short-term housing in munich. 

To analyse the data, first step is to clean it. I used python 'new_csv.py' to clean the data and removed the wrong localization information according to the zipcodes of munich. 

The house location map I drew is based google openstreetmap. Since there is too much data which makes the map loading slow when drawing all the location information, the whole area is devided by 26 times 26 blocks. K-means clustering is used to get the centroids of the data in these blocks, and the price to represent the block is the average of all house prices in this block. The final result looks like:
![alt text](https://github.com/Qianyu-Chen/Airbnb2019/blob/master/Location%20information.png)

Then I used basemap to create the price map based on the zipcode information from 'suche postleitzahl', which looks like: 
![alt text](https://github.com/Qianyu-Chen/Airbnb2019/blob/master/airbnb.png)

In the end, power BI is used to analysis the data group by room type and the zipcode like:
![alt text](https://github.com/Qianyu-Chen/Airbnb2019/blob/master/Analysis%20power%20bi.png)
![alt text](https://github.com/Qianyu-Chen/Airbnb2019/blob/master/Analysis%20power%20bi%202.png)
The entire house/apt is more polular for shoer-term renting in munich last year and also get higher review score than others. The city center is still the most popular area even is it has higher average price than other areas.
