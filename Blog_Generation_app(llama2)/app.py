import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import ctransformers
from ctransformers import AutoModelForCausalLM

## create virtual env 'python -m vnv myenvironment'
## to instal requirement 'pip install -r requirements.txt'
## to run streamlit 'streamlit run app.py'
##Function to get llm response
def  getresponse(input_text,no_words,blog_style):
    #calling model
    llm = AutoModelForCausalLM.from_pretrained("model/llama-2-7b-chat.ggmlv3.q2_K.bin", model_type="llama")

    # llm=ctransformers(model='model\llama-2-7b-chat.ggmlv3.q2_K.bin',
    #                   model_type='llama',
    #                   config = {'max_new_tokens' : 256,
    #                             'temperature' : 0.01})
    #Prompt Template
    template = """
       Create a blog post tailored to the {blog_style} job profile on the topic '{input_text}',
        with a word count limit of {no_words} words.
               """
    prompt = PromptTemplate(input_variables=['blog_style', 'input_text','no_words'],
                            template=template)
    #generate the response
    response=llm(prompt.format(blog_style=blog_style, input_text=input_text,no_words=no_words))
    print(response)
    return response 

st.set_page_config(page_title= 'Generate Blogs',
                   page_icon='0Q0',
                   initial_sidebar_state='collapsed')

st.header('Generate Blogs')
input_text=st.text_input('Enter the blog topic')

#creating 2 addititonal cols
col1,col2=st.columns([5,5])
with col1:
    no_words=st.text_input('No of words')
with col2 :
    blog_style=st.selectbox('writing the blog as',
                            ('Researcher','Data Scientist', 'Common People'),
                              index=0)
submit=st.button('GENERATE')

## Final response
if submit :
    st.write(getresponse(input_text,no_words,blog_style))