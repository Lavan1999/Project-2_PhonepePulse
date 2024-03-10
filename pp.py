#Once created the clone of GIT-HUB repository then,
#Required libraries for the program

import pandas as pd
import json
import os
from sqlalchemy import create_engine, Text, String, Interval,Integer,Date, PrimaryKeyConstraint
from sqlalchemy.exc import SQLAlchemyError
import plotly.express as px
import plotly.io as pio
import streamlit as st

st.set_page_config(layout= "wide")
#1 Aggregated/trans
#This is to direct the path to get the data as states
path="C:/Users/DELL/Desktop/Phonepay/pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)
#Agg_state_list--> to get the list of states in India

#This is to extract the data's to create a dataframe

clm1={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
                Name=z['name']
                count=z['paymentInstruments'][0]['count']
                amount=z['paymentInstruments'][0]['amount']
                clm1['Transaction_type'].append(Name)
                clm1['Transaction_count'].append(count)
                clm1['Transaction_amount'].append(amount)
                clm1['State'].append(i)
                clm1['Year'].append(j)
                clm1['Quater'].append(int(k.strip('.json')))
#Succesfully created a dataframe
agg_trans=pd.DataFrame(clm1)

agg_trans['State']=agg_trans['State'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
agg_trans['State']=agg_trans['State'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
agg_trans['State']=agg_trans['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
agg_trans['State']=agg_trans['State'].str.replace("-"," ")
agg_trans['State']=agg_trans['State'].str.title()
agg_trans['Transaction_amount']=agg_trans['Transaction_amount'].round(3)
agg_trans['Year']=agg_trans['Year'].astype(int)



#2 aggregated/User DF

#This is to direct the path to get the data as states
path="C:/Users/DELL/Desktop/Phonepay/pulse/data/aggregated/user/country/india/state/"
Agg_state_list=os.listdir(path)

#Agg_state_list--> to get the list of states in India

clm2={'State':[], 'Year':[],'Quater':[],'user_brand':[], 'reg_userbrand_count':[], 'reg_percentage':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
                for z in D['data']['usersByDevice']:
                    Brand=z['brand']
                    count=z['count']
                    percentage=z['percentage']
                    clm2['user_brand'].append(Brand)
                    clm2['reg_userbrand_count'].append(count)
                    clm2['reg_percentage'].append(percentage)
                    clm2['State'].append(i)
                    clm2['Year'].append(j)
                    clm2['Quater'].append(int(k.strip('.json')))
            except:
                pass
#Succesfully created a dataframe
agg_users=pd.DataFrame(clm2)

agg_users['State']=agg_users['State'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
agg_users['State']=agg_users['State'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
agg_users['State']=agg_users['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
agg_users['State']=agg_users['State'].str.replace("-"," ")
agg_users['State']=agg_users['State'].str.title()
agg_users['reg_percentage']=agg_users['reg_percentage'].round(3)
agg_users['Year']=agg_users['Year'].astype(int)



    

#This is to direct the path to get the data as states

path="C:/Users/DELL/Desktop/Phonepay/pulse/data/map/transaction/hover/country/india/state/"
map_state_list=os.listdir(path)
#map_state_list--> to get the list of states in India


#This is to extract the data's to create a dataframe

clm3={'State':[], 'Year':[],'Quater':[],'district_name':[], 'transaction_count':[], 'transaction_amount':[]}

for i in map_state_list:
    p_i=path+i+"/"
    map_yr=os.listdir(p_i)
    for j in map_yr:
        p_j=p_i+j+"/"
        map_yr_list=os.listdir(p_j)
        for k in map_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
                for z in D['data']['hoverDataList']:
                    Name=z['name']
                    count=z['metric'][0]['count']
                    amount=z['metric'][0]['amount']
                    clm3['district_name'].append(Name)
                    clm3['transaction_count'].append(count)
                    clm3['transaction_amount'].append(amount)
                    clm3['State'].append(i)
                    clm3['Year'].append(j)
                    clm3['Quater'].append(int(k.strip('.json')))
            except Exception as e:
                print(f"Error processing file '{p_k}': {e}")

#Succesfully created a dataframe
map_trans=pd.DataFrame(clm3)

map_trans['State']=map_trans['State'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
map_trans['State']=map_trans['State'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
map_trans['State']=map_trans['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
map_trans['State']=map_trans['State'].str.replace("-"," ")
map_trans['State']=map_trans['State'].str.title()
map_trans['transaction_amount']=map_trans['transaction_amount'].round(3)
map_trans['Year']=map_trans['Year'].astype(int)




#4 map/User DF----

#This is to direct the path to get the data as states

path="C:/Users/DELL/Desktop/Phonepay/pulse/data/map/user/hover/country/india/state/"
map_state_list=os.listdir(path)
#map_state_list--> to get the list of states in India


#This is to extract the data's to create a dataframe

clm4={'State':[], 'Year':[],'Quater':[],'District_name':[], 'reg_users':[], 'app_opens':[]}

for i in map_state_list:
    p_i=path+i+"/"
    map_yr=os.listdir(p_i)
    for j in map_yr:
        p_j=p_i+j+"/"
        map_yr_list=os.listdir(p_j)
        for k in map_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['hoverData'].items():
                district=z[0]
                regusers=z[1]['registeredUsers']
                appopens=z[1]['appOpens']
                clm4['District_name'].append(district)
                clm4['reg_users'].append(regusers)
                clm4['app_opens'].append(appopens)
                clm4['State'].append(i)
                clm4['Year'].append(j)
                clm4['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
map_users=pd.DataFrame(clm4)

map_users['State']=map_users['State'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
map_users['State']=map_users['State'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
map_users['State']=map_users['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
map_users['State']=map_users['State'].str.replace("-"," ")
map_users['State']=map_users['State'].str.title()
map_users['Year']=map_users['Year'].astype(int)




#5 Top transaction DF ---

#This is to direct the path to get the data as states

path="C:/Users/DELL/Desktop/Phonepay/pulse/data/top/transaction/country/india/state/"
top_state_list=os.listdir(path)
#top_state_list--> to get the list of states in India


#This is to extract the data's to create a dataframe

clm5={'State':[], 'Year':[],'Quater':[],'pincodes':[], 'transaction_count':[], 'transaction_amount':[]}

for i in top_state_list:
    p_i=path+i+"/"
    top_yr=os.listdir(p_i)
    for j in top_yr:
        p_j=p_i+j+"/"
        top_yr_list=os.listdir(p_j)
        for k in top_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['pincodes']:
                Entity_name=z['entityName']
                count=z['metric']['count']
                amount=z['metric']['amount']
                clm5['pincodes'].append(Entity_name)
                clm5['transaction_count'].append(count)
                clm5['transaction_amount'].append(amount)
                clm5['State'].append(i)
                clm5['Year'].append(j)
                clm5['Quater'].append(int(k.strip('.json')))
#Succesfully created a dataframe
top_trans=pd.DataFrame(clm5)

top_trans['State']=top_trans['State'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
top_trans['State']=top_trans['State'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
top_trans['State']=top_trans['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
top_trans['State']=top_trans['State'].str.replace("-"," ")
top_trans['State']=top_trans['State'].str.title()
top_trans['transaction_amount']=top_trans['transaction_amount'].round(3)
top_trans['Year']=top_trans['Year'].astype(int)



    #6 Top country----

#This is to direct the path to get the data as states

path="C:/Users/DELL/Desktop/Phonepay/pulse/data/top/user/country/india/state/"
top_state_list=os.listdir(path)
#top_state_list--> to get the list of states in India


#This is to extract the data's to create a dataframe

clm6={'State':[], 'Year':[],'Quater':[],'Pincodes': [], 'reg_users':[]}

for i in top_state_list:
    p_i=path+i+"/"
    top_yr=os.listdir(p_i)
    for j in top_yr:
        p_j=p_i+j+"/"
        top_yr_list=os.listdir(p_j)
        for k in top_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['pincodes']:
                Name=z['name']
                reg_users=z['registeredUsers']
                clm6['Pincodes'].append(Name)
                clm6['reg_users'].append(reg_users)
                clm6['State'].append(i)
                clm6['Year'].append(j)
                clm6['Quater'].append(int(k.strip('.json')))


#Succesfully created a dataframe
top_users=pd.DataFrame(clm6)

top_users['State']=top_users['State'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
top_users['State']=top_users['State'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
top_users['State']=top_users['State'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
top_users['State']=top_users['State'].str.replace("-"," ")
top_users['State']=top_users['State'].str.title()
top_users['Year']=top_users['Year'].astype(int)





#Created engine using sqlalchemy for migrating dataframe to sql table
engine = create_engine('postgresql://postgres:Lavan123@localhost:5432/phonepe')

# Convert DataFrame to SQL table
tab1 = agg_trans.to_sql('agg_trans', engine, if_exists='replace', index=False)
tab2 = agg_users.to_sql('agg_users', engine, if_exists='replace', index=False)
tab3 = map_trans.to_sql('map_trans', engine, if_exists='replace', index=False)
tab4 = map_users.to_sql('map_users', engine, if_exists='replace', index=False)
tab5 = top_trans.to_sql('top_trans', engine, if_exists='replace', index=False)
tab6 = top_users.to_sql('top_users', engine, if_exists='replace', index=False)



# Read data from SQL Table
df1 = pd.read_sql('agg_trans', engine)
df2 = pd.read_sql('agg_users', engine)
df3 = pd.read_sql('map_trans', engine)
df4 = pd.read_sql('map_users', engine)
df5 = pd.read_sql('top_trans', engine)
df6 = pd.read_sql('top_users', engine)



#streamlit part----
import streamlit as st 
import streamlit_option_menu
import requests
import json
import numpy as np


st.title(':blue[Phonepe Pulse Data Visualization and Exploration]')


#MAP----
imurl = ("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson")
response = requests.get(imurl)
data = json.loads(response.content)
states_name = []
for i in data['features']:
    states_name.append(i['properties']["ST_NM"])
states_name.sort()

#agg_trans map 1
ag_tr = agg_trans.groupby(["State","Year"])[["Transaction_amount","Transaction_count"]].sum()
ag_tr.reset_index(inplace=True)

ifig11 = px.choropleth(
    ag_tr,
    geojson=data,
    featureidkey='properties.ST_NM',
    locations='State',
    color='Transaction_amount',
    color_continuous_scale='Rainbow',
    hover_name = 'State',
    height=600, width=600,
    range_color = (ag_tr["Transaction_amount"].min(),ag_tr["Transaction_amount"].max()),
    animation_frame='Year'
    )
ifig11.update_geos(fitbounds="locations", visible=False)


ifig12 = px.choropleth(
    ag_tr,
    geojson=data,
    featureidkey='properties.ST_NM',
    locations='State',
    color='Transaction_count',
    color_continuous_scale='Rainbow',
    hover_name = 'State',
    height=600, width=600,
    range_color = (ag_tr["Transaction_count"].min(),ag_tr["Transaction_count"].max()),
    animation_frame='Year'
    )
ifig12.update_geos(fitbounds="locations", visible=False)

#Agg_user map 2

ag_us = agg_users.groupby(["State","Year","Quater"])[["reg_userbrand_count","reg_percentage"]].sum()
ag_us.reset_index(inplace=True)

ifig21 = px.choropleth(
    ag_us,
    geojson=data,
    featureidkey='properties.ST_NM',
    locations='State',
    color='reg_userbrand_count',
    color_continuous_scale='Rainbow',
    hover_name = 'State',
    height=600, width=600,
    range_color = (ag_us["reg_userbrand_count"].min(),ag_us["reg_userbrand_count"].max()),
    animation_frame='Year'
    )
ifig21.update_geos(fitbounds="locations", visible=False)

ifig22 = px.choropleth(
    ag_us,
    geojson=data,
    featureidkey='properties.ST_NM',
    locations='State',
    color='reg_percentage',
    color_continuous_scale='Rainbow',
    hover_name = 'State',
    height=600, width=600,
    range_color = (ag_us["reg_percentage"].min(),ag_us["reg_percentage"].max()),
    animation_frame='Year'
    )
ifig22.update_geos(fitbounds="locations", visible=False)

#Map trans Map 3----------


mp_tr = map_trans.groupby(["State","Year",'Quater'])[["transaction_amount","transaction_count"]].sum()
mp_tr.reset_index(inplace=True)

ifig31 = px.choropleth(
    mp_tr,
    geojson=data,
    featureidkey='properties.ST_NM',
    locations='State',
    color='transaction_amount',
    color_continuous_scale='Rainbow',
    hover_data = 'State',
    height=600, width=600,
    range_color = (mp_tr["transaction_amount"].min(),mp_tr["transaction_amount"].max()),
    animation_frame='Year'
    )
ifig31.update_geos(fitbounds="locations", visible=False)

ifig32 = px.choropleth(
    mp_tr,
    geojson=data,
    featureidkey='properties.ST_NM',
    locations='State',
    color='transaction_count',
    color_continuous_scale='Rainbow',
    hover_data = 'State', 
    height=600, width=600,
    range_color = (mp_tr["transaction_count"].min(),mp_tr["transaction_count"].max()),
    animation_frame='Year'
    )
ifig32.update_geos(fitbounds="locations", visible=False)


#Map user Map 4-----

mp_us = map_users.groupby(["State","Year","Quater"])[["reg_users","app_opens"]].sum()
mp_us.reset_index(inplace=True)

ifig41 = px.choropleth(
    mp_us,
    geojson=data,
    featureidkey='properties.ST_NM',
    locations='State',
    color='reg_users',
    color_continuous_scale='Rainbow',
    hover_name = 'State',
    height=600, width=600,
    range_color = (mp_us["reg_users"].min(),mp_us["reg_users"].max()),
    animation_frame='Year'
    )
ifig41.update_geos(fitbounds="locations", visible=False)

ifig42 = px.choropleth(
    mp_us,
    geojson=data,
    featureidkey='properties.ST_NM',
    locations='State',
    color='app_opens',
    color_continuous_scale='Rainbow',
    hover_name = 'State', 
    height=600, width=600,
    range_color = (mp_us["app_opens"].min(),mp_us["app_opens"].max()),
    animation_frame='Year'
    )
ifig42.update_geos(fitbounds="locations", visible=False)

#Top trans Map 5-----


tp_tr = top_trans.groupby(["State","Year",'Quater'])[["transaction_amount","transaction_count"]].sum()
tp_tr.reset_index(inplace=True)

ifig51 = px.choropleth(
    tp_tr,
    geojson=data,
    featureidkey='properties.ST_NM',
    locations='State',
    color='transaction_amount',
    color_continuous_scale='Rainbow',
    hover_data = 'State', title = 'Top Transaction amount analysis',
    height=600, width=600,
    range_color = (tp_tr["transaction_amount"].min(),tp_tr["transaction_amount"].max()),
    animation_frame='Year'
    )
ifig51.update_geos(fitbounds="locations", visible=False)

ifig52 = px.choropleth(
    tp_tr,
    geojson=data,
    featureidkey='properties.ST_NM',
    locations='State',
    color='transaction_count',
    color_continuous_scale='Rainbow',
    hover_data = 'State', title = 'Top Transaction count analysis',
    height=600, width=600,
    range_color = (tp_tr["transaction_count"].min(),tp_tr["transaction_count"].max()),
    animation_frame='Year'
    )
ifig52.update_geos(fitbounds="locations", visible=False)


#Top users Map 6----

tp_us = top_users.groupby(["State","Year",'Quater'])[["reg_users"]].sum()
tp_us.reset_index(inplace=True)

ifig61 = px.choropleth(
    tp_us,
    geojson=data,
    featureidkey='properties.ST_NM',
    locations='State',
    color='reg_users',
    color_continuous_scale='Rainbow',
    hover_data = 'State', title = 'Top Register Users Analysis',
    height=600, width=600,
    range_color = (tp_us["reg_users"].min(),tp_us["reg_users"].max()),
    animation_frame='Year'
    )
ifig61.update_geos(fitbounds="locations", visible=False)


# Tabs
tab1, tab2, tab3 = st.tabs(["Aggregate", "Map", "Top"])
with tab1:
    if st.button('Aggregate Transaction'):
        
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(":green[Aggregate Transaction amount Analysis]")
            fig11 = px.bar(agg_trans, x = "State", y = "Transaction_amount",
                        color='Transaction_type',hover_name = 'State',
                        animation_frame='Year', range_y=[0, 13000000000000])
            st.plotly_chart(fig11)

        with col2:
            st.subheader(":green[Aggregate Transaction count Analysis]")
            fig12 = px.scatter(agg_trans, x = "State", y = "Transaction_count",
                         color = 'Transaction_type',hover_name='State',size = "Year",
                        animation_frame='Year',range_y=[0, 1000000000])
            st.plotly_chart(fig12)
            
        col3,col4 = st.columns(2)
        
        with col3:
            st.subheader(":green[Aggregate Transaction amount Analysis]")
            st.plotly_chart(ifig11, theme="streamlit", use_container_width=True)
        
        with col4:
            st.subheader(":green[Aggregate Transaction count Analysis]")
            st.plotly_chart(ifig12, theme="streamlit", use_container_width=True)
        
    if st.button('Aggregate User'):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(":green[TN User registered percentage Analysis]")
            fig21 = px.bar(agg_users, x = "user_brand", y = "reg_percentage",width = 600,
                color='user_brand',hover_name = 'State',
               animation_frame='Year')
            st.plotly_chart(fig21)
        with col2:
            st.subheader(":green[TN user brand with Quater Analysis]")
            ag_us = agg_users[agg_users["State"] == "Tamil Nadu"]
            ag_us.reset_index(inplace = True)
            fig22 = px.sunburst(ag_us,path = ['user_brand','Quater'],values='Year',color='user_brand',
                                hover_name = "State",height=400,width=400)
            st.plotly_chart(fig22)
    
        col3,col4 = st.columns(2)
        
        with col3:
            st.subheader(":green[Aggregate User Register brands Analysis]")
            st.plotly_chart(ifig21, theme="streamlit", use_container_width=True)
        
        with col4:
            st.subheader(":green[Aggregate User Register count Analysis]")
            st.plotly_chart(ifig22, theme="streamlit", use_container_width=True)
        
        



with tab2:
    if st.button('Map Transaction'):
        
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(":green[Map Transaction amount Analysis]")
            fig31 = px.bar(map_trans, x = "State", y = "transaction_amount",
                        color='transaction_amount',hover_name = 'State',
                        animation_frame='Year',range_y=[0,15000000000000])
            st.plotly_chart(fig31)

        with col2:
            st.subheader(":green[Map Transaction count Analysis]")
            fig32 = px.scatter(map_trans, x = "State", y = "transaction_count",color_continuous_scale='Rainbow',
                         color = 'transaction_count',hover_name='State',
                         range_color = (map_trans["transaction_count"].min(),map_trans["transaction_count"].max()),size = "Year",
                        animation_frame='Year',range_y=[0, 1500000000])
            st.plotly_chart(fig32)
            
        col3,col4 = st.columns(2)
        
        with col3:
            st.subheader(":green[Map Transaction amount Analysis]")
            st.plotly_chart(ifig31, theme="streamlit", use_container_width=True)
        
        with col4:
            st.subheader(":green[Map Transaction count Analysis]")
            st.plotly_chart(ifig32, theme="streamlit", use_container_width=True)
        
    if st.button('Map User'):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(":green[Map registered users Analysis]")
            fig41 = px.bar(map_users, x = "State", y = "reg_users",width = 600,color_continuous_scale='Rainbow',
                color='reg_users',hover_name="State",range_color = (map_users["reg_users"].min(),map_users["reg_users"].min()),
               animation_frame='Year',range_y = [0,250000000])
            st.plotly_chart(fig41)
        with col2:
            st.subheader(":green[Map user app opens Analysis]")
            fig42 = px.scatter(map_users, x = "State", y = "app_opens",width = 600,
                color='Quater',hover_name = "State",size = "Year",
               animation_frame='Year',range_y = [0,500000000])

            st.plotly_chart(fig42)
    
        col3,col4 = st.columns(2)
        
        with col3:
            st.subheader(":green[Map reg users Analysis]")
            st.plotly_chart(ifig41, theme="streamlit", use_container_width=True)
        
        with col4:
            st.subheader(":green[Map app opens Analysis]")
            st.plotly_chart(ifig42, theme="streamlit", use_container_width=True)
       

with tab3:
    if st.button('Top Transaction'):
        
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(":green[Top Transaction amount Analysis]")
            tp_tr = top_trans[top_trans["State"] == "Tamil Nadu"]
            fig51 = px.bar(tp_tr, x = "Quater", y = "transaction_count",width = 600,
                color='Quater',hover_name="State",
               animation_frame='Year',range_y = [0,40000000])
            st.plotly_chart(fig51)

        with col2:
            st.subheader(":green[Top Transaction count Analysis]")
            fig52 = px.sunburst(tp_tr, path = ["State","Year","Quater"], values= "transaction_count")
            st.plotly_chart(fig52)
            
        col3,col4 = st.columns(2)
        
        with col3:
            st.subheader(":green[Top Transaction amount Analysis]")
            st.plotly_chart(ifig51, theme="streamlit", use_container_width=True)
        
        with col4:
            st.subheader(":green[Top Transaction count Analysis]")
            st.plotly_chart(ifig52, theme="streamlit", use_container_width=True)
        
    if st.button('Top User'):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(":green[Top registered users Analysis]")
            tp_us = top_users[top_users["State"] == "Tamil Nadu"]
            fig61 = px.bar(tp_us, x = "Quater", y = "reg_users",width = 600,color_continuous_scale='tempo',

                color='reg_users',hover_name="State",range_color = (map_users["reg_users"].min(),map_users["reg_users"].min()),
                animation_frame='Year',range_y=[0, 2000000])
            st.plotly_chart(fig61)
                
        with col2:
            st.subheader(":green[Top registered user Analysis]")
            fig62 = px.scatter(tp_us, x = "Quater", y = "reg_users",width = 600,color_continuous_scale='Rainbow',
                color='reg_users',hover_name="State",range_color = (map_users["reg_users"].min(),map_users["reg_users"].min()),size = "Quater",
                animation_frame='Year',range_y=[0, 300000])
            st.plotly_chart(fig62)
    
        col3,col4 = st.columns(2)
        
        with col3:
            st.subheader(":green[Top reg users Analysis]")
            st.plotly_chart(ifig61, theme="streamlit", use_container_width=True)
        
        with col4:
            st.subheader(":green[Top reg users Analysis]")
            
            fig63 = px.sunburst(tp_us, path = ["Quater","Year"],values = "reg_users",width = 600,color_continuous_scale='twilight',
                color='reg_users',hover_name="State",range_color = (map_users["reg_users"].min(),map_users["reg_users"].min()))
            st.plotly_chart(fig63, theme="streamlit", use_container_width=True)
       
