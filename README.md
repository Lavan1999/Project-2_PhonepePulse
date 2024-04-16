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

1.The first step is to collect data from the Github using the Github link. 
2.Once created the clone of GIT-HUB repository then,imported required libraries for the program.
3.Extracted from the Github link used to retrieve Aggregated Transaction, Aggregated User, Map Transaction, Map user, Top Transaction, Top user. 
4.I have used this to connect direct path to get the data as states for Python to make requests
to the Data and the responses are Collected as a Dictionary (Data Collection)

Create DataFrame:

Once the Data Collection is done, then I used pandas to create dataframe for the collected datas
For the 6 Dataset:

1.Aggregated Transaction.
2.Aggregated User.
3.Map Transaction.
4.Map user.
5.Top Transaction .
6.Top user.

Data Cleaning
1.After Crating all the dataframe, I cleaned the data for the process of identifying and correcting errors, inconsistencies,
and inaccuracies in a dataset to improve its quality and reliability. 

Data Analysis and Data Visualization:

1.With the help of SQL query, I have got many interesting insights about the datas.
2.Finally, the data retrieved from the SQL is displayed using the Streamlit Web app. 
3.Streamlit is used to create dashboard that allows users to visualize and analyze the data.
4.Also used Plotly for the Data Visualization to create charts and graphs to analyze the data.
![Screenshot (236)](https://github.com/Lavan1999/Project-2_PhonepePulse/assets/152668558/79d7ee28-6b88-41c3-9470-bc23400a5118)

![Screenshot (238)](https://github.com/Lavan1999/Project-2_PhonepePulse/assets/152668558/37152454-ecc7-44ac-b2d7-e8da0b5d9c13)

