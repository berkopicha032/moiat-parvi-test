import streamlit as st


st.title("Моето първо приложение")


name = st.text_input("Как се казваш?")


if name:
    st.success(f"Здравей, {name}!") 
    
    st.write("---") 
    
   
    st.subheader("Малък тест за теб:")
    answer = st.number_input("Колко е 5 × 5?", step=1, value=0)
    
 
    if st.button("Провери"):
        if answer == 25:
            st.success("Точно така! Браво! 🎉")
            st.balloons()
        else:
            st.error("Хмм, не е това. Опитай пак! 🧐")
