import streamlit as st
import pandas as pd
import plotly.express as px

#organizing 
st.set_page_config(layout="centered")
header = st.container()
object1 = st.container()
object2 = st.container()
object3 = st.container()
#data
#df = pd.read_excel('2023 Analytics Internship Problem Dataset.xlsx')
#df = df[df.PITCHER_KEY == "A" | df.PITCHER_KEY == "B"]
df = pd.read_excel('Reds_data.xlsx')
pitcherA = df[df.PITCHER_KEY == "A"]
pitcherB = df[df.PITCHER_KEY == "B"]



with header:

	st.title("Reds Baseball Analytics Internship Project Part 2A")
	st.text("By Isaac Zelcer")


with object1:
	st.title("Pitch Metrics")
	#data manipulation

	figDfA = pitcherA.groupby(['PITCH_TYPE_KEY']).mean()
	figDfA["Pitcher_ID"] = "A"
	figDfB = pitcherB.groupby(['PITCH_TYPE_KEY']).mean()
	figDfB["Pitcher_ID"] = "B"
	figDf = pd.concat([figDfA,figDfB])

	#velocity figure
	fig = px.bar(figDf, y = "RELEASE_SPEED", color = "Pitcher_ID", barmode = 'group', 
		title = "Velocity at Release", hover_data={'RELEASE_SPEED':':.1f'}, text = 'RELEASE_SPEED', height = 600)
	fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
	fig.update_yaxes(range = [50,105])
	st.write(fig)
	st.markdown("**Pitcher A clearly has a higher release speed with an average fastball speed above 96 MPH.**")
	st.text("\n")

	#Spin rate figure
	fig = px.bar(figDf, y = "SPIN_RATE", color = "Pitcher_ID", barmode = 'group', 
		title = "Spin Rate", hover_data={'SPIN_RATE':':.1f'}, text = 'SPIN_RATE', height = 600)
	fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
	st.write(fig)
	st.markdown("**Pitcher A clearly has a higher spin rate on his Fastball and CurveBall.**")
	st.text("\n\n")

	#Plate Speed figure
	fig = px.bar(figDf, y = "PLATE_SPEED", color = "Pitcher_ID", barmode = 'group', 
		title = "Velocity at the plate", hover_data={'PLATE_SPEED':':.1f'}, text = 'PLATE_SPEED', height = 600)
	fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
	fig.update_yaxes(range = [50,95])
	st.write(fig)
	st.markdown("**Pitcher A mostly uses the fastball and slider.**")
	st.markdown("**Pitcher B mostly uses the fastball and curveball.**")
with object2:
	st.title("Pitch Distributions")
	pitcherAdf = pd.DataFrame(pitcherA["PITCH_TYPE_KEY"].value_counts())
	pitcherAdf["Pitcher_ID"] = "A"
	pitcherBdf = pd.DataFrame(pitcherB["PITCH_TYPE_KEY"].value_counts())
	pitcherBdf["Pitcher_ID"] = "B"
	figDf = pd.concat([pitcherAdf,pitcherBdf])
	fig = px.bar(figDf, y = "PITCH_TYPE_KEY", color = "Pitcher_ID", 
		barmode = 'group', labels={'PITCH_TYPE_KEY':'Count'}, text= 'PITCH_TYPE_KEY')
	fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
	st.write(fig)

with object3:
	st.title("Location")
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
	fig.add_shape(type="rect",
    x0= left_plate, y0= bottom_plate, x1= right_plate, y1= top_plate,
    line=dict(color="White"))
	st.write(fig)

	fig = px.density_heatmap(data_frame=pitcherB, y="PLATE_Z", x="PLATE_X", 
		range_x = [-1.2,1.2], range_y = [1,4],nbinsx = 20, nbinsy = 20, 
		title = "Pitcher B", text_auto=True)
	#creates a typical strike zone
	fig.add_shape(type="rect",
    x0= left_plate, y0= bottom_plate, x1= right_plate, y1= top_plate,
    line=dict(color="White"))
	st.write(fig)



