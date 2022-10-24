import streamlit as st
import pandas as pd
import plotly.express as px

#organizing 
st.set_page_config(layout="centered")
header = st.container()
object1 = st.container()
object2 = st.container()
object3 = st.container()
#data import
df = pd.read_excel('2023 Analytics Internship Problem Dataset.xlsx')
#selecting data only from Pithcers A and B
df = df[(df.PITCHER_KEY == "A") | (df.PITCHER_KEY == "B")]
pitcherA = df[df.PITCHER_KEY == "A"]
pitcherB = df[df.PITCHER_KEY == "B"]


#title
with header:

	st.title("Reds Baseball Analytics Internship Project Part 2A")
	st.text("By Isaac Zelcer")

with object1:
	st.title("Pitch Metrics")

	#Data Manipulation:

	#taking the average of each mertric for each type of pitch
	figDfA = pitcherA.groupby(['PITCH_TYPE_KEY']).mean()
	figDfA["Pitcher_ID"] = "A"
	figDfB = pitcherB.groupby(['PITCH_TYPE_KEY']).mean()
	figDfB["Pitcher_ID"] = "B"
	figDf = pd.concat([figDfA,figDfB])

	#Data Visual Creations:

	#velocity figure bar chart
	#creates a bar chart with the side by side comparison of Pitcher A and B
	#bar chart has a x value of each pitch type and y value of average velocity on release
	fig = px.bar(figDf, y = "RELEASE_SPEED", color = "Pitcher_ID", barmode = 'group', 
		title = "Velocity at Release", hover_data={'RELEASE_SPEED':':.1f'}, text = 'RELEASE_SPEED', height = 600)
	fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
	fig.update_yaxes(range = [50,105])
	st.write(fig)

	#quick analysis of the velocity on release chart
	st.markdown("**Pitcher A clearly has a higher release speed with an average fastball speed above 96 MPH.**")
	st.text("\n")

	#Spin rate figure
	#creates a bar chart with the side by side comparison of Pitcher A and B
	#bar chart has a x value of each pitch type and y value of average spin rate
	fig = px.bar(figDf, y = "SPIN_RATE", color = "Pitcher_ID", barmode = 'group', 
		title = "Spin Rate", hover_data={'SPIN_RATE':':.1f'}, text = 'SPIN_RATE', height = 600)
	fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
	st.write(fig)

	#quick analysis of the spin rate chart
	st.markdown("**Pitcher A clearly has a higher spin rate on his Fastball and CurveBall.**")
	st.text("\n\n")

	#Plate Speed figure
	#creates a bar chart with the side by side comparison of Pitcher A and B
	#bar chart has a x value of each pitch type and y value of average velocity at the plate
	fig = px.bar(figDf, y = "PLATE_SPEED", color = "Pitcher_ID", barmode = 'group', 
		title = "Velocity at the plate", hover_data={'PLATE_SPEED':':.1f'}, text = 'PLATE_SPEED', height = 600)
	fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
	fig.update_yaxes(range = [50,95])
	st.write(fig)

	#analysis gives an understanding on why the pitcher may use certain pitches more often
	st.markdown("**Pitcher A mostly uses the fastball and slider.**")
	st.markdown("**Pitcher B mostly uses the fastball and curveball.**")


with object2:

	st.title("Pitch Distributions")

	#Data Manipulation:

	#create a dataframe to take the counts of each type of pitch for each pitcher
	pitcherAdf = pd.DataFrame(pitcherA["PITCH_TYPE_KEY"].value_counts())
	pitcherAdf["Pitcher_ID"] = "A"
	pitcherBdf = pd.DataFrame(pitcherB["PITCH_TYPE_KEY"].value_counts())
	pitcherBdf["Pitcher_ID"] = "B"
	figDf = pd.concat([pitcherAdf,pitcherBdf])

	#Data Visual Creation

	#Pitch Distribution figure
	#creates a bar chart with the side by side comparison of Pitcher A and B
	#bar chart has a x value of each pitch type and y value of the number of pitches thrown
	fig = px.bar(figDf, y = "PITCH_TYPE_KEY", color = "Pitcher_ID", 
		barmode = 'group', labels={'PITCH_TYPE_KEY':'Count'}, text= 'PITCH_TYPE_KEY')
	fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
	st.write(fig)

with object3:
	st.title("Location")

	#Data Visual Creation

	#Heatmap for PitcherA 
	#Heatmap shows the most frequent locations the pitches end up
	#the X axis is centered around 0 (the center of the plate) 
	#and the y axis starts at 1 (1 foot off the ground)
	fig = px.density_heatmap(data_frame=pitcherA, y="PLATE_Z", x="PLATE_X", 
		range_x = [-1.2,1.2], range_y = [1,4],
		title = "Pitcher A",
		nbinsx = 20, nbinsy = 20, text_auto = True
		)
	left_plate = -1 * 8.5/12
	right_plate = 8.5/12
	bottom_plate = 1.5
	top_plate = 3.6

	#creates a typical strike zone
	#Used the values of a 17inch plate wide 
	# and on average the height of the strike zone being 1.5 to 3.6 feet off the ground
	fig.add_shape(type="rect",
    x0= left_plate, y0= bottom_plate, x1= right_plate, y1= top_plate,
    line=dict(color="White"))
	st.write(fig)

	#Heatmap for Pitcher B. Uses the same structure as before
	fig = px.density_heatmap(data_frame=pitcherB, y="PLATE_Z", x="PLATE_X", 
		range_x = [-1.2,1.2], range_y = [1,4],nbinsx = 20, nbinsy = 20, 
		title = "Pitcher B", text_auto=True)
	
	#creates a typical strike zone for the second figure
	fig.add_shape(type="rect",
    x0= left_plate, y0= bottom_plate, x1= right_plate, y1= top_plate,
    line=dict(color="White"))
	st.write(fig)



