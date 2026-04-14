import streamlit as st
from utils import add_sidebar, set_common_style

# 페이지 설정
st.set_page_config(page_title="포트폴리오 | VCD Toolkit", layout="wide")

# 스타일 및 사이드바 적용
set_common_style()
add_sidebar()

st.markdown('<h1 class="main-title">🖼️ 디자인 포트폴리오 갤러리</h1>', unsafe_allow_html=True)
st.write("작업물을 카테고리별로 우아하게 분류하고 큐레이션하세요. 실제 이미지를 업로드하여 여러분만의 포트폴리오를 완성해 보세요.")

st.markdown("""
    <style>
    .category-label {
        font-size: 0.75rem;
        background: #f1f5f9;
        color: #475569;
        padding: 4px 10px;
        border-radius: 20px;
        width: fit-content;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 카테고리 탭 구성
tabs = st.tabs(["전체", "로고 디자인", "웹 UI", "브랜딩"])

def render_gallery(category_name, seed):
    cols = st.columns(3)
    project_names = [
        f"{category_name} 프로젝트 A", 
        f"{category_name} 프로젝트 B", 
        f"{category_name} 프로젝트 C"
    ]
    
    for i in range(3):
        with cols[i]:
            st.markdown(f'<div class="glass-card">', unsafe_allow_html=True)
            # 카테고리 라벨
            st.markdown(f'<div class="category-label">{category_name}</div>', unsafe_allow_html=True)
            # 이미지
            img_url = f"https://picsum.photos/600/400?random={seed}{i}"
            st.image(img_url, use_container_width=True)
            
            # 제목 및 설명
            st.subheader(project_names[i])
            with st.expander("프로젝트 개요"):
                st.write(f"이 작품은 {category_name}의 핵심 가치를 담은 결과물입니다. 사용자의 경험을 최우선으로 고려하여 디자인되었습니다.")
                st.caption("사용한 도구: Adobe CC, Figma, Cinema 4D")
            st.markdown('</div>', unsafe_allow_html=True)

with tabs[0]:
    st.write("### 🌐 모든 프로젝트")
    render_gallery("General", 10)

with tabs[1]:
    st.write("### 🏷️ 로고 & 아이덴티티")
    render_gallery("Logo", 20)

with tabs[2]:
    st.write("### 💻 웹 & 모바일 UI")
    render_gallery("WebUI", 30)

with tabs[3]:
    st.write("### 📦 브랜딩 패키지")
    render_gallery("Branding", 40)

st.divider()
st.info("🎨 **디자이너의 조언**: 포트폴리오는 단순히 결과물만 보여주는 것이 아니라, '어떤 문제를 어떻게 해결했는지' 과정을 보여주는 것이 중요합니다.")