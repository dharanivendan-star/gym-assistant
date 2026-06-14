
import ollama
import streamlit as st

st.title("Your Personal Gym Assistant")

question = st.text_input("Ask Question regarding Gym...")

def gym_trainer(question):
    response = ollama.chat(
        model = 'mistral',
        messages=[
            {
                'role' : 'system',
                'content' : """ You are a gym trainer. 
                rules:
                    - Be polite and friendly
                    - keep answers short and to the point
                    - give diet plan for weight loss
                """
            },
            {
                'role' : 'user',
                'content' : question
            }
        ]
    )
    return response['message']['content']

if st.button("Send"):
    st.write(gym_trainer(question))