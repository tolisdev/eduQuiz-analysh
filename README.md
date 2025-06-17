# Adaptive Educational Quiz Question Generator Using OpenAI GPT

## Description
This project automatically evaluates student quiz answers on linguistic awareness topics (implicit meaning, ambiguity, advertising techniques) and generates personalized follow-up multiple-choice questions tailored to each student's weaknesses. It leverages OpenAI’s GPT models via API to create meaningful, adaptive questions to support targeted learning interventions.

The tool is ideal for educators who want to provide differentiated learning paths based on students’ individual needs, enhancing engagement and understanding. It is designed to be easy to use and extend for various subject areas.

## Features
- Automatic scoring of student responses with detailed comments.
- Identification of individual learning weaknesses.
- Generation of personalized multiple-choice questions via OpenAI GPT.
- Output saved per student for easy review and assignment.
- UTF-8 support for multilingual content, especially Greek.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/tolisdev/edu-quiz-generator.git```
2. Install dependencies:
    ```bash
    pip install openai```
3. Set your OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY="your_api_key_here"```
4. Run:
    ```bash
    python main.py```


