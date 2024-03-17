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


def agg_tran():
    #1 Aggregated/trans
    #This is to direct the path to get the data as states
    path="C:/Users/DELL/Desktop/Phonepay/pulse/data/aggregated/transaction/country/india/state/"
    Agg_state_list=os.listdir(path)
    #Agg_state_list--> to get the list of states in India

    #This is to extract the data's to create a dataframe

    clm1={'state':[], 'year':[],'quater':[],'transaction_type':[], 'transaction_count':[], 'transaction_amount':[]}

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
                    clm1['transaction_type'].append(Name)
                    clm1['transaction_count'].append(count)
                    clm1['transaction_amount'].append(amount)
                    clm1['state'].append(i)
                    clm1['year'].append(j)
                    clm1['quater'].append(int(k.strip('.json')))
    #Succesfully created a dataframe
    agg_trans=pd.DataFrame(clm1)

    agg_trans['state']=agg_trans['state'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
    agg_trans['state']=agg_trans['state'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
    agg_trans['state']=agg_trans['state'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
    agg_trans['state']=agg_trans['state'].str.replace("-"," ")
    agg_trans['state']=agg_trans['state'].str.title()
    agg_trans['transaction_amount']=agg_trans['transaction_amount'].round()
    agg_trans['year']=agg_trans['year'].astype(int)
    
    return agg_trans

agg_trans = agg_tran()



def agg_user():
    #2 aggregated/User DF

    #This is to direct the path to get the data as states
    path="C:/Users/DELL/Desktop/Phonepay/pulse/data/aggregated/user/country/india/state/"
    Agg_state_list=os.listdir(path)

    #Agg_state_list--> to get the list of states in India

    clm2={'state':[], 'year':[],'quater':[],'user_brand':[], 'reg_userbrand_count':[], 'reg_percentage':[]}

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
                        clm2['state'].append(i)
                        clm2['year'].append(j)
                        clm2['quater'].append(int(k.strip('.json')))
                except:
                    pass
    #Succesfully created a dataframe
    agg_users=pd.DataFrame(clm2)

    agg_users['state']=agg_users['state'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
    agg_users['state']=agg_users['state'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
    agg_users['state']=agg_users['state'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
    agg_users['state']=agg_users['state'].str.replace("-"," ")
    agg_users['state']=agg_users['state'].str.title()
    agg_users['reg_percentage']=agg_users['reg_percentage'].round()
    agg_users['year']=agg_users['year'].astype(int)
    
    return agg_users

agg_users = agg_user()

    
def map_tran():
    #This is to direct the path to get the data as states

    path="C:/Users/DELL/Desktop/Phonepay/pulse/data/map/transaction/hover/country/india/state/"
    map_state_list=os.listdir(path)
    #map_state_list--> to get the list of states in India


    #This is to extract the data's to create a dataframe

    clm3={'state':[], 'year':[],'quater':[],'district_name':[], 'transaction_count':[], 'transaction_amount':[]}

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
                        clm3['state'].append(i)
                        clm3['year'].append(j)
                        clm3['quater'].append(int(k.strip('.json')))
                except Exception as e:
                    print(f"Error processing file '{p_k}': {e}")

    #Succesfully created a dataframe
    map_trans=pd.DataFrame(clm3)

    map_trans['state']=map_trans['state'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
    map_trans['state']=map_trans['state'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
    map_trans['state']=map_trans['state'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
    map_trans['state']=map_trans['state'].str.replace("-"," ")
    map_trans['state']=map_trans['state'].str.title()
    map_trans['transaction_amount']=map_trans['transaction_amount'].round()
    map_trans['year']=map_trans['year'].astype(int)
    
    return map_trans

map_trans = map_tran()

def map_user():
    #4 map/User DF----

    #This is to direct the path to get the data as states

    path="C:/Users/DELL/Desktop/Phonepay/pulse/data/map/user/hover/country/india/state/"
    map_state_list=os.listdir(path)
    #map_state_list--> to get the list of states in India


    #This is to extract the data's to create a dataframe

    clm4={'state':[], 'year':[],'quater':[],'district_name':[], 'reg_users':[], 'app_opens':[]}

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
                    clm4['district_name'].append(district)
                    clm4['reg_users'].append(regusers)
                    clm4['app_opens'].append(appopens)
                    clm4['state'].append(i)
                    clm4['year'].append(j)
                    clm4['quater'].append(int(k.strip('.json')))

    #Succesfully created a dataframe
    map_users=pd.DataFrame(clm4)

    map_users['state']=map_users['state'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
    map_users['state']=map_users['state'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
    map_users['state']=map_users['state'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
    map_users['state']=map_users['state'].str.replace("-"," ")
    map_users['state']=map_users['state'].str.title()
    map_users['year']=map_users['year'].astype(int)

    return map_users
map_users = map_user()

def top_tran():
    #5 Top transaction DF ---

    #This is to direct the path to get the data as states

    path="C:/Users/DELL/Desktop/Phonepay/pulse/data/top/transaction/country/india/state/"
    top_state_list=os.listdir(path)
    #top_state_list--> to get the list of states in India


    #This is to extract the data's to create a dataframe

    clm5={'state':[], 'year':[],'quater':[],'pincodes':[], 'transaction_count':[], 'transaction_amount':[]}

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
                    clm5['state'].append(i)
                    clm5['year'].append(j)
                    clm5['quater'].append(int(k.strip('.json')))
    #Succesfully created a dataframe
    top_trans=pd.DataFrame(clm5)

    top_trans['state']=top_trans['state'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
    top_trans['state']=top_trans['state'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
    top_trans['state']=top_trans['state'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
    top_trans['state']=top_trans['state'].str.replace("-"," ")
    top_trans['state']=top_trans['state'].str.title()
    top_trans['transaction_amount']=top_trans['transaction_amount'].round()
    top_trans['year']=top_trans['year'].astype(int)

    return top_trans
top_trans = top_tran()

def top_user():
        #6 Top country----

    #This is to direct the path to get the data as states

    path="C:/Users/DELL/Desktop/Phonepay/pulse/data/top/user/country/india/state/"
    top_state_list=os.listdir(path)
    #top_state_list--> to get the list of states in India


    #This is to extract the data's to create a dataframe

    clm6={'state':[], 'year':[],'quater':[],'pincodes': [], 'reg_users':[]}

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
                    clm6['pincodes'].append(Name)
                    clm6['reg_users'].append(reg_users)
                    clm6['state'].append(i)
                    clm6['year'].append(j)
                    clm6['quater'].append(int(k.strip('.json')))


    #Succesfully created a dataframe
    top_users=pd.DataFrame(clm6)

    top_users['state']=top_users['state'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
    top_users['state']=top_users['state'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
    top_users['state']=top_users['state'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
    top_users['state']=top_users['state'].str.replace("-"," ")
    top_users['state']=top_users['state'].str.title()
    top_users['year']=top_users['year'].astype(int)
    
    return top_users
top_users = top_user()


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


st.set_page_config(layout= "wide")
st.title(':blue[Phonepe Pulse Data Visualization and Exploration]')


#MAP----
imurl = ("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson")
response = requests.get(imurl)
data = json.loads(response.content)
states_name = []
for i in data['features']:
    states_name.append(i['properties']["ST_NM"])
states_name.sort()

import pandas as pd
import plotly.express as px
import streamlit as st
import psycopg2

def ag_trans():
    engine = create_engine('postgresql://postgres:Lavan123@localhost:5432/phonepe')
    df1 = pd.read_sql('agg_trans', engine)
    
    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(2)
    row4 = st.columns(2)
    
    with row1[0]:
        column1 = df1["year"].unique()
        selected_yr = st.selectbox("Choose a year to see both transaction amount and count", column1) 

    with row2[0]:
        st.subheader(":green[Transaction amount Analysis]")
        ag_year = df1[df1["year"]==selected_yr]
        fig1 = px.bar(ag_year, x="state", y="transaction_amount",
                      color = "transaction_type", hover_name = "state")
        
        # Add dropdown menu for year selection on the plot
        st.plotly_chart(fig1)
        
    with row2[1]:
        st.subheader(":green[Transaction count Analysis]")
        fig2 = px.bar(ag_year, x="state", y="transaction_count",
                      color = "transaction_type", hover_name = "state")
        
        # Add dropdown menu for year selection on the plot
        st.plotly_chart(fig2)
        
    with row3[0]:
        coloum1 = df1["year"].unique()
        selected_year = st.selectbox("Select a year", coloum1)
        
    with row4[0]:
        st.subheader(":green[Transaction Amount Analysis]")
        agg_tran_yr = df1[df1["year"]==selected_year]
        agg_map = agg_tran_yr.groupby(['state',"year"])[['transaction_count', 'transaction_amount']].sum()
        agg_map.reset_index(inplace = True)

        fig3 = px.choropleth(
            agg_map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='transaction_amount',
            color_continuous_scale='turbo',
            range_color = (agg_map['transaction_amount'].min(), agg_map['transaction_amount'].max()))

        fig3.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(fig3)
        
    with row4[1]:
        st.subheader(":green[Transaction Count Analysis]")
        fig4 = px.choropleth(
            agg_map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='transaction_count',
            color_continuous_scale='turbo',
            range_color = (agg_map['transaction_count'].min(), agg_map['transaction_count'].max()))

        fig4.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(fig4)

    
def ag_users():
    engine = create_engine('postgresql://postgres:Lavan123@localhost:5432/phonepe')
    df2 = pd.read_sql('agg_users', engine)
    
    row1 = st.columns(4)
    row2 = st.columns(1)
    row3 = st.columns(2)
    row4 = st.columns(2)
    with row1[0]:
        column1 = df2["year"].unique()
        selected_yr = st.selectbox("Choose a year", column1) 

    with row1[1]:
        column2 = df2["user_brand"].unique()
        selected_brand = st.selectbox("Choose a brand",column2)
        
    with row2[0]:
        st.subheader(":green[Aggregate User brand Analysis]")
        # Assuming selected_yr and selected_brand are defined earlier in your code
        ag_year = df2[df2["year"] == selected_yr]
        ag_brand = ag_year[ag_year["user_brand"] == selected_brand]
        
        fig1 = px.scatter(ag_brand, x="state", y="reg_userbrand_count",
                        color="state", hover_name="state", size="reg_userbrand_count",range_x= [0, 36],
                        )
        
        
    
        # Create a dropdown menu to switch between scatter and bar plot types
        button_x = 0.01
        button_y = 1.7
        fig1.update_layout(updatemenus=[
            {
                "buttons": [{
                        "args": [{"type": "scatter"}],
                        "label": "Scatter Plot",
                        "method": "restyle"},
                    {"args": [{"type": "bar"}],
                        "label": "Bar Plot",
                        "method": "restyle"},
                    
                ],
                "direction": "down","showactive": True,"x": 0.01,"y": 1.7}])
        fig1.update_layout(updatemenus=[dict(x=button_x, y=button_y, xanchor='right', yanchor='top')])
        st.plotly_chart(fig1,width = "auto")
        
        
    with row3[0]:
        state = agg_users['state'].unique()
        sub_col = st.columns(2)
        with sub_col[0]:
            selected_state = st.selectbox("Select a state", ['All states'] + list(state))  
        with sub_col[1]:
            selected_yr1 = st.selectbox("Choose a year", column1,key="unique_key1") 
            
    with row4[0]:
        ag_year1 = df2[df2["year"] == selected_yr1]
        ag_user_map = ag_year1.groupby(['state','user_brand'])[['reg_userbrand_count']].sum()
        ag_user_map.reset_index(inplace = True)

        if selected_state == 'All states':
            stateau = ag_user_map
        else:
            stateau = ag_user_map[ag_user_map['state'] == selected_state]
        st.subheader(":green[State User registered percentage Analysis]")
        fig2 = px.bar(stateau, x = "user_brand", y = "reg_userbrand_count",width = 600,
                color='user_brand',hover_name = 'state')
        st.plotly_chart(fig2)
          
    with row4[1]:
        st.subheader(":green[User Registered brands Analysis]")
        agg_map = ag_year1.groupby(['state'])[['reg_userbrand_count']].sum()
        agg_map.reset_index(inplace = True)

        fig3 = px.choropleth(
            agg_map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='reg_userbrand_count',
            color_continuous_scale='turbo',
            range_color = (agg_map['reg_userbrand_count'].min(), agg_map['reg_userbrand_count'].max()),
            )

        fig3.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(fig3)
        

def mp_trans():


    # Create engine and read data from SQL database
    engine = create_engine('postgresql://postgres:Lavan123@localhost:5432/phonepe')
    df3 = pd.read_sql('SELECT * FROM map_trans', engine)  # Correct SQL query string

    row1= st.columns(2)
    row2= st.columns(2)
    row3= st.columns(2)
    row4= st.columns(2)
    row5 = st.columns(2)
    with row1[0]:
        column1 = df3["year"].unique()
        selected_year = st.selectbox("Select a year", column1, key="year_selectbox")  # Unique key added

    with row1[1]:
        states = df3['state'].unique()
        selected_state = st.selectbox("Select a state", ['All states'] + list(states), key="state_selectbox")  # Unique key added

# Other parts of your code remain unchange
        if selected_state == 'All states':
            stateMT = df3.groupby('state')[['transaction_count', 'transaction_amount']].sum().reset_index()
        else:
            stateMT = df3[df3['state'] == selected_state]

    with row2[0]:
        if selected_state != 'All states':
            st.subheader(":green[Map Transaction amount Analysis]")
            mp_tr = df3.query('state == @selected_state and year == @selected_year')
            fig1 = px.bar(mp_tr, x=mp_tr['district_name'].apply(lambda x: x.replace("district", "")), y="transaction_amount",
                        color='transaction_amount', hover_name='district_name',color_continuous_scale='Viridis')
            st.plotly_chart(fig1)

    with row2[1]:
        if selected_state != 'All states':
            st.subheader(":green[Map Transaction count Analysis]")
            fig2 = px.bar(mp_tr, x=mp_tr['district_name'].apply(lambda x: x.replace("district", "")), y="transaction_count",
                            color='transaction_count', hover_name='district_name', color_continuous_scale='Viridis',
                            range_color=(df3["transaction_count"].min(), df3["transaction_count"].max()),
                            animation_frame='year')
            st.plotly_chart(fig2)

    with row3[0]:
        coloum1 = df3["year"].unique()
        selected_year = st.selectbox("Select a year", coloum1)

    with row4[0]:
        st.subheader(":green[Map Transaction amount Analysis]")
        agg_tran_yr = df3[df3["year"] == selected_year]
        agg_map = agg_tran_yr.groupby(['state', "year"])[['transaction_count', 'transaction_amount']].sum().reset_index()
        fig3 = px.choropleth(
            agg_map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='transaction_amount',
            color_continuous_scale='turbo',
            range_color=(agg_map['transaction_amount'].min(), agg_map['transaction_amount'].max())
        )
        fig3.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig3)

    with row4[1]:
        st.subheader(":green[Map Transaction count Analysis]")
        fig4 = px.choropleth(
            agg_map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='transaction_count',
            color_continuous_scale='turbo',
            range_color=(agg_map['transaction_count'].min(), agg_map['transaction_count'].max())
        )
        fig4.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig4)
    
    with row5[0]:
        st.subheader(":green[Map Transaction count Analysis]")
        fig4 = px.choropleth(
            mp_tr,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='transaction_count',
            color_continuous_scale='turbo',
            range_color=(agg_map['transaction_count'].min(), agg_map['transaction_count'].max())
        )
        fig4.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig4)
        

def mp_users():
    engine = create_engine('postgresql://postgres:Lavan123@localhost:5432/phonepe')
    df4 = pd.read_sql('map_users', engine)
    state = df4['state'].unique()
    row1 = st.columns(2)
    row2 = st.columns(2)
    
    with row1[0]:
        sub_col = st.columns(2)
        with sub_col[0]:
            coloum1 = df4["year"].unique()
            selected_year = st.selectbox("Select a year", coloum1, key = "year_select_box")
        with sub_col[1]:
            column2 = df4["quater"].unique()
            selected_qt = st.selectbox("select a quater", column2,)

    with row2[0]:
        mp_year = df4[df4["year"]==selected_year]
        mp_qt = mp_year[mp_year["quater"]==selected_qt]
        st.subheader(":green[Map registered users Analysis]")
        fig41 = px.bar(mp_qt, x = "state", y = "reg_users",width = 600,color_continuous_scale='Viridis',
            color='reg_users',hover_name="state",
            range_color = (map_users["reg_users"].min(),map_users["reg_users"].min()))
        st.plotly_chart(fig41)
        
    with row2[1]:
        st.subheader(":green[Map user app opens Analysis]")
        fig42 = px.scatter(mp_qt, x = "state", y = "reg_users",width = 600,
            color='reg_users',hover_name = "state",color_continuous_scale='Plasma')
        st.plotly_chart(fig42)


def tp_trans():

    engine = create_engine('postgresql://postgres:Lavan123@localhost:5432/phonepe')
    df5 = pd.read_sql('top_trans', engine)
    
    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(2)
    row4 = st.columns(2)
    
    with row1[0]:
        sub_col1 = st.columns(2)
        with sub_col1[0]:
            column1 = df5["year"].unique()
            selected_year = st.selectbox("Choose a year", column1) 
    
        with sub_col1[1]:
            states = df5['state'].unique()
            selected_state = st.selectbox("Select a state", ['All states'] + list(states), key="state_selectbox")
    with row2[0]:
        ag_year = df5[df5["year"]==selected_year]
        st.subheader(":green[Top Transaction amount Analysis]")
        if selected_state != 'All states':
            mp_tr = df5.query('state == @selected_state and year == @selected_year')
        fig1 = px.scatter(mp_tr, x = "transaction_count", y = "transaction_amount",
                        color='transaction_amount',hover_name = 'transaction_amount',
                        color_continuous_scale='Viridis')
        st.plotly_chart(fig1)
        if selected_state == 'All states':
            stateMT = df6.groupby(['state','quater','year'])[['transaction_amount','transaction_count']].sum().reset_index()
        else:
            stateMT = df6[df6['state'] == selected_state]
    with row2[1]:
        st.subheader(":green[Top Transaction count Analysis]")
        fig2 = px.bar(ag_year, x = "quater", y = "transaction_count",color_continuous_scale='Rainbow',
                         color = 'transaction_count',hover_name='state',
                         range_color = (map_trans["transaction_count"].min(),map_trans["transaction_count"].max()),
                        animation_frame='year')
        st.plotly_chart(fig2)

        
    with row3[0]:
        coloum1 = df5["year"].unique()
        selected_year = st.selectbox("Select a year", coloum1)
        
    with row4[0]:
        st.subheader(":green[Top Transaction amount Analysis]")
        tp_tran_yr = df5[df5["year"]==selected_year]
        top_map = tp_tran_yr.groupby(['state',"year"])[['transaction_count', 'transaction_amount']].sum()
        top_map.reset_index(inplace = True)

        fig3 = px.choropleth(
            top_map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='transaction_amount',
            color_continuous_scale='turbo',
            range_color = (top_map['transaction_amount'].min(), top_map['transaction_amount'].max()),)

        fig3.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(fig3)
        
    with row4[1]:
        st.subheader(":green[Top Transaction count Analysis]")
        fig4 = px.choropleth(
            top_map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='transaction_count',
            color_continuous_scale='turbo',
            range_color = (top_map['transaction_count'].min(), top_map['transaction_count'].max()))

        fig4.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(fig4)

    


def tp_users():
    
    engine = create_engine('postgresql://postgres:Lavan123@localhost:5432/phonepe')
    df6 = pd.read_sql('top_users', engine)
    
    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(2)
    row4 = st.columns(2)
    
    with row1[0]:
        sub_col1 = st.columns(2)
        with sub_col1[0]:
            column1 = df6["year"].unique()
            selected_year = st.selectbox("Choose a years", column1) 
    
        with sub_col1[1]:
            states = df6['state'].unique()
            selected_state = st.selectbox("Select a state", ['All states'] + list(states), key="state_selectbox")
        
    with row2[0]:
        st.subheader(":green[Top registered users Analysis]")
        if selected_state != 'All states':
            mp_tr = df6.query('state == @selected_state and year == @selected_year')
        fig61 = px.bar(mp_tr, x = "quater", y = "reg_users",width = 600,color_continuous_scale='tempo',
                       color='reg_users',hover_name="state",
                range_color = (top_users["reg_users"].min(),top_users["reg_users"].min()))
        st.plotly_chart(fig61)
        if selected_state == 'All states':
            stateMT = df6.groupby(['state','quater','year'])[['reg_users']].sum().reset_index()
        else:
            stateMT = df6[df6['state'] == selected_state]
        

    with row3[0]:
        coloum1 = df6["year"].unique()
        selected_year = st.selectbox("Select a year", coloum1)
        
    with row4[0]:
        st.subheader(":green[Top Users Analysis]")
        tp_tran_yr = df6[df6["year"]==selected_year]
        top_us= tp_tran_yr.groupby(['state',"year"])[['reg_users']].sum()
        top_us.reset_index(inplace = True)
 
        fig3 = px.choropleth(
            top_us,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='reg_users',
            color_continuous_scale='turbo',
            range_color = (top_us['reg_users'].min(), top_us['reg_users'].max()),)

        fig3.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(fig3)
        
def a_trans():
    mydb = psycopg2.connect(host = 'localhost',user = 'postgres',password = 'Lavan123',database = 'phonepe',port = 5432)
    mycursor = mydb.cursor()

    query1 = ''' SELECT state, sum(transaction_amount) AS transaction_amount 
                    from agg_trans
                    GROUP BY state ORDER BY transaction_amount 
                    DESC LIMIT 10; '''
                    
    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()
    dfone = pd.DataFrame(table1, columns = ['state', 'transaction_amount'])
    st.subheader(":green[Aggregated Highest Transaction Amount]")
    fig_1 = px.bar(dfone, x = 'state', y = 'transaction_amount',
                color_discrete_sequence = px.colors.sequential.Aggrnyl, hover_name = 'state')
    st.plotly_chart(fig_1)

    query1 = ''' SELECT state, avg(transaction_amount) AS transaction_amount 
                    from agg_trans
                    GROUP BY state ORDER BY transaction_amount 
                    Desc LIMIT 10; '''
                    
    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()
    
    dfone1 = pd.DataFrame(table1, columns = ['state', 'transaction_count'])
    st.subheader(":green[Aggregated Average Transaction Count]")
    fig_2 = px.bar(dfone1, x = 'state', y = 'transaction_count', 
                color_discrete_sequence = px.colors.sequential.Aggrnyl, hover_name = 'state')
    st.plotly_chart(fig_2)


def m_trans():
    mydb = psycopg2.connect(host='localhost', user='postgres', password='Lavan123', database='phonepe', port=5432)
    mycursor = mydb.cursor()

    query1 = '''SELECT state, sum(transaction_amount) AS transaction_amount 
                FROM map_trans
                GROUP BY state ORDER BY transaction_amount DESC LIMIT 10;'''
                    
    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()
    dfone = pd.DataFrame(table1, columns=['state', 'transaction_amount'])
    st.subheader(":green[Top 10 Map Transaction Amount]")
    fig_1 = px.bar(dfone, x='state', y='transaction_amount', color='state',
                   color_continuous_scale=px.colors.sequential.Aggrnyl, hover_name='state')
    st.plotly_chart(fig_1)

    query2 = '''SELECT state, avg(transaction_amount) AS transaction_amount 
                FROM map_trans
                GROUP BY state ORDER BY transaction_amount DESC LIMIT 10;'''
                    
    mycursor.execute(query2)
    table2 = mycursor.fetchall()
    mydb.commit()
    st.subheader(":green[Average Map Transaction Amount]")
    dftwo = pd.DataFrame(table2, columns=['state', 'transaction_amount'])

    fig_2 = px.bar(dftwo, x='state', y='transaction_amount',
                   color='state', color_discrete_sequence=px.colors.sequential.Aggrnyl, hover_name='state')
    st.plotly_chart(fig_2)

    mycursor.close()
    mydb.close()
    
    
def t_trans():
    mydb = psycopg2.connect(host='localhost', user='postgres', password='Lavan123', database='phonepe', port=5432)
    mycursor = mydb.cursor()

    query1 = '''SELECT state, sum(transaction_amount) AS transaction_amount 
                FROM top_trans
                GROUP BY state ORDER BY transaction_amount DESC LIMIT 10;'''
                    
    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()
    dfone = pd.DataFrame(table1, columns=['state', 'transaction_amount'])
    st.subheader(":green[Top 10 Map Transaction Amount]")
    fig_1 = px.bar(dfone, x='state', y='transaction_amount', color='state',
                   color_continuous_scale=px.colors.sequential.Aggrnyl, hover_name='state')
    st.plotly_chart(fig_1)

    query2 = '''SELECT state, avg(transaction_amount) AS transaction_amount 
                FROM top_trans
                GROUP BY state ORDER BY transaction_amount DESC LIMIT 10;'''
                    
    mycursor.execute(query2)
    table2 = mycursor.fetchall()
    mydb.commit()
    #st.subheader(":green[Average Map Transaction Amount]")
    dftwo = pd.DataFrame(table2, columns=['state', 'transaction_amount'])

    fig_2 = px.bar(dftwo, x='state', y='transaction_amount',
                   color='state', color_discrete_sequence=px.colors.sequential.Aggrnyl, hover_name='state')
    st.plotly_chart(fig_2)

    mycursor.close()
    mydb.close()

option = st.sidebar.radio(":blue[Choose your page]", ["Aggregate", "Map", "Top", "Top charts"])

#Top Charts----

def trans_amount(table_nm):
    mydb = psycopg2.connect(host = 'localhost',user = 'postgres',password = 'Lavan123',database = 'phonepe',port = 5432)
    mycursor = mydb.cursor()

    query1 = f'''SELECT state, sum(transaction_amount) AS transaction_amount 
                    from {table_nm}
                    GROUP BY state ORDER BY transaction_amount 
                    DESC LIMIT 10; '''
                    
    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()
    dfone = pd.DataFrame(table1, columns = ['state', 'transaction_amount'])
    st.subheader(":green[Top Transaction Amount]")
    fig_1 = px.bar(dfone, x = 'state', y = 'transaction_amount',
                color_discrete_sequence = px.colors.sequential.Aggrnyl, hover_name = 'state',)
    st.plotly_chart(fig_1)

    query2 = f'''SELECT state, avg(transaction_amount) AS transaction_amount 
                    from {table_nm}
                    GROUP BY state ORDER BY transaction_amount desc
                    ; '''
                    
    mycursor.execute(query2)
    table2 = mycursor.fetchall()
    mydb.commit()
    dftwo = pd.DataFrame(table2, columns = ['state', 'transaction_amount'])
    st.subheader(":green[Average Transaction Amount]")
    fig_2 = px.bar(dftwo, y = 'state', x = 'transaction_amount', title = 'Average Transaction Amount',
                 color_discrete_sequence = px.colors.sequential.BuPu_r, hover_name = 'state',height=650,width = 1000,
                orientation='h',color='state',)
    st.plotly_chart(fig_2)

#trans_count----

def trans_count(table_nm):
    mydb = psycopg2.connect(host = 'localhost',user = 'postgres',password = 'Lavan123',database = 'phonepe',port = 5432)
    mycursor = mydb.cursor()

    query1 = f'''SELECT state, sum(transaction_count) AS transaction_count 
                    from {table_nm}
                    GROUP BY state ORDER BY transaction_count 
                    DESC LIMIT 10; '''
                    
    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()
    dfone = pd.DataFrame(table1, columns = ['state', 'transaction_count'])
    st.subheader(":green[Top 10 Transaction Count]")
    fig_1 = px.bar(dfone, x = 'state', y = 'transaction_count',
                color_discrete_sequence = px.colors.sequential.Viridis, hover_name = 'state',)
    st.plotly_chart(fig_1)
    
    query2 = f'''SELECT state, avg(transaction_count) AS transaction_count 
                    from {table_nm}
                    GROUP BY state ORDER BY transaction_count desc
                    ; '''
                    
    mycursor.execute(query2)
    table2 = mycursor.fetchall()
    mydb.commit()
    dftwo = pd.DataFrame(table2, columns = ['state', 'transaction_count'])
    st.subheader(":green[Average Transaction count]")
    fig_2 = px.bar(dftwo, y = 'state', x = 'transaction_count', title = 'Average Transaction Count',
                 color_discrete_sequence = px.colors.sequential.PuBuGn, hover_name = 'state',height=650,width = 1000,
                orientation='h',color='state',)
    st.plotly_chart(fig_2)
    

def ag_us():
    mydb = psycopg2.connect(host = 'localhost',user = 'postgres',password = 'Lavan123',database = 'phonepe',port = 5432)
    mycursor = mydb.cursor()

    query1 = f'''SELECT state, user_brand, avg(reg_userbrand_count) AS usersbrand_count 
                    from agg_users
                    GROUP BY state,user_brand ORDER BY usersbrand_count desc '''
                    
    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()
    dfone = pd.DataFrame(table1, columns = ['state', 'usersbrand_count', 'user_brand'])
    st.subheader(":green[Transaction Count of Aggregated User]")
    fig_1 = px.bar(dfone, x = 'state', y = 'usersbrand_count',
                color_discrete_sequence = px.colors.sequential.Aggrnyl, hover_name = 'user_brand',
                height = 650)
    st.plotly_chart(fig_1)
    
if option == "Aggregate":
    op = st.radio("",["Aggregated Transaction", "Aggregated Users"] )
    
    if op == "Aggregated Transaction":
        ag_trans()
    if op == "Aggregated Users":
        ag_users()
        
    
if option =="Map":
    op = st.radio("",["Map Transaction", "Map Users"])
    if op == ("Map Transaction"):
        mp_trans()
    if op == ("Map Users"):
        mp_users()

        
if option =="Top":
    op = st.radio("",["Top Transaction", "Top Users"])
    if op == ("Top Transaction"):
        tp_trans()
    if op == ("Top Users"):
        tp_users()


if option =="Top charts":
    option = st.selectbox(":violet[Select figures to display]",
              ["1.Aggregated Transaction Amount",
               "2.Map Transaction Amount",
               "3.Top Transaction Amount",
               "4.Aggregated Transaction Count",
               "5.Map Transaction Count",
               "6.Top Transaction Count",
               "7.Transaction Count of Aggregated User"])

    if option == "1.Aggregated Transaction Amount":
        trans_amount("agg_trans")
    if option == "2.Map Transaction Amount":
        trans_amount("map_trans")
    if option == "3.Top Transaction Amount":
        trans_amount("top_trans")
    if option == "4.Aggregated Transaction Count":
        trans_count("agg_trans")
    if option == "5.Map Transaction Count":
        trans_count("map_trans")
    if option == "6.Top Transaction Count":
        trans_count("top_trans")
    if option == "7.Transaction Count of Aggregated User":
        ag_us()
    
