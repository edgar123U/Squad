import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch

# Load data from a local CSV file


df=pd.read_csv("Position id_1 - Folha1.csv")

# Streamlit app
st.title("Football Pitch Player Position")

# Create a dropdown to select the player
player_names = df['player_name'].unique()
selected_player = st.selectbox("Select a player:", player_names)

# Filter the DataFrame for the selected player
player_to_plot = df[df['player_name'] == selected_player]

# Drawing the pitch
pitch = VerticalPitch(pitch_type="statsbomb", goal_type="box", corner_arcs=True)
fig, ax = pitch.draw(figsize=(8, 14))

# Plotting the player's positions
# Initial position
x1, y1 = player_to_plot['position_x'].values[0], player_to_plot['position_y'].values[0]
# Final position
x2, y2 = player_to_plot['position_x2'].values[0], player_to_plot['position_y2'].values[0]

# Plotting the positions
sc1 = pitch.scatter([x1], [y1], ax=ax, s=500, c="red",  linewidth=3)


sc2 = pitch.scatter([x2], [y2], ax=ax, s=300, c="red",  linewidth=3)

# Display the plot in Streamlit
st.pyplot(fig)

