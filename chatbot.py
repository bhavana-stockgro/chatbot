"""
Created on Mon Jul 17 14:39:11 2023

@author: kedar
"""
import os
import sys
import constants
import openai
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

api_key = "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"

# Set OpenAI API key as environment variable
os.environ["OPENAI_API_KEY"] = api_key

query = sys.argv[0]
print(query)

loader = TextLoader('data.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

# Use OpenAI API directly
openai.api_key = api_key
response = openai.Completion.create(engine="text-davinci-003", prompt=query)

print(response.choices[0].text)
