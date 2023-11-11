import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('i am learning streamlit')
st.subheader('enjoying')


st.write('This is the normal text')

st.markdown("""
### best movies
- 3 idiots
- 2 state
""")

#display code:

st.code("""
def cube(x):
    return x**3

""")

#latex



#dataframe

df =pd.DataFrame({
   'name':['ram','shyam'],
   'marks':['60','70'],
   'package':['6','8']
})

st.dataframe(df)

#metric

st.metric('revenue', 'Rs 3L','1%')

#json

st.json({
   'name':['ram','shyam'],
   'marks':['60','70'],
   'package':['6','8']
})

#image

st.image('xg1.png')

#Video
st.video('vide0.mp4')

#audio

st.audio('har.m4a')

#layouts

#sidebar

st.sidebar.title('sidebar title')

col1,col2 = st.columns(2)

with col1:
   st.image('xg1.png')

with col2:
   st.image('xg1.png')

#showing process

st.error('login failed')
st.success('login success')
st.info('welcome')
st.warning('you are moving to other website')

'''
#progress bar:

bar= st.progress(0)

for i in range(1,101):
   time.sleep(0.1)
   bar.progress(i)

'''
#user input

email = st.text_input('Enter email')
number=st.number_input('Enter number')
date=st.date_input('Enter date')

#button


import streamlit as st

email =st.text_input('Enter email')
password=st.text_input('enter password')
gender=st.selectbox('select gender',['male','female'])

btn=st.button('login')

if btn:
   if email=='r121@gmail.com'  and password == '123':
      st.write(gender)
      st.success('welcome 😊')
      st.balloons()

   else:
      st.error('tu hai kaun be 👀')


import streamlit as st
import  pandas as pd

#file uploader

file=st.file_uploader('upload csv file')

if file is not None:
   df=pd.read_csv(file)
   st.dataframe(df.describe())


#
import streamlit as st
import  pandas as pd

df = pd.read_csv('startup_funding.csv')

st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
   st.title('Overall Analysis')
elif option == 'Startup':
   st.sidebar.selectbox('Select Startup',['Byjus','Ola','Flipcart'])
   st.title('Startup Analysis')
else:
   st.sidebar.selectbox('Select Startup',['amir aadmi 1','amir aadmi 2','amir aadmi 3'])
   st.title('Invester Analysis')















