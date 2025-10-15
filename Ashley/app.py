import streamlit as st



st.set_page_config(page_title="Sparkle And Shine", page_icon=":heart:", layout="wide")
contact_form = """
<form action="https://formsubmit.co/asht4664@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="text" name="address" placeholder="Your Address" required>
     <input type="text" name="phone" placeholder="Your Phone Number" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <button type="submit">Send</button>
</form> 
"""

# ------ Header Section ------
st.title("Sparkle And Shine")
st.subheader("A Cleaning Business That Wont Disapoint")
st.write("Hello Im :heart: Ashley :heart:, I believe every home desserves to feel fresh, welcoming, and truly clean-without harming the environment. I provide detailed cleaning services for apartments, houses, and town homes using safe, eco-friendly products that i bring myself.I understand that every family's situation is different so I don't have set rates. Instead, I work with you to find a price that fits your budget, because a sparkling home shouldn't come with added stress. Whether you need a one-time deep clean or regular upkeep, I would love to help your home shine this season! ")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("What I Do")
        st.write("I Clean Houses With My Own Cleaning Supplies Around The Grayson County Area")
    with right_column:
        st.header("Please Feel Free To Get In Touch With Me")
        st.markdown(contact_form, unsafe_allow_html=True)

