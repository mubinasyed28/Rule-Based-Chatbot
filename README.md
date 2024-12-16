# Chatbot with NLP and Conversation Flow
This project features a Rule-based Chatbot built using spaCy for natural language processing (NLP). The chatbot is designed to understand and respond to user queries based on predefined rules, leveraging NLP techniques like Named Entity Recognition (NER) to improve the accuracy of responses.

# Features:
- Intent Identification: The chatbot uses regex patterns to identify user intents such as greetings, wellbeing inquiries, weather queries, jokes, and farewells.
- spaCy Integration: spaCy's NLP model is used to process user input and recognize entities (e.g., locations, dates) to provide more personalized responses.
- Conversation Flow: The chatbot maintains a smooth conversation, offering relevant responses based on the identified intent, and can handle multiple user interactions in one session.
- Fallback Responses: For unknown inputs, the chatbot provides a generic response to guide the user.

# Technologies Used:
- Python: The primary programming language.
- spaCy: For NLP tasks like tokenization and named entity recognition (NER).
- Regex: Used for basic pattern matching to identify different types of user input.

 # How to Run the Chatbot:
 1. Clone the repository:

    git clone https://github.com/mubinasyed28/Rule-Based-Chatbot

2. Download the spaCy language model:

   python -m spacy download en_core_web_sm

3. Run the chatbot:

   python chatbot.py


