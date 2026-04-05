import streamlit as st

# 페이지 설정: 화면을 넓게 쓰고 제목을 정합니다.
st.set_page_config(page_title="컬러 팔레트", layout="wide")

# 공통 사이드바 내비게이션
with st.sidebar:
    st.title("🎨 VCD Toolkit")
    st.caption("시각디자인 전공자를 위한 실무형 도구 모음")
    st.divider()
    st.markdown("### 🧭 내비게이션")
    st.page_link("main.py", label="홈 화면", icon="🏠")
    st.page_link("pages/01_color_palette.py", label="1. 컬러 팔레트", icon="🎨")
    st.page_link("pages/02_font_preview.py", label="2. 폰트 미리보기", icon="🔠")
    st.page_link("pages/03_filter.py", label="3. 이미지 필터", icon="📷")
    st.page_link("pages/04_data.py", label="4. 데이터 인포그래픽", icon="📊")
    st.page_link("pages/05_portfolio.py", label="5. AI 포트폴리오", icon="🖼️")
    st.divider()

st.title("🎨 컬러 팔레트 메이커")
st.write("슬라이더를 움직여 나만의 색상을 찾아보세요!")

# 3개의 슬라이더를 가로로 나란히 배치합니다. (Red, Green, Blue)
col1, col2, col3 = st.columns(3)
with col1:
    r = st.slider("빨강(Red)", 0, 255, 120)
with col2:
    g = st.slider("초록(Green)", 0, 255, 180)
with col3:
    b = st.slider("파랑(Blue)", 0, 255, 255)

# 선택한 RGB 값을 16진수 HEX 코드로 변환합니다.
hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()

# 결과 화면: 둥근 모서리와 그림자(box-shadow)가 들어간 컬러 박스를 만듭니다.
st.markdown(
    f"""
    <div style="background-color: {hex_color}; height: 300px; border-radius: 25px; 
    box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
    display: flex; align-items: center; justify-content: center; color: white; font-size: 30px;">
        <b style="text-shadow: 1px 1px 5px rgba(0,0,0,0.3);">{hex_color} <br> (RGB: {r}, {g}, {b})</b>
    </div>
    """, 
    unsafe_allow_html=True
)
st.button("메인으로 돌아가기", on_click=lambda: st.switch_page("main.py"))