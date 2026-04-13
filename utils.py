import streamlit as st
from PIL import Image

def set_common_style():
    """
    공통 디자인 시스템 스타일을 입힙니다.
    """
    st.markdown("""
        <style>
        /* 메인 배경색 및 폰트 설정 */
        @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Pretendard', sans-serif;
        }

        /* 유리 효과 카드 디자인 */
        .glass-card {
            background: rgba(255, 255, 255, 0.7);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            margin-bottom: 20px;
            transition: transform 0.3s ease;
        }
        
        .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.12);
        }

        /* 버튼 프리미엄 스타일 */
        .stButton>button {
            border-radius: 12px;
            padding: 10px 24px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        /* Streamlit 컨테이너 보더 스타일을 glass-card 느낌으로 변경 */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(255, 255, 255, 0.7);
            border-radius: 20px !important;
            padding: 20px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(255, 255, 255, 0.18) !important;
            margin-bottom: 20px;
        }

        /* 헤더 스타일링 */
        .main-title {
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(90deg, #6366f1, #a855f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

def add_sidebar():
    """
    모든 페이지에서 보여지는 공통 사이드바 내비게이션입니다.
    """
    with st.sidebar:
        # 상단 로고 추가
        st.image("data/yasu-logo.png", use_container_width=True)
        
        st.title("🎨 VCD Toolkit")
        st.caption("시각디자인 전공자를 위한 프리미엄 도구")
        st.divider()

        st.markdown("### 🧭 내비게이션")
        st.page_link("main.py", label="홈 화면", icon="🏠")
        st.page_link("pages/01_color_palette.py", label="1. 컬러 팔레트", icon="🎨")
        st.page_link("pages/02_font_preview.py", label="2. 폰트 미리보기", icon="🔠")
        st.page_link("pages/03_filter.py", label="3. 이미지 필터", icon="📷")
        st.page_link("pages/04_data.py", label="4. 데이터 인포그래픽", icon="📊")
        st.page_link("pages/05_portfolio.py", label="5. AI 포트폴리오", icon="🖼️")

        st.divider()
        st.info("""
        **VCD Toolkit Guide**  
        이 대시보드는 용인예술과학대학교 시각디자인과 학생들을 위한 샘플 앱으로 제작되었습니다. 피드백이 있다면 언제든 알려주세요!
        """)
        
        # 메인으로 돌아가기 버튼 (사이드바 하단 고정 느낌)
        if st.button("↩️ 메인 홈으로", use_container_width=True):
            st.switch_page("main.py")

def get_contrast_ratio(hex1, hex2):
    """
    두 색상의 대비비를 계산합니다. (단순화된 버전)
    """
    def luminance(hex_color):
        hex_color = hex_color.lstrip('#')
        rgb = [int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
        rgb = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
        return 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]
    
    lum1 = luminance(hex1)
    lum2 = luminance(hex2)
    
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    
    return (lighter + 0.05) / (darker + 0.05)

def extract_colors(image, num_colors=5):
    """
    이미지에서 주요 색상을 추출하여 HEX 코드 리스트로 반환합니다.
    """
    # 속도를 위해 이미지 축소
    img = image.copy()
    img.thumbnail((100, 100))
    
    # 팔레트 양자화 (Pillow built-in)
    paletted = img.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    
    colors = []
    for count, index in color_counts[:num_colors]:
        r = palette[index*3]
        g = palette[index*3+1]
        b = palette[index*3+2]
        hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
        colors.append(hex_color)
    
    return colors
