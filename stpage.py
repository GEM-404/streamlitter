import base64
import streamlit as st

from PIL import Image
from stream_bg import set_background
from serp_ads import searcher

from countries import COUNTRIES as cts


def get_items(dct):

    for value in dct.values():
        if isinstance(value, dict):
            st.text("|------------------------------------------------------|")
            for key1, value1 in value.items():
                st.text(f"{key1}: {value1}")
            st.text("|______________________________________________________|")


def number_of_searches(dct):
    keys = dct.keys()
    return keys.keys()


def new_bg():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7");
            background-size: cover;
        }

       .sidebar .sidebar-content {
            background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7");
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def main_bar(side_bg):

    side_bg_ext = 'png'
    b64data = f'{base64.b64encode(open(side_bg, "rb").read()).decode()}'
    dta = f'data:image/{side_bg_ext};base64,{b64data}'
    st.markdown(
      f"""
      <style>
      .stApp {{
             background: url({dta});
             background-size: cover
         }}

      </style>
      """,
      unsafe_allow_html=True,
      )

    return


def sidebar_bg(side_bg):
    side_bg_ext = 'png'
    b64data = f'{base64.b64encode(open(side_bg, "rb").read()).decode()}'
    dta = f'data:image/{side_bg_ext};base64,{b64data}'
    st.markdown(
      f"""
      <style>

      [data-testid="stSidebar"] > div:first-child {{
          background: url({dta});
          background-size: cover;
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )

    return


def headers():
    st.header("AD SEARCH SYSTEM")
    image = Image.open('worldmap1.jpg')
    st.image(image, caption='WorldMap System Search')
    st.subheader("Google ad search system in python")

    st.sidebar.title("Google Search Ad System")
    return


def get_total_results(country, domain, query):
    """The total results is also given as a json response in the search results."""
    searches = searcher(country=country, query=query, domain=domain)
    st.text(f"{number_of_searches(searches)} results")
    return


def create_body():
    st.info("GIVE THE COUNTRY YOU WANT ADS FROM")
    country = st.selectbox(
        "Select a country you wanna see ads from",
        list(cts.values())
    )

    st.info("GIVE THE SEARCH TERM FOR YOUR ADS")
    query = st.text_input("Please input the item you wanna search")

    st.info("GIVE THE SEARCH DOMAIN FOR YOUR ADS")
    domain = st.text_input("Please input the web domain you wanna search from")

    st.button("Reset")

    if st.button('Search'):
        get_items(searcher(country=country, query=query, domain=domain))


def main():
    main_bar('worldmap4.jpg')
    sidebar_bg('search4.jpg')
    headers()
    create_body()


if __name__ == '__main__':
    main()
