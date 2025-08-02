from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def generate_blog(topic):
    '''Generates a full blog post based on a given topic'''
    
    template = '''write a detailed blog post on the topic "{topic}".
    - include an engaging introduction
    - provide 3 key points with explanations
    - use SEO-friendly keywords
    - End with a conclusion and call to action
    
    Return the blog in structured markdown format.
    '''

    prompt = PromptTemplate(input_variables = ['topic'], template = template)
    llm = ChatOpenAI(model_name = 'gpt-4o-mini')
    chain = LLMChain(llm = llm, prompt = prompt)

    return chain.run(topic = topic)

