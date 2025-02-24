import streamlit as slt
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
slt.title('hello')
slt.header('Header title')
slt.subheader('subHeader title')
slt.subheader('subHeader title')
slt.text('text')

slt.markdown('#hi')
slt.markdown('##hi')
slt.markdown('###hi')
slt.markdown('####hi')
slt.markdown('###hi')

slt.success('data is submitted')
slt.info('Information')
slt.warning('warning')
slt.error('Error!')

slt.exception(ZeroDivisionError('Division is not possible'))

slt.help(ZeroDivisionError)

slt.write(range(1, 10))
slt.write("Hello World")

slt.code('x  = 10'
         'for  i  in range(x):'
         
         'print(i)')

#checkbox

slt.checkbox('male')
slt.checkbox('female')

if(slt.checkbox('Adult')):
    slt.write("you are male")


option = slt.radio('select',['check', 'unckeck'])
slt.write('you selected' , option)


slt.subheader('select box')
selection = slt.selectbox('Data science' , ['Data Analytics', 'Webdeveloper' , 'python Developer'])

slt.write('you selected' ,selection)

slt.subheader('Multiselect Box')

multi = slt.multiselect('Datascience' ,['Webdeveloper' , 'pythondeveloper'])

slt.write('you selected' , len(multi))

slt.subheader('button')
if(slt.button('click me')):
    slt.write('thanks')
    
slt.slider('select level' , 1,100 , step = 2)


slt.subheader('userinput')
name = slt.text_input('name')
slt.write('hi', name)
password = slt.text_input('Password' , type='password')
slt.write('Text area')
slt.text_area('write something')
slt.write('select age')
slt.number_input('select age' , 18 , 40)

slt.date_input('date')

slt.time_input('Time')


slt.subheader('uploading csv file')

# slt.file_uploader('upload csv file' , type=['csv', 'xsl', 'pdf' ])
# df = pd.read_csv('ResumeYash.csv') #use path file

# slt.table(df.head())


slt.subheader('images')
slt.image(r'c:\Users\abc\Pictures\Screenshots\Screenshot 2024-10-26 201401.png')

videos = slt.file_uploader('upload video' ,type=['mkv' , 'mp4'])
if videos is not None:
    slt.video(videos , start_time= 0)
audios = slt.file_uploader('upload video' ,type=['mp3' , 'wav'])
if audios is not None:
    slt.audio(audios , start_time= 0)
    
char_data = pd.DataFrame(np.random.randn(100 , 2) , columns=['Line-1' ,'Line-2'])
slt.subheader('Linechart')
slt.line_chart(char_data)

slt.area_chart(char_data)
slt.bar_chart(char_data)

# slt.subheader('distance plot')
# plt.figure(figsize = (15 , 0))
