import streamlit as st
import random

# Define the characters to use in the password
letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Streamlit user inputs
st.title("Welcome to the PyPassword Generator!")
nr_letters = st.number_input("How many letters would you like in your password?", min_value=0, step=1)
nr_symbols = st.number_input("How many symbols would you like?", min_value=0, step=1)
nr_numbers = st.number_input("How many numbers would you like?", min_value=0, step=1)

# Function to generate the password
def generate_password(nr_letters, nr_symbols, nr_numbers):
    password_list = []

    for char in range(0, nr_letters):
        password_list.append(random.choice(letters))
    
    for char in range(0, nr_symbols):
        password_list.append(random.choice(symbols))
    
    for char in range(0, nr_numbers):
        password_list.append(random.choice(numbers))
    
    random.shuffle(password_list)
    
    password = ''.join(password_list)
    return password

if st.button("Generate Password"):
    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    st.success(f"Your password is: {password}")
    st.info("Symbols included make your password stronger and more secure!")
