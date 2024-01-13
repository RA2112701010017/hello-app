import streamlit as st

def main():
    # Set page title and configure page layout
    st.set_page_config(
        page_title="Public Health Website",
        page_icon=":hospital:",
        layout="wide",
    )

    # Set background color and padding
    st.markdown(
        """
        <style>
            body {
                background-color: #f0f5f5;
                padding: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("Go to:", ["Home", "Latest News", "Disease Information", "Prevention Tips", "Contact Us"])

    # Title with a colored background
    st.title("Public Health Website")
    st.markdown(
        """
        <style>
            div.stTitle {
                background-color: #3498db;
                padding: 20px;
                border-radius: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Home Page
    if menu_selection == "Home":
        st.header("Welcome to our Public Health Portal")
        st.markdown(
            """
            <style>
                div.stHeader {
                    background-color: #2ecc71;
                    padding: 10px;
                    border-radius: 5px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.write("This website provides information about public health, diseases, and prevention measures.")

    # Latest News Page
    elif menu_selection == "Latest News":
        st.header("Latest News")
        st.markdown(
            """
            <style>
                div.stLatestNews {
                    background-color: #e74c3c;
                    padding: 10px;
                    border-radius: 5px;
                </style>
            </style>
            """,
            unsafe_allow_html=True
        )
        st.write("Stay updated with the latest news and developments in public health.")

        # Add a checkbox for showing/hiding the latest news
        show_news = st.checkbox("Show Latest News")
        if show_news:
            st.write("1. New Study on Vaccine Efficacy")
            st.write("2. Tips for Staying Healthy During Flu Season")
            st.write("3. Community Outreach Programs")

    # Disease Information Page
    elif menu_selection == "Disease Information":
        st.header("Disease Information")
        st.markdown(
            """
            <style>
                div.stDiseaseInfo {
                    background-color: #f39c12;
                    padding: 10px;
                    border-radius: 5px;
                </style>
            </style>
            """,
            unsafe_allow_html=True
        )
        selected_disease = st.selectbox("Select a Disease:", ["COVID-19", "Influenza", "Malaria", "Diabetes"])

        # Display information based on the selected disease
        if selected_disease == "COVID-19":
            st.write("COVID-19 is a respiratory illness caused by the SARS-CoV-2 virus.")
            st.write("Preventive measures include wearing masks, social distancing, and vaccination.")
        elif selected_disease == "Influenza":
            st.write("Influenza is a viral infection affecting the respiratory system.")
            st.write("Get vaccinated annually to prevent the flu.")
        elif selected_disease == "Malaria":
            st.write("Malaria is a mosquito-borne disease caused by Plasmodium parasites.")
            st.write("Use bed nets and take antimalarial medications for prevention.")
        elif selected_disease == "Diabetes":
            st.write("Diabetes is a chronic condition affecting blood sugar levels.")
            st.write("Maintain a healthy lifestyle and monitor blood glucose regularly.")

    # Prevention Tips Page
    elif menu_selection == "Prevention Tips":
        st.header("Prevention Tips")
        st.markdown(
            """
            <style>
                div.stPreventionTips {
                    background-color: #2c3e50;
                    padding: 10px;
                    border-radius: 5px;
                    color: #ecf0f1;
                </style>
            </style>
            """,
            unsafe_allow_html=True
        )
        st.write("Follow these tips to maintain good health and prevent diseases:")

        st.markdown("""
            - Wash hands regularly with soap and water.
            - Eat a balanced diet rich in fruits and vegetables.
            - Exercise regularly to stay physically active.
            - Stay hydrated by drinking plenty of water.
            - Get enough sleep to support overall well-being.
        """)

    # Contact Us Page
    elif menu_selection == "Contact Us":
        st.header("Contact Us")
        st.markdown(
            """
            <style>
                div.stContactUs {
                    background-color: #9b59b6;
                    padding: 10px;
                    border-radius: 5px;
                    color: #ecf0f1;
                </style>
            </style>
            """,
            unsafe_allow_html=True
        )
        st.write("For more information, feel free to contact us:")

        st.write("Email: info@publichealth.com")
        st.write("Phone: 123-456-7890")

if __name__ == "__main__":
    main()
