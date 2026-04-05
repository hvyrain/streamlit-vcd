import streamlit as st

# 1. 페이지 설정 (넓게 보기)
st.set_page_config(
    page_title="디자인과 Streamlit 쇼케이스", 
    layout="wide",
    initial_sidebar_state="expanded"  # 사이드바를 기본적으로 펼침 상태로 설정
)

# 사이드바 구성 추가
with st.sidebar:
    st.title("🎨 VCD Toolkit")
    st.caption("시각디자인 전공자를 위한 실무형 도구 모음")
    st.divider()

    st.markdown("### 🧭 내비게이션")
    # st.page_link를 사용하여 사이드바에 직관적인 메뉴를 구성합니다.
    # 경로가 정확해야 하며, pages/ 폴더 내의 파일명과 일치해야 합니다.
    st.page_link("main.py", label="홈 화면", icon="🏠")
    st.page_link("pages/01_color_palette.py", label="1. 컬러 팔레트", icon="🎨")
    st.page_link("pages/02_font_preview.py", label="2. 폰트 미리보기", icon="🔠")
    st.page_link("pages/03_filter.py", label="3. 이미지 필터", icon="📷")
    st.page_link("pages/04_data.py", label="4. 데이터 인포그래픽", icon="📊")
    st.page_link("pages/05_portfolio.py", label="5. AI 포트폴리오", icon="🖼️")

    st.divider()
    st.info("""
    **디자인 가이드**  
    이 툴킷은 디자인 프로세스를 돕기 위해 제작되었습니다. 왼쪽 메뉴를 통해 도구를 자유롭게 전환하세요!
    """)

# 2. 메인 타이틀 디자인
st.title("🚀 시각디자인 + Streamlit")
st.subheader("디자이너를 위한 5가지 마법 도구 샘플")
st.markdown("이 샘플은 **시각디자인과 학생**들의 `streamlit`을 활용한 UI 디자인과 데이터 시각화에 대한 이해를 돕기 위해 **서대우 교수**가 AI를 활용하여 제작하였습니다.")
st.write("왼쪽 사이드바의 메뉴를 클릭하거나, 아래 카드를 보고 원하는 도구를 선택해 보세요!")

st.divider() # 구분선

# 3. 5개 프로젝트 소개 (3컬럼 그리드 배치로 변경하여 균형 조절)
col1, col2, col3 = st.columns(3)

with col1:
    st.info("### 🎨 1. 컬러")
    st.write("슬라이더로 HEX 코드를 실시간 생성하는 기초 도구")
    if st.button("컬러 팔레트 구경하기", key="btn1"):
        st.switch_page("pages/01_color_palette.py")

    st.success("### 🔠 2. 폰트")
    st.write("구글 폰트를 적용해 타이포그래피를 비교하는 웹")
    if st.button("폰트 미리보기 구경하기", key="btn2"):
        st.switch_page("pages/02_font_preview.py")

with col2:
    st.warning("### 📷 3. 필터")
    st.write("사진을 올리고 필터를 적용해 보는 변환기")
    if st.button("이미지 필터 구경하기", key="btn3"):
        st.switch_page("pages/03_filter.py")

    st.error("### 📊 4. 데이터")
    st.write("수치를 예쁜 그래프로 바꿔주는 대시보드")
    if st.button("인포그래픽 구경하기", key="btn4"):
        st.switch_page("pages/04_data.py")

with col3:
    st.warning("### 🖼️ 5. 포트폴리오")
    st.write("작업물을 카테고리별로 모아보는 갤러리")
    if st.button("포트폴리오 구경하기", key="btn5"):
        st.switch_page("pages/05_portfolio.py")

    st.warning("### 🖼️ Info")
    st.write("시각디자인과 학생들을 위한 샘플입니다.")
    st.write("각 페이지에서 '메인으로 돌아가기' 버튼을 눌러 언제든지 이 화면으로 돌아올 수 있습니다.")
