import streamlit as st
import requests



st.set_page_config(page_title="Blog Writer", page_icon=":books:")
st.title('Blog Writer')

topic = st.text_input('Enter the Topic: ')

if st.button('Generate Blog'):
    with st.spinner('...generating blog...'):
        response = requests.post('http://127.0.0.1:5000/generate', json = {'topic': topic})
        if response.status_code == 200:
            result = response.json()
            st.subheader('Generated Blog')
            st.markdown(result['blog'])
        else:
            st.error('Error generating blog!')


st.markdown(
    "<div style='margin-top:2em; font-size:.9em;color:#888'>"
    "Powered by RyBell Cognitive Concepts"
    "</div>",
    unsafe_allow_html=True
)
        

