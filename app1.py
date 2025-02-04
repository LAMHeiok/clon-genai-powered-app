import streamlit
import llm
# Create a text input box
text_input = streamlit.text_input("Input your question")
# Create a submit button
if streamlit.button("Submit"):
    user_prompt = text_input
    system_prompt = "Answer questions in funny tone with Emoji"
    result = llm.answer(system_prompt, user_prompt)
    streamlit.markdown("## Response")
    streamlit.write("Response:", result)