from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Red Lucifer", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_gvdwzaoj.json")
gtavs1tss = Image.open("images/gtavs1tss.png")
gtav1st = Image.open("images/gtav1st.png")

with st.container():
    st.subheader("Hi, I am Red Lucifer :wave:")
    st.title("A YouTuber From India")
    st.write("I am a Gamer and a Teenager. Seeking for audience to support")
    st.write("[Learn More >](https://www.youtube.com/channel/UCvHDa2xT2uArBBS3_plbX1w)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating gameplay videos for people who:
            - are looking for a way to spend some good time.
            - wanted to get entertained.
            - want to learn something from my channel.

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you never miss any update.
            """
        )
        st.write("[Youtube Channel >](https://www.youtube.com/channel/UCvHDa2xT2uArBBS3_plbX1w)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="gaming")

with st.container():
    st.write("---")
    st.header("My Videos")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(gtav1st)


    with text_column:
        st.subheader("Grand Theft Auto V | Mission Bank Robbery | Walkthrough Part 1 | NO COMMENTARY GAMEPLAY |")
        st.write(
            """
            Hello Peoples!!
            Welcome to the video. This video,thumbnail and all the other objects are purely owned by The Red Lucifer and Teams. If you use this video please don't forget to give credits in the description as you can FREELY use my video.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/Kih44QAr_cA)")
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(gtavs1tss)
        with text_column:
            st.subheader("Grand Theft Auto V | Mission Friend Request | Walkthrough Part 7 | NO COMMENTARY GAMEPLAY |")
            st.write(
                """
                Hello Peoples!!
            Welcome to the video. This video,thumbnail and all the other objects are purely owned by The Red Lucifer and Teams. If you use this video please don't forget to give credits in the description as you can FREELY use my video.
            """
        )
            st.markdown("[Watch video...](https://youtu.be/nEaNavH9Skw)")
            

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/redlucifer110@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
