#!/usr/bin/env python
# coding: utf-8

# # ALBIS - AI Language-Based Information System for Business

# In[ ]:


# You can either use text-davinci-003 or text-ada-001.
# The former is more advanced but more expensive.


# In[38]:


# Import necessary libraries for the script
from gpt_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
import os
from IPython.display import Markdown, display

# Define a function named construct_index that takes a directory_path parameter
def construct_index(directory_path):
    
    # set maximum input size
    max_input_size = 4096
    
    # set number of output tokens
    num_outputs = 300
    
    # set maximum chunk overlap
    max_chunk_overlap = 20
    
    # set chunk size limit
    chunk_size_limit = 600 

    # Define an LLMPredictor object with the OpenAI language model, and a PromptHelper object with the above-defined parameters
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-ada-001", max_tokens=num_outputs))
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
 
    # Load data from the directory at directory_path using SimpleDirectoryReader
    documents = SimpleDirectoryReader(directory_path).load_data()
    
    # Construct a GPTSimpleVectorIndex object with the loaded documents, LLMPredictor, and PromptHelper
    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )

    #Save the constructed index to a file named 'index.json' and return the index object
    index.save_to_disk('index.json')

    return index

# Define a function named ask_ai
def ask_ai():
    
    # Load the previously saved GPTSimpleVectorIndex object from 'index.json'
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    
    # Enter a loop that prompts the user for input
    while True: 
        
        # Query the loaded index for a response to the input
        query = input("What can ALBIS help you with?")
        response = index.query(query, response_mode="compact")
        
        # Display the response in bold using IPython.display
        display(Markdown(f"Response: <b>{response.response}</b>"))  


# In[ ]:


# Prompt the user for their OpenAI API key and save it as an environment variable

os.environ["OPENAI_API_KEY"] = input('Paste your OpenAI key here and hit enter:')


# In[40]:


# Call the construct_index function with "data" as the directory path to create and save the index

construct_index("data")


# In[ ]:


# Define a function named "ask_ai()" that takes no arguments
def ask_ai():
    
    # Load a pre-trained GPT model index from a file named "index.json" and assign it to the variable "index"
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    
    # Define a list of keywords that the GPT model is trained to respond to
    keywords = ['business', 'product', 'SEO','service', 'pricing', 'support', 'website', 'traffic', 'search engine rankings',
                'customer churn rate', 'social media marketing', 'email marketing', 'automation', 'supply chain management',
                'data-driven marketing', 'user experience', 'content marketing', 'AI', 'customer sentiment', 'data analytics',
                'mobile app development', 'online reputation management', 'lead generation', 'machine learning', 
                'customer service', 'chatbots', 'social media', 'conversion rates', 'marketing ROI', 
                'customer loyalty program', 'personalization', 'email deliverability', 'sales process', 
                'digital product strategy', 'omnichannel marketing', 'brand messaging', 'influencer marketing', 
                'user acquisition strategy', 'customer segmentation', 'product development process', 'lead nurturing', 
                'fraud detection', 'employee performance', 'customer-centric approach', 'predictive maintenance', 
                'inventory management', 'digital advertising', 'financial forecasting', 'accessibility', 
                'logistics operations', 'lead scoring model', 'HR operations', 'competitor analysis', 'competitive analysis', 'buyer journey', 
                'customer lifetime value', 'voice search optimization', 'email open rates', 'social media advertising', 
                'sales funnel', 'marketing automation', 'chatbot performance', 'mobile-first strategy', 'event marketing', 
                'personalized email marketing', 'customer insights', 'landing pages', 'customer acquisition cost', 
                'referral marketing', 'crisis communication', 'omnichannel customer engagement', 'supply chain forecasting',
                'brand ambassador program', 'sustainability', 'blockchain technology', 'gamification', 'sentiment analysis',
                'local SEO', 'virtual reality', 'augmented reality', 'inventory forecasting accuracy', 'video marketing', 
                'product recommendation engine', 'email segmentation optimization', 'loyalty program customization',
                'mobile app development', 'artificial intelligence', 'lead gen', 'ML', 'UX']
    
    # Start a continuous loop that will run until the program is interrupted or terminated
    while True: 
        
        # Prompts the user to input a query and assigns it to the variable "query"
        query = input("What can ALBIS help you with?  ")
        
        # Check if any of the keywords defined in "keywords" are present in the user's query, regardless of case 
        # If at least one keyword is present, the condition is true and the code inside the "if" statement is executed
        if any(keyword in query.lower() for keyword in keywords):
            
            # Query the GPT model index with the user's query and assigns the result to the variable "response". 
            # The "response_mode" parameter is set to "compact" to return only the best matching response.
            response = index.query(query, response_mode="compact")
            
            # Display the GPT model's response in bold using the Markdown function from IPython.display.
            display(Markdown(f"Response: <b>{response.response}</b>"))
        
        # If the user's query does not contain any of the keywords defined in "keywords", print a default message indicating
        # that the chatbot cannot answer the question and prompts the user to ask something related to business or automation.
        else:
            display(Markdown("<b>Sorry, I cannot answer that question. Please ask something related to business or automation.</b>"))

# Call the "ask_ai()" function to start the chatbot.            
ask_ai()

