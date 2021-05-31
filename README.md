# SQLAlchemy Homework - Surfs Up!

## Summary
* Exploratory analysis of Hawaiian weather data.
* Also included is climate application that observes weather patterns during the year.

### Files
* 'HW10_Main.ipynb' is the initial analysis of resource file 'hawaii.sqlite'.
* 'BONUS - Challenge Assignment.ipynb' continues the analysis further.
* A "app.py" python file that functions as a climate application which calls weather data.
* 'Images' folder includes .png files of analysis graphics.

## Instructions: 

### Step 1 - Climate Analysis and Exploration
* Use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
    * Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.
    * Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.
    * Use SQLAlchemy create_engine to connect to your sqlite database.
    * Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.
* Precipitation Analysis
    * Design a query to retrieve the last 12 months of precipitation data.
    * Select only the date and prcp values.
    * Load the query results into a Pandas DataFrame and set the index to the date column.
    * Sort the DataFrame values by date.
    * Plot the results using the DataFrame plot method.
    * Use Pandas to print the summary statistics for the precipitation data.
* Station Analysis
    * Design a query to calculate the total number of stations.
    * Design a query to find the most active stations.
    * Design a query to retrieve the last 12 months of temperature observation data (tobs).
* Temperature Analysis
    * The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d and return the minimum, average, and maximum temperatures for that range of dates.
    * Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").
    * Plot the min, avg, and max temperature from your previous query as a bar chart.
    
### Step 2 - Climate App
Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.
* Use FLASK to create your routes.

![image](https://user-images.githubusercontent.com/72557712/120234721-c929e580-c215-11eb-9204-390016c67257.png)

* Date & Precipitation: <br>
![image](https://user-images.githubusercontent.com/72557712/120234765-dd6de280-c215-11eb-848a-94722d38ee55.png)

