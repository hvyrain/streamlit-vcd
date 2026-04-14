import streamlit as st
import pandas as pd
import plotly.express as px
from utils import add_sidebar, set_common_style

# 페이지 설정
st.set_page_config(page_title="인포그래픽 | VCD Toolkit", layout="wide")

# 스타일 및 사이드바 적용
set_common_style()
add_sidebar()

st.markdown('<h1 class="main-title">📊 디자인 트렌드 인포그래픽</h1>', unsafe_allow_html=True)
st.write("2024년 디자인 트렌드 선호도 수치를 시각화한 대시보드입니다. 차트의 요소를 클릭하거나 호버하여 상세 데이터를 확인하세요.")

# 차트 색상 (파스텔 테마)
colors = ['#FFC1CC', '#B0E0E6', '#F0E68C', '#E6E6FA', '#98FB98', '#FFDAB9']

# 샘플 데이터 생성 (캐싱)
@st.cache_data(show_spinner=False)
def get_sample_df() -> pd.DataFrame:
    data = {
        "디자인 키워드": ["미니멀리즘", "3D 일러스트", "레트로", "다크모드", "뉴모피즘", "AI 아트"],
        "선호도(%)": [40, 25, 15, 10, 5, 5],
        "성장률": ["+12%", "+20%", "+5%", "+2%", "-3%", "+300%"],
    }
    return pd.DataFrame(data)

df = get_sample_df()

# 레이아웃 구성
col1, col2 = st.columns([1, 1.5])

with col1:
    with st.container(border=True):
        st.subheader("📋 트렌드 순위표")
        # 표 디자인 개선
        st.dataframe(
            df, 
            column_config={
                "선호도(%)": st.column_config.ProgressColumn(format="%d%%", min_value=0, max_value=50),
                "성장률": st.column_config.TextColumn("전년 대비")
            },
            use_container_width=True,
            hide_index=True
        )
    
    st.info("""
    💡 **2024 디자인 트렌드 분석**  
    현재 시장은 **미니멀리즘**이 40%의 점유율로 가장 견고한 베이스를 형성하고 있습니다. 
    주목할 점은 **AI 아트**의 폭발적인 성장률(+300%)과 **3D 일러스트**의 약진(+20%)입니다. 
    이는 기초적인 형태는 단순화하되, 제작 방식은 AI와 3D 기술을 적극 활용하는 하이테크 디자인이 주류가 될 것임을 시사합니다.
    """)

with col2:
    with st.container(border=True):
        st.subheader("📈 인터랙티브 선호도 분석")
        
        # Plotly 파이 차트 생성
        fig = px.pie(
            df, 
            values='선호도(%)', 
            names='디자인 키워드',
            color_discrete_sequence=colors,
            hole=0.4
        )
        
        fig.update_layout(
            margin=dict(t=0, b=0, l=0, r=0),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            font=dict(family="Pretendard", size=14)
        )
        
        st.plotly_chart(fig, use_container_width=True)

st.success("데이터 시각화는 정보를 단순히 전달하는 것을 넘어, 보는 이의 감성까지 움직일 수 있는 강력한 도구입니다.")