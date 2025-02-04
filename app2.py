import streamlit, llm, json

# Request LLM to generate questions in JSON format
def generate_questions(topic, num_questions):
    system_prompt = "You are proficient quiz generator."
    with open("prompt.txt", "r") as f:  # Read user_prompt from prompt.txt
        user_prompt = f.read()
    
    # Replace the placeholders with the actual values
    user_prompt = user_prompt.replace("{topic}", topic)
    user_prompt = user_prompt.replace("{num_questions}", str(num_questions))
    
    # Invoke LLM to generate the output based on user and system prompts
    results = llm.answer(system_prompt, user_prompt)
    return results

# Handle the button click event
def generate_question_handler():
    # Get the topic and num_questions from streamlit.session_state
    topic = streamlit.session_state["topic"]
    num_questions = streamlit.session_state["num_questions"]
    
    # Generate questions
    questions = generate_questions(topic, num_questions)
    
    # Show questions generated
    streamlit.write("Generated Questions:")
    streamlit.json(questions)

# Streamlit sidebar for input
with streamlit.sidebar:  # The input widgets are placed in the sidebar
    streamlit.title("Quiz Generator")
    streamlit.session_state["topic"] = streamlit.text_input("Enter the topic:", "")
    streamlit.session_state["num_questions"] = streamlit.number_input("Number of questions:", min_value=1, max_value=100, value=5)
    
    if streamlit.button("Generate Questions"):
        generate_question_handler()