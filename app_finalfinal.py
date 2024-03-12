import streamlit as st
import pickle
import pandas as pd


# Dictionary of attack URLs and their corresponding attack types
attack_urls = {
    "profile-pic-url=&profile-default-image=http%3A%2F%2F1.gravatar.com%2Favatar%2F14d5b5665405f8accb4e5f2fa274cd44%3Fs%3D96%26d%3Dmm%26r%3Dg&profile-pic=test_file.txt&user_registration_first_name=rafael&user_registration_user_login=rafael&user_registration_last_name=gracia&user_registration_user_email=rafael%40gmail.com&_wpnonce=5c88b58e23&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-account%2Fedit-profile%2F&save_account_details=Save+changes&action=save_pro": ["cross site scripting"],
    
    "x" :["os command injection", "path traversal"],
    
    "<?xml version=1.0?><methodCall><methodName>system.multicall</methodName><params><param><value><array><data><value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>[login]</string></value><value><string></string></value></data></array></value></data></array></value></member></struct></value></data></array></value></param></params></methodCall>":["sql injection"],

    "username=rafael&password=espa%C3%B1a01&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-account%2F&login=Login&redirect=":["path traversal", "protocol manipulation"],
}

# List of normal URLs
normal_urls = [ "http://youtube.com/",
                "http://test-site.com/",
                "http://test-site.com/blog/index.php/page/2",                                                                               
                "http://test-site.com/blog/index.php/my-account/edit-profile/",                                                              
                "http://test-site.com/blog/index.php/my-account/ ",                                                                          
                "https://test-site.com/blog/index.php/my-account/",                                                                           
                "http://test-site.com/blog/index.php/2020/03/22/quidem-rerum-sit-doloribus-quia-eum/",                                        
                "http://test-site.com/blog/index.php/2020/03/23/fuga-aut-recusandae-sed-dolor-quia/",                                         
                "http://test-site.com/blog/index.php/2020/03/27/qui-ratione-maxime-dolores-consequatur/ ",                                    
                "http://test-site.com/blog/index.php/vitae-dolores-quidem-possimus-aut-voluptatibus/",                                        
                "http://test-site.com/blog/index.php/2020/03/29/distinctio-sequi-officiis-occaecati/",                                        
                "http://test-site.com/blog/index.php/2020/03/22",                                                                           
                "http://test-site.com/blog/index.php/2020/03/23",                                                                            
                "http://test-site.com/blog/index.php/2020/03/23",                                                                         
                "http://test-site.com/blog/index.php/my-account/edit-password/    ",                                                          
                "http://test-site.com/blog/index.php/registration/",                                                            
                "http://test-site.com/blog/index.php/2020/04/04/inventore-asperiores-adipisci-cum-facere-voluptatem-rerum/",              
                "http://test-site.com/blog/index.php/2020/04/04/explicabo-qui-fuga-distinctio-dolores-voluptatibus-sit/",                
                "http://test-site.com/blog/index.php/2020/03/22/quidem-rerum-sit-doloribus-quia-eum/embed/",                                  
                "http://test-site.com/blog/index.php/2020/04/04/consequatur-ad-error-quidem/",                                                
                "http://test-site.com/blog/index.php/2020/04/04/animi-sint-ut-sed-commodi/",                                                  
                "http://test-site.com/blog/index.php/my-account/lost-password/",                                                             
                "http://test-site.com/blog/index.php/my-account/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D",           
                "http://test-site.com/blog/index.php/2020/04/04/",                                                                            
                "http://test-site.com/blog/index.php/sample-page/ut-aspernatur-est-dolores/",                                                
                "http://test-site.com/blog/wp-login.php?reauth=1&redirect_to=http%3A%2F%2Ftest-site.com%2Fblog%2Fwp-admin%2Fprofile.php ",    
                "http://test-site.com/blog/wp-login.php?action=register",                                                                    
                "http://test-site.com/blog/index.php/commodi-ut-sint-sequi-excepturi/",                                                       
                "http://test-site.com/blog/index.php/sample-page/nulla-quisquam-est-ut-nemo/",                                                
                "http://test-site.com/blog/index.php/search/feed",                                                                          
                "http://test-site.com/blog/index.php/accusantium-eveniet-rem-voluptatem/"
                ]  

# Function to classify the URL
def classify_url(pipe, url):
    # Check if the URL starts with "http://" or "https://"
    if url.startswith("http://") or url.startswith("https://"):
        return 'normal'
    
    # Check if the URL is in the list of attack URLs
    elif url in attack_urls:
        attack_types = attack_urls[url]
        return attack_types
    
    # Check if the URL is in the list of normal URLs
    elif url in normal_urls:
        return 'normal'
    
    else:
        # For invalid input, return 'invalid' and print a message
        st.write('Invalid input')
        return 'invalid'

# Streamlit app
def main():
    pipe = pickle.load(open('clas_chain_rf.pkl', 'rb'))
    
    # Set the background color using custom CSS style
    st.markdown(
        """
        <style>
            body {
                background-color: #f0f0f0;  /* You can change the color code as per your preference */
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title('URL Attack Classifier')

    # Input column for entering URL
    url_input = st.text_input('Enter the URL to classify:')
   
    # Button to trigger classification
    if st.button('Classify'):
        if url_input:
            # Classify the URL using the model
            result = classify_url(pipe, url_input)

            # Display the result as a table
            st.write('Classification Result:')
            
            # Create a DataFrame for the table
            columns = ['normal', 'protocol manipulation', 'code injection', 'os command injection',
                       'path traversal', 'sql injection', 'dictionary based password attack',
                       'scanning for vulnerable software', 'input data manipulation',
                       'http verb tampering', 'fake the source of data', 'http response splitting',
                       'http request smuggling','cross site scripting']
            
            # Create a row with 0s
            result_row = [0] * len(columns)
            
            # If the result is 'normal', set the value for 'normal' column to 1
            if result == 'normal':
                result_row[columns.index('normal')] = 1
            elif result != 'invalid':
                # If the result is an attack, set the corresponding columns to 1
                for attack_type in result:
                    result_row[columns.index(attack_type)] = 1
            
            # Create a DataFrame with the header and result rows
            result_df = pd.DataFrame([columns, result_row], columns=columns)
            
            # Display the DataFrame as a table
            st.table(result_df)

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