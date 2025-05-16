import streamlit as st
from my_summarizer import extractive_summary, abstractive_summary


st.title("🧠 LLM-based Text Summarizer Tool")

text = st.text_area("Paste your text here:", height=300)

if st.button("Generate Summaries"):
    with st.spinner("Generating Extractive Summary..."):
        extractive = extractive_summary(text)
    with st.spinner("Generating Abstractive Summary..."):
        abstractive = abstractive_summary(text)

    st.subheader("Extractive Summary:")
    st.write(extractive)

    st.subheader("Abstractive Summary:")
    st.write(abstractive)
