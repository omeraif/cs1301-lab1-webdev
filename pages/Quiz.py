import streamlit as st

st.title("Quiz: What kind of builder are you?")
st.write("Answer the questions below and get a result at the end!")

# NEW: progress bar
progress = st.progress(0)  # NEW

# Q1 (radio)
q1 = st.radio("1) Pick a weekend activity:", ["Build a small app", "Design something creative", "Go outside & explore", "Watch movies"], index=0)

progress.progress(20)

# Q2 (selectbox)
q2 = st.selectbox("2) Which sounds most fun right now?", ["Robotics", "AI/ML", "Web apps", "Game dev"])  # NEW
progress.progress(40)

# Q3 (multiselect)
q3 = st.multiselect("3) Choose up to 3 tools you like:", ["Python", "C/C++", "Figma", "Excel", "Arduino", "Git"], max_selections=3)  # NEW
progress.progress(60)

# Q4 (slider)
q4 = st.slider("4) How much do you like working in teams?", 0, 10, 7)
progress.progress(80)

# Q5 (number input)
q5 = st.number_input("5) How many hours/week can you realistically focus on a project?", min_value=0, max_value=40, value=6, step=1)
progress.progress(100)

st.divider()
st.subheader("Images (just for fun 😄)")
c1, c2, c3 = st.columns(3)
with c1:
    st.image("images/puff.jpg", caption="Option A")
with c2:
    st.image("images/cook.jpg", caption="Option B")
with c3:
    st.image("images/jelly.jpg", caption="Option C")

# Simple scoring -> at least 2 result types
score = 0
if q1 == "Build a small app":
    score += 2
elif q1 == "Design something creative":
    score += 1

if q2 in ["AI/ML", "Robotics"]:
    score += 2
else:
    score += 1

score += min(len(q3), 3)

score += 1 if q4 >= 6 else 0
score += 1 if q5 >= 5 else 0

st.divider()
if st.button("Get my result!"):
    if score >= 7:
        st.success("Result: **Builder Mode 🚀** — You like shipping projects and learning by doing.")
        st.balloons()
    else:
        st.info("Result: **Explorer Mode 🌱** — You’re still finding your favorite direction, and that’s great.")
        st.write("Tip: pick one small project and iterate weekly.")
