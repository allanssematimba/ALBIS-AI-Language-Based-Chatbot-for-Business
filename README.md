# ALBIS-AI-Language-Based-Chatbot-for-Business

This project is a Python script that utilizes OpenAI's GPT model to answer queries based on the data from a directory. The script constructs an index of the documents in the given directory using GPTSimpleVectorIndex from the gpt_index module. It uses LLMPredictor and PromptHelper objects to predict the best responses to queries.

## Dependencies
The script requires the following dependencies to be installed:
- gpt_index
- langchain
- IPython

The dependencies can be installed using the following command:
`pip install gpt_index langchain IPython`

## Usage
To use the script, follow these steps:
- Set your OpenAI API key as an environment variable by pasting it after running the script when prompted. The key will be saved as an environment variable.
- Put the data you want the script to use to construct the index in a directory named "data" in the same directory as the script.
- Run the script. The script will then construct an index from the documents in the "data" directory and save it as a file named "index.json" in the same directory.
- After the index is constructed, the script will enter a loop that will prompt you to input a query. The script will use the constructed index to provide an answer to your query. If the query contains one or more of the pre-defined keywords, the script will respond using the GPT model. The response will be displayed in bold.

## Acknowledgments
This project was inspired by the [GPT-3-Based Search Engine for PDF Files](https://github.com/markoprodanovic/GPT3_PDF_Search_Engine) created by Marko Prodanović.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
