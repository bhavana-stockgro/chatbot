# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:42:16 2023

@author: kedar
"""

import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

#loading text document
from langchain.document_loaders import TextLoader

loader = TextLoader('chatbot_test.txt')
document = loader.load()
print(document)