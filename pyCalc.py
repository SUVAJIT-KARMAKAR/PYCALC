# IMPORTING THE REQUIRED MODULES 
import streamlit as st
import re

# CALCULATION FUNCITON
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# TITILE
st.title("PYCALC")

# CHAT HISTORY 
if "messages" not in st.session_state:
    st.session_state.messages = []

# CHAT MESSAGES FROM HISTORY ON RERUM 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# USER INPUT 
if prompt := st.chat_input("Enter your calculation (e.g., '5 + 3' or '10 / 2')"):
    # MESSAGE CHAT CONTAINER
    st.chat_message("user").markdown(prompt)
    # USER MESSAGE CHAT HISTORY 
    st.session_state.messages.append({"role": "user", "content": prompt})

    # INPUT PARSING
    match = re.match(r"(\-?\d+\.?\d*)\s*([\+\-\*/])\s*(\-?\d+\.?\d*)", prompt)
    if match:
        num1 = float(match.group(1))
        operation = match.group(2)
        num2 = float(match.group(3))

        result = calculate(num1, num2, operation)

        # ASSISTANCE REPLY
        with st.chat_message("assistant"):
            st.markdown(f"The result of {num1} {operation} {num2} is : {result}")
        # ADDING ASSISTANCE HISTORY
        st.session_state.messages.append({"role": "assistant", "content": f"The result of {num1} {operation} {num2} is: {result}"})
    else:
        # EDGE CASE FOR WRONG INPUT
        with st.chat_message("assistant"):
            st.markdown("I'm sorry, I couldn't understand that. Please enter your calculation in the format 'number operation number' (e.g., '5 + 3' or '10 / 2').")
        
        st.session_state.messages.append({"role": "assistant", "content": "I'm sorry, I couldn't understand that. Please enter your calculation in the format 'number operation number' (e.g., '5 + 3' or '10 / 2')."})