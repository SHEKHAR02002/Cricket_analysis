import pandas as pd

data = pd.read_csv("Rohit.csv")

def most_out(player,opponent,venue):

    global data

    player_name = player
    opponent_name = opponent
    venue_name = venue
    sort_data1 = data.loc[(data['Batsman']== player_name)]
    sort_data2 = data.loc[(data['Batsman']==player_name) & (data['Opponent Team Name']==opponent_name)]
    sort_data3 = data.loc[(data['Batsman']==player_name) & (data['Opponent Team Name']==opponent_name) & (data['Venue']==venue_name)]
    y1=len(sort_data1.axes[0])
    y2=len(sort_data2.axes[0])
    y=len(sort_data3.axes[0])
    return y1,y2,y

def data_main(player,opponent,venue):

    global data
    player_name = player
    opponent_name = opponent
    venue_name = venue
    sort_data3 = data.loc[(data['Batsman']==player_name) & (data['Opponent Team Name']==opponent_name) & (data['Venue']==venue_name)]
    y=len(sort_data3.axes[0])
    
    faster=sort_data3.loc[(sort_data3['Baller Type']=='Faster')]
    faster_rows = len(faster.axes[0])
    

    medium_faster=sort_data3.loc[(sort_data3['Baller Type']=='Medium Faster')]
    medium_faster_rows = len(medium_faster.axes[0])
    

    off_spin=sort_data3.loc[(sort_data3['Baller Type']=='Off Spiner')]
    off_spin_rows= len(off_spin.axes[0])
    
 
    on_spin=sort_data3.loc[(sort_data3['Baller Type']=='On Spiner')]
    on_spin_rows = len(on_spin.axes[0])
    
   
    ###Percentage
    
    percentage_faster = int((faster_rows*100)/y)
    percentage_medium_faster = int((medium_faster_rows*100)/y)
    percentage_off_spin = int((off_spin_rows*100)/y)
    percentage_on_spin = int((on_spin_rows*100)/y)
    
    
    
    

    if(percentage_faster>percentage_medium_faster and percentage_faster>percentage_off_spin and percentage_faster>percentage_on_spin):
        
        faster_yorker=faster.loc[(faster['Ball Type']=='Yorker')]
        faster_slower=faster.loc[(faster['Ball Type']=='Slower')]
        faster_length_ball=faster.loc[(faster['Ball Type']=='Length Ball')]
        faster_bouncer=faster.loc[(faster['Ball Type']=='Bouncer')]
        
        faster_yorker_rows= len(faster_yorker.axes[0])
        faster_slower_rows = len(faster_slower.axes[0])
        faster_length_ball_rows= len(faster_length_ball.axes[0])
        faster_bouncer_rows= (len(faster_bouncer.axes[0]))
        
        #Percentage 
        percentage_faster_yorker_rows= int((faster_yorker_rows*100)/faster_rows)
        percentage_faster_slower_rows = int((faster_slower_rows*100)/faster_rows)
        percentage_faster_length_ball_rows= int((faster_length_ball_rows*100)/faster_rows)
        percentage_faster_bouncer_rows= int((faster_bouncer_rows*100)/faster_rows)
        
        if(percentage_faster_yorker_rows>percentage_faster_slower_rows and percentage_faster_yorker_rows>percentage_faster_length_ball_rows and percentage_faster_yorker_rows>percentage_faster_bouncer_rows):
            baller_type = "FASTER BALLER"
            ball_type = "YORKER BALL"
            return baller_type,ball_type

        elif(percentage_faster_slower_rows>percentage_faster_yorker_rows and percentage_faster_slower_rows>percentage_faster_length_ball_rows and percentage_faster_slower_rows>percentage_faster_bouncer_rows):
            baller_type = "FASTER BALLER"
            ball_type = "SLOWER BALL"
            return baller_type,ball_type

        elif(percentage_faster_length_ball_rows>percentage_faster_yorker_rows and percentage_faster_length_ball_rows>percentage_faster_slower_rows and percentage_faster_length_ball_rows>percentage_faster_bouncer_rows):
            baller_type = "FASTER BALLER"
            ball_type = "LENGTH BALL"
            return baller_type,ball_type
            
        else:
            baller_type = "FASTER BALLER"
            ball_type = "BOUNCER"
            return baller_type,ball_type
    
            
            
    #medium faster
    elif(percentage_medium_faster>percentage_faster and percentage_medium_faster> percentage_off_spin and percentage_medium_faster>percentage_on_spin):
        medium_faster_yorker=medium_faster.loc[(medium_faster['Ball Type']=='Yorker')]
        medium_faster_slower=medium_faster.loc[(medium_faster['Ball Type']=='Slower')]
        medium_faster_length_ball=medium_faster.loc[(medium_faster['Ball Type']=='Length Ball')]
        medium_faster_bouncer=medium_faster.loc[(medium_faster['Ball Type']=='Bouncer')]
        
        medium_faster_yorker_rows= (len(medium_faster_yorker.axes[0]))
        medium_faster_slower_rows = (len(medium_faster_slower.axes[0]))
        medium_faster_length_ball_rows= int(len(medium_faster_length_ball.axes[0]))
        medium_faster_bouncer_rows= (len(medium_faster_bouncer.axes[0]))
        
        #Percentage 
        percentage_medium_faster_yorker_rows= int((medium_faster_yorker_rows*100)/medium_faster_rows)
        percentage_medium_faster_slower_rows = int((medium_faster_slower_rows*100)/medium_faster_rows)
        percentage_medium_faster_length_ball_rows= int((medium_faster_length_ball_rows*100)/medium_faster_rows)
        percentage_medium_faster_bouncer_rows= int((medium_faster_bouncer_rows*100)/medium_faster_rows)
        
        if(percentage_medium_faster_yorker_rows>percentage_medium_faster_slower_rows and percentage_medium_faster_yorker_rows>percentage_medium_faster_length_ball_rows and percentage_medium_faster_yorker_rows>percentage_medium_faster_bouncer_rows):
            baller_type = "MEDIUM FASTER BALLER"
            ball_type = "YORKER BALL"
            return baller_type,ball_type

          
        elif(percentage_medium_faster_slower_rows>percentage_medium_faster_yorker_rows and percentage_medium_faster_slower_rows>percentage_medium_faster_length_ball_rows and percentage_medium_faster_slower_rows>percentage_medium_faster_bouncer_rows):
            baller_type = "MEDIUM FASTER BALLER"
            ball_type = "SLOWER BALL"
            return baller_type,ball_type
            
        elif(percentage_medium_faster_length_ball_rows>percentage_medium_faster_yorker_rows and percentage_medium_faster_length_ball_rows>percentage_medium_faster_slower_rows and percentage_medium_faster_length_ball_rows>percentage_medium_faster_bouncer_rows):
            baller_type = "MEDIUM FASTER BALLER"
            ball_type = "LENGTH BALL"
            return baller_type,ball_type
            
        else:
            baller_type = "MEDIUM FASTER BALLER"
            ball_type = "BOUNCER BALL"
            return baller_type,ball_type
           

    ##Off Spiner
    elif(percentage_off_spin>percentage_faster and percentage_off_spin>percentage_medium_faster and percentage_off_spin>percentage_on_spin):
        
        offspin_googly=off_spin.loc[(off_spin['Ball Type']=='Googly')]
        offspin_OFFSPIN=off_spin.loc[(off_spin['Ball Type']=='Off Spin')]
        offspin_carrom_ball=off_spin.loc[(off_spin['Ball Type']=='Carrom Ball')]
        
        
        offspin_googly_rows= (len(offspin_googly.axes[0]))
        offspin_OFFSPIN_rows = (len(offspin_OFFSPIN.axes[0]))
        offspin_carrom_ball_rows= int(len(offspin_carrom_ball.axes[0]))
        
        
        #Percentage 
        percentage_offspin_googly_rows= int((offspin_googly_rows*100)/off_spin_rows)
        percentage_offspin_OFFSPIN_rows = int((offspin_OFFSPIN_rows*100)/off_spin_rows)
        percentage_offspin_carrom_ball_rows= int((offspin_carrom_ball_rows*100)/off_spin_rows)
        
        if(percentage_offspin_googly_rows>percentage_offspin_OFFSPIN_rows and percentage_offspin_googly_rows>offspin_carrom_ball_rows):
            baller_type = "OFF SPINER BALLER"
            ball_type = "GOOGLY BALL"
            return baller_type,ball_type
            
        elif(percentage_offspin_OFFSPIN_rows>percentage_offspin_googly_rows and percentage_offspin_OFFSPIN_rows>percentage_offspin_carrom_ball_rows):
            baller_type = "OFF SPINER BALLER"
            ball_type = "OFF SPIN BALL"
            return baller_type,ball_type
            
        else:
            baller_type = "OFF SPINER BALLER"
            ball_type = "CARROM BALL"
            return baller_type,ball_type
           
        
    else:
        onspin_googly=on_spin.loc[(on_spin['Ball Type']=='Googly')]
        onspin_OFFSPIN=on_spin.loc[(on_spin['Ball Type']=='Off Spin')]
        onspin_carrom_ball=on_spin.loc[(on_spin['Ball Type']=='Carrom Ball')]
        
        
        onspin_googly_rows= (len(onspin_googly.axes[0]))
        onspin_OFFSPIN_rows = (len(onspin_OFFSPIN.axes[0]))
        onspin_carrom_ball_rows= int(len(onspin_carrom_ball.axes[0]))
        
        
        #Percentage 
        percentage_onspin_googly_rows= int((onspin_googly_rows*100)/on_spin_rows)
        percentage_onspin_OFFSPIN_rows = int((onspin_OFFSPIN_rows*100)/on_spin_rows)
        percentage_onspin_carrom_ball_rows= int((onspin_carrom_ball_rows*100)/on_spin_rows)
        
        if(percentage_onspin_googly_rows>percentage_onspin_OFFSPIN_rows and percentage_onspin_googly_rows>onspin_carrom_ball_rows):
            baller_type = "ON SPINER BALLER"
            ball_type = "GOOGLY BALL"
            return baller_type,ball_type
           
        elif(percentage_onspin_OFFSPIN_rows>percentage_onspin_googly_rows and percentage_onspin_OFFSPIN_rows>percentage_onspin_carrom_ball_rows):
            baller_type = "ON SPINER BALLER"
            ball_type = "ON SPIN BALL"
            return baller_type,ball_type
           
        else:
            baller_type = "ON SPINER BALLER"
            ball_type = "CARROM BALL"
            return baller_type,ball_type


def faster(player,opponent,venue):
    player_name = player
    opponent_name = opponent
    venue_name = venue

    sort_data3 = data.loc[(data['Batsman']==player_name) & (data['Opponent Team Name']==opponent_name) & (data['Venue']==venue_name)]
    y=len(sort_data3.axes[0])
    
    faster=sort_data3.loc[(sort_data3['Baller Type']=='Faster')]
    faster_rows = len(faster.axes[0])
    
    ###Percentage
    
    percentage_faster = int((faster_rows*100)/y)
    
    
    
    
    ######Faster########
        
    faster_yorker=faster.loc[(faster['Ball Type']=='Yorker')]
    faster_slower=faster.loc[(faster['Ball Type']=='Slower')]
    faster_length_ball=faster.loc[(faster['Ball Type']=='Length Ball')]
    faster_bouncer=faster.loc[(faster['Ball Type']=='Bouncer')]
        
    faster_yorker_rows= len(faster_yorker.axes[0])
    faster_slower_rows = len(faster_slower.axes[0])
    faster_length_ball_rows= len(faster_length_ball.axes[0])
    faster_bouncer_rows= (len(faster_bouncer.axes[0]))
        
     #Percentage 
    percentage_faster_yorker_rows= int((faster_yorker_rows*100)/faster_rows)
    percentage_faster_slower_rows = int((faster_slower_rows*100)/faster_rows)
    percentage_faster_length_ball_rows= int((faster_length_ball_rows*100)/faster_rows)
    percentage_faster_bouncer_rows= int((faster_bouncer_rows*100)/faster_rows)

    return faster_rows,faster_yorker_rows,faster_slower_rows,faster_length_ball_rows,faster_bouncer_rows
    
def medium_faster(player,opponent,venue):
    sort_data3 = data.loc[(data['Batsman']==player) & (data['Opponent Team Name']==opponent) & (data['Venue']==venue)]
    y=len(sort_data3.axes[0])

    medium_faster=sort_data3.loc[(sort_data3['Baller Type']=='Medium Faster')]
    medium_faster_rows = len(medium_faster.axes[0])

    percentage_medium_faster = int((medium_faster_rows*100)/y)

    #########Medium Faster############
        
    medium_faster_yorker=medium_faster.loc[(medium_faster['Ball Type']=='Yorker')]
    medium_faster_slower=medium_faster.loc[(medium_faster['Ball Type']=='Slower')]
    medium_faster_length_ball=medium_faster.loc[(medium_faster['Ball Type']=='Length Ball')]
    medium_faster_bouncer=medium_faster.loc[(medium_faster['Ball Type']=='Bouncer')]
        
    medium_faster_yorker_rows= (len(medium_faster_yorker.axes[0]))
    medium_faster_slower_rows = (len(medium_faster_slower.axes[0]))
    medium_faster_length_ball_rows= int(len(medium_faster_length_ball.axes[0]))
    medium_faster_bouncer_rows= (len(medium_faster_bouncer.axes[0]))
        
    #Percentage 
    percentage_medium_faster_yorker_rows= int((medium_faster_yorker_rows*100)/medium_faster_rows)
    percentage_medium_faster_slower_rows = int((medium_faster_slower_rows*100)/medium_faster_rows)
    percentage_medium_faster_length_ball_rows= int((medium_faster_length_ball_rows*100)/medium_faster_rows)
    percentage_medium_faster_bouncer_rows= int((medium_faster_bouncer_rows*100)/medium_faster_rows)

    return medium_faster_rows,medium_faster_yorker_rows,medium_faster_slower_rows,medium_faster_length_ball_rows,medium_faster_bouncer_rows


def off_spiner(player,opponent,venue):
    sort_data3 = data.loc[(data['Batsman']==player) & (data['Opponent Team Name']==opponent) & (data['Venue']==venue)]
    y=len(sort_data3.axes[0])

    off_spin=sort_data3.loc[(sort_data3['Baller Type']=='Off Spiner')]
    off_spin_rows= len(off_spin.axes[0])

    percentage_off_spin = int((off_spin_rows*100)/y)

    #####Off Spiner#######
    offspin_googly=off_spin.loc[(off_spin['Ball Type']=='Googly')]
    offspin_OFFSPIN=off_spin.loc[(off_spin['Ball Type']=='Off Spin')]
    offspin_carrom_ball=off_spin.loc[(off_spin['Ball Type']=='Carrom Ball')]
        
        
    offspin_googly_rows= (len(offspin_googly.axes[0]))
    offspin_OFFSPIN_rows = (len(offspin_OFFSPIN.axes[0]))
    offspin_carrom_ball_rows= int(len(offspin_carrom_ball.axes[0]))
        
        
    #Percentage 
    percentage_offspin_googly_rows= int((offspin_googly_rows*100)/off_spin_rows)
    percentage_offspin_OFFSPIN_rows = int((offspin_OFFSPIN_rows*100)/off_spin_rows)
    percentage_offspin_carrom_ball_rows= int((offspin_carrom_ball_rows*100)/off_spin_rows)

    return off_spin_rows,offspin_googly_rows,offspin_OFFSPIN_rows,offspin_carrom_ball_rows
  


def on_spiner(player,opponent,venue):
    sort_data3 = data.loc[(data['Batsman']==player) & (data['Opponent Team Name']==opponent) & (data['Venue']==venue)]
    y=len(sort_data3.axes[0])

    on_spin=sort_data3.loc[(sort_data3['Baller Type']=='On Spiner')]
    on_spin_rows = len(on_spin.axes[0])

    percentage_on_spin = int((on_spin_rows*100)/y)

    #####On Spiner#######
    onspin_googly=on_spin.loc[(on_spin['Ball Type']=='Googly')]
    onspin_OFFSPIN=on_spin.loc[(on_spin['Ball Type']=='Off Spin')]
    onspin_carrom_ball=on_spin.loc[(on_spin['Ball Type']=='Carrom Ball')]
        
        
    onspin_googly_rows= (len(onspin_googly.axes[0]))
    onspin_ONSPIN_rows = (len(onspin_OFFSPIN.axes[0]))
    onspin_carrom_ball_rows= int(len(onspin_carrom_ball.axes[0]))
        
        
     #Percentage 
    percentage_onspin_googly_rows= int((onspin_googly_rows*100)/on_spin_rows)
    percentage_onspin_OFFSPIN_rows = int((onspin_ONSPIN_rows*100)/on_spin_rows)
    percentage_onspin_carrom_ball_rows= int((onspin_carrom_ball_rows*100)/on_spin_rows)

    return on_spin_rows,onspin_googly_rows,onspin_ONSPIN_rows,onspin_carrom_ball_rows
    
def graph(player,opponent,venue):

    sort_data3 = data.loc[(data['Batsman']==player) & (data['Opponent Team Name']==opponent) & (data['Venue']==venue)]
    sort_data3.head()
    y=len(sort_data3.axes[0])
    
    faster=sort_data3.loc[(sort_data3['Baller Type']=='Faster')]
    faster_rows = len(faster.axes[0])
    

    medium_faster=sort_data3.loc[(sort_data3['Baller Type']=='Medium Faster')]
    medium_faster_rows = len(medium_faster.axes[0])
    

    off_spin=sort_data3.loc[(sort_data3['Baller Type']=='Off Spiner')]
    off_spin_rows= len(off_spin.axes[0])
    
 
    on_spin=sort_data3.loc[(sort_data3['Baller Type']=='On Spiner')]
    on_spin_rows = len(on_spin.axes[0])
    
   
    ###Percentage
    
    percentage_faster = int((faster_rows*100)/y)
    percentage_medium_faster = int((medium_faster_rows*100)/y)
    percentage_off_spin = int((off_spin_rows*100)/y)
    percentage_on_spin = int((on_spin_rows*100)/y)
    
    x=['Faster','Medium Faster','Off Spin','On Spin']
    h=[percentage_faster,percentage_medium_faster,percentage_off_spin,percentage_on_spin]
    return x,h





           
               
   


