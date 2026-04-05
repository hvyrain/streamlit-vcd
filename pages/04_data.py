import streamlit as st
import pandas as pd

st.set_page_config(page_title="데이터 인포그래픽", layout="wide")
st.title("📊 디자인 트렌드 인포그래픽")

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

# 샘플 데이터 생성
data = {
    "디자인 키워드": ["미니멀리즘", "3D 일러스트", "레트로", "다크모드", "뉴모피즘"],
    "선호도(%)": [45, 25, 15, 10, 5]
}
df = pd.DataFrame(data)

st.write("2024년 가장 주목받는 디자인 스타일 트렌드 조사 결과입니다.")

col1, col2 = st.columns([1, 2])
with col1:
    st.write("### 📋 데이터 표")
    st.table(df)

with col2:
    st.write("### 📈 선호도 차트")
    # 막대 그래프 출력 (파스텔 느낌은 테마에서 조절 가능)
    st.bar_chart(df.set_index("디자인 키워드"))

st.success("데이터를 시각화하면 복잡한 수치도 한눈에 파악할 수 있습니다!")

if st.button("메인으로 돌아가기"):
    st.switch_page("main.py")