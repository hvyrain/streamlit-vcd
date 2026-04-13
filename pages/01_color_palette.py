import streamlit as st
from utils import add_sidebar, set_common_style, get_contrast_ratio

# 페이지 설정
st.set_page_config(page_title="컬러 팔레트 | VCD Toolkit", layout="wide")

# 공통 테마 및 사이드바
set_common_style()
add_sidebar()

st.markdown('<h1 class="main-title">🎨 컬러 팔레트 & 대비 검사</h1>', unsafe_allow_html=True)
st.write("슬라이더를 움직여 디자인에 사용할 완벽한 색상을 찾아보고, 텍스트 가독성을 확인해 보세요.")

# 1. 메인 컬러 선택 구역
with st.container():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("📍 메인 컬러 설정")
    col1, col2, col3 = st.columns(3)
    with col1:
        r = st.slider("빨강 (Red)", 0, 255, 120, key="r_slider")
    with col2:
        g = st.slider("초록 (Green)", 0, 255, 180, key="g_slider")
    with col3:
        b = st.slider("파랑 (Blue)", 0, 255, 255, key="b_slider")
    
    hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
    
    st.markdown(
        f"""
        <div style="background-color: {hex_color}; height: 180px; border-radius: 20px; 
        box-shadow: 0px 10px 30px rgba(0,0,0,0.1); margin-top: 20px;
        display: flex; flex-direction: column; align-items: center; justify-content: center; color: white;">
            <h2 style="text-shadow: 1px 1px 10px rgba(0,0,0,0.2); margin:0;">{hex_color}</h2>
            <p style="text-shadow: 1px 1px 5px rgba(0,0,0,0.2); opacity: 0.9;">RGB({r}, {g}, {b})</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# 2. 대비비(Contrast) 검사 구역
st.divider()
col_bg, col_txt = st.columns(2)

with col_bg:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("👁️ 가독성(대비) 테스트")
    text_color = st.color_picker("텍스트 색상 선택", "#FFFFFF")
    
    contrast = get_contrast_ratio(hex_color, text_color)
    
    # WCAG 기준 판단
    if contrast >= 7:
        status = "✅ 매우 우수 (AAA)"
        color = "green"
    elif contrast >= 4.5:
        status = "⚠️ 양호 (AA)"
        color = "orange"
    else:
        status = "❌ 가독성 낮음"
        color = "red"
        
    st.markdown(f"### 대비비: <span style='color:{color};'>{contrast:.2f}:1</span>", unsafe_allow_html=True)
    st.markdown(f"**결과:** {status}")
    
    # 미리보기 박스
    st.markdown(f"""
        <div style="background-color: {hex_color}; color: {text_color}; padding: 30px; border-radius: 15px; border: 1px solid #ddd; margin-top: 15px;">
            <h3 style="color: {text_color}; margin-top:0;">디자인 가독성 테스트</h3>
            <p>이 텍스트가 잘 보이나요? 배경색과 글자색의 대비가 높을수록 사용자가 정보를 파악하기 쉬워집니다.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_txt:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("💡 디자인 팁")
    st.info("""
    - **가독성 원칙**: 배경과 텍스트의 대비비는 최소 4.5:1 이상(AA 등급)을 권장합니다.
    - **색상 감정**: 파란색은 신뢰를, 주황색은 활력을 줍니다.
    - **브랜딩**: 브랜드의 핵심 색상을 정하고, 2~3개의 보조 색상을 조합해 보세요.
    """)
    st.success(f"현재 선택된 **{hex_color}** 색상은 디지털 인터페이스에서 청량감을 주는 포인트 컬러로 좋습니다.")
    st.markdown('</div>', unsafe_allow_html=True)