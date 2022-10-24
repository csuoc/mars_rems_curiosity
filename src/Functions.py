# Import box
from dotenv import load_dotenv
import os
import requests
import pandas as pd
from pandas import json_normalize
from IPython.display import Image
from IPython.core.display import HTML
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import time
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import re

load_dotenv()

# Function to remove undesired columns

def remove_columns(df, column_name):
    
    """
    This is a function that removes undesired columns. Requires two arguments.
    Arguments: dataframe, column name
    Input: the current dataframe
    Output: the current dataframe without the selected columns
    """
    
    df.drop(columns=f"{column_name}", inplace=True)
    
    return df.sample(2)

# Function to rename columns

def rename_columns(df, old_name, new_name):
    
    """
    This a functions that renames the name of any given columns. Requires three arguments.
    Arguments: dataframe, old name of the column, new name of the column.
    Input: the current column name
    Output: the column renamed
    """
    
    df.rename(columns={f"{old_name}": f"{new_name}"}, inplace=True)
    return df.sample(2)

# Function to clean the atmosphere column

def clean_atmosphere(df,column_name,string,replacement):
    
    """
    This a function that cleans the Atmospheric opacity columns by replacing its elements.
    Requires three arguments.
    Arguments: dataframe, column name, string to replace, new string.
    Input: any string
    Output: a string
    """
    
    df[f"{column_name}"] = df[f"{column_name}"].replace(f"{string}",f"{replacement}")    
    return df.sample(2)

# Function to clean the month column

def clean_month(df,column_name):
    
    """
    This is a function that cleans the Month column. Requires two arguments. Removes unwanted strings and only keeps the value
    Arguments: dataframe, column name
    Input: string + digit
    Output: digit
    """
    
    df[f"{column_name}"] = df[f"{column_name}"].str.extract(r"(\d)")    
    return df.sample(2)

# Function to convert degrees Fahrenheit to degrees Celsius

def FtoC(df, column_name):
    
    """
    This is a function that converts any temperature in degrees Fahrenheit to degrees Celsius.
    Requires two arguments.
    Arguments: dataframe, column name
    Input: an INTEGER in Fahrenheit degrees
    Output: an INTEGER in Celsius degrees
    """
    
    df[f"{column_name}"] = [((i - 32.0) * 5.0/9.0) for i in df[f"{column_name}"]]

    return df.sample(2)

# Function to convert milibar to Pascals

def mbartoPa(df, column_name):
    
    """
    This is a function that converts any temperature in degrees Fahrenheit to degrees Celsius.
    Requires two arguments.
    Arguments: dataframe, column name
    Input: an INTEGER in Fahrenheit degrees
    Output: an INTEGER in Celsius degrees
    """
    
    df[f"{column_name}"] = [i*100 for i in df[f"{column_name}"]]

    return df.sample(2)

# Function to round decimals from floats

def roundval(df, column_name, n):
    """
    This is a function that rounds any float to a given n value. Requires three arguments.
    Arguments: dataframe, name of the column where you want to rewrite the values, value of the round
    Input: a float with multiple decimals
    Output: a float with n decimals
    """
    df[f"{column_name}"] = [round(i,n) for i in df[f"{column_name}"]]
    return df.sample(2)

def floatify(df, column_name):
    """
    This is a function that floats any value. Requires two arguments.
    Arguments: dataframe, name of the column where you want to rewrite the values
    Input: a string or integer
    Output: a float
    """
    df[f"{column_name}"] = df[f"{column_name}"].astype(float)
    return df.sample(2)

# This is a function to call NASA api with a given a specific date and Camera type.

def call_Curiosity (date, camera):
    """
    This is a function that calls NASA API 'Mars Rover Photos' with two arguments. It returns the url from
    a specific camera onboard Curiosity rover.
    date: input the desired date in the format YYYY-MM-DD as a STRING,
    camera: select between FHAZ, RHAZ, MAST, CHEMCAM, MAHLI, MARDI, NAVCAM, PANCAM, MINITES, as STRING
    
    """
        
    try:
        nasa = os.getenv("token")
        url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&camera={camera}&api_key={nasa}"
        request = requests.get(url)
        df = pd.DataFrame(request.json())
        df_clean = pd.DataFrame(df.values[0][0])
        image_url = list(df_clean["img_src"])[0]
        display(Image(image_url, width=300, height=200))
        
        return f"Image available for camera {camera} onboard Curiosity rover"

    except:
            
        return f"No image available on {date} for camera {camera} onboard Curiosity rover, please select another date"
    
def get_pictures_Curiosity(date):
    
    """
    This is a function that calls call_NASA function with one argument. It returns the url of all the pictures 
    taken by all the cameras of Curiosity rover from a specific Sol date.
    date: input the desired date in the format YYYY-MM-DD as STRING.
    """       
    cameralist = ["FHAZ", "RHAZ", "MAST", "CHEMCAM", "MAHLI", "MARDI", "NAVCAM", "PANCAM", "MINITES"]
    for i in cameralist:
        print(call_Curiosity(date, i))
    pass

def cool_plots():

    #Necessary readings

    mars = pd.read_csv("../data/mars-weather-cleaned.csv")
    earth = pd.read_csv("../data/papua-weather-cleaned.csv")
    
    #Start
    fig = make_subplots(rows=3, cols=2, 
                        subplot_titles=("Temperature cycle of Mars", "Temperature cycle of Papua New Guinea",
                                        "Pressure cycle of Mars", "Pressure cycle of Papua New Guinea",
                                       "Pressure vs Temperature on Mars",
                                       "Pressure vs Temperature on Papua New Guinea"))

    # Add traces
    fig.add_trace(
        go.Line(x=mars["Earth Date"], y=mars["Mean_temp"], name="Temp Mars"),
        row=1, col=1)
    fig.add_trace(
        go.Line(x=earth["Earth Date"], y=earth["Mean_temp"], name="Temp Earth"),
        row=1, col=2)
    fig.add_trace(
        go.Line(x=mars["Earth Date"], y=mars["Pressure"], name="Pressure Mars"),
        row=2, col=1)
    fig.add_trace(
        go.Line(x=earth["Earth Date"], y=earth["Pressure"], name="Pressure Earth"),
        row=2, col=2)
    fig.add_trace(
        go.Scatter(x=mars["Mean_temp"], y=mars["Pressure"], mode="markers", name="Temp vs Pres Mars"),
        row=3, col=1)
    fig.add_trace(
        go.Scatter(x=earth["Mean_temp"], y=earth["Pressure"], mode="markers", name="Temp vs Pres Earth"),
        row=3, col=2)

    # Update xaxis properties
    fig.update_xaxes(title_text="Years", row=1, col=1)
    fig.update_xaxes(title_text="Years", row=1, col=2)
    fig.update_xaxes(title_text="Years", row=2, col=1)
    fig.update_xaxes(title_text="Years", row=2, col=2)
    fig.update_xaxes(title_text="Temperature (°C)", row=3, col=1)
    fig.update_xaxes(title_text="Temperature (°C)", row=3, col=2)

    # Update yaxis properties
    fig.update_yaxes(title_text="Temperature (°C)", row=1, col=1)
    fig.update_yaxes(title_text="Temperature (°C)", row=1, col=2)
    fig.update_yaxes(title_text="Pressure (Pa)", row=2, col=1)
    fig.update_yaxes(title_text="Pressure (Pa)", row=2, col=2)
    fig.update_yaxes(title_text="Pressure (Pa)", row=3, col=1)
    fig.update_yaxes(title_text="Pressure (Pa)", row=3, col=2)

    # Update title and height
    fig.update_layout(height=1100, width=1000, title_text="Summary of surface conditions on Mars and Papua New Guinea")
    
    return fig.show()

def Mars_Today():

    """
    This is a function that retrieves a prediction of the Mars weather from
    2018-02-28 in advance. It also shows the real conditions and some
    photos that rover Curiosity took in the specified date.
    The user only needs to specify the desired date in the 
    format YYYY-MM-DD.
    """ 
    #Necessary readings
    mars = pd.read_csv("../data/mars-weather-cleaned.csv")
    widget = pd.read_csv("../data/widget-cleaned.csv")

    # Intro
    time.sleep(2)
    print("LOADING..........\n")
    time.sleep(2)
    print("COMPLETE\n")
    time.sleep(2)
    print("WELCOME TO THE MARS ENVIRONMENTAL CONDITIONS PREDICTOR!\n")
    time.sleep(2)

    # Data input
    date = input("Please input a date in the following format YYYY-MM-DD from 2018-03-01: \n")
    time.sleep(2)
    print("This is my forecast for the selected date:\n")
    time.sleep(2)

    # Retrieving the years before the date input. This is the the function to split the input date in year,
    # month and day independently.
    dateinput = date.split("-")
    current_date = datetime.datetime((int(dateinput[0])),int(dateinput[1]),int(dateinput[2]))

    #For the selected year, it will be sustracted "i" times until the year 2012 and appended into a list:
    lst_=[]
    appended_data = []
    for i in range(0,13):
        past_date = str(current_date - relativedelta(years=i))

        f = past_date.split(" ")[0]
        lst_.append(f)

    # Now that I have all years in a list, I call each one of them and see if that year is inside the mars
    # database and the widget database
    for j in lst_:

        if mars.loc[mars["Earth Date"] == f"{j}"].empty == False or widget.loc[widget["Earth Date"] == f"{j}"].empty == False :

            df = mars.loc[mars["Earth Date"] == f"{j}"]
            df2 = widget.loc[widget["Earth Date"] == f"{j}"]
            appended_data.append(df)
            appended_data.append(df2)
            filter_data = pd.concat(appended_data)
            filter_data = filter_data.iloc[1: , :]
            filter_data[["MinT StDev", "MaxT StDev", "MeanT StDev", "Press StDev"]] = filter_data[["Min_temp", "Max_temp", "Mean_temp", "Pressure"]].std()
            filter_data = filter_data[["Min_temp", "Max_temp", "Mean_temp", "Pressure","MinT StDev", "MaxT StDev", "MeanT StDev", "Press StDev"]].mean()
            filter_data = pd.DataFrame(filter_data)
            filter_data = filter_data.transpose()
            for i in list(filter_data.columns):
                filter_data[f"{i}"] = [round(i,1) for i in filter_data[f"{i}"]]
            filter_data["Atmo_opacity"] = "Sunny"

    display(filter_data)

    # All findings are displayed as individual dataframes, so with the pd.concat I merge all of them
    # into a single one.

    time.sleep(2)

    print("The real conditions are: \n")

    time.sleep(2)

    # Now I can compare what were the real conditions according to the widget-scrapped database:
    if date in widget["Earth Date"].values:

        display(widget.loc[widget["Earth Date"] == f"{date}"]) 
        time.sleep(3)
        print("Wanna see cool pictures that Curiosity took from that day? :)\n")
        time.sleep(3)
        get_pictures_Curiosity(date)

    # Added the cool feature to show pictures taken from Curiosity in that day!
    
    return