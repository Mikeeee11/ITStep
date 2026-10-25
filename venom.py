import streamlit as st
st.title("моя первая страничка на Phyton!")
st.write("этот сайт был сделан при помощи Phyton")

user_name = st.text_input("Имя твоё?")
if st.button("назвать имя"):
    if user_name:
        st.success(f"ну привет, {user_name}, это типо мой сайт")
    else:
        st.warning("ало гараж, черкани своё имя!")

st.subheader("звгрузи своё фото")
upload_file = st.file_uploader("выбери свою фотку...", type=["png", "jpg", "jpeg"])
if upload_file is not None:
    st.image(upload_file, use_container_width=True)