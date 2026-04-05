import streamlit as st

st.set_page_config(page_title="폰트 미리보기", layout="wide")

st.title("🔠 타이포그래피 미리보기")
st.write("디자인에 어울리는 구글 폰트를 테스트해 보세요.")

# 사이드바에서 텍스트 속성 조절
with st.sidebar:
    st.title("🎨 VCD Toolkit")
    st.divider()
    st.markdown("### 🧭 내비게이션")
    st.page_link("main.py", label="홈 화면", icon="🏠")
    st.page_link("pages/01_color_palette.py", label="1. 컬러 팔레트", icon="🎨")
    st.page_link("pages/02_font_preview.py", label="2. 폰트 미리보기", icon="🔠")
    st.page_link("pages/03_filter.py", label="3. 이미지 필터", icon="📷")
    st.page_link("pages/04_data.py", label="4. 데이터 인포그래픽", icon="📊")
    st.page_link("pages/05_portfolio.py", label="5. AI 포트폴리오", icon="🖼️")
    st.divider()
    
    st.header("설정")
    user_text = st.text_input("테스트 문구 입력", "용인예술과학대학교 학생들의 학생 성공을 기원합니다.")
    font_size = st.slider("글자 크기", 10, 100, 40)
    letter_spacing = st.slider("자간 (px)", -5, 20, 0)

# 구글 폰트 불러오기 및 스타일 정의
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700&family=Noto+Serif+KR:wght@700&family=Nanum+Pen+Script&family=Black+Han+Sans&family=Dongle&family=Gamja+Flower&family=Song+Myung&family=Dokdo&family=Bagel+Fat+One&display=swap');
    .font-card {{
        padding: 20px; border-radius: 15px; border: 1px solid #eee; margin-bottom: 20px;
        background: white; box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }}
    .preview-text {{
        font-size: {font_size}px;
        letter-spacing: {letter_spacing}px;
        line-height: 1.2;
    }}
    </style>
    """, unsafe_allow_html=True)

# 폰트별 카드 출력
fonts = [
    {"name": "Noto Sans Korean (고딕)", "family": "'Noto Sans KR', sans-serif"},
    {"name": "Noto Serif Korean (명조)", "family": "'Noto Serif KR', serif"},
    {"name": "Nanum Pen Script (손글씨)", "family": "'Nanum Pen Script', cursive"},
    {"name": "Black Han Sans (검은고딕)", "family": "'Black Han Sans', sans-serif"},
    {"name": "Dongle (동글)", "family": "'Dongle', sans-serif"},
    {"name": "Gamja Flower (감자꽃)", "family": "'Gamja Flower', display"},
    {"name": "Song Myung (송명)", "family": "'Song Myung', serif"},
    {"name": "Dokdo (독도)", "family": "'Dokdo', display"},
    {"name": "Bagel Fat One (베이글)", "family": "'Bagel Fat One', system-ui"}
]

for f in fonts:
    st.markdown(f"""
        <div class="font-card">
            <small style="color: gray;">{f['name']}</small>
            <div class="preview-text" style="font-family: {f['family']};">
                {user_text}
            </div>
        </div>
    """, unsafe_allow_html=True)

if st.button("메인으로 돌아가기"):
    st.switch_page("main.py")