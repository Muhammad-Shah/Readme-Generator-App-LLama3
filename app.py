import streamlit as st
import readme_generator as rmgen

st.header('README Generation with the help of Llama3-70b from code')
uploaded_file = st.file_uploader('Upload Code File')

if uploaded_file is not None:
    content = uploaded_file.read.decode()
    response = rmgen.ask(content)
    st.markdown("""-----------------------------""")
    st.subheader('Response')
    st.text(response)
    st.markdown("""-----------------------------""")
    st.subheader('Preview')
    st.markdown(response)

    # Add a button to copy the response
    if st.button('Copy Response'):
        st.text_area('Copied Response', value=response)
        st.info('Response copied to clipboard!')
