import streamlit as st

def main():
    st.title("Public Health Website")

    st.header("Welcome to our Public Health Portal")
    st.write("This website provides information about public health, diseases, and prevention measures.")

    st.header("Latest News")
    st.write("Stay updated with the latest news and developments in public health.")

    # Add a checkbox for showing/hiding the latest news
    show_news = st.checkbox("Show Latest News")
    if show_news:
        st.write("1. New Study on Vaccine Efficacy")
        st.write("2. Tips for Staying Healthy During Flu Season")
        st.write("3. Community Outreach Programs")

    st.header("Disease Information")
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

    st.header("Prevention Tips")
    st.write("Follow these tips to maintain good health and prevent diseases:")

    st.markdown("""
        - Wash hands regularly with soap and water.
        - Eat a balanced diet rich in fruits and vegetables.
        - Exercise regularly to stay physically active.
        - Stay hydrated by drinking plenty of water.
        - Get enough sleep to support overall well-being.
    """)

    st.header("Contact Us")
    st.write("For more information, feel free to contact us:")

    st.write("Email: info@publichealth.com")
    st.write("Phone: 123-456-7890")

if __name__ == "__main__":
    main()


