import streamlit as st

st.set_page_config(page_title="AI 포트폴리오", layout="wide")
st.title("🖼️ 디자인 포트폴리오 갤러리")

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

st.markdown("**주의** 아래 작품들은 picsum 사이트에서 가져온 임의의 작품입니다. 실제 여러분의 작업물로 채워보세요.")
# 카테고리 선택
category = st.tabs(["전체", "로고 디자인", "웹 디자인", "영상 제작"])

# 샘플 데이터 (실제 이미지가 없으므로 플레이스홀더 사용)
def show_gallery(title):
    cols = st.columns(3)
    for i in range(3):
        with cols[i]:
            st.image(f"https://picsum.photos/400/300?random={title}{i}")
            st.subheader(f"{title} 작업물 {i+1}")
            with st.expander("상세 설명 보기"):
                st.write(f"이 작품은 {title} 카테고리의 대표 프로젝트입니다.")
                st.caption("사용한 도구: Photoshop, Figma, After Effects")

with category[0]:
    st.write("### 모든 작품")
    show_gallery("All")

with category[1]:
    st.write("### 로고 디자인")
    show_gallery("Logo")

with category[2]:
    st.write("### 웹 디자인")
    show_gallery("Web")

with category[3]:
    st.write("### 영상 제작")
    show_gallery("Video")

st.button("메인으로 돌아가기", on_click=lambda: st.switch_page("main.py"))