import streamlit as st
import time
import pandas as pd
import numpy as np

# 1. Title, Header, Subheader, and Text
st.title("This is a Title")               # Biggest heading
st.header("This is a Header")             # Second-level heading
st.subheader("This is a Subheader")       # Smaller than header
st.text("This is a standard text message.")  # Normal plain text

# 2. Markdown, Code, LaTeX, and Write
st.markdown("# Markdown Title\nSome **bold** and _italic_ text.")  # Markdown formatting
st.code('print("Hello, Streamlit!")', language="python")           # Display code with syntax highlighting
st.latex(r"e^{i\pi} + 1 = 0")                                     # Display mathematical equation
st.write("Write can display text, numbers, lists, DataFrames, etc.")  # Flexible output method

# 3. Interactive Widgets (User Input)
if st.button("Click me"):   # Button widget
    st.write("Button clicked!")

if st.checkbox("Check me"):  # Checkbox widget
    st.write("Checkbox is checked")

choice = st.radio("Choose one:", ["Option 1", "Option 2"])  # Radio buttons
st.write(f"You chose {choice}")

option = st.selectbox("Select:", ["A", "B", "C"])  # Dropdown single choice
st.write(f"Selected {option}")

options = st.multiselect("Select multiple:", ["A", "B", "C"])  # Multi-select dropdown
st.write(f"Selected {options}")

val = st.slider("Slide me", 0, 100, 25)  # Slider with default value
st.write(f"Slider value: {val}")

text = st.text_input("Enter text:")  # Text input box
st.write(f"Your input: {text}")

num = st.number_input("Enter a number:", 0, 100)  # Number input
st.write(f"Number: {num}")

date = st.date_input("Pick a date")  # Date picker
st.write(f"Date selected: {date}")

time_val = st.time_input("Pick a time")  # Time picker
st.write(f"Time selected: {time_val}")

# 4. File and Media Inputs
file = st.file_uploader("Upload file")  # File uploader
if file:
    st.write(f"Filename: {file.name}")

img = st.camera_input("Take a picture")  # Capture image from camera
if img:
    st.image(img)

color = st.color_picker("Pick a color")  # Color picker
st.write(f"Color: {color}")

# 5. Layout & Animation
col1, col2 = st.columns(2)   # Columns for layout
col1.write("Column 1")
col2.write("Column 2")

with st.expander("Expand me"):   # Collapsible section
    st.write("Hidden text here")

with st.sidebar:   # Sidebar content
    st.write("This is a Sidebar")

st.balloons()   # Celebration balloons animation

with st.spinner("Loading..."):   # Spinner (loading indicator)
    time.sleep(2)
st.write("Done!")

progress = st.progress(0)   # Progress bar
for i in range(100):
    time.sleep(0.02)
    progress.progress(i + 1)
st.write("Progress complete")

st.metric(label="Temperature", value="70 °F", delta="-5 °F")   # Metric widget

# 6. Data & Visualization Example
data = pd.DataFrame(   # Create sample DataFrame
    np.random.randn(10, 2),  # 10 rows, 2 columns of random numbers
    columns=["Column A", "Column B"]
)

st.write("### Sample DataFrame")
st.dataframe(data)  # Display interactive DataFrame

st.write("### Line Chart")
st.line_chart(data)  # Plot a line chart of DataFrame

st.write("### Bar Chart")
st.bar_chart(data)   # Plot a bar chart
