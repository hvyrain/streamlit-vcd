import streamlit as st
import html
from utils import add_sidebar, set_common_style

# 페이지 설정
st.set_page_config(page_title="폰트 미리보기 | VCD Toolkit", layout="wide")

# 스타일 및 사이드바 적용
set_common_style()
add_sidebar()

st.markdown('<h1 class="main-title">🔠 타이포그래피 스튜디오</h1>', unsafe_allow_html=True)
st.write("다양한 폰트를 실시간으로 비교하고, 프로젝트의 인상에 가장 잘 어울리는 스타일을 선택하세요.")

# 사이드바 설정 강화
with st.sidebar:
    st.header("🎛️ 타이포 옵션")
    user_text = st.text_area("테스트 문구 입력", "디자인은 문제를 해결하는 과정이자 아름다움을 찾는 여정입니다.")
    font_size = st.slider("글자 크기", 10, 120, 48)
    letter_spacing = st.slider("자간 (px)", -10, 30, 0)
    font_weight = st.selectbox("폰트 두께", ["Regular", "Bold", "Black"], index=1)
    
    weight_map = {"Regular": 400, "Bold": 700, "Black": 900}
    weight_val = weight_map[font_weight]

# 사용자 입력은 HTML에 삽입되므로 escape 처리
safe_user_text = html.escape(user_text).replace("\n", "<br/>")

# 구글 폰트 주입
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&family=Noto+Serif+KR:wght@400;700;900&family=Nanum+Pen+Script&family=Black+Han+Sans&family=Dongle:wght@400;700&family=Gamja+Flower&family=Song+Myung&family=Bagel+Fat+One&display=swap');
    
    .specimen-card {{
        background: white;
        padding: 40px;
        border-radius: 20px;
        border: 1px solid #eee;
        margin-bottom: 30px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }}
    .font-label {{
        color: #6366f1;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 0.8rem;
        margin-bottom: 15px;
        display: block;
    }}
    .font-preview {{
        font-size: {font_size}px;
        letter-spacing: {letter_spacing}px;
        font-weight: {weight_val};
        line-height: 1.3;
        word-break: keep-all;
    }}
    </style>
""", unsafe_allow_html=True)

# 폰트 리스트
fonts = [
    {"name": "Noto Sans KR (Gothic)", "family": "'Noto Sans KR', sans-serif"},
    {"name": "Noto Serif KR (Myeongjo)", "family": "'Noto Serif KR', serif"},
    {"name": "Black Han Sans (Impact)", "family": "'Black Han Sans', sans-serif"},
    {"name": "Song Myung (Classic Serif)", "family": "'Song Myung', serif"},
    {"name": "Nanum Pen Script (Handwriting)", "family": "'Nanum Pen Script', cursive"},
    {"name": "Bagel Fat One (Display)", "family": "'Bagel Fat One', display"},
    {"name": "Dongle (Cute & Rounded)", "family": "'Dongle', sans-serif"},
]

# 2열 그리드로 렌더링
col1, col2 = st.columns(2)

for i, f in enumerate(fonts):
    target_col = col1 if i % 2 == 0 else col2
    with target_col:
        st.markdown(f"""
            <div class="specimen-card">
                <span class="font-label">{f['name']}</span>
                <div class="font-preview" style="font-family: {f['family']};">
                    {safe_user_text}
                </div>
            </div>
        """, unsafe_allow_html=True)

st.success("💡 Tip: 제목용 폰트는 두껍고 개성 있는 서체를, 본문용 폰트는 가독성이 좋은 산세리프(고딕) 서체를 추천합니다.")