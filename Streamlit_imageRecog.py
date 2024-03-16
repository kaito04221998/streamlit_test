"""
Streamlit_imageRecog.py: Streamlit app for background removal using rembg and OpenCV

This Streamlit app allows users to upload an image, remove its background using the rembg library, and display the result using OpenCV.

Copyright 2024 Kaito Yamazaki

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import streamlit as st
from rembg import remove
import cv2
from PIL import Image
import numpy as np

radio_res = st.radio("以下から選択", ("背景削除", "グレースケール", "ぼやけた画像を選別"))


if (radio_res) == "背景削除":
    "coming soon..."
    pass
    # input_file = st.file_uploader("Choose a file", type=['.jpg', '.png', '.gif','.tiff','.raw'])
    # print(input_file)
    # if input_file is not None:
    #     image = Image.open(input_file)
    #     input = np.array(image)
    #     rem_image = remove(input)
    #     output = Image.fromarray(rem_image)
    #     st.image(output, caption="Not back ground image", use_column_width=True)

elif (radio_res) == "グレースケール":
    input_file = st.file_uploader("Choose a file", type=['.jpg', '.png', '.gif','.tiff','.raw'])

    if input_file is not None:
        image = Image.open(input_file)
        # 画像を白黒に変換
        l_image = image.convert("L")
        
        st.image(l_image, caption="グレースケール", use_column_width=True)

elif (radio_res) == "ぼやけた画像を選別":
    "coming soon..."
    pass
