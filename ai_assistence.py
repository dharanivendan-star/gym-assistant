
import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title("Your Personal Gym Assistant")

question = st.text_input("Ask Question regarding Gym...")

def gym_trainer(question):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": """You are a gym trainer. 
                rules:
                    - Be polite and friendly
                    - keep answers short and to the point
                    - give diet plan for weight loss
                """
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return response.choices[0].message.content

if st.button("Send"):
    st.write(gym_trainer(question))