
import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="Special Birthday Surprise! 🎂",
    page_icon="🎁",
    layout="centered"
)

# Custom Styling (CSS)
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #FF4B4B;
        font-family: 'Comic Sans MS', cursive;
        font-size: 3em;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #FFA500;
        font-size: 1.5em;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        font-size: 18px;
        font-weight: bold;
        background-color: #FF4B4B;
        color: white;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: #f0f2f6;
        text-align: center;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Session State for tracking steps
if 'step' not in st.session_state:
    st.session_state.step = 1

# Header
st.markdown("<h1 class='main-title'>🎉 Happy Birthday! 🎈</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>A Special Surprise Just For You ✨</p>", unsafe_allow_html=True)
st.divider()

# --- STEP 1: WELCOME & UNLOCK ---
if st.session_state.step == 1:
    st.markdown("### 🔒 Step 1: Unlock Your Birthday Gift")
    st.write("Welcome to your special birthday portal! Click below to start your surprise journey.")
    
    if st.button("🎁 Tap to Unlock Surprise!"):
        st.session_state.step = 2
        st.rerun()

# --- STEP 2: CAKE CUTTING ---
elif st.session_state.step == 2:
    st.balloons()
    st.markdown("### 🎂 Step 2: Make a Wish & Blow the Candles!")
    st.image("https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600", caption="Make a wish! 🕯️")
    
    if st.button("🕯️ Blow the Candle & Cut the Cake!"):
        st.snow()
        st.success("🎉 Woohoo! Wish granted! Cake is cut! 🍰")
        time.sleep(1)
        st.session_state.step = 3
        st.rerun()

# --- STEP 3: CHOCOLATE & GIFTS ---
elif st.session_state.step == 3:
    st.markdown("### 🍫 Step 3: Collect Your Sweet Treats & Gifts!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🍫 Chocolates")
        if st.button("Claim Chocolates ✨"):
            st.toast(" Here is your lifetime supply of Chocolates! 🍫", icon="🍫")
            
    with col2:
        st.markdown("#### 🎈 Hugs & Wishes")
        if st.button("Claim Hugs 💖"):
            st.toast(" Sending warm birthday hugs your way! 🤗", icon="🤗")
            
    with col3:
        st.markdown("#### 🎁 Mystery Box")
        if st.button("Open Mystery Box 📦"):
            st.toast(" Surprise! You get endless happiness today! ✨", icon="🎁")
            
    st.divider()
    if st.button("➡️ Move to Special Messages"):
        st.session_state.step = 4
        st.rerun()

# --- STEP 4: SPECIAL MESSAGES & WISHES ---
elif st.session_state.step == 4:
    st.markdown("### 💌 Step 4: Special Wishes & Letter")
    
    tab1, tab2, tab3 = st.tabs(["📝 Birthday Note", "🌟 Best Memories", "🎵 Birthday Song"])
    
    with tab1:
        st.info("""
        Dear Birthday Star 🌟,
        
        May your day be filled with lots of love, laughter, chocolate, and unforgettable moments! 
        You deserve all the happiness in the world. Keep shining and smiling always! 😊✨
        """)
        
    with tab2:
        st.markdown("* Here's to making more amazing memories together! 📸")
        st.markdown("* May all your dream projects and code compile without errors! 💻🚀")
        
    with tab3:
        st.markdown("🎶 *Happy Birthday to you~ Happy Birthday to you~* 🎶")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # Replace with actual song link if you have one
        
    st.divider()
    if st.button("✨ Finish Celebration"):
        st.session_state.step = 5
        st.rerun()
# --- STEP 5: FINAL CELEBRATION ---
elif st.session_state.step == 5:
    st.balloons()
    st.snow()
    st.success("🎉 Happy Birthday Once Again! Hope you enjoyed the surprise! ❤️")
    
    st.image("https://images.unsplash.com/photo-1513151233558-d860c5398176?w=600", caption="Have a Fantastic Year Ahead!")
    
    if st.button("🔄 Restart Celebration"):
        st.session_state.step = 1
        st.rerun()