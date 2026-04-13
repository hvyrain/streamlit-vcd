import streamlit as st
from utils import add_sidebar, set_common_style

# 1. 페이지 설정
st.set_page_config(
    page_title="VCD Toolkit | 스튜디오", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 공통 스타일 및 사이드바 적용
set_common_style()
add_sidebar()

# 2. 메인 타이틀 디자인
st.markdown('<h1 class="main-title">🚀 VCD Studio Toolkit</h1>', unsafe_allow_html=True)
st.subheader("디자이너를 위한 5가지 도구 세트")
st.markdown("""
이 대시보드는 **용인예술과학대학교 시각디자인과** 학생들이 데이터와 디지털 기술을 활용해 창의적인 결과물을 낼 수 있도록 돕는 **AI 기반의 워크스페이스**입니다. 원하는 도구를 선택하여 작업 효율을 극대화해 보세요!     
>용인예술과학대학교 **서대우 교수**
""")

st.divider()

# 3. 도구 카드 렌더링 함수
def render_tool_card(title, description, page_path, icon, color_class):
    with st.container():
        st.markdown(f"""
            <div class="glass-card">
                <div style="font-size: 2rem; margin-bottom: 15px;">{icon}</div>
                <h3 style="margin: 0; padding: 0;">{title}</h3>
                <p style="color: #666; font-size: 0.9rem; margin: 15px 0;">{description}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"{title} 구경하기", key=f"btn_{page_path}", use_container_width=True):
            st.switch_page(page_path)

# 4. 그리드 배치
col1, col2, col3 = st.columns(3)

with col1:
    render_tool_card(
        "컬러 팔레트", 
        "실시간 RGB/HEX 변환 및 디자인 명도 대비(Contrast)를 확인하는 컬러 마법사",
        "pages/01_color_palette.py", "🎨", "info"
    )
    render_tool_card(
        "폰트 미리보기", 
        "타이포그래피의 인상과 가독성을 구글 폰트 시스템으로 즉시 테스트",
        "pages/02_font_preview.py", "🔠", "success"
    )

with col2:
    render_tool_card(
        "이미지 필터", 
        "Pillow 기반의 고급 필터링으로 사진의 톤과 분위기를 즉시 변환",
        "pages/03_filter.py", "📷", "warning"
    )
    render_tool_card(
        "인포그래픽", 
        "데이터를 직관적이고 아름다운 파스텔 톤의 대화형 차트로 시각화",
        "pages/04_data.py", "📊", "error"
    )

with col3:
    render_tool_card(
        "AI 포트폴리오", 
        "여러분의 창작물을 카테고리별로 우아하게 정리하는 갤러리 큐레이션",
        "pages/05_portfolio.py", "🖼️", "warning"
    )
    
    # 추가 안내 카드
    st.markdown("""
        <div class="glass-card" style="background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white;">
            <h3>✨ 학생 성공 가이드</h3>
            <p style="color: rgba(255,255,255,0.9); font-size: 0.85rem;">
                용인예술과학대학교 시각디자인과 학생들의 성공을 기원합니다. 각 도구에는 실무 디자인 팁이 포함되어 있습니다.
            </p>
        </div>
    """, unsafe_allow_html=True)
