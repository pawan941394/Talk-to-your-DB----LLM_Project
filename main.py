from GenAI_helper import get_few_shots_Db_Chain
import streamlit as st
st.title("Talk To Your DB")
question = st.text_input("Question : ")

if question:
    chain = get_few_shots_Db_Chain()
    st.header("Answer :")
    ans = chain.run(question)
    st.write(ans)
