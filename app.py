# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd

st.title("Web App")

# プルダウンを表示させる
what_lang = st.selectbox(
    'あなたの好きな言語を選んでね！',
     ('python','Rust', 'go', 'C++'))

# プルダウンサイドバーに表示させる
what_lang_size = st.sidebar.selectbox(
    'あなたの好きな言語を選んで！',
     ('python','Rust', 'go', 'C++'))

answer = st.button('Say hello')

if answer == True:
     st.write('Why hello there')
else:
     st.write('Goodbye')
data = {
    'lat': np.random.randn(100) / 100 + 35.68,
    'lon': np.random.randn(100) / 100 + 139.75,
}
map_data = pd.DataFrame(data)
# 地図に散布図を描く
st.map(map_data)
