# Link to Strong & Lean App [https://strongleanapp.herokuapp.com/](https://strongleanapp.herokuapp.com/)

Strong & Lean is a Strava club, where members are actively participating 
in an 8 week workout challenge from YouTube channel Sarah's Day. This 
dashboard is aimed at tracking activity of the club members. 

## Strong & Lean Strava Club, API Data Dashboard 

This is a flask app that visualizes data from the Strava API. Data is
pulled directly from the API and then visualized using Plotly (from the 
[Udacity dashboard template](https://github.com/udacity/DSND_Term2/tree/master/lessons/WebDevelopment/AdvancedDataDashboardCode/world_bank_api_dashboard)).

Given recent changes in the Strava Club API only very limited data is 
available now and therefore significant improvements in this dashboard 
could be made by manually authorising each member, to collect their full
workout data.

Strava API Resources
1. [Strava developers page](https://developers.strava.com) 
2. [YouTube tutorial on getting authorisation tokens](https://youtu.be/sgscChKfGyg)

## Getting Started 

This flask app can be used as a template for visualizing other data or 
the basis from which to build out . Use the template to enhance your 
professional portfolio. 

## Prerequisites

To install the flask app, you need:
- python3
- all python packages in the requirements.txt file
 
 Install the packages with
``` 
 pip install -r requirements.txt
```

## Installing

On a MacOS/linux system, installation is easy. Open a terminal, and go into 
the directory with the flask app files. Run `python strongleanapp.py` in the terminal.
