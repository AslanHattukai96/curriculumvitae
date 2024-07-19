def login():
    # Load credentials from secrets
    credentials = st.secrets["credentials"]
    username = credentials["username"]
    password = credentials["password"]
 
    # Function to check login credentials
    def check_credentials(input_username, input_password):
        return input_username == username and input_password == password
 
    # Create a session state to track login status
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
 
    # Display login form if not logged in
    if not st.session_state.logged_in:
        with st.container():
            st.title("Login")
            input_username = st.text_input("Username", "")
            input_password = st.text_input("Password", "", type="password")
 
            if st.button("Login"):
                if check_credentials(input_username, input_password):
                    st.session_state.logged_in = True
 
                    # Create a placeholder for the success message
                    success_placeholder = st.empty()
                    success_placeholder.success("Login successful!")
 
                    # Wait for 1 second and then clear the message
                    time.sleep(1)
                    success_placeholder.empty()
                    # Clear the login inputs after successful login
                    st.rerun()
                else:
                    st.error("Invalid username or password")
 
        # Additional content can be added here for logged-in users
 
    return st.session_state.logged_in