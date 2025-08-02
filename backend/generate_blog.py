from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# from langchain import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

def generate_blog(topic):
    '''Generates a full blog post based on a given topic'''
    
    template = """write a detailed blog post on the topic "{topic}".
    - include an engaging introduction
    - provide 3 key points with explanations
    - use SEO-friendly keywords
    - End with a conclusion and call to action
    
    Return the blog in structured markdown format.
    """

    prompt = PromptTemplate.from_template(template)
    llm = ChatOpenAI(model_name = 'gpt-4o-mini')
    chain = (
    RunnableParallel(
        {
            'topic': RunnablePassthrough()
        }
    )
        | prompt | llm | StrOutputParser()
    )

    return chain.invoke(topic)

