import streamlit as st
import info

st.title("Portfolio")

col1, col2 = st.columns([1, 2])
with col1:
    st.image(info.profile_picture, width=200)
with col2:
    st.header("About Me")
    st.write(info.about_me)

st.divider()

st.subheader("Education")
st.write(f"**{info.education_data['Degree']}** — {info.education_data['Institution']}")
st.write(f"Expected graduation: {info.education_data['Expected Graduation']}")

st.subheader("Skills")
st.write("\n".join([f"- {s}" for s in info.skills]))

st.divider()

st.subheader("Projects")
st.write(
    "- **Interactive Quiz (Part 2)**: A fun quiz that uses multiple input types, images, and gives you a result."
)

st.divider()

st.subheader("Links")
c1, c2, c3 = st.columns(3)
with c1:
    st.image(info.linkedin_image_url, width=40)
    st.markdown(f"[LinkedIn]({info.my_linkedin_url})")
with c2:
    st.image(info.github_image_url, width=40)
    st.markdown(f"[GitHub]({info.my_github_url})")
with c3:
    st.image(info.email_image_url, width=40)
    st.markdown(f"Email: {info.my_email_address}")
