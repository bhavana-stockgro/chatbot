import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI
from IPython.display import display, Markdown
import pandas as pd

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
            
        #CONVERTING INTO DATAFRAME    
        df = pd.read_csv(temp_csv_path)
            
        # CALLING THE LANGUAGE MODEL - Text Davinci model
        llm = OpenAI(openai_api_key=OPEN_API_KEY, temperature=0)
        
        # CREATING AN AGENT INSTANCE
        agent = create_csv_agent(llm, temp_csv_path , verbose=True)
        
        # #CALLING A SECOND LANGUAGE MODEL- GPT4 model
        # gpt3_llm = ChatOpenAI(openai_api_key=OPEN_API_KEY, temperature=0, model_name = "gpt-3.5-turbo")
        
        # # CREATING A SECOND AGENT INSTANCE
        # gpt3_agent = create_csv_agent(gpt3_llm, temp_csv_path, verbose = True)

        if prompt is not None and prompt != "":
            response_davinci = agent.run(prompt)
            model_davinci = st.text("Text Davinci model:")
            st.write(response_davinci)
            # response_gpt3 = gpt3_agent.run(prompt)
            # model_gpt3 = st.text("GPT3.5 Turbo  model:")
            # st.write(response_gpt3)

if __name__ == "__main__":
    main()