import streamlit as st
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import io
from utils import add_sidebar, set_common_style

# 페이지 설정
st.set_page_config(page_title="이미지 필터 | VCD Toolkit", layout="wide")

# 스타일 및 사이드바 적용
set_common_style()
add_sidebar()

st.markdown('<h1 class="main-title">📷 이미지 필터 스튜디오</h1>', unsafe_allow_html=True)
st.write("이미지를 업로드하고 다양한 필터를 적용해 보세요. 디자인 무드 보드 제작에 활용할 수 있습니다.")

# 파일 업로더
uploaded_file = st.file_uploader("🖼️ 처리할 이미지를 선택하세요 (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB") # 분석을 위해 RGB 변환
    
    # 🎨 컬러 테마 추출 섹션
    with st.container(border=True):
        st.subheader("🎨 이미지 컬러 팔레트 추출")
        
        from utils import extract_colors
        extracted_colors = extract_colors(img, num_colors=6)
        
        # 컬러 스와치 렌더링
        c_cols = st.columns(len(extracted_colors))
        for i, color in enumerate(extracted_colors):
            with c_cols[i]:
                st.markdown(f"""
                    <div style="background-color: {color}; height: 60px; border-radius: 10px; 
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 5px;"></div>
                    <code style="font-size: 0.8rem; display: block; text-align: center;">{color}</code>
                """, unsafe_allow_html=True)

    # 필터 제어 구역
    with st.container(border=True):
        st.subheader("✨ 필터 제어 & 미세 조정")
        
        ctrl_col1, ctrl_col2 = st.columns([1, 2])
        
        with ctrl_col1:
            filter_type = st.radio("기본 필터 선택", ["Original", "Grayscale", "Blur", "Sepia", "Vibrant"], index=0, horizontal=True)
        
        with ctrl_col2:
            s_col1, s_col2, s_col3 = st.columns(3)
            with s_col1:
                brightness = st.slider("밝기", 0.5, 2.0, 1.0)
            with s_col2:
                contrast = st.slider("대비", 0.5, 2.0, 1.0)
            with s_col3:
                if filter_type == "Blur":
                    blur_intensity = st.slider("블러 강도", 1, 20, 5)
                else:
                    st.write("") # 공간 맞춤용

    # 이미지 처리 로직
    filtered_img = img.copy()
    
    # 1. 기본 필터 적용
    if filter_type == "Grayscale":
        filtered_img = ImageOps.grayscale(img).convert("RGB")
    elif filter_type == "Blur":
        filtered_img = img.filter(ImageFilter.GaussianBlur(blur_intensity))
    elif filter_type == "Sepia":
        sepia_matrix = (
            0.393, 0.769, 0.189, 0,
            0.349, 0.686, 0.168, 0,
            0.272, 0.534, 0.131, 0
        )
        filtered_img = img.convert("RGB").convert("RGB", sepia_matrix)
    elif filter_type == "Vibrant":
        enhancer = ImageEnhance.Color(img)
        filtered_img = enhancer.enhance(2.0)

    # 2. 미세 조정 적용
    enhancer_bright = ImageEnhance.Brightness(filtered_img)
    filtered_img = enhancer_bright.enhance(brightness)
    enhancer_con = ImageEnhance.Contrast(filtered_img)
    filtered_img = enhancer_con.enhance(contrast)

    # UI 레이아웃
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.subheader("Original")
            st.image(img, use_container_width=True)
        
    with col2:
        with st.container(border=True):
            st.subheader(f"Filtered: {filter_type}")
            st.image(filtered_img, use_container_width=True)

    # 다운로드 섹션
    st.divider()
    buf = io.BytesIO()
    filtered_img.save(buf, format="PNG")
    st.download_button(
        label="📥 처리된 이미지 저장하기",
        data=buf.getvalue(),
        file_name=f"vcd_filtered_{filter_type.lower()}.png",
        mime="image/png",
        use_container_width=True
    )

else:
    st.markdown("""
        <div style="text-align: center; padding: 100px; background: #f8fafc; border: 2px dashed #cbd5e1; border-radius: 20px;">
            <h2 style="color: #64748b;">📷 파일 업로드를 기다리고 있습니다</h2>
            <p style="color: #94a3b8;">이미지를 선택하면 즉시 보정 도구가 활성화됩니다.</p>
        </div>
    """, unsafe_allow_html=True)