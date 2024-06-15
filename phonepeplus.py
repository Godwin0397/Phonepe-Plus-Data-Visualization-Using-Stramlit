import os
import pandas as pd
import json
import sqlite3
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import requests
import json
from PIL import Image


# creating a database in sqlite3
conn = sqlite3.connect('phonepe.db')
cursor = conn.cursor() #creating a cursor to execute a queries


AggTransDF = ''
def dataFrameCreationFromFile():
    aggregatedTransactionpath="C:/Users/Godveen/Guvi/capstoneProjects/pulse/data/aggregated/transaction/country/india/state/"
    AggTransactionStateList=os.listdir(aggregatedTransactionpath)
#     AggTransactionStateList
    
    aggtransactionDict={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

    for i in AggTransactionStateList:
        pathi=aggregatedTransactionpath+i+"/"
        AggYr=os.listdir(pathi)
        for j in AggYr:
            pathj=pathi+j+"/"
            AggYrList=os.listdir(pathj)
            for k in AggYrList:
                pathk=pathj+k
                Data=open(pathk,'r')
                D=json.load(Data)
                for z in D['data']['transactionData']:
                  Name=z['name']
                  count=z['paymentInstruments'][0]['count']
                  amount=z['paymentInstruments'][0]['amount']
                  aggtransactionDict['Transaction_type'].append(Name)
                  aggtransactionDict['Transaction_count'].append(count)
                  aggtransactionDict['Transaction_amount'].append(amount)
                  aggtransactionDict['State'].append(i)
                  aggtransactionDict['Year'].append(j)
                  aggtransactionDict['Quater'].append(int(k.strip('.json')))
    #Succesfully created a dataframe
    AggTransDF=pd.DataFrame(aggtransactionDict)
    AggTransDF['State'] = AggTransDF['State'].str.replace("-", " ")
    AggTransDF['State'] = AggTransDF['State'].str.title()
    AggTransDF['State'] = AggTransDF['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
#     AggTransDF
    
    aggregatedUserpath="C:/Users/Godveen/Guvi/capstoneProjects/pulse/data/aggregated/user/country/india/state/"
    AggUserStateList=os.listdir(aggregatedUserpath)
#     AggUserStateList
    
    agguserDict={'State':[], 'Year':[],'Quater':[],'Brand':[], 'Transaction_count':[], 'percentage':[], 'registeredUsers':[], 'appOpens':[]}

    for i in AggUserStateList:
        pathi=aggregatedUserpath+i+"/"
        AggYr=os.listdir(pathi)
        for j in AggYr:
            pathj=pathi+j+"/"
            AggYrList=os.listdir(pathj)
            for k in AggYrList:
                pathk=pathj+k
                Data=open(pathk,'r')
                D=json.load(Data)
                try:
                    for z in D['data']['usersByDevice']:
                        Brand=z['brand']
                        count=z['count']
                        percentage=z['percentage']
                        registeredUsers = D['data']['aggregated']['registeredUsers']
                        appOpens = D['data']['aggregated']['appOpens']
                        agguserDict['Brand'].append(Brand)
                        agguserDict['Transaction_count'].append(count)
                        agguserDict['percentage'].append(percentage)
                        agguserDict['registeredUsers'].append(registeredUsers)
                        agguserDict['appOpens'].append(appOpens)
                        agguserDict['State'].append(i)
                        agguserDict['Year'].append(j)
                        agguserDict['Quater'].append(int(k.strip('.json')))
                except:
                    pass
    #Succesfully created a dataframe
    AggUsersDF=pd.DataFrame(agguserDict)
    AggUsersDF['State'] = AggUsersDF['State'].str.replace("-", " ")
    AggUsersDF['State'] = AggUsersDF['State'].str.title()
    AggUsersDF['State'] = AggUsersDF['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
#     AggUsersDF
    
    mapTransactionpath="C:/Users/Godveen/Guvi/capstoneProjects/pulse/data/map/transaction/hover/country/india/state/"
    mapTransactionStateList=os.listdir(mapTransactionpath)
#     mapTransactionStateList
    
    mapTransactionDict={'State':[], 'Year':[],'Quater':[],'District':[], 'Transaction_count':[], 'Transaction_amount':[]}

    for i in mapTransactionStateList:
        pathi=mapTransactionpath+i+"/"
        AggYr=os.listdir(pathi)
        for j in AggYr:
            pathj=pathi+j+"/"
            AggYrList=os.listdir(pathj)
            for k in AggYrList:
                pathk=pathj+k
                Data=open(pathk,'r')
                D=json.load(Data)
                try:
                    for z in D['data']['hoverDataList']:
                        name=z['name']
                        count=z['metric'][0]['count']
                        amount=z['metric'][0]['amount']
                        mapTransactionDict['District'].append(name)
                        mapTransactionDict['Transaction_count'].append(count)
                        mapTransactionDict['Transaction_amount'].append(amount)
                        mapTransactionDict['State'].append(i)
                        mapTransactionDict['Year'].append(j)
                        mapTransactionDict['Quater'].append(int(k.strip('.json')))
                except:
                    pass
    #Succesfully created a dataframe
    mapTransactionDF=pd.DataFrame(mapTransactionDict)
    mapTransactionDF['State'] = mapTransactionDF['State'].str.replace("-", " ")
    mapTransactionDF['State'] = mapTransactionDF['State'].str.title()
    mapTransactionDF['State'] = mapTransactionDF['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
#     mapTransactionDF
    
    mapUserpath="C:/Users/Godveen/Guvi/capstoneProjects/pulse/data/map/user/hover/country/india/state/"
    mapUserStateList=os.listdir(mapUserpath)
#     mapUserStateList
    
    mapUserDict={'State':[], 'Year':[],'Quater':[],'District':[], 'registeredUsers':[], 'appOpens':[]}

    for i in mapUserStateList:
        pathi=mapUserpath+i+"/"
        AggYr=os.listdir(pathi)
        for j in AggYr:
            pathj=pathi+j+"/"
            AggYrList=os.listdir(pathj)
            for k in AggYrList:
                pathk=pathj+k
                Data=open(pathk,'r')
                D=json.load(Data)
                try:
                    for z in D['data']['hoverData'].items():
                        name=z[0]
                        registeredUsers=z[1]['registeredUsers']
                        appOpens=z[1]['appOpens']
                        mapUserDict['District'].append(name)
                        mapUserDict['registeredUsers'].append(registeredUsers)
                        mapUserDict['appOpens'].append(appOpens)
                        mapUserDict['State'].append(i)
                        mapUserDict['Year'].append(j)
                        mapUserDict['Quater'].append(int(k.strip('.json')))
                except:
                    pass
    #Succesfully created a dataframe
    mapUserDF=pd.DataFrame(mapUserDict)
    mapUserDF['State'] = mapUserDF['State'].str.replace("-", " ")
    mapUserDF['State'] = mapUserDF['State'].str.title()
    mapUserDF['State'] = mapUserDF['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
#     mapUserDF
    
    topTransactionpath="C:/Users/Godveen/Guvi/capstoneProjects/pulse/data/top/transaction/country/india/state/"
    topTransactionStateList=os.listdir(topTransactionpath)
#     topTransactionStateList
    
    topTransactionDict={'State':[], 'Year':[],'Quater':[],'District':[], 'Transaction_count':[], 'Transaction_amount':[]}

    for i in topTransactionStateList:
        pathi=topTransactionpath+i+"/"
        AggYr=os.listdir(pathi)
        for j in AggYr:
            pathj=pathi+j+"/"
            AggYrList=os.listdir(pathj)
            for k in AggYrList:
                pathk=pathj+k
                Data=open(pathk,'r')
                D=json.load(Data)
                try:
                    for z in D['data']['pincodes']:
                        name=z['entityName']
                        count=z['metric']['count']
                        amount=z['metric']['amount']
                        topTransactionDict['District'].append(name)
                        topTransactionDict['Transaction_count'].append(count)
                        topTransactionDict['Transaction_amount'].append(amount)
                        topTransactionDict['State'].append(i)
                        topTransactionDict['Year'].append(j)
                        topTransactionDict['Quater'].append(int(k.strip('.json')))
                except:
                    pass
    #Succesfully created a dataframe
    topTransactionDF=pd.DataFrame(topTransactionDict)
    topTransactionDF['State'] = topTransactionDF['State'].str.replace("-", " ")
    topTransactionDF['State'] = topTransactionDF['State'].str.title()
    topTransactionDF['State'] = topTransactionDF['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
#     topTransactionDF
    
    topUserpath="C:/Users/Godveen/Guvi/capstoneProjects/pulse/data/top/user/country/india/state/"
    topUserStateList=os.listdir(topUserpath)
#     topUserStateList
    
    topUserDict={'State':[], 'Year':[],'Quater':[],'District':[], 'registeredUsers':[]}

    for i in topUserStateList:
        pathi=topUserpath+i+"/"
        AggYr=os.listdir(pathi)
        for j in AggYr:
            pathj=pathi+j+"/"
            AggYrList=os.listdir(pathj)
            for k in AggYrList:
                pathk=pathj+k
                Data=open(pathk,'r')
                D=json.load(Data)
                try:
                    for z in D['data']['pincodes']:
                        name=z['name']
                        registeredUsers=z['registeredUsers']
                        topUserDict['District'].append(name)
                        topUserDict['registeredUsers'].append(registeredUsers)
                        topUserDict['State'].append(i)
                        topUserDict['Year'].append(j)
                        topUserDict['Quater'].append(int(k.strip('.json')))
                except:
                    pass
    #Succesfully created a dataframe
    topUserDF=pd.DataFrame(topUserDict)
    topUserDF['State'] = topUserDF['State'].str.replace("-", " ")
    topUserDF['State'] = topUserDF['State'].str.title()
    topUserDF['State'] = topUserDF['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
#     topUserDF
#      return {
#         AggTransDF, AggUsersDF, mapTransactionDF, mapUserDF, topTransactionDF, topUserDF
#     }
    return { 'AggTransDF': AggTransDF, 'AggUsersDF': AggUsersDF, 'mapTransactionDF': mapTransactionDF, 'mapUserDF': mapUserDF, 'topTransactionDF': topTransactionDF, 'topUserDF': topUserDF
           }
    
def createAndInsertDataToDatabase():
    # creating aggregatedTransactionTable
    def aggregatedTransactionTableCreation():
        createaggregatedTransactionTable = '''create table if not exists
        aggregatedTransaction(State varchar(255), Year int, Quater int, Transaction_type varchar(255),
        Transaction_count bigint, 
        Transaction_amount bigint)'''
        cursor.execute(createaggregatedTransactionTable)
        conn.commit()
        return 'Successfully Aggregated Transaction Table Created'
    aggregatedTransactionTableCreationObj = aggregatedTransactionTableCreation()
#     print(aggregatedTransactionTableCreationObj)
    
    insertingaggregatedTransactionData = '''insert into aggregatedTransaction(State, Year, Quater, Transaction_type, Transaction_count,
                   Transaction_amount)
                    values(?, ?, ?, ?, ?, ?)'''
    
    AggTransDF = dataFrameCreationFromFileObj['AggTransDF']
    AggTransDFValues = AggTransDF.values.tolist()
    cursor.executemany(insertingaggregatedTransactionData, AggTransDFValues)
    conn.commit()
    
    # creating aggregatedUserTable
    def aggregatedUserTableCreation():
        createaggregatedUserTable = '''create table if not exists
        aggregatedUser(State varchar(255), Year int, Quater int, Brand varchar(255),
        Transaction_count bigint, 
        percentage float,
        registeredUsers bigint,
        appOpens bigint)'''
        cursor.execute(createaggregatedUserTable)
        conn.commit()
        return 'Successfully Aggregated Transaction Table Created'
    aggregatedUserTableCreationObj = aggregatedUserTableCreation()
#     print(aggregatedUserTableCreationObj)
    
    insertingaggregatedUserData = '''insert into aggregatedUser(State, Year, Quater, Brand, Transaction_count,
                   percentage, registeredUsers, appOpens)
                    values(?, ?, ?, ?, ?, ?, ?, ?)'''
    
    AggUsersDF = dataFrameCreationFromFileObj['AggUsersDF']
    AggUsersDFValues = AggUsersDF.values.tolist()
    cursor.executemany(insertingaggregatedUserData, AggUsersDFValues)
    conn.commit()
    
    # creating mapTransactionTable
    def mapTransactionTableCreation():
        createmapTransactionTable = '''create table if not exists
        mapTransaction(State varchar(255), Year int, Quater int, District varchar(255),
        Transaction_count bigint, 
        Transaction_amount bigint)'''
        cursor.execute(createmapTransactionTable)
        conn.commit()
        return 'Successfully Aggregated Transaction Table Created'
    mapTransactionTableCreationObj = mapTransactionTableCreation()
#     print(mapTransactionTableCreationObj)
    
    insertingmapTransactionData = '''insert into mapTransaction(State, Year, Quater, District, Transaction_count,
                   Transaction_amount)
                    values(?, ?, ?, ?, ?, ?)'''
    
    mapTransactionDF = dataFrameCreationFromFileObj['mapTransactionDF']
    mapTransactionDFValues = mapTransactionDF.values.tolist()
    cursor.executemany(insertingmapTransactionData, mapTransactionDFValues)
    conn.commit()
    
    # creating mapUserTable
    def mapUserTableCreation():
        createmapUserTable = '''create table if not exists
        mapUser(State varchar(255), Year int, Quater int, District varchar(255),
        registeredUsers bigint, 
        appOpens bigint)'''
        cursor.execute(createmapUserTable)
        conn.commit()
        return 'Successfully Aggregated Transaction Table Created'
    mapUserTableCreationObj = mapUserTableCreation()
#     print(mapUserTableCreationObj)
    
    insertingmapUserData = '''insert into mapUser(State, Year, Quater, District, registeredUsers,
                   appOpens)
                    values(?, ?, ?, ?, ?, ?)'''
    
    mapUserDF = dataFrameCreationFromFileObj['mapUserDF']
    mapUserDFValues = mapUserDF.values.tolist()
    cursor.executemany(insertingmapUserData, mapUserDFValues)
    conn.commit()
    
    # creating topTransactionTable
    def topTransactionTableCreation():
        createtopTransactionTable = '''create table if not exists
        topTransaction(State varchar(255), Year int, Quater int, District varchar(255),
        Transaction_count bigint, 
        Transaction_amount bigint)'''
        cursor.execute(createtopTransactionTable)
        conn.commit()
        return 'Successfully Aggregated Transaction Table Created'
    topTransactionTableCreationObj = topTransactionTableCreation()
#     print(topTransactionTableCreationObj)
    
    insertingtopTransactionData = '''insert into topTransaction(State, Year, Quater, District, Transaction_count,
                   Transaction_amount)
                    values(?, ?, ?, ?, ?, ?)'''
    
    topTransactionDF = dataFrameCreationFromFileObj['topTransactionDF']
    topTransactionDFValues = topTransactionDF.values.tolist()
    cursor.executemany(insertingtopTransactionData, topTransactionDFValues)
    conn.commit()
    
    # creating topUserTable
    def topUserTableCreation():
        createtopUserTable = '''create table if not exists
        topUser(State varchar(255), Year int, Quater int, District varchar(255),
        registeredUsers bigint)'''
        cursor.execute(createtopUserTable)
        conn.commit()
        return 'Successfully Aggregated Transaction Table Created'
    topUserTableCreationObj = topUserTableCreation()
#     print(topUserTableCreationObj)
    
    insertingtopUserData = '''insert into topUser(State, Year, Quater, District, registeredUsers)
                    values(?, ?, ?, ?, ?)'''
    
    topUserDF = dataFrameCreationFromFileObj['topUserDF']
    topUserDFValues = topUserDF.values.tolist()
    cursor.executemany(insertingtopUserData, topUserDFValues)
    conn.commit()
    
def dataFrameCreationFromDb():
    # aggregateTransactionDataFrame
    cursor.execute('select * from aggregatedTransaction')
    conn.commit()
    aggTransactionTable = cursor.fetchall()
    aggTransactionTableDF = pd.DataFrame(aggTransactionTable, columns=['State', 'Year', 'Quater', 'Transaction_type', 'Transaction_count',
           'Transaction_amount'])
#     aggTransactionTableDF
    
    # aggregateUserDataFrame
    cursor.execute('select * from aggregatedUser')
    conn.commit()
    aggUserTable = cursor.fetchall()
    aggUserTableDF = pd.DataFrame(aggUserTable, columns=['State', 'Year', 'Quater', 'Brand', 'Transaction_count', 'percentage',
           'registeredUsers', 'appOpens'])
#     aggUserTableDF
    
    # mapTransactionDataFrame
    cursor.execute('select * from mapTransaction')
    conn.commit()
    mapTransactionTable = cursor.fetchall()
    mapTransactionTableDF = pd.DataFrame(mapTransactionTable, columns=['State', 'Year', 'Quater', 'District', 'Transaction_count', 'Transaction_amount'])
#     mapTransactionTableDF
    
    # mapUserDataFrame
    cursor.execute('select * from mapUser')
    conn.commit()
    mapUserTable = cursor.fetchall()
    mapUserTableDF = pd.DataFrame(mapUserTable, columns=['State', 'Year', 'Quater', 'District', 'registeredUsers', 'appOpens'])
#     mapUserTableDF
    
    # topTransactionDataFrame
    cursor.execute('select * from topTransaction')
    conn.commit()
    topTransactionTable = cursor.fetchall()
    topTransactionTableDF = pd.DataFrame(topTransactionTable, columns=['State', 'Year', 'Quater', 'District', 'Transaction_count', 'Transaction_amount'])
#     topTransactionTableDF
    
    # topUserDataFrame
    cursor.execute('select * from topUser')
    conn.commit()
    topUserTable = cursor.fetchall()
    topUserTableDF = pd.DataFrame(topUserTable, columns=['State', 'Year', 'Quater', 'District', 'registeredUsers'])
#     topUserTableDF

dataFrameCreationFromFileObj = dataFrameCreationFromFile()
createAndInsertDataToDatabase()
dataFrameCreationFromDb()


# Transaction Amount and Transaction Count Yearwise Function
def Transaction_amount_count_Y(df, year):
    tacy = df[df['Year']==str(year)]
    tacy.reset_index(drop = True, inplace = True)
    tacyg = tacy.groupby('State')[['Transaction_count', 'Transaction_amount']].sum()
    tacyg.reset_index(inplace=True)
    fig_amount = px.bar(tacyg, x='State', y='Transaction_amount', title=f'{year} Transaction Amount', color_discrete_sequence=px.colors.sequential.Aggrnyl, height=650, width=600)
    fig_count = px.bar(tacyg, x='State', y='Transaction_count', title=f'{year} Transaction Count', color_discrete_sequence=px.colors.sequential.Bluered_r, height=650, width=600)
    
#     India Map Code Logic Start
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response = requests.get(url)
    data1 = json.loads(response.content)
    stateNames = []
    for feature in data1['features']:
        stateNames.append(feature['properties']['ST_NM'])
    stateNames.sort()
#     India Map Code Logic end

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_amount)
        figIndia1 = px.choropleth(tacyg, geojson=data1, locations='State', featureidkey='properties.ST_NM',
                                 color='Transaction_amount',color_continuous_scale='Rainbow',
                                 range_color=(tacyg['Transaction_amount'].min(), tacyg['Transaction_amount'].max()),
                                 hover_name='State', title=f'{year} Transaction Amount', fitbounds='locations',
                                 height=600, width=600)
        figIndia1.update_geos(visible=False)
        st.plotly_chart(figIndia1)
#     fig_amount.show()
#     figIndia1.show()
    with col2:
        st.plotly_chart(fig_count)
        figIndia2 = px.choropleth(tacyg, geojson=data1, locations='State', featureidkey='properties.ST_NM',
                                 color='Transaction_count',color_continuous_scale='Rainbow',
                                 range_color=(tacyg['Transaction_count'].min(), tacyg['Transaction_count'].max()),
                                 hover_name='State', title=f'{year} Transaction Count', fitbounds='locations',
                                 height=600, width=600)
        figIndia2.update_geos(visible=False)
        st.plotly_chart(figIndia2)
#         figIndia2.show()
#         fig_count.show()
    return tacy


# Transaction Amount and Transaction Count Quarterwise Function
def Transaction_amount_count_Q(df, quarter):
    tacy = df[df['Quater']==quarter]
    tacy.reset_index(drop = True, inplace = True)
    tacyg = tacy.groupby('State')[['Transaction_count', 'Transaction_amount']].sum()
    tacyg.reset_index(inplace=True)
    fig_amount = px.bar(tacyg, x='State', y='Transaction_amount', title=f"{quarter} Quarter {tacy['Year'].min()} Transaction Amount", color_discrete_sequence=px.colors.sequential.Aggrnyl, height=650, width=600)
    fig_count = px.bar(tacyg, x='State', y='Transaction_count', title=f"{quarter} Quarter {tacy['Year'].min()} Transaction Count", color_discrete_sequence=px.colors.sequential.Bluered_r, height=650, width=600)
    
#     India Map Chart Logic Start
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response = requests.get(url)
    data1 = json.loads(response.content)
    stateNames = []
    for feature in data1['features']:
        stateNames.append(feature['properties']['ST_NM'])
    stateNames.sort()
#     India Map Chart Logic End

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_amount)
        figIndia1 = px.choropleth(tacyg, geojson=data1, locations='State', featureidkey='properties.ST_NM',
                             color='Transaction_amount',color_continuous_scale='Rainbow',
                             range_color=(tacyg['Transaction_amount'].min(), tacyg['Transaction_amount'].max()),
                             hover_name='State', title=f"{quarter} Quarter {tacy['Year'].min()} Transaction Amount", fitbounds='locations',
                             height=600, width=600)
        figIndia1.update_geos(visible=False)
        st.plotly_chart(figIndia1)
#         figIndia1.show()
#         fig_amount.show()
    
    with col2:
        st.plotly_chart(fig_count)
        figIndia2 = px.choropleth(tacyg, geojson=data1, locations='State', featureidkey='properties.ST_NM',
                                 color='Transaction_count',color_continuous_scale='Rainbow',
                                 range_color=(tacyg['Transaction_count'].min(), tacyg['Transaction_count'].max()),
                                 hover_name='State', title=f"{quarter} Quarter {tacy['Year'].min()} Transaction Count", fitbounds='locations',
                                 height=600, width=600)
        figIndia2.update_geos(visible=False)
        st.plotly_chart(figIndia2)
#         fig_count.show()
#         figIndia2.show()
    return tacy

# Transaction Amount and Transaction Count Transaction Type and Statewise Function
def Transaction_amount_count_Type_State(df, state):
    tacys = df[df['State']==state]
    tacys.reset_index(drop = True, inplace = True)
    tacygsty = tacys.groupby('Transaction_type')[['Transaction_count', 'Transaction_amount']].sum()
    tacygsty.reset_index(inplace=True)
    figPie1 = px.pie(data_frame=tacygsty, names='Transaction_type', values='Transaction_amount',
                    width=500, title=f"{state} Transaction Amount")
    figPie2 = px.pie(data_frame=tacygsty, names='Transaction_type', values='Transaction_count',
                    width=500, title=f"{state} Transaction Count")
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(figPie1)
#     figPie1.show()
    with col2:
        st.plotly_chart(figPie2)
#     figPie2.show()
    return tacys

# Aggregated User Yearwise Brand and Transaction Count Function
def aggregated_User_Yearwise(df, year):
    auy = df[df['Year']==str(year)]
    auy.reset_index(drop=True, inplace=True)
    auyg = pd.DataFrame(auy.groupby('Brand')['Transaction_count'].sum())
    auyg.reset_index(inplace=True)
    figYearwise = px.bar(auyg, x='Brand', y='Transaction_count', title=f"{year} Transaction Count", 
                     width=800, color_discrete_sequence=px.colors.sequential.haline_r, hover_name='Brand')
    st.plotly_chart(figYearwise)
#     figYearwise.show()
    return auy

# Aggregated User Quarterwise Brand and Transaction Count Function
def aggregated_User_Quarterwise(df, quarter):
    auy = df[df['Quater']==quarter]
    auy.reset_index(drop=True, inplace=True)
    auyg = pd.DataFrame(auy.groupby('Brand')['Transaction_count'].sum())
    auyg.reset_index(inplace=True)
    figQuarterwise = px.bar(auyg, x='Brand', y='Transaction_count', title=f"{quarter} Quarter, Transaction Count", 
                     width=800, color_discrete_sequence=px.colors.sequential.haline_r, hover_name='Brand')
    st.plotly_chart(figQuarterwise)
#     figQuarterwise.show()
    return auy

# Aggregated User Statewise Brand and Transaction Count Function
def aggregated_User_Statewise(df, state):
    auy = df[df['State']==state]
    auy.reset_index(drop=True, inplace=True)
    auyg = pd.DataFrame(auy.groupby('Brand')['Transaction_count'].sum())
    auyg.reset_index(inplace=True)
    figStatewise = px.line(auyg, x='Brand', y='Transaction_count', title=f"{state} Transaction Count", 
                     width=1000, hover_data='Brand', markers=True)
    st.plotly_chart(figStatewise)
#     figStatewise.show()
    return auy

def mapTransactionAmountCountStatewise(df, state):
    tacys = df[df['State']==state]
    tacys.reset_index(drop = True, inplace = True)
    tacygsty = tacys.groupby('District')[['Transaction_count', 'Transaction_amount']].sum()
    tacygsty.reset_index(inplace=True)
    col1, col2 = st.columns(2)
    with col1:
        figBar1 = px.bar(tacygsty, x='Transaction_amount', y='District', orientation='h',
                        height=600, title=f"{state} Transaction Amount", color_discrete_sequence=px.colors.sequential.Mint_r)
        st.plotly_chart(figBar1)
    #     figBar1.show()
    with col2:
        figBar2 = px.bar(tacygsty, x='Transaction_count', y='District', orientation='h',
                        height=600, title=f"{state} Transaction Count", color_discrete_sequence=px.colors.sequential.Bluered_r)
        st.plotly_chart(figBar2)
    #     figBar2.show()
    return tacys

def mapUserAnalysisYearwise(df, year):
    auy = df[df['Year']==str(year)]
    auy.reset_index(drop=True, inplace=True)
    auyg = pd.DataFrame(auy.groupby('State')[['registeredUsers', 'appOpens']].sum())
    auyg.reset_index(inplace=True)
    figStatewise = px.line(auyg, x='State', y=['registeredUsers', 'appOpens'], title=f"Registered Users Appopens", 
                     width=1000, height=800, hover_data='State', markers=True)
    st.plotly_chart(figStatewise)
#     figStatewise.show()
    return auy

def mapUserAnalysisQuaterwise(df, Quater):
    auy = df[df['Quater']==Quater]
    auy.reset_index(drop=True, inplace=True)
    auyg = pd.DataFrame(auy.groupby('State')[['registeredUsers', 'appOpens']].sum())
    auyg.reset_index(inplace=True)
    figStatewise = px.line(auyg, x='State', y=['registeredUsers', 'appOpens'], title=f"Quarterwise Registered Users Appopens", 
                     width=1000, height=800, hover_data='State', markers=True)
    st.plotly_chart(figStatewise)
#     figStatewise.show()
    return auy

def mapUserAnalysisStatewise(df, state):
    tacys = df[df['State']==state]
    tacys.reset_index(drop = True, inplace = True)
    col1, col2 = st.columns(2)
    with col1:
        figBar1 = px.bar(tacys, x='registeredUsers', y='District', orientation='h',
                        height=600, title=f"{state} Registered Users", color_discrete_sequence=px.colors.sequential.Mint_r)
        st.plotly_chart(figBar1)
    #     figBar1.show()
    with col2:
        figBar2 = px.bar(tacys, x='appOpens', y='District', orientation='h',
                        height=600, title=f"{state} AppOpens", color_discrete_sequence=px.colors.sequential.Bluered_r)
        st.plotly_chart(figBar2)
    #     figBar2.show()
    return tacys

def topTransactionAnalysisStatewise(df, state):
    tacys = df[df['State']==state]
    tacys.reset_index(drop = True, inplace = True)
    col1, col2 = st.columns(2)
    with col1:
        figBar1 = px.bar(tacys, x='Quater', y='Transaction_amount', hover_name = 'District',
                        height=600, width=500, title=f"{state.upper()} TRANSACTION AMOUNT", color_discrete_sequence=px.colors.sequential.Mint_r)
        st.plotly_chart(figBar1)
    #     figBar1.show()
    with col2:
        figBar2 = px.bar(tacys, x='Quater', y='Transaction_count', hover_name = 'District',
                        height=600, width=500, title=f"{state.upper()} TRANSACTION COUNT", color_discrete_sequence=px.colors.sequential.Bluered_r)
        st.plotly_chart(figBar2)
    #     figBar2.show()
    return tacys

def topUserYearwiseQuaterwiseAnalysis(df, year):
    auy = df[df['Year']==str(year)]
    auy.reset_index(drop=True, inplace=True)
    auyg = pd.DataFrame(auy.groupby(['State', 'Quater'])['registeredUsers'].sum())
    auyg.reset_index(inplace=True)
    figYearwise = px.bar(auyg, x='State', y='registeredUsers', title=f"{year} Registered Users", color='Quater', height=800,
                     width=1000, color_discrete_sequence=px.colors.sequential.haline_r, hover_name='State')
    st.plotly_chart(figYearwise)
#     figYearwise.show()
    return auy

def topUserYearwiseQuaterwiseStatewisePincodeAnalysis(df, state):
    auy = df[df['State']==state]
    auy.reset_index(drop=True, inplace=True)
    figYearwise = px.bar(auy, x='Quater', y='registeredUsers', title=f"Registered Users Pincodes Quarter ", color='registeredUsers', height=800,
                     width=1000, color_continuous_scale=px.colors.sequential.Magenta, hover_name='District')
    st.plotly_chart(figYearwise)
#     figYearwise.show()
    return auy

def transactionAmountAnalysis(tableName):
    top10TransactionAmount = f'''SELECT State, SUM(Transaction_amount) as Transaction_amount FROM {tableName}
                GROUP BY State ORDER BY Transaction_amount DESC LIMIT 10;'''
    cursor.execute(top10TransactionAmount)
    existingrecord1 = cursor.fetchall()
    df1 = pd.DataFrame(existingrecord1, columns=['State', 'Transaction Amount'])
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(df1, x='State', y='Transaction Amount', title=f"Top 10 Transaction Amount", height=600,
                             width=600, color_continuous_scale=px.colors.sequential.Magenta, hover_name='State')
        st.plotly_chart(fig1)
    #     fig1.show()

    last10TransactionAmount = f'''SELECT State, SUM(Transaction_amount) as Transaction_amount FROM {tableName}
                GROUP BY State ORDER BY Transaction_amount LIMIT 10;'''
    cursor.execute(last10TransactionAmount)
    existingrecord2 = cursor.fetchall()
    df2 = pd.DataFrame(existingrecord2, columns=['State', 'Transaction Amount'])
    with col2:
        fig2 = px.bar(df2, x='State', y='Transaction Amount', title=f"Last 10 Transaction Amount", height=670,
                             width=600, color_discrete_sequence=px.colors.sequential.Bluered_r, hover_name='State')
        st.plotly_chart(fig2)
    #     fig2.show()

    averageTransactionAmount = f'''SELECT State, AVG(Transaction_amount) as Transaction_amount FROM {tableName}
                GROUP BY State ORDER BY Transaction_amount;'''
    cursor.execute(last10TransactionAmount)
    existingrecord3 = cursor.fetchall()
    df3 = pd.DataFrame(existingrecord3, columns=['State', 'Transaction Amount'])
    col1, col2 = st.columns(2)
    with col1:
        fig3 = px.bar(df3, x='Transaction Amount', y='State', title=f"Average Transaction Amount", orientation='h', height=800,
                             width=1000, color_discrete_sequence=px.colors.sequential.Aggrnyl, hover_name='State')
        st.plotly_chart(fig3)
    #     fig3.show()

    
def transactionCountAnalysis(tableName):
    top10TransactionAmount = f'''SELECT State, SUM(Transaction_count) as Transaction_count FROM {tableName}
                GROUP BY State ORDER BY Transaction_count DESC LIMIT 10;'''
    cursor.execute(top10TransactionAmount)
    existingrecord1 = cursor.fetchall()
    df1 = pd.DataFrame(existingrecord1, columns=['State', 'Transaction Count'])
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(df1, x='State', y='Transaction Count', title=f"Top 10 Transaction Count", height=600,
                             width=600, color_continuous_scale=px.colors.sequential.Magenta, hover_name='State')
        st.plotly_chart(fig1)
    #     fig1.show()

    last10TransactionAmount = f'''SELECT State, SUM(Transaction_count) as Transaction_count FROM {tableName}
                GROUP BY State ORDER BY Transaction_count LIMIT 10;'''
    cursor.execute(last10TransactionAmount)
    existingrecord2 = cursor.fetchall()
    df2 = pd.DataFrame(existingrecord2, columns=['State', 'Transaction count'])
    with col2:
        fig2 = px.bar(df2, x='State', y='Transaction count', title=f"Last 10 Transaction Count", height=670,
                             width=600, color_discrete_sequence=px.colors.sequential.Bluered_r, hover_name='State')
        st.plotly_chart(fig2)
    #     fig2.show()

    averageTransactionAmount = f'''SELECT State, AVG(Transaction_count) as Transaction_count FROM {tableName}
                GROUP BY State ORDER BY Transaction_count;'''
    cursor.execute(last10TransactionAmount)
    existingrecord3 = cursor.fetchall()
    df3 = pd.DataFrame(existingrecord3, columns=['State', 'Transaction Count'])
    col1, col2 = st.columns(2)
    with col1:
        fig3 = px.bar(df3, x='Transaction Count', y='State', title=f"Average Transaction Count", orientation='h', height=800,
                             width=1000, color_discrete_sequence=px.colors.sequential.Aggrnyl, hover_name='State')
        st.plotly_chart(fig3)
    #     fig3.show()

def statewiseRegisteredUsersAnalysis(tableName, state):
    top10MapUsersRegisteredUsers = f'''SELECT District, SUM(registeredUsers) as registeredUsers FROM {tableName}
                WHERE State = '{state}'
                GROUP BY District ORDER BY registeredUsers DESC LIMIT 10;'''
    cursor.execute(top10MapUsersRegisteredUsers)
    existingrecord1 = cursor.fetchall()
    df1 = pd.DataFrame(existingrecord1, columns=['District', 'Registered Users'])
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(df1, x='District', y='Registered Users', title=f"Top 10 Registered Users", height=600,
                             width=600, color_continuous_scale=px.colors.sequential.Magenta, hover_name='District')
        st.plotly_chart(fig1)
    #     fig1.show()

    last10MapUsersRegisteredUsers = f'''SELECT District, SUM(registeredUsers) as registeredUsers FROM {tableName}
                WHERE State = '{state}'
                GROUP BY District ORDER BY registeredUsers LIMIT 10;'''
    cursor.execute(last10MapUsersRegisteredUsers)
    existingrecord2 = cursor.fetchall()
    df2 = pd.DataFrame(existingrecord2, columns=['District', 'Registered Users'])
    with col2:
        fig2 = px.bar(df2, x='District', y='Registered Users', title=f"Top 10 Registered Users", height=600,
                             width=600, color_discrete_sequence=px.colors.sequential.Bluered_r, hover_name='District')
        st.plotly_chart(fig2)
#         fig2.show()

    averageMapUsersRegisteredUsers = f'''SELECT District, AVG(registeredUsers) as registeredUsers FROM {tableName}
                WHERE State = '{state}'
                GROUP BY District ORDER BY registeredUsers LIMIT 10;'''
    cursor.execute(averageMapUsersRegisteredUsers)
    existingrecord3 = cursor.fetchall()
    df3 = pd.DataFrame(existingrecord3, columns=['District', 'Registered Users'])
    col1, col2 = st.columns(2)
    with col1:
        fig3 = px.bar(df3, x='Registered Users', y='District', title=f"Top 10 Registered Users", orientation='h', height=800,
                             width=1000, color_discrete_sequence=px.colors.sequential.Aggrnyl, hover_name='District')
        st.plotly_chart(fig3)
    #     fig3.show()


def statewiseAppOpensAnalysis(tableName, state):
    top10MapUsersRegisteredUsers = f'''SELECT District, SUM(appOpens) as appOpens FROM {tableName}
                WHERE State = '{state}'
                GROUP BY District ORDER BY appOpens DESC LIMIT 10;'''
    cursor.execute(top10MapUsersRegisteredUsers)
    existingrecord1 = cursor.fetchall()
    df1 = pd.DataFrame(existingrecord1, columns=['District', 'App Opens'])
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(df1, x='District', y='App Opens', title=f"Top 10 App Opens", height=600,
                             width=600, color_continuous_scale=px.colors.sequential.Magenta, hover_name='District')
        st.plotly_chart(fig1)
#         fig1.show()

    last10MapUsersRegisteredUsers = f'''SELECT District, SUM(appOpens) as appOpens FROM {tableName}
                WHERE State = '{state}'
                GROUP BY District ORDER BY appOpens LIMIT 10;'''
    cursor.execute(last10MapUsersRegisteredUsers)
    existingrecord2 = cursor.fetchall()
    df2 = pd.DataFrame(existingrecord2, columns=['District', 'App Opens'])
    with col2:
        fig2 = px.bar(df2, x='District', y='App Opens', title=f"Top 10 App Opens", height=600,
                             width=600, color_discrete_sequence=px.colors.sequential.Bluered_r, hover_name='District')
        st.plotly_chart(fig2)
    #     fig2.show()

    averageMapUsersRegisteredUsers = f'''SELECT District, AVG(appOpens) as appOpens FROM {tableName}
                WHERE State = '{state}'
                GROUP BY District ORDER BY appOpens LIMIT 10;'''
    cursor.execute(averageMapUsersRegisteredUsers)
    existingrecord3 = cursor.fetchall()
    df3 = pd.DataFrame(existingrecord3, columns=['District', 'App Opens'])
    col1, col2 = st.columns(2)
    with col1:
        fig3 = px.bar(df3, x='App Opens', y='District', title=f"Top 10 App Opens", orientation='h', height=800,
                             width=1000, color_discrete_sequence=px.colors.sequential.Aggrnyl, hover_name='District')
        st.plotly_chart(fig3)
    #     fig3.show()
    
def registeredUsersAnalysis(tableName):
    top10MapUsersRegisteredUsers = f'''SELECT State, SUM(registeredUsers) as registeredUsers FROM {tableName}
                GROUP BY State ORDER BY registeredUsers DESC LIMIT 10;'''
    cursor.execute(top10MapUsersRegisteredUsers)
    existingrecord1 = cursor.fetchall()
    df1 = pd.DataFrame(existingrecord1, columns=['State', 'Registered Users'])
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(df1, x='State', y='Registered Users', title=f"Top 10 Registered Users", height=600,
                             width=600, color_continuous_scale=px.colors.sequential.Magenta, hover_name='State')
        st.plotly_chart(fig1)
    #     fig1.show()

    last10MapUsersRegisteredUsers = f'''SELECT State, SUM(registeredUsers) as registeredUsers FROM {tableName}
                GROUP BY State ORDER BY registeredUsers LIMIT 10;'''
    cursor.execute(last10MapUsersRegisteredUsers)
    existingrecord2 = cursor.fetchall()
    df2 = pd.DataFrame(existingrecord2, columns=['State', 'Registered Users'])
    with col2:
        fig2 = px.bar(df2, x='State', y='Registered Users', title=f"Top 10 Registered Users", height=640,
                             width=600, color_discrete_sequence=px.colors.sequential.Bluered_r, hover_name='State')
        st.plotly_chart(fig2)
    #     fig2.show()

    averageMapUsersRegisteredUsers = f'''SELECT State, AVG(registeredUsers) as registeredUsers FROM {tableName}
                GROUP BY State ORDER BY registeredUsers LIMIT 10;'''
    cursor.execute(averageMapUsersRegisteredUsers)
    existingrecord3 = cursor.fetchall()
    df3 = pd.DataFrame(existingrecord3, columns=['State', 'Registered Users'])
    with col1:
        fig3 = px.bar(df3, x='Registered Users', y='State', title=f"Top 10 Registered Users", orientation='h', height=800,
                             width=1000, color_discrete_sequence=px.colors.sequential.Aggrnyl, hover_name='State')
        st.plotly_chart(fig3)
    #     fig3.show()

    
def transactionTypeAnalysis(tableName):
    transactionAmountAnalysis = f'''SELECT Transaction_type, SUM(Transaction_amount) as Transaction_amount FROM {tableName}
                GROUP BY Transaction_type ORDER BY Transaction_amount DESC;'''
    cursor.execute(transactionAmountAnalysis)
    existingrecord1 = cursor.fetchall()
    df1 = pd.DataFrame(existingrecord1, columns=['Transaction Type', 'Transaction Amount'])
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(df1, x='Transaction Type', y='Transaction Amount', title=f"Transaction Type And Transaction Amount", height=600,
                                 width=600, color_continuous_scale=px.colors.sequential.Magenta, hover_name='Transaction Type')
        st.plotly_chart(fig1)
    #     fig1.show()

    transactionCountAnalysis = f'''SELECT Transaction_type, SUM(Transaction_count) as Transaction_count FROM {tableName}
                GROUP BY Transaction_type ORDER BY Transaction_count DESC;'''
    cursor.execute(transactionCountAnalysis)
    existingrecord2 = cursor.fetchall()
    df2 = pd.DataFrame(existingrecord2, columns=['Transaction Type', 'Transaction Count'])
    with col2:
        fig2 = px.bar(df2, x='Transaction Type', y='Transaction Count', title=f"Transaction Type And Transaction Count", height=600,
                                 width=600, color_continuous_scale=px.colors.sequential.Magenta, hover_name='Transaction Type')
        st.plotly_chart(fig2)
    #     fig2.show()


def brandAnalysis(tableName):
    transactionCountAnalysis = f'''SELECT Brand, SUM(Transaction_count) as Transaction_count FROM {tableName}
                GROUP BY Brand ORDER BY Transaction_count DESC;'''
    cursor.execute(transactionCountAnalysis)
    existingrecord1 = cursor.fetchall()
    df1 = pd.DataFrame(existingrecord1, columns=['Brand', 'Transaction Count'])
    fig1 = px.bar(df1, x='Brand', y='Transaction Count', title=f"Brand And Transaction Count", height=600,
                             width=1000, color_continuous_scale=px.colors.sequential.Magenta, hover_name='Brand')
    st.plotly_chart(fig1)
#     fig1.show()

def brandWiseRegisteredUsersAnalysis(tableName):
    registeredUsersAnalysis = f'''SELECT Brand, SUM(registeredUsers) as registeredUsers FROM {tableName}
                GROUP BY Brand ORDER BY registeredUsers DESC;'''
    cursor.execute(registeredUsersAnalysis)
    existingrecord1 = cursor.fetchall()
    df1 = pd.DataFrame(existingrecord1, columns=['Brand', 'Registeredusers'])
    fig1 = px.bar(df1, x='Brand', y='Registeredusers', title=f"Brand And RegisteredUsers", height=600,
                             width=1000, color_continuous_scale=px.colors.sequential.Magenta, hover_name='Brand')
    st.plotly_chart(fig1)
#     fig1.show()
    
    

# Streamlit Part
st.set_page_config(layout='wide')
st.title("Phonepe Plus Data Visualization Exploration")

with st.sidebar:
    select = option_menu("Main Menu",["Home", "Data Exploration", "Top Charts"])
    
if select == "Home":
    col1,col2= st.columns(2)

    with col1:
        st.header("PHONEPE")
        st.subheader("INDIA'S BEST TRANSACTION APP")
        st.markdown("PhonePe  is an Indian digital payments and financial technology company")
        st.write("****FEATURES****")
        st.write("****Credit & Debit card linking****")
        st.write("****Bank Balance check****")
        st.write("****Money Storage****")
        st.write("****PIN Authorization****")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.image(Image.open(r"C:\Users\Godveen\Guvi\capstoneProjects\images\Phonepay.jpg"),width= 600)

    col3,col4= st.columns(2)
    
    with col3:
        video_file = open("C:/Users/Godveen/Guvi/capstoneProjects/videos/phonepeAdv1.mp4", 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    with col4:
        st.write("****Easy Transactions****")
        st.write("****One App For All Your Payments****")
        st.write("****Your Bank Account Is All You Need****")
        st.write("****Multiple Payment Modes****")
        st.write("****PhonePe Merchants****")
        st.write("****Multiple Ways To Pay****")
        st.write("****1.Direct Transfer & More****")
        st.write("****2.QR Code****")
        st.write("****Earn Great Rewards****")

    col5,col6= st.columns(2)

    with col5:
        st.write("****No Wallet Top-Up Required****")
        st.write("****Pay Directly From Any Bank To Any Bank A/C****")
        st.write("****Instantly & Free****")

    with col6:
        st.image(Image.open(r"C:\Users\Godveen\Guvi\capstoneProjects\images\phonepe2.jpg"),width= 600)
elif select == "Data Exploration":
    tab1, tab2, tab3 = st.tabs(["Aggregated Analysis", "Map Analysis", "Top Analysis"])
    
    with tab1:
        aggmethodvalue = st.radio("Select The Method", ["Aggregated Transaction Analysis", "Aggregated User Analysis"])
        if aggmethodvalue == "Aggregated Transaction Analysis":
            AggTransDF = dataFrameCreationFromFileObj['AggTransDF']
            col1, col2 = st.columns(2)
            with col1:
                year = st.slider("Select the Year", int(AggTransDF['Year'].min()), int(AggTransDF['Year'].max()), int(AggTransDF['Year'].min()))
            Transaction_amount_count_Y_Obj = Transaction_amount_count_Y(AggTransDF, year)
            col1, col2 = st.columns(2)
            with col1:
                stateYearwise = st.selectbox("Select the State For Yearwise Analysis", Transaction_amount_count_Y_Obj['State'].unique())
            Transaction_amount_count_Type_State_Y_Obj = Transaction_amount_count_Type_State(Transaction_amount_count_Y_Obj, stateYearwise)
            col1, col2 = st.columns(2)
            with col1:
                quarter = st.slider("Select the Quarter", Transaction_amount_count_Y_Obj['Quater'].min(), Transaction_amount_count_Y_Obj['Quater'].max(), Transaction_amount_count_Y_Obj['Quater'].min())
            Transaction_amount_count_Q_Obj = Transaction_amount_count_Q(Transaction_amount_count_Y_Obj, quarter)
            col1, col2 = st.columns(2)
            with col1:
                stateQuarterwise = st.selectbox("Select the State For Quarterwise Analysis", Transaction_amount_count_Q_Obj['State'].unique())
            Transaction_amount_count_Type_State_Q_Obj = Transaction_amount_count_Type_State(Transaction_amount_count_Q_Obj, stateQuarterwise)
            
        elif aggmethodvalue == "Aggregated User Analysis":
            AggUsersDF = dataFrameCreationFromFileObj['AggUsersDF']
            
            col1, col2 = st.columns(2)
            with col1:
                year = st.slider("Select the Year", int(AggUsersDF['Year'].min()), int(AggUsersDF['Year'].max()), int(AggUsersDF['Year'].min()))
            aggregated_User_Yearwise_obj = aggregated_User_Yearwise(AggUsersDF, str(year))
            
            col1, col2 = st.columns(2)
            with col1:
                quarter = st.slider("Select the Quarter", aggregated_User_Yearwise_obj['Quater'].min(), aggregated_User_Yearwise_obj['Quater'].max(), aggregated_User_Yearwise_obj['Quater'].min())
            aggregated_User_Quarterwise_Obj = aggregated_User_Quarterwise(aggregated_User_Yearwise_obj, quarter)
            
            col1, col2 = st.columns(2)
            with col1:
                stateYearwise = st.selectbox("Select the State For Yearwise Analysis", aggregated_User_Yearwise_obj['State'].unique())
            aggregated_User_Statewise_Obj = aggregated_User_Statewise(aggregated_User_Yearwise_obj, stateYearwise)
                
    with tab2:
        mapmethodvalue = st.radio("Select The Method", ["Map Transaction Analysis", "Map User Analysis"])
        if mapmethodvalue == "Map Transaction Analysis":
            mapTransactionDF = dataFrameCreationFromFileObj['mapTransactionDF']
            col1, col2 = st.columns(2)
            with col1:
                year = st.slider("Select the Map Transaction Analysis Year", int(mapTransactionDF['Year'].min()), int(mapTransactionDF['Year'].max()), int(mapTransactionDF['Year'].min()))
            mapTransactionAmountCountYearwiseObj = Transaction_amount_count_Y(mapTransactionDF, year)
            
            col1, col2 = st.columns(2)
            with col1:
                stateYearwise = st.selectbox("Select the State For Map Transaction Analysis Statewise", mapTransactionAmountCountYearwiseObj['State'].unique())
            mapTransactionAmountCountStatewiseobj = mapTransactionAmountCountStatewise(mapTransactionAmountCountYearwiseObj, stateYearwise)
            
            col1, col2 = st.columns(2)
            with col1:
                quarter = st.slider("Select the For Map Transaction Analysis Qyaterwise", mapTransactionAmountCountYearwiseObj['Quater'].min(), mapTransactionAmountCountYearwiseObj['Quater'].max(), mapTransactionAmountCountYearwiseObj['Quater'].min())
            mapTransactionAmountCountQuaterwiseObj = Transaction_amount_count_Q(mapTransactionAmountCountYearwiseObj, quarter)
            
            col1, col2 = st.columns(2)
            with col1:
                stateYearwise = st.selectbox("Select the State For Map Transaction Analysis Quaterwise Statewise", mapTransactionAmountCountQuaterwiseObj['State'].unique())
            mapTransactionAmountCountQuaterwiseStatewiseObj = mapTransactionAmountCountStatewise(mapTransactionAmountCountQuaterwiseObj, stateYearwise)
 
        elif mapmethodvalue == "Map User Analysis":
            mapUserDF = dataFrameCreationFromFileObj['mapUserDF']
            col1, col2 = st.columns(2)
            with col1:
                year = st.slider("Select the Map User Analysis Yearwise", int(mapUserDF['Year'].min()), int(mapUserDF['Year'].max()), int(mapUserDF['Year'].min()))
            mapUserAnalysisYearwiseObj = mapUserAnalysisYearwise(mapUserDF, year)
            
            col1, col2 = st.columns(2)
            with col1:
                quater = st.slider("Select the Map User Analysis Quaterwise", int(mapUserAnalysisYearwiseObj['Quater'].min()), int(mapUserAnalysisYearwiseObj['Quater'].max()), int(mapUserAnalysisYearwiseObj['Quater'].min()))
            mapUserAnalysisQuaterwiseObj = mapUserAnalysisQuaterwise(mapUserAnalysisYearwiseObj, quater)
            
            col1, col2 = st.columns(2)
            with col1:
                stateYearwise = st.selectbox("Select the State For Map User Analysis Quaterwise Statewise", mapUserAnalysisQuaterwiseObj['State'].unique())
            mapUserAnalysisStatewiseObj = mapUserAnalysisStatewise(mapUserAnalysisQuaterwiseObj, stateYearwise)
 
    with tab3:
        topmethodvalue = st.radio("Select The Method", ["Top Transaction Analysis", "Top User Analysis"])
        if topmethodvalue == "Top Transaction Analysis":
            topTransactionDF = dataFrameCreationFromFileObj['topTransactionDF']
            col1, col2 = st.columns(2)
            with col1:
                year = st.slider("Select the Top Transaction Analysis For Yearwise", int(topTransactionDF['Year'].min()), int(topTransactionDF['Year'].max()), int(topTransactionDF['Year'].min()))
            topTransactionAmountCountYearwiseobj = Transaction_amount_count_Y(topTransactionDF, year)

            col1, col2 = st.columns(2)
            with col1:
                stateYearwise = st.selectbox("Select the State For Top Transaction Analysis Statewise", topTransactionAmountCountYearwiseobj['State'].unique())
            topTransactionAnalysisStatewiseObj = topTransactionAnalysisStatewise(topTransactionAmountCountYearwiseobj, stateYearwise)
 
            col1, col2 = st.columns(2)
            with col1:
                quarter = st.slider("Select the Top Transaction Analysis For Quaterwise", topTransactionAmountCountYearwiseobj['Quater'].min(), topTransactionAmountCountYearwiseobj['Quater'].max(), topTransactionAmountCountYearwiseobj['Quater'].min())
            topTransactionAmountCountQuaterwiseObj = Transaction_amount_count_Q(topTransactionAmountCountYearwiseobj, quarter)
            
        elif topmethodvalue == "Top User Analysis":
            topUserDF = dataFrameCreationFromFileObj['topUserDF']
            col1, col2 = st.columns(2)
            with col1:
                year = st.slider("Select the Top User Analysis For Yearwise", int(topUserDF['Year'].min()), int(topUserDF['Year'].max()), int(topUserDF['Year'].min()))
            topUserYearwiseQuaterwiseAnalysisObj = topUserYearwiseQuaterwiseAnalysis(topUserDF, year)
            
            col1, col2 = st.columns(2)
            with col1:
                stateYearwise = st.selectbox("Select the State For Top User Analysis Statewise", topUserYearwiseQuaterwiseAnalysisObj['State'].unique())
            topUserYearwiseQuaterwiseStatewisePincodeAnalysisObj = topUserYearwiseQuaterwiseStatewisePincodeAnalysis(topUserYearwiseQuaterwiseAnalysisObj, stateYearwise)
            
            
elif select == "Top Charts":
    stateYearwise = st.selectbox("Select the Questions",[
        '1.Transaction Amount and Count of Aggregated Transaction',
        '2.Transaction Amount and Count of Map Transaction',
        '3.Transaction Amount and Count of Top Transaction',
        '4.Transaction Count of Aggregated User',
        '5.Registered USers of Map User',
        '6.App Opens of Map User',
        '7.Registered Users of Top User',
        '8.Transaction Type Analysis in Aggregated Transaction',
        '9.Brand Analysis in Aggregated User',
        '10.Brandwise Registered Users Analysis in Aggregated User'
    ])
    if (stateYearwise == '1.Transaction Amount and Count of Aggregated Transaction'):
        transactionAmountAnalysis('aggregatedTransaction')
        transactionCountAnalysis('aggregatedTransaction')
    elif (stateYearwise == '2.Transaction Amount and Count of Map Transaction'):
        transactionAmountAnalysis('mapTransaction')
        transactionCountAnalysis('mapTransaction')
    elif (stateYearwise == '3.Transaction Amount and Count of Top Transaction'):
        transactionAmountAnalysis('topTransaction')
        transactionCountAnalysis('topTransaction')
    elif (stateYearwise == '4.Transaction Count of Aggregated User'):
        transactionCountAnalysis('aggregatedUser')
    elif (stateYearwise == '5.Registered USers of Map User'):
        mapUserDF = dataFrameCreationFromFileObj['mapUserDF']
        state = st.selectbox("Select the State", mapUserDF['State'].unique())
        statewiseRegisteredUsersAnalysis('mapUser', state)
    elif (stateYearwise == '6.App Opens of Map User'):
        mapUserDF = dataFrameCreationFromFileObj['mapUserDF']
        state = st.selectbox("Select the State", mapUserDF['State'].unique())
        statewiseAppOpensAnalysis('mapUser', state)
    elif (stateYearwise == '7.Registered Users of Top User'):
        registeredUsersAnalysis('topUser')
    elif (stateYearwise == '8.Transaction Type Analysis in Aggregated Transaction'):
        transactionTypeAnalysis('aggregatedTransaction') 
    elif (stateYearwise == '9.Brand Analysis in Aggregated User'):
        brandAnalysis('aggregatedUser') 
    elif (stateYearwise == '10.Brandwise Registered Users Analysis in Aggregated User'):
        brandWiseRegisteredUsersAnalysis('aggregatedUser')
        
        
conn.close()