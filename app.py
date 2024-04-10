import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="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")

def generate_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": prompt},
        ]
    )
    # Correctly access the 'content' attribute of the message
    return completion.choices[0].message.content

st.title("Chatbot")
user_input = st.text_input("Type your message here:")
if st.button("Send"):
    response = generate_response(user_input)
    st.write(f"Bot: {response}")

 


# commands
# python -m venv venv
# venv/scripts/activate
# pip install streamlit
# pip install operai
# streamlit run app.py