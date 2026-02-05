import streamlit as st


st.title("Моето първо приложение")

name = st.text_input("Как се казваш?")

if name:
    st.success(f"Здравей, {name}! Радвам се да те видя тук.")

    st.divider()

    st.subheader("Време е за малък тест!")
    answer = st.number_input(
        "Колко е 5 × 5?",
        step=1,
        value=0
    )

    if st.button("Провери"):
        if answer == 25:
            st.success("Вярно! Ти си математик!")
            st.balloons()
        else:
            st.error("Грешно. Опитай пак.")
