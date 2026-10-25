import streamlit as st

st.title("ну крч цельсии фаренгейты, пук пук короче")
st.write("переводим цельсии на язык омерики")

st.number_input(
    "черкани сюда цельсии"
    min_value = -273.15
    max_value = 1000.0
    value = 25.0
    step = 1.0
)

if st.number_input == "Числовое поле":
    result = celsius * 9 / 5 + 32
else:
    result = temperature * 9 / 5 + 32

st.success(f"Результат: {result:.2f} °F")