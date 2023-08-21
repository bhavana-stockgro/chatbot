# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:06:10 2023

@author: kedar
"""

import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms.openai import OpenAI
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
def main():
    
    # API KEY VARIABLE
    OPEN_API_KEY = "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"
    
    # STARTING STREAMLIT APPLICATION
    st.set_page_config(page_title="Ask your CSV")
    
    # HEADING OF THE APPLICATION
    st.header("Ask your CSV")
    
    # CSV FILE UPLOADED BY THE USER
    csv_file = st.file_uploader("upload your csv file", type="csv")

    
    if csv_file is not None:
        prompt = st.text_input("Ask a Question about your CSV")
        
        #CREATING TEMPORARY PATH
        temp_csv_path = "temp.csv"
        
        #COPYING CONTENTS OF CSV FILE INTO TEMPORARY PATH
        with open(temp_csv_path, "wb") as temp_file:
            temp_file.write(csv_file.getvalue())
            
        # CALLING THE LANGUAGE MODEL
        llm = OpenAI(openai_api_key=OPEN_API_KEY, temperature=0)
        
        # CREATING AN AGENT INSTANCE
        agent = create_csv_agent(
            ChatOpenAI(openai_api_key=OPEN_API_KEY, temperature=0, model="gpt-3.5-turbo"),temp_csv_path,
            verbose=True)

        if prompt is not None and prompt != "":
            response = agent.run(prompt)
            
            st.write(response)

if __name__ == "__main__":
    main()