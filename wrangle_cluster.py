import pandas as pd
import numpy as np
import os
import env
from env import host, user, pwd

def get_db_url(database):
    return f'mysql+pymysql://{user}:{pwd}@{host}/{database}'
    
def get_zillow_data():
    sql_query = '''
    SELECT * FROM properties_2017
    JOIN predictions_2017 USING (parcelid)
    WHERE transactiondate < '2018'
    AND propertylandusetypeid = 261;
    '''
    
    df = pd.read_sql(sql_query, get_db_url('zillow'))
    df = df.drop(columns='id')
    
    return df


