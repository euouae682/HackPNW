import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import geopandas as gpd
import json
import matplotlib.pyplot as plt
import geojson
import folium
from shapely.geometry import Point, Polygon


def precipit(lat=44, long=-103):
    geographic = gpd.read_file("data/uscounties/USA_Counties.shp")
    geographic = geographic[['NAME','STATE_NAME','geometry']]
        #geographic.drop(geographic.columns.difference(['NAME','STATE_NAME','geometry']),1,inplace=True)
    geographic['STATE_NAME'] =geographic['STATE_NAME'].str.upper()
    geographic = geographic[geographic.STATE_NAME != "PUERTO RICO"]
    geographic = geographic[geographic.STATE_NAME != "ALASKA"]
    geographic.rename(columns={'NAME':'County'},inplace=True)
    geographic['County'] = geographic['County'].str.lower()
    geographic["State"] = geographic["STATE_NAME"]

    tribal = gpd.read_file("data/NativeAmerican.geojson")
    precip = pd.read_csv("data/Precip22.csv")
    temp = pd.read_csv("data/temp22.csv")

    precip[['State','ID']] = precip['Location ID'].str.split('-',expand=True)

    temp[['State','ID']] = temp['Location ID'].str.split('-',expand=True)
    precip = precip[precip.State!="AK"]


    temp.State.unique()
    temp = temp[temp.State!="AK"]

    precip['Location'] = precip['Location'].str.split(' ',expand=True)[0]
    precip.drop(['Location ID','Rank','Anomaly (1901-2000 base period)','1901-2000 Mean'], axis=1,inplace=True)
    precip.rename(columns={'Value':'Precipitation (inches)'},inplace=True)

    temp['Location'] = temp['Location'].str.split(' ',expand=True)[0]
    temp.drop(['Location ID','Rank','Anomaly (1901-2000 base period)','1901-2000 Mean'], axis=1,inplace=True)
    temp.rename(columns={'Value':'Temp (F)'},inplace=True)

    us_state_to_abbrev = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY",
        "District of Columbia": "DC",
        "American Samoa": "AS",
        "Guam": "GU",
        "Northern Mariana Islands": "MP",
        "Puerto Rico": "PR",
        "United States Minor Outlying Islands": "UM",
        "U.S. Virgin Islands": "VI",
    }

    us_state_to_abbrev =  {k.lower(): v for k, v in us_state_to_abbrev.items()}

    geographic["STATE_NAME"] =  geographic["STATE_NAME"].str.lower()
    geographic["STATE_NAME"] = geographic["STATE_NAME"].map(us_state_to_abbrev)

    precip["STATE_NAME"] = precip["State"]
    precip.rename(columns={'Location':'County'},inplace=True)
    precip['County'] = precip['County'].str.lower()
    # precip_data= precip.merge(geographic,how="inner", right_on=["County",'STATE_NAME'], left_on=['County','STATE_NAME'])
    precip['Precipitation (inches)'] = precip['Precipitation (inches)'] .astype(int)
    #precip_gpd = gpd.GeoDataFrame(precip_data)

    temp["STATE_NAME"] = temp["State"]
    temp.rename(columns={'Location':'County'},inplace=True)
    temp['County'] = temp['County'].str.lower()
    #temp_data= temp.merge(geographic,how="inner", right_on=["County",'STATE_NAME'], left_on=['County','STATE_NAME'])
    temp['Temp (F)'] = temp['Temp (F)'] .astype(int)
    #temp_gpd = gpd.GeoDataFrame(temp_data)
    # when you get the location of the user in latitude and longitude, replace with the variables. 
    m = folium.Map(location=[lat, long],tiles ='Stamen Terrain')
    style2 = {'fillColor': '#32773F', 'lineColor': '#32773F'}
    folium.GeoJson(tribal,style_function=lambda x:style2).add_to(m)
    precip = pd.DataFrame(precip)
    folium.Choropleth(geo_data=geographic,data=precip,columns=["County", "Precipitation (inches)"],key_on="feature.properties.County",fill_opacity = 0.7,line_opacity = 0.2,legend_name = "Precipitation").add_to(m)
    disasters = pd.read_csv("data/disasters.csv")
    for i in disasters: 
        if i["Description"] == "Fire":
            folium.Marker(location=[i["Lat","Long"]],popup=i['Description'],icon=folium.Icon()).add_to(m)

    #folium.GeoJson(state_df).add_to(m)

    # Display the map
    return m

def temper(lat=44,long=-103): 
    # when you get the location of the user in latitude and longitude, replace with the variables. 
    geographic = gpd.read_file("data/uscounties/USA_Counties.shp")
    geographic = geographic[['NAME','STATE_NAME','geometry']]
        #geographic.drop(geographic.columns.difference(['NAME','STATE_NAME','geometry']),1,inplace=True)
    geographic['STATE_NAME'] =geographic['STATE_NAME'].str.upper()
    geographic = geographic[geographic.STATE_NAME != "PUERTO RICO"]
    geographic = geographic[geographic.STATE_NAME != "ALASKA"]
    geographic.rename(columns={'NAME':'County'},inplace=True)
    geographic['County'] = geographic['County'].str.lower()
    geographic["State"] = geographic["STATE_NAME"]

    tribal = gpd.read_file("data/NativeAmerican.geojson")
    precip = pd.read_csv("data/Precip22.csv")
    temp = pd.read_csv("data/temp22.csv")

    precip[['State','ID']] = precip['Location ID'].str.split('-',expand=True)

    temp[['State','ID']] = temp['Location ID'].str.split('-',expand=True)
    precip = precip[precip.State!="AK"]


    temp.State.unique()
    temp = temp[temp.State!="AK"]

    precip['Location'] = precip['Location'].str.split(' ',expand=True)[0]
    precip.drop(['Location ID','Rank','Anomaly (1901-2000 base period)','1901-2000 Mean'], axis=1,inplace=True)
    precip.rename(columns={'Value':'Precipitation (inches)'},inplace=True)

    temp['Location'] = temp['Location'].str.split(' ',expand=True)[0]
    temp.drop(['Location ID','Rank','Anomaly (1901-2000 base period)','1901-2000 Mean'], axis=1,inplace=True)
    temp.rename(columns={'Value':'Temp (F)'},inplace=True)

    us_state_to_abbrev = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY",
        "District of Columbia": "DC",
        "American Samoa": "AS",
        "Guam": "GU",
        "Northern Mariana Islands": "MP",
        "Puerto Rico": "PR",
        "United States Minor Outlying Islands": "UM",
        "U.S. Virgin Islands": "VI",
    }

    us_state_to_abbrev =  {k.lower(): v for k, v in us_state_to_abbrev.items()}

    geographic["STATE_NAME"] =  geographic["STATE_NAME"].str.lower()
    geographic["STATE_NAME"] = geographic["STATE_NAME"].map(us_state_to_abbrev)

    precip["STATE_NAME"] = precip["State"]
    precip.rename(columns={'Location':'County'},inplace=True)
    precip['County'] = precip['County'].str.lower()
    # precip_data= precip.merge(geographic,how="inner", right_on=["County",'STATE_NAME'], left_on=['County','STATE_NAME'])
    precip['Precipitation (inches)'] = precip['Precipitation (inches)'] .astype(int)
    #precip_gpd = gpd.GeoDataFrame(precip_data)

    temp["STATE_NAME"] = temp["State"]
    temp.rename(columns={'Location':'County'},inplace=True)
    temp['County'] = temp['County'].str.lower()
    #temp_data= temp.merge(geographic,how="inner", right_on=["County",'STATE_NAME'], left_on=['County','STATE_NAME'])
    temp['Temp (F)'] = temp['Temp (F)'] .astype(int)
    #temp_gpd = gpd.GeoDataFrame(temp_data)
    m = folium.Map(location=[lat, long],tiles ='Stamen Terrain')
    folium.GeoJson(tribal).add_to(m)
    temp = pd.DataFrame(temp)
    folium.Choropleth(
        geo_data=geographic,
        data=temp,
        columns=["County", "Temp (F)"],
        #fill_color = 'RdYlBu',
        key_on="feature.properties.County",
        fill_opacity = 0.7,
        line_opacity = 0.2,
        legend_name = "Temperature"
    ).add_to(m)
    disasters = pd.read_csv("data/disasters.csv")
    for i in disasters: 
        folium.Marker(location=[i["Lat","Long"]],popup=i['Description'],icon=folium.Icon()).add_to(m)

    #folium.GeoJson(state_df).add_to(m)

    # Display the map
    return m
