import streamlit as st
import random

# 1. 추천 메뉴 리스트 정의
# 메뉴 리스트를 딕셔너리로 정의하여 나중에 카테고리 확장을 대비할 수 있습니다.
menu_list = [
    "김치찌개 🍲", "된장찌개 🥘", "비빔밥 🥗", "제육볶음 🍖", 
    "짜장면 🍜", "짬뽕 🌶️", "탕수육 🥡", "볶음밥 🍚",
    "파스타 🍝", "피자 🍕", "샐러드 🥗", "햄버거 🍔",
    "쌀국수 🍜", "닭갈비 🐔"
]

st.set_page_config(layout="centered", page_title="오늘의 점심 메뉴 추천")

## 앱 제목 및 설명
st.title("🍽️ 점심 메뉴 랜덤 추천기")
st.write("버튼을 누르면 메뉴 리스트에서 하나를 무작위로 추천해 드립니다. 오늘 점심 고민은 이제 끝!")

# 2. 메뉴 추천 로직 구현
if 'recommended_menu' not in st.session_state:
    # 세션 상태에 저장된 메뉴가 없으면 초기 문구를 설정합니다.
    st.session_state.recommended_menu = "버튼을 눌러 추천받으세요!"

def recommend_menu():
    """메뉴 리스트에서 무작위로 하나를 선택하여 세션 상태에 저장합니다."""
    # random.choice() 함수로 메뉴를 선택합니다.
    selected_menu = random.choice(menu_list)
    # 선택된 메뉴를 Streamlit의 세션 상태(Session State)에 저장합니다.
    st.session_state.recommended_menu = selected_menu
    # 애니메이션 효과를 위한 부스터
    st.balloons()


# 3. 사용자 인터페이스 (UI) 구성
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    # 추천 결과를 표시하는 박스
    st.subheader("오늘의 추천 메뉴:")
    st.markdown(
        f"""
        <div style="background-color: #fff3e0; border: 3px dashed #ff9800; padding: 25px; border-radius: 8px; text-align: center;">
            <p style='font-size: 2.5em; font-weight: bold; color: #e65100; margin: 0;'>
                {st.session_state.recommended_menu}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 메뉴 추천 버튼
    st.markdown("---")
    st.button(
        "✨ 메뉴 추천받기", 
        on_click=recommend_menu, 
        use_container_width=True,
        type="primary"
    )

st.markdown("---")
st.caption(f"현재 메뉴 목록에 등록된 메뉴 수: **{len(menu_list)}개**")
