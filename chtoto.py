import streamlit as st

st.set_page_config(page_title="файлы МИХАИЛштейна", page_icon="кобачков.jpg",
                   layout="wide")

st.title("это приложуха для просмотров файлов МИХАИЛА!!!!!")

tab1, tab2 = st.tabs(["оправдывание персов", "хз что"])

with tab1:
    st.header("персы")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("гаврюша.jpg", caption="ГАВРЮША НИКОГО НЕ УБИВАЛ, ОН БЫЛ В МАКЕ И КУШАЛ, БУРГЕРЫ!!!", width=400)
    with col2:
        st.image("ДОБРІЇ МІСТЕР МУЖЧІНА.jpg", caption="филилетовый чилавек никого ТОЖЕ не убивал, он здох в своём костюме", width=400)
        with st.container():
            st.error("ЕСЛИ ЕСТЬ У ВАС ДРУГРИЕ ПРУФЫ, СТРОЧИТЬ СЮДА:")
            st.markdown("- Email: naebal.loxov@gmail.com")

with tab2:
    st.info("вкладка в командировке")