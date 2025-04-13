import streamlit as st
st.set_page_config(page_title="Calculator", layout="centered")

# Initialize the session state
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Display title
st.title(" Simple Calculator(Amar)")

# Function to handle button press
def press(button_value):
    if button_value == "=":
        try:
            st.session_state.expression = str(eval(st.session_state.expression))
        except Exception as e:
            st.session_state.expression = "Error"
    elif button_value == "C":
        st.session_state.expression = ""
    else:
        st.session_state.expression += button_value

# Display current expression
st.text_input("Expression", value=st.session_state.expression, key="display", disabled=True)

# Button layout (you can change it)
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Create button grid
for row in buttons:
    cols = st.columns(len(row))
    for i, label in enumerate(row):
        if cols[i].button(label):
            press(label)
