import streamlit as st

st.title("Моето първо приложение")

name = st.text_input("Как се казваш?")

if name:
     st.success(f"Здравей, {name}! 👋")
    
    st.write("---")

    answer = st.number_input("Колко е 5 × 5?", step=1, value=0)
    
    if st.button("Провери"):
        if answer == 25:
            st.success("Вярно! 🎉")
            st.balloons()
        else:
            st.error("Грешно. Опитай пак!")
