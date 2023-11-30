import streamlit as st

st.title(":1234: Interact Voice Clone")
st.subheader("Welcome to the beta Interact-Vocal-AI")

text = st.text_input("Enter text to clone: ")

image = st.file_uploader("Upload an image to read from: ", type=["jpg", "JPEG", "png"])
if image is not None:
        st.image(image, caption="", use_column_width=True)

voice = st.file_uploader("Upload voice example to tune: ", type=["mp3"])
audio_file = open('wild_rose.wav', 'rb')
audio_bytes = audio_file.read()

if st.button("Vocalize Text"):
    # st.audio(I_love, format="audio/wav")
    st.audio(audio_bytes, format='audio/wav')


