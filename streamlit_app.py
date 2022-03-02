import streamlit as st

st.write(f'secret_a: {st.secrets["secret_a"]}')
st.write(f'secret_b: {st.secrets["secret_b"]}')
st.write(f'secret_block - subsecret_a: {st.secrets["secret_block"]["subsecret_a"]}')
st.write(f'secret_block - subsecret_b: {st.secrets["secret_block"]["subsecret_b"]}')
