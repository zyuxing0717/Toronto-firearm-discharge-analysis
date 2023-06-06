import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time
import plotly.express as px

df = pd.read_csv("Data-Toronto-Police.csv")
df.info()

df_noout = df.drop(df[df['Y'] == 0.0].index)
# df_noout.info()

latitude = df_noout['LAT_WGS84']
longitude = df_noout['LONG_WGS84']

# Create a scatter plot
fig = plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.scatter(longitude, latitude, s=10, alpha=0.6)  # Adjust marker size and transparency as desired
plt.title('Geographical Distribution of Shooting and Firearm Discharge Events')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)

######################################
#
# Show the scatter plot of total distribution, similar to the one on Toronto Police website
plt.show()

sorted = df_noout.sort_values('OCC_DATE')
# sorted

##################################################
#
#   This section generates a heatmap that grows gradually, but there is no actual map as background (it may
#   -have but it's a bit more work.
#
#

# for i in range(sorted.size):
#     # plt.close(fig)
#     # time.sleep(1)
#     part = sorted[:i]
#     sns.kdeplot(part, x='X', y='Y', cmap='hot', shade=True)
#     plt.pause(0.1)
#     plt.clf()
# plt.show()
# time.sleep(0.3)


####################################
# Here it Generates a "web" that allows to check each year's event heatmap and adjust it back and forth.
#
#
#
fig = px.density_mapbox(df_noout, lat = 'Y', lon = 'X', hover_name='OCC_DATE', radius=15, zoom = 10
                        , animation_frame='OCC_YEAR', animation_group = 'EVENT_UNIQUE_ID', color_continuous_scale='YlOrRd'
                        )
fig.update_layout(mapbox_style="carto-positron")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()