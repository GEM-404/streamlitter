
import base64
import random
import streamlit as st
import os


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as file:
        data = file.read()

    return base64.b64encode(data).decode()


def get_bgs():
    bg_list = os.listdir("images")
    random_bg = random.choice(bg_list)

    return random_bg


def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    side_bg_ext = 'png'
    b64data = f'{base64.b64encode(open(png_file, "rb").read()).decode()}'
    dta = f'data:image/{side_bg_ext};base64,{b64data}'
    page_bg_img = f'''
    <style>

    body {{
        background: url({dta});
        background-size: cover;
    }}

    </style>
    ''' % bin_str

    _ = '''
      [data-testid="stSidebar"] > div:first-child {{
          background: url({dta});
          background-size: cover;
      }}
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


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


def main():
    print(get_bgs())


if __name__ == '__main__':
    main()
