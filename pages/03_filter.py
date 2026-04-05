import streamlit as st
from PIL import Image, ImageFilter, ImageOps
import io

st.set_page_config(page_title="이미지 필터", layout="wide")
st.title("📷 이미지 필터 스튜디오")

# 공통 사이드바 내비게이션 (파일 업로드 여부와 상관없이 항상 표시되도록 위로 이동)
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

# 파일 업로더
uploaded_file = st.file_uploader("이미지를 업로드하세요 (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)

    st.sidebar.header("필터 선택")
    filter_type = st.sidebar.radio("필터", ["Original", "Grayscale (흑백)", "Blur (블러)", "Sepia (세피아)"])
    
    # 필터 적용 로직
    filtered_img = img.copy()
    if filter_type == "Grayscale (흑백)":
        filtered_img = ImageOps.grayscale(img)
    elif filter_type == "Blur (블러)":
        filtered_img = img.filter(ImageFilter.GaussianBlur(5))
    elif filter_type == "Sepia (세피아)":
        # 세피아 톤 계산 매트릭스
        sepia_matrix = (
            0.393, 0.769, 0.189, 0,
            0.349, 0.686, 0.168, 0,
            0.272, 0.534, 0.131, 0
        )
        filtered_img = img.convert("RGB").convert("RGB", sepia_matrix)

    # Before / After 비교 레이아웃
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Before")
        st.image(img, use_container_width=True)
    with col2:
        st.subheader("After")
        st.image(filtered_img, use_container_width=True)

    # 다운로드 버튼
    buf = io.BytesIO()
    filtered_img.save(buf, format="PNG")
    st.download_button("결과 이미지 저장하기", buf.getvalue(), "filtered_image.png", "image/png")

else:
    st.info("왼쪽 상단에서 이미지를 업로드해 주세요.")

if st.button("메인으로 돌아가기"):
    st.switch_page("main.py")