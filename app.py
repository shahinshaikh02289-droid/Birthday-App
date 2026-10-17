
import streamlit as st
import time

# 1. Dost ka naam yahan set karein:
friend_name = "shahin"

st.balloons()

# Surprise Button
if st.button("Click to Open Your Gift! 🎁"):
    with st.spinner('Opening your surprise...'):
        time.sleep(1.5)

    # Snow effect & Big Wish
    st.snow()
    st.markdown(
        f"<h1 style='text-align: center; color: #FF4B4B;'>🎉 HAPPIEST BIRTHDAY {friend_name}! 🎉</h1>", 
        unsafe_allow_html=True
    )

    # Personal Message
    st.markdown("""
    ### 🎂 Wishing you a wonderful day full of joy, love, and laughter!
    May this year bring you endless happiness and success! ✨
    """)

    st.success("Enjoy your special day! 🥳🎈")
