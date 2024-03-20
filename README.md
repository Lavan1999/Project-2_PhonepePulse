# Phonepe-Project

Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly

Problem Statement:
1. Extract data from the Phonepe pulse Github repository through scripting and
clone it..
2. Transform the data into a suitable format and perform any necessary cleaning
and pre-processing steps.
3. Insert the transformed data into a MySQL database for efficient storage and
retrieval.
4. Create a live geo visualization dashboard using Streamlit and Plotly in Python
to display the data in an interactive and visually appealing manner.
5. Fetch the data from the MySQL database to display in the dashboard.
6. Provide at least 10 different dropdown options for users to select different
facts and figures to display on the dashboard.


Workflow of the Project:

Data Collection:

1.The first step is to collect data from the Github using the Github link. 2. Once created the clone of GIT-HUB repository then,
imported required libraries for the program.
2.Extracted from the Github link used to retrieve Aggregated Transaction, Aggregated User, Map Transaction, Map user, Top Transaction, Top user. 
3.I have used this to connect direct path to get the data as states for Python to make requests to the Data and the responses are Collected as a Dictionary (Data Collection)

Create DataFrame:

1.Once the Data Collection is done, then I used pandas to create dataframe for the collected datas
For the 6 Dataset of
1.Aggregated Transaction, 
2.Aggregated User, 
3.Map Transaction, 
4.Map user,
5.Top Transaction, 
6.Top user

1.After Loading all the data into MongoDB, it is then migrated to a structured postgres data warehouse. 2.Then used SQL queries to join the tables and retrieve data for specific channels.

Data Analysis and Data Visualization:

1.With the help of SQL query, I have got many interesting insights about the youtube channels. 2.Finally, the data retrieved from the SQL is displayed using the Streamlit Web app. 3.Streamlit is used to create dashboard that allows users to visualize and analyze the data. 4.Also used Plotly for the Data Visualization to create charts and graphs to analyze the data.
