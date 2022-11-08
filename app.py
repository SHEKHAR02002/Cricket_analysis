
from gettext import npgettext
from queue import Empty
from sqlite3 import Row
from tkinter import X
import streamlit as st
import pandas as pd
from PIL import Image
import preprocessor
import matplotlib.pyplot as plt




 
# with open("styles.css") as source_code:

with st.sidebar:
        st.title("Cricket Analysis")
        st.title("Enter Data")
        player_name = st.text_input("Enter Batsman Name:", "")
        opponent_name = st.text_input("Enter Opponent Team Name:", "")
        Venue = st.text_input("Enter Venue:", "")

        if st.button('Enter'):
           button_type = "enter"
           match,opponent,venue = preprocessor.most_out(player_name,opponent_name,Venue)
           baller_type,ball_type = preprocessor.data_main(player_name,opponent_name,Venue)
           #x_graph,h_graph = preprocessor.graph(player_name,opponent_name,Venue)
        else:
            
            st.write('Something went wrong')
        
        if st.button('Get Detail Data'):
          button_type = "detail"
          fast,yorker,slower,length,bounser = preprocessor.faster(player_name,opponent_name,Venue)
          mfast,myorker,mslower,mlength,mbounser = preprocessor.medium_faster(player_name,opponent_name,Venue)
          offspiner,googly,offspin,carrom = preprocessor.off_spiner(player_name,opponent_name,Venue)
          ooffspiner,ogoogly,ooffspin,ocarrom = preprocessor.off_spiner(player_name,opponent_name,Venue)
        else:
           
           st.write('Something went wrong')

        if st.button('Get Graph'):
           button_type = "graph"
           
           x_graph,h_graph = preprocessor.graph(player_name,opponent_name,Venue)

        else:
            
            st.write('Something went wrong')


       

           
           
    
################
if(button_type=="enter"):
    st.header("Player Pervious Out Detail")
    st.title("Most Of The Time Out On")      
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Baller Type")
        st.text(baller_type)

    with col2:
        st.subheader("Ball type")
        st.text(ball_type)

    ############
    st.title("   ")
    st.title("Player Match Details")      
    col3,col4,col5 = st.columns(3)
    with col3:
        st.subheader("Total Match")
        st.text(match)

    with col4:
        st.subheader("Total Match Against Opponent")
        st.text(opponent)

    with col5:
        st.subheader("Total Match on This Venue")
        st.text(venue)
    



   ############

elif(button_type=="detail"):
    st.title("   ")
    st.title("FASTER")
    col6,col7,col8,col9,col10= st.columns(5)
    with col6:
        st.subheader("Faster")
        st.text(fast)

    with col7:
        st.subheader("Yorker")
        st.text(yorker)

    with col8:
        st.subheader("Slower")
        st.text(slower)

    with col9:
        st.subheader("Length Ball")
        st.text(length)

    with col10:
        st.subheader("Bouncer")
        st.text(bounser)


    st.title("   ")
    st.title("MEDIUM FASTER")
    col11,col12,col3,col4,col15= st.columns(5)
    with col11:
        st.subheader("Medium Faster")
        st.text(mfast)

    with col12:
        st.subheader("Yorker")
        st.text(myorker)

    with col3:
        st.subheader("Slower")
        st.text(mslower)

    with col4:
        st.subheader("Length Ball")
        st.text(mlength)

    with col15:
        st.subheader("Bouncer")
        st.text(mbounser)


    st.title("   ")
    st.title("OFF SPINER")
    col16,col17,col18,col19= st.columns(4)
    with col16:
        st.subheader("Off Spiner")
        st.text(offspiner)

    with col17:
        st.subheader("GOOGLY")
        st.text(googly)

    with col18:
        st.subheader("Off Spin")
        st.text(offspin)

    with col19:
        st.subheader("Carrom Ball")
        st.text(carrom)



    st.title("   ")
    st.title("ON SPINER")
    col20,col21,col22,col23= st.columns(4)
    with col20:
        st.subheader("On Spiner")
        st.text(ooffspiner)

    with col21:
        st.subheader("GOOGLY")
        st.text(ogoogly)

    with col22:
        st.subheader("ON SPIN")
        st.text(ooffspin)

    with col23:
        st.subheader("CARROM BALL")
        st.text(ocarrom)


elif(button_type=="graph"):
    st.title("Batsman Out Analysis")
    data={"Baller Type":x_graph,"Most Time Out":h_graph}
    data=pd.DataFrame(data)
    data=data.set_index("Baller Type")
    st.bar_chart(data)

elif(button_type=="empty"):
    st.title("     ")







    

    
    


    





    #image = Image.open('Image.png')

    #st.image(image, caption='Sunrise by the mountains')



        


       












