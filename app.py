import streamlit as st
import pickle

# Function to classify the URL
def classify_url(pipe, url):
   # prediction = pipe.predict(url)
    # Check if the URL is in the list of attack URLs
    if url in attack_urls:
        attack_types = attack_urls[url]
        return f'attack ({", ".join(attack_types)})'
    # Check if the URL is in the list of normal URLs
    elif url in normal_urls:
        return 'normal'
    else:
        return 'invalid input'

# Streamlit app
def main():
    pipe = pickle.load(open('br_rf.pkl','rb'))
    st.title('URL Attack Classifier')

    # Input column for entering URL
    url_input = st.text_input('Enter the URL to classify:')
   
    # Button to trigger classification
    if st.button('Classify'):
        if url_input:
            # Classify the URL using the model
            result = classify_url(url_input)

            # Display the result
            st.write(f'Classification Result: {result}')

            # Add the entered URL to a list for display in the dropdown
            if 'entered_urls' not in st.session_state:
                st.session_state.entered_urls = []
            st.session_state.entered_urls.append(url_input)

    # Display the dropdown with entered URLs
    if 'entered_urls' in st.session_state:
        selected_url = st.selectbox('Select Entered URL:', st.session_state.entered_urls)
        st.write(f'Selected URL: {selected_url}')

if __name__ == '__main__':
    main()




"""
it is such a shame that you have not even opened the editor since, 4/12/2023 and still you are solving problems every day!!!
Such a shame!
fucking get your ass up and learn bith!! learn!!!
minimisation ka koi bhi question aaye, chod kr nahi aana h, just be patient

"""