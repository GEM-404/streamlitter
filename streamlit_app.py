import streamlit as st

from PIL import Image

from serp_ads import searcher
from stream_bg import main_bar, get_bgs
from countries import COUNTRIES as cts


def get_items(dct):

    for value in dct.values():
        if isinstance(value, dict):
            st.text("|------------------------------------------------------|")
            for key1, value1 in value.items():
                st.success(f"{key1}: {value1}")
            st.text("|______________________________________________________|")


def number_of_searches(dct):
    keys = dct.keys()
    return keys.keys()


def headers():
    st.header("AD SEARCH SYSTEM")
    image = Image.open('images/worldmap1.jpg')
    st.image(image, caption='WorldMap System Search')
    st.subheader("Google ad search system in python")
    return


def sidebar():
    st.sidebar.title("Google Search Ad System")
    st.sidebar.button("Remove wallpaper")
    return


def button_functionalities():
    random_bg = get_bgs()

    if st.sidebar.button("Change wallpaper"):
        main_bar(f"images/{random_bg}")

    return


def get_total_results(country, domain, query):
    """
    The total results is also given as a json response in the search results.
    """
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
    headers()
    sidebar()
    create_body()
    button_functionalities()


if __name__ == '__main__':
    main()
