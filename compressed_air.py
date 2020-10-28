import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd



#Title on main page

st.title("Compressed Air Consumption")

#subheader on sidebar

st.subheader("Change slider values to see updated results at the bottom")

#To create sliders on sidebar

a = st.slider('Weft Count (Ne)', 10, 80, 20)  # 👈 this is a widget
b = st.slider('Fabric Width (in)', 60, 120, 60)
c = st.slider('Loom RPM', 450, 650, 500)
d = st.slider('Reed (dents/in)', 15, 55, 30)

#Regression equation to calculate air consumption; int is used to convert float into integer; this is done because other arguments in slider are also int types
e = int(6.10295 -(0.0169465 * a)+(0.0158989 * b)-(0.000147579 * c)+(0.0228664 * d)+(0.00114483 * b * b)+(0.000127147 * b * c)-(0.000849611 * b * d))

#To show results on the main page, under the heading
st.subheader("The Estimated Compressed Air Consumption on Airjet Loom") 
st.write(':', e, 'Litres per second')


# Images
from PIL import Image
img = Image.open("airjetloom.jpg")
st.image(img, width=600, caption="")







