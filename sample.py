import streamlit as st
import plotly.express as px
from PIL import Image
import numpy as np
import pandas as pd
from datetime import datetime
import re

st.title("Hello, Drishu :hearts:")
st.markdown(
    """
    ##### Happy Anniversary &nbsp; -- &nbsp;  SECOND!!
    """
)


audio_file = open("media/Modern loneliness 2.m4a", "rb")
audio_bytes = audio_file.read()

st.markdown(
    "Here is some music while you browse through this static page of our dynamic lives :kiss:"
)
st.audio(audio_bytes, format="audio/m4a")
st.caption(
    """
    "Modern Loneliness - Lauv"
                          - Eklavya
    """
)

col1, col2, col3, col4 = st.columns(4)
with col1:
    video_file = open("media/IMG_5075.MOV", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)

with col2:
    image = Image.open("images/07BD87CA-B170-4618-B5A2-2049C309471A.JPG")
    st.image(image, caption="Cuties with booties")

with col3:
    image = Image.open("images/B414855F-F8F1-4FC2-AA4D-AE5A71F1790B.JPG")
    st.image(image, caption="smiley cyrus")

with col4:
    video_file = open("media/IMG_7016.mov", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)


st.info(
    "The following plots have used real data from our WhatsApp Chats dated Nov 11, 2019 - July 27, 2023"
)


f = open("_chat.txt", "r")
chats = f.read()
words = [
    "lol",
    "love",
    "helu",
    "ily",
    "miss",
    "wow",
    "hello",
    "i love you",
    "sahi hai",
    "lmao",
    "hot",
    "cute",
    "wot",
    "damn",
    "cutie",
    "chalo",
    "acha",
    "baber",
    "babe",
    "baby",
    "haha",
]
counts = []
for word in words:
    counts.append(chats.count(word))

df = pd.DataFrame({"words": words, "counts": counts})
fig = px.bar(df.sort_values("counts", ascending=False), x="words", y="counts")
fig.update_layout(title="Words we use often :)")
fig.update_xaxes(title="Word")
fig.update_yaxes(title="Frequency")
st.plotly_chart(fig, use_container_width=True)
st.info("Obviously, *LOL*! You are the *HOT*TEST alive :fire:")

st.divider()

lines = chats.split("\n")

drish_words = []
drish = 0
len_drish = 0

eku_words = []
eku = 0
len_eku = 0

for line in lines:
    if "Drish:" in line:
        drish += 1
        len_drish += len(line.split(":")[-1])
        drish_words.extend(line.split(":")[-1].split(" "))
    elif "Eklavya Jain:" in line:
        eku += 1
        len_eku += len(line.split(":")[-1])
        eku_words.extend(line.split(":")[-1].split(" "))

col1, col2 = st.columns(2)

with col1:
    fig = px.pie(names=["Drish", "Eku"], values=[drish, eku])
    fig.update_layout(title="Text Proportion")
    st.plotly_chart(fig, use_container_width=True)
    st.info(
        """
        ###### Does Drish really text more often? 
        *Like we really needed an answer, haha* :see_no_evil:\n
        """
    )

with col2:
    fig = px.bar(
        x=["Drish", "Eku"],
        y=[len_drish // drish, len_eku // eku],
        color=["Drish", "Eku"],
    )
    fig.update_layout(title="Average Text Length")
    fig.update_xaxes(title="Person")
    fig.update_yaxes(title="Length")
    fig.update_traces(marker_line_width=0)
    st.plotly_chart(fig, use_container_width=True)
    st.info(
        """
        ###### Does Eku really send one-word texts?
        *More like one-word less texts, haha* :stuck_out_tongue:\n
        """
    )

st.divider()

col1, col2 = st.columns(2)
with col1:
    fig = px.bar(
        x=["Drish", "Eku"],
        y=[len(set(drish_words)), len(set(eku_words))],
        color=["Drish", "Eku"],
    )
    fig.update_layout(title="How original are we?")
    fig.update_xaxes(title="Person")
    fig.update_yaxes(title="Number of Unique Words")
    fig.update_traces(marker_line_width=0)
    st.plotly_chart(fig, use_container_width=True)
    st.info(
        f"""
        In terms of percentages:\n

        - Drish: {len(set(drish_words))/len(drish_words):,.2%}\n
        - Eku: {len(set(eku_words))/len(eku_words):,.2%}\n

        Dissappointing, rather pun-derwhelming :disappointed_relieved:
        """
    )

with col2:
    d = {}
    for line in lines:
        if line.startswith("["):
            if ("Eklavya Jain:" in line) or ("Drish:" in line):
                date = line.split(",")[0].split("[")[1]

                if date in d:
                    d[date] += len(line.split(":")[-1])
                else:
                    d[date] = len(line.split(":")[-1])

    df = pd.DataFrame({"Date": list(d.keys()), "len": d.values()})
    df["MA10"] = df["len"].rolling(10).mean()

    fig = px.line(df, x="Date", y="MA10")
    fig.update_layout(title="Daily Text Length")
    fig.update_xaxes(title="Date")
    fig.update_yaxes(title="Length of Texts Each Day")
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        f"""
        Some Statistics:
        - Mean Length: {df["len"].mean():,.0f} words\n
        - Standard Deviation: {df["len"].std():,.0f} words\n

        LETSSS FKN GO :muscle:
        """
    )

st.divider()

ekumojis = 0
drishumojis = 0
for line in lines:
    if "Drish:" in line:
        text = line.split(":")[-1]
        text = re.sub("[$@#%&*! ]", "", text)
        if not text.isalnum():
            drishumojis += 1

    elif "Eklavya Jain:" in line:
        text = line.split(":")[-1]
        text = re.sub("[$@#%&*! ]", "", text)
        if not text.isalnum():
            ekumojis += 1

col1, col2 = st.columns(2)

with col1:
    fig = px.bar(x=["Drish", "Eku"], y=[drishumojis, ekumojis], color=["Drish", "Eku"])
    fig.update_layout(title="# Emojis We Use")
    fig.update_xaxes(title="Person")
    fig.update_yaxes(title="Number of Emojis Used")
    st.plotly_chart(fig, use_container_width=True)
    st.info(
        ":blue_heart: :two_hearts: :yellow_heart: :purple_heart: :cupid: :hearts: :kiss: :tongue: :eyes: :100: :sparkles: :couplekiss: :love_letter: :heartbeat: :bouquet: :kissing_heart:"
    )

with col2:
    image = Image.open("images/7bda3bb4-945f-40a9-a1e1-423bf90b3b07.JPG")
    st.image(image)
    st.info("Peace. Piss. Peas.")

st.divider()


st.markdown(
    """
    Dear Drish,  

    Life is soooo difficult. \n
    You make it better, happier, prettier, mushy-er, tushy-er, juicy-er. \n
    Happy 2 years, baby AND :clinking_glasses: to many more. \n
    Thanks for being a part of this journey - full of ups and downs, lefts and rights, ins and outs  :wink:. \n
    """
)

st.divider()

b = st.button("\nClick for Cuteness :kissing:")

if b:
    with st.columns(3)[1]:
        link = "https://media.giphy.com/media/Om7JsvGN4SFCOqxgvi/giphy.gif"
        st.markdown(f"![Alt Text]({link})")

col1, col2, col3, col4 = st.columns(4)
with col1:
    image = Image.open("images/IMG_5996.JPG")
    st.image(image)
    st.caption("You're soft :icecream:")

with col2:
    image = Image.open("images/B3FA70FA-8461-4558-A136-1EF246362488.JPG")
    st.image(image)
    st.caption("You're pretty :sparkles:")

with col3:
    image = Image.open("images/IMG_6041.JPG")
    st.image(image)
    st.caption("You're kind :monkey_face:")

with col4:
    image = Image.open("images/WhatsApp Image 2023-07-27 at 7.51.11 PM.jpeg")
    st.image(image)
    st.caption("You're the Best :hearts:")

st.markdown("Ok, bye. I Love You. :kissing:")

st.markdown(
    '<div style="text-align: right; font-size: 0.8em">Copyright @ 2023 | Designed by Eku</div>',
    unsafe_allow_html=True,
)
