import streamlit as st

st.title('나의 첫 웹 서비스 만들기!!')
name = st.text_input('이름을 입력하세요 : ')
menu = st.selectbox('가장 많이 스는 앱은? : ', ['카카오톡','네이버', '구글'])
time = st.slider('하루 사용 시간은?', 0, 12, 3)
if st.button('나의 디지털 습관') : 
    st.write(f'{name}님! {menu}를 {time}시간 동안 사용합니다')
    st.balloons()
