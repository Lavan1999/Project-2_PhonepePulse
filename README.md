# Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly
**LinkedIn Video Post: https://www.linkedin.com/feed/update/urn:li:activity:7180750658222895104/**
# Problem Statement:
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


# Workflow of the Project:

# Data Collection:

- The first step is to collect data from the Github using the Github link. 
- Once created the clone of GIT-HUB repository then,imported required libraries for the program.
- Extracted from the Github link used to retrieve Aggregated Transaction, Aggregated User, Map Transaction, Map user, Top Transaction, Top user. 
-  I have used this to connect direct path to get the data as states for Python to make requests
to the Data and the responses are Collected as a Dictionary (Data Collection)

# Create DataFrame:

Once the Data Collection is done, then I used pandas to create dataframe for the collected datas
For the 6 Dataset:

- Aggregated Transaction.
- Aggregated User.
- Map Transaction.
- Map user.
- Top Transaction .
- Top user.

# Data Cleaning
- After Crating all the dataframe, I cleaned the data for the process of identifying and correcting errors, inconsistencies,
and inaccuracies in a dataset to improve its quality and reliability. 

# Data Analysis and Data Visualization:

- With the help of SQL query, I have got many interesting insights about the datas.
- Finally, the data retrieved from the SQL is displayed using the Streamlit Web app. 
- Streamlit is used to create dashboard that allows users to visualize and analyze the data.
- Also used Plotly for the Data Visualization to create charts and graphs to analyze the data.

![pp1](https://github.com/Lavan1999/Project-2_PhonepePulse/assets/152668558/1e735c33-a50b-40b5-a49f-5a25078c8e2e)
![pp2](https://github.com/Lavan1999/Project-2_PhonepePulse/assets/152668558/71e63ac0-838e-4317-aa51-e9bebf31780d)
