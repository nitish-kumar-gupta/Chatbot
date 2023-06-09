# Simple Job Website Chatbot

This project showcases the implementation of a simple chatbot for a job website using Python. The chatbot allows users to inquire about current job openings, check eligibility criteria, and obtain relevant information.

## Requirements

- Python 3.x

## Getting Started

1. Clone the repository or download the source code files.
2. Ensure that you have Python 3.x installed on your system.
3. Open a text editor and create a new file named `Chatbot.py`.
4. Copy and paste the code provided below into the `Chatbot.py` file.
5. Save the file and close the text editor.

## Usage

1. Open the `Chatbot.py` file in a text editor.
2. The code provided includes a simple implementation of the chatbot using if-else statements.
3. Modify the code to add more functionality and responses based on user queries.
4. Use the `input()` function to get user input and display the chatbot's responses using the `print()` function. For example:

```python
user_input = input("User: ")
if user_input == "1":
    print("Chatbot: The current job openings are...")
elif user_input == "2":
    print("Chatbot: To check eligibility, please provide your qualifications...")
else:
    print("Chatbot: I'm sorry, I didn't understand. Can you please rephrase your query?")
```

5. Run the `Chatbot.py` file using the following command:

```shell
python Chatbot.py
```

6. The program will prompt the user for input and display the chatbot's response based on the user's query.

## Customization

You can customize the code according to your specific requirements. Add more if-else statements or functions to handle different user inquiries and provide appropriate responses. You can also integrate external APIs or databases to fetch job data or eligibility criteria.

## Note

This is a basic implementation of a simple chatbot for a job website. It does not utilize natural language processing techniques. The chatbot's responses are based on exact user input matches.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use the code according to your needs.

## Acknowledgements

The simple job website chatbot project provides a basic implementation of a chatbot using if-else statements in Python. This project can be further expanded and enhanced with more complex logic and integrations to improve the chatbot's functionality and user experience.
