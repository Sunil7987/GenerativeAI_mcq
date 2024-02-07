# import streamlit as st
# import os

# # Function to extract title from a file
# def get_file_title(file_content):
#     # You can customize this function based on the file type you expect
#     # For simplicity, this example assumes the file content is text and extracts the first line as the title
#     lines = file_content.split('\n')
#     return lines[0] if lines else "No Title"

# # Main Streamlit app
# def main():
#     st.title("File Title Extractor")

#     with st.form("user_input"):
#         uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf"])

#         if st.form_submit_button("Get Title") and uploaded_file is not None:
#             # Read the content of the file
#             file_content = uploaded_file.read()

#             # Get the title from the file content
#             file_title = get_file_title(file_content)

#             # Display the title
#             st.success(f"Title: {file_title}")

#     # You can add more content or features to your app here

# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None: 
    # Read the file into a Pandas DataFrame
    try:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
    except Exception as e:
        st.error(f"Error: {e}")
