#Homework 10 

#Import additional dependencies

import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Set up database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Set up application
app = Flask(__name__)

#Create a home route that defines all other routes
@app.route('/')
def home():
    return (
        f"<strong>Welcome to Climate API for Hawaii!</strong><br/>"
        '<br/>'
        f"<strong>Available Routes Include:</strong><br/>"
        '<br/>'
        f"<strong>Precipitation Data:</strong><br/>"
        f"<a href=/api/v1.0/precipitation>Date & Precpitation</a><br/>"
        '<br/>'
        f"<strong>Station Information:</strong><br/>"
        f"<a href=/api/v1.0/stations>Nine Stations Available</a><br/>"
        '<br/>'
        f"<strong>TOBS:</strong><br/>"
        f"<a href=/api/v1.0/tobs>Temperature Observation Data</a><br/>"
        '<br/>'
        f"<strong>Search Start Date (yyyy-mm-dd) for Temperature - Mini, Avg, Max:</strong><br/>"
        f"/api/v1.0/2017-04-10<br/>"
        '<br/>'
        f"<strong>Search Start & End Date (yyyy-mm-dd) for Temperature - Min, Avg, Max:</strong><br/>"
        f"/api/v1.0/2017-04-10/2017-04-15<br/>")

#Create a date and precipitation route
@app.route('/api/v1.0/precipitation')
def precipitation():
    #Creat session link from Python to Database
    session = Session(engine)

    #Query date and preciptation data
    data_prcp = session.query(Measurement.date, Measurement.prcp)\
                .order_by(Measurement.date).all()
    session.close()

    #Create a dictionary using date as the key and prcp as the value {'date': 'prcp'}
    results = []
    for date, prcp in data_prcp:
        results_dict = {}
        results_dict[date] = prcp
        results.append(results_dict)
    
    #Return the JSON representation of your dictionary
    return jsonify(results)

#Create a stations route
@app.route('/api/v1.0/stations')
def stations():
    #Create session link from Python to Database
    session = Session(engine)

    #Query to return a list of stations
    stations_list = session.query(Station.station, Station.name).all()
    session.close()

    #Convert list of tuples into a normal list
    station_names = list(np.ravel(stations_list))

    #Return a JSON list of stations from the dataset
    return jsonify(station_names)

#Create a TOBs route
@app.route('/api/v1.0/tobs')
def tobs():

    #Date info from Part 1 query determined latest date as 2017-08-23 calulate for previous year
    date_info = dt.date(2017,8,23) - dt.timedelta(days=365)

    #Create session link from Python to Database
    session = Session(engine)

    #Query the dates and temperature observations of the most active station for the last year of data
    #Return a JSON list of temperature observations (TOBS) for the previous year
    #Last date in database = 201-08-23
    tob_results = session.query(Measurement.date, Measurement.tobs)\
                .filter(Measurement.station == 'USC00519281')\
                .filter(Measurement.date >= date_info).all()
    session.close()
    
    #Convert list of tuples into a normal list
    tobs_info = list(np.ravel(tob_results))

    return jsonify(tobs_info)

#Create a start route
#Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start
#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

# start = '2017-04-10'

@app.route('/api/v1.0/<start>')
def date_start(start=None):

    session = Session(engine)
    random_date = session.query(func.min(Measurement.tobs), 
                           func.max(Measurement.tobs), 
                           func.avg(Measurement.tobs))\
                .filter(Measurement.date >= start).all()
    session.close()

    return_all = []
    for min_date,avg_date,max_date in random_date:
        return_dict= {}
        # return_dict['Start Date'] = start_date
        return_dict['Min'] = min_date
        return_dict['Avg'] = avg_date
        return_dict['Max'] = max_date
        return_all.append(return_dict)
    
    return jsonify(return_all)

#Create a start/end route
#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
@app.route('/api/v1.0/<start>/<end>')
def start_end(start=None, end=None):

    session = Session(engine)
    start_ends = session.query(func.min(Measurement.tobs), 
                           func.max(Measurement.tobs), 
                           func.avg(Measurement.tobs))\
                .filter(Measurement.date >= start)\
                .filter(Measurement.date <= end).all()
    session.close()

    return_info = []
    for min_se,avg_se,max_se in start_ends:
        final_dict= {}
        final_dict['Min'] = min_se
        final_dict['Avg'] = avg_se
        final_dict['Max'] = max_se
        return_info.append(final_dict)
    
    return jsonify(return_info)

#Running the app
if __name__ == "__main__":
    app.run(debug=True)