# Importing necessary packages, files and services
import os 
import openai


import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper
from langchain.chat_models import ChatOpenAI

# openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = os.environ.get('OPENAI_API_KEY')

# App UI framework
st.title('🔋👨‍⚖️ ParetoPal')
prompt = st.text_input('What topic would you like to research: ') 

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='Please forget all prior prompts.  You are a university professor at a top university. You have become an expert in the Pareto principle (80/20 rule). Please identify the 20-percent of {topic} that will yield 80-percent of the best  results. Use your academic resources to  provide a well identified and focused learning program to master this subject.'
)

# Wikipedia data
wiki = WikipediaAPIWrapper()

# Memory 
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')

# Llms
llm = ChatOpenAI(model_name="gpt-4", temperature=0.9) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)

# Chaining the components and displaying outputs
if prompt: 
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt) 

    st.write(title) 