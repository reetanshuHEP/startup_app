import streamlit as st
import  pandas as pd
import plotly.express as px

st.set_page_config(layout='wide',page_title='Startup Analysis')
df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

def load_overall_analysis():
   st.title('Overall Analysis')
   #total invested amount
   total = round(df['amount'].sum())

   # max investment
   max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]

   #average investement
   avg_funding = df.groupby('startup')['amount'].sum().mean()

   #total no of startup
   num_startup = df['startup'].nunique()


   col1,col2,col3,col4=st.columns(4)

   with col1:
      st.metric('Total Investments', str(total) + ' Cr')

   with col2:
      st.metric('Max',str(max_funding)  + ' Cr')


   with col3:
      st.metric('Avg', str(round(avg_funding)) + ' Cr')

   with col4:
      st.metric('Total Funded Startup', str(num_startup))


   # top 5 startups
   grouped = df.groupby('startup')['amount']

   # Calculate total, highest, and average investment for each startup
   investment_data = pd.concat([grouped.sum(), grouped.max(), grouped.mean()], axis=1)
   investment_data.columns = ['Total Investment', 'Highest Investment', 'Average Investment']

   # Select the top 5 startups with the highest total investment
   top_5_companies = investment_data.nlargest(5, 'Total Investment')


   # Display the data
   st.write("Top 5 Startups in terms of Total Investments:")
   st.table(top_5_companies)

   st.header('MoM graph')
   selected_option = st.selectbox('Select Type',['Total','Count'])
   if selected_option == 'Total':
       temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
       temp_df.columns = ['year', 'month', 'Total']
   else:
       temp_df = df.groupby(['year', 'month']).size().reset_index(name='Count')

   temp_df['x_axis'] = temp_df['month'].astype('str') + '_' + temp_df['year'].astype('str')

   # use plotly express to create a line chart
   fig6 = px.line(temp_df, x=temp_df['x_axis'], y=temp_df[selected_option], title='Month on Month Wise Investments')
   # Change line color to green
   fig6.update_traces(line=dict(color='green'))
   st.plotly_chart(fig6)  # display the plotly chart





def load_investor_details(investor):
   st.title(investor)
   #load recent 5 investments of the investor
   last5_df = df[df['investors'].str.contains(investor)].head(5)[
      ['date', 'startup', 'vertical', 'city', 'round', 'amount']]
   st.subheader('Most Recent Investments')
   st.dataframe(last5_df)

   col1,col2 = st.columns(2)
   with col1:
      # biggest investment
      big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
      st.subheader('Biggest Investments')
      # use plotly express to create a bar chart with hover features
      fig = px.bar(big_series, x=big_series.index, y=big_series.values, color=big_series.index, labels={'x': 'Startup', 'y': 'Amount (in cr)'})
      fig.update_layout(showlegend=False) # remove the legend
      st.plotly_chart(fig) # display the plotly chart

   with col2:
      vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
      st.subheader('Sector Wise Investments')
      # use plotly express to create a pie chart with hover features
      fig1 = px.pie(vertical_series, values=vertical_series.values, names=vertical_series.index, title='Sector Wise Investments')
      fig1.update_traces(textposition='inside', textinfo='percent+label') # show the percentage and label inside the slices
      st.plotly_chart(fig1) # display the plotly chart

   col3,col4 = st.columns(2)
   with col3:
      round_series = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
      st.subheader('Round Wise Investments')
      # use plotly express to create a pie chart with hover features
      fig2 = px.pie(round_series, values=round_series.values, names=round_series.index, title='Round Wise Investments')
      fig2.update_traces(textposition='inside', textinfo='percent+label')  # show the percentage and label inside the slices
      st.plotly_chart(fig2)  # display the plotly chart

   with col4:
      city_series = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
      st.subheader('City Wise Investments')
      # use plotly express to create a pie chart with hover features
      fig3 = px.pie(city_series, values=city_series.values, names=city_series.index, title='City Wise Investments')
      fig3.update_traces(textposition='inside', textinfo='percent+label')  # show the percentage and label inside the slices
      st.plotly_chart(fig3)  # display the plotly chart


   col5,col6 = st.columns(2)

   with col5:
      df['year'] = df['date'].dt.year
      year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
      st.subheader('Year Wise Investments')
      # use plotly express to create a line chart
      fig4 = px.line(year_series, y=year_series.values, x=year_series.index, title='Year Wise Investments')
      st.plotly_chart(fig4)  # display the plotly chart


st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
      load_overall_analysis()

elif option == 'Startup':
   st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
   btn1=st.sidebar.button('Find Startup Details')
   st.title('Startup Analysis')
else:
   selected_investor = st.sidebar.selectbox('Select Startup',sorted(set(df['investors'].str.split(',').sum())))
   btn2 = st.sidebar.button('Find Investor Details')
   if btn2:
      load_investor_details(selected_investor)
