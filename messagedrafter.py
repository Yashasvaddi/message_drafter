import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv
import threading as th
def caption():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    image_upload=st.file_uploader("Upload the image files",type=["jpg","jpeg","png"],accept_multiple_files=True)
    if not api_key:
        st.error("API Key not found. Please check your .env file.")
        st.stop()

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    user_text = st.text_area("Enter your keywords", height=70)

    if st.button("Try it?") and user_text:
        with st.spinner("Cooking up fresh captions"):
            # folder_path = r"images"
            # image_exts = (".png", ".jpg", ".jpeg", ".webp", ".bmp")

            # image_paths = sorted([
            #     os.path.join(folder_path, f)
            #     for f in os.listdir(folder_path)
            #     if f.lower().endswith(image_exts)
            # ])

            answer = ''
            for path in image_upload:
                img = Image.open(path)
                response = model.generate_content([
                    f'Give me a good caption for this picture. Use {user_text} for help. Keep it descriptive (up to 5 lines). No aesthetic or abstract captions, just meaningful ones.',
                    img
                ])
                answer += response.text

            final = model.generate_content(
                f"Summarize {answer} and give me the best caption of almost 2 lines. Only return the caption. Dont say anything else apart from the caption"
            )

            st.write(final.text + '\n\n\n' +
                    '#ScholarsPreschool #PreschoolLife #LittleLearners #EarlyEducation '
                    '#PreschoolMoments #LearningThroughPlay #CuriousMinds #ChildDevelopment '
                    '#GrowingTogether #PreschoolFun #CreativeKids #SummerCamp2025 '
                    '#KidsActivities #HandsOnLearning #VasaiVirarKids #VasaiPreschool')
            
if __name__=="__main__":
    caption()