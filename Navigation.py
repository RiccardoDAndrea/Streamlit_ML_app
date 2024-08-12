## streamlit run 1_Home.py
import streamlit as st 


Home = st.Page(
    "navigation/1_Home.py",
    title="Home",
    icon=":material/home:")

Linear_Regression = st.Page(
    "navigation/2_🤖_Machine_Learning.py",
    title="Linear Regression",
    icon=":material/data_exploration:",
)

Stock_Dashboard = st.Page(
    "navigation/3_📈_Stock_Dashboard.py",
    title="Stocks Dashboard",
    icon=":material/dashboard:",
)

Explore_the_power_of_rnns = st.Page(
    "navigation/4_🤖_Recurrent_Neural_Network.py",
    title="Recurent Neural Network",
    icon=":material/smart_toy:",
)

face_detection = st.Page(
    "navigation/face_detection.py",
    title="Face Recognition",
    icon=":material/familiar_face_and_zone:",
)

Contact = st.Page(
    "navigation/5_🤵‍♂️_Contact.py",
    title="Contact",
    icon=":material/contacts_product:",
)


pg = st.navigation(
    {
        "Home": [Home],
        "Projects": [Linear_Regression, Stock_Dashboard,Explore_the_power_of_rnns, face_detection],
        "Info": [Contact],
    }
)


pg.run()