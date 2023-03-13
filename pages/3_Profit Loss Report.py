import pandas as pd
import streamlit as st
import time
import numpy as np
import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect


credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)
cursor=conn.cursor()
# Perform SQL query on the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
#@st.cache_data(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["private_gsheets_url"]
sql_query = run_query(f'SELECT * FROM "{sheet_url}"')


df=pd.read_sql(f'SELECT * FROM "{sheet_url}"',conn,index_col="Id")
conn.close()
df

df=df.replace({'\$':''}, regex = True)


df

df2=df[(df['Unnamed: 0']=="Total Income")|(df['Unnamed: 0']=="Total 4000 Purchases - COS")|
                   (df['Unnamed: 0']=="Total 4009 Shipping and delivery expense")|(df['Unnamed: 0']=="Total Cost of Goods Sold")
                   |(df['Unnamed: 0']=="GROSS PROFIT")]

df2

df2.set_index('Unnamed: 0',inplace=True)

df2=df2.T

df2=df2.replace({'\,':''}, regex = True)

df2

cols=[i for i in df2.columns if i not in ['Unnamed: 0']]
for col in cols:
    df2[col]=pd.to_numeric(df2[col])

df2

df2['GROSS PROFIT %']=df2['GROSS PROFIT']/df2['Total Income']*100


cols=[i for i in df2.columns if i not in ['Unnamed: 0','GROSS PROFIT %']]
for col in cols:
    df2[col]=pd.to_numeric(df2[col]).fillna(0).astype(int)

df2

df2.rename(columns = {'Unnamed: 0':'', 'Total Income':'Sales','Total 4000 Purchases - COS':'COGS',
                      'Total 4009 Shipping and delivery expense':'ADVT','Total Cost of Goods Sold':'COGS+ADVT'}, inplace = True)

df2['GROSS PROFIT %']=df2['GROSS PROFIT %'].map("{:,.2f}%".format)

df3=df2.T.reset_index()

pd.set_option('display.float_format',  '{:,.2f}'.format)

df3.columns

df3

df3['FY-2021-22']=df3.loc[0:4,'Aug. 2021':'Jul. 2022'].sum(axis=1)


df3.loc[5,'FY-2021-22']=df3.loc[4,'FY-2021-22']/df3.loc[0,'FY-2021-22']*100

df3

df4=df3

col=df4.pop('FY-2021-22')

df4.insert(13,'FY-2021-22',col)

pd.set_option('display.max_columns', 30)

df4

import numpy as np

def perc(a):
    p=a.map("{:,.2f}%".format)
    return p

df5=df4

df5.loc[5,'FY-2021-22']=df5.loc[5,'FY-2021-22'].round(2).astype(str)+'%'

df5

st.write("df")
df



df6=df[(df['Unnamed: 0']=="Total 4021 Payroll Expenses")|
                   (df['Unnamed: 0']=="Total 4001 Bank Charges and Fees")|(df['Unnamed: 0']=="Total 4003 Legal and professional fees")
                   |(df['Unnamed: 0']=="Total 4006 Other general and administrative expenses")|
      (df['Unnamed: 0']=="Total 4008 Office Rent")|
      (df['Unnamed: 0']=="Total 4010 Insurance")|
      (df['Unnamed: 0']=="Total 4011 Software License/Agreement/Annual Fee")|
      (df['Unnamed: 0']=="Total 4013 Telephone and Utilities")|
      (df['Unnamed: 0']=="Total 4025 Marketing & Advertising")|
      (df['Unnamed: 0']=="Total 4020 Travel and Entertainment")|
      (df['Unnamed: 0']=="4023 Amortization/Depreciation Expense")|
      (df['Unnamed: 0']=="4022 Interest on Loan")]

df6
st.write("numeric")
df6=df6.replace({'\,':''}, regex = True)

df6=df6.replace('nan',np.nan)
cols=[i for i in df6.columns if i not in ['Unnamed: 0']]
for col in cols:
    df6[col]=pd.to_numeric(df6[col])

for i in df6['Aug. 2021']:
    st.write(type(i))

df6


df6['Total']=df6['Total'].replace({'\,':''}, regex = True)

df6['Total']=df6['Total'].astype('float')

df6['Total']


st.write("df6",df6)
total=df6.sum(axis=0)

total

total[0]="Total Expense"

#total.name='Total'
df7=df6.append(total.transpose(),ignore_index=True)

st.write('df7',df7)

df7['FY-2021-22']=df7.loc[:,'Aug. 2021':'Jul. 2022'].sum(axis=1)
col=df7.pop('FY-2021-22')
df7.insert(13,'FY-2021-22',col)

df8 = df5.append(df7, ignore_index=True)

df8.set_index('Unnamed: 0',inplace=True)

df8=df8.T

df8

st.write(df8['GROSS PROFIT'][1])

count=0
for i in df8['GROSS PROFIT']:
    count+=1
    st.write(type(i))
    st.write(count)

df8['PROFIT']=df8['GROSS PROFIT'].astype(float)-df8['Total Expense']

df8['PROFIT']=df8['PROFIT'].map('${:,.2f}'.format)

df8=df8.T.reset_index()

df8
st.session_state['dataframe']=df8