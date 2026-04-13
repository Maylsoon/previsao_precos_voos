import pandas as pd

def create_features(df):
    
    df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'])
    
    df['journey_day'] = df['Date_of_Journey'].dt.day
    df['journey_month'] = df['Date_of_Journey'].dt.month
    
    df['dep_hour'] = pd.to_datetime(df['Dep_Time']).dt.hour
    df['arrival_hour'] = df['Arrival_Time'].str.extract('(\d{2})').astype(int)
    
    df['Total_Stops'] = df['Total_Stops'].map({
        'non-stop': 0,
        '1 stop': 1,
        '2 stops': 2,
        '3 stops': 3,
        '4 stops': 4
    })
    
    df = df.drop(['Date_of_Journey'], axis=1)
    
    return df