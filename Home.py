import streamlit as st
from streamlit_lottie import st_lottie
import requests
from streamlit_option_menu import option_menu

st.set_page_config(page_title="UrbanAcer")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://lottie.host/c1a2caee-3eb9-4b53-8fa6-e62ea25f8ac2/kGTa4XsLv6.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height=None,
    width=None,
    key=None,
)




st.write("# Your Gurgaon Dream Within Reach")






