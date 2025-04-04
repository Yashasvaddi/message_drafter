import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

user_text = st.text_area("Enter your text", height=70)

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini model
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash')

if user_text:
    folder_path = "C:\\New folder\\codes\\college stuff\\message_drafter\\images"
    image_exts = (".png", ".jpg", ".jpeg", ".webp", ".bmp")

    # Get sorted list of image paths
    image_paths = sorted([
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(image_exts)
    ])

    answer = ''
    for i, path in enumerate(image_paths):
        img = Image.open(path)
        response = model.generate_content([
            f'Give me a good caption for this picture, just give me single caption dont give me multiple. Make it a bit long upto 5 lines. Dont give asthetic captions. Try describing the image, use {user_text} for help',
            img
        ])
        answer += response.text

    final = model.generate_content(
        f"Summarize {answer} and give me the best caption of almost 2 lines. Dont say anything apart from the generated result"
    )
    st.write(
        final.text + '\n\n\n'
        '#ScholarsPreschool #PreschoolLife #LittleLearners #EarlyEducation '
        '#PreschoolMoments #LearningThroughPlay #CuriousMinds #ChildDevelopment '
        '#GrowingTogether #PreschoolFun #CreativeKids #SummerCamp2025 '
        '#KidsActivities #HandsOnLearning #VasaiVirarKids #VasaiPreschool'
    )
