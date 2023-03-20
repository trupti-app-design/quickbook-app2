import streamlit as st

st.set_page_config(
    page_title="Profit & Loss Report App",
    page_icon=":)",
)
custom_css = """
    body {
        color: #1a1a1a;  /* dark grey */
        background-color: #f0f0f5;  /* light grey */
    }
    .css-1gkpy7w {
        background-color: #008080;  /* teal */
    }
"""

# Set the custom CSS using st.markdown
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)



st.title("Main Page")
st.sidebar.success("Select a page above")
