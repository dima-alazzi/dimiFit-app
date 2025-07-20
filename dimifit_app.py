import streamlit as st

st.set_page_config(page_title="DimiFit 💪", layout="centered")

st.title("💥 DimiFit: Your No-BS Fitness Coach")
st.markdown("Let's get you moving in a way that suits **you** today.")

energy = st.radio("💖 How's your energy today?", ["low", "medium", "high"])
goal = st.radio("✨ What's your current goal?", ["tone", "strength", "fat loss", "energy", "maintenance"])
focus = st.radio("🎯 Which area are you focusing on?", ["upper body", "lower body", "core", "full body"])
time = st.radio("⏰ How much time do you have?", ["10", "20", "30+"])

if st.button("Get My Workout Plan"):
    st.subheader("🎽 Your Custom Workout Plan:")
    st.markdown(f"""
    **Energy**: {energy}  
    **Goal**: {goal}  
    **Focus Area**: {focus}  
    **Time**: {time} minutes  

    _Since API quota is exceeded, here's your offline plan suggestion based on your inputs:_  
    > Stay consistent, {goal}-focused, and energised. Pick 4 exercises focused on your **{focus}**, do 3 sets of 12 reps,  
    rest 60 sec between sets. Keep it simple and solid. 💪
    """)

    st.success("Come back tomorrow – we do this one rep at a time 🧠")

