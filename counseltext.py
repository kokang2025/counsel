import streamlit as st

# 페이지 설정
st.set_page_config(page_title="💬 무료 GPT 상담 챗봇", layout="centered")

# 타이틀
st.title("💬 무료 GPT 상담 챗봇")
st.markdown("""
학생 여러분, 고민이 있나요?  
지금 이 챗봇과 함께 **진로, 성격, 친구, 공부, 가족 문제**에 대해 상담해보세요.  
**무료이고, 설치가 필요 없으며**, 여러분의 고민을 친절하게 들어줄 거예요.  
""")

# 상담 주제
topics = {
    "진로 고민": "앞으로 어떤 직업을 가져야 할지 고민되고 방향이 잡히지 않을 때.",
    "성격 분석": "내 성격에 대한 이해를 돕고 장단점을 파악하고 싶을 때.",
    "학습 습관": "공부가 잘 안되거나 더 효과적인 방법을 찾고 싶을 때.",
    "친구 관계": "친구와의 갈등이나 어색한 상황을 해결하고 싶을 때.",
    "가족 문제": "가족과의 갈등이나 고민을 털어놓고 싶을 때."
}

# 상담 주제 선택
selected_topic = st.selectbox("🧠 상담하고 싶은 주제를 선택하세요:", list(topics.keys()))

# 주제에 대한 설명 출력
if selected_topic:
    st.markdown(f"### 📝 {selected_topic}")
    st.info(topics[selected_topic])

# 구분선
st.markdown("---")

# 챗봇 설명
st.subheader("🤖 아래 챗봇에게 질문해보세요!")
st.markdown("""
**예시 질문**:  
- "공부가 잘 안돼요. 어떻게 해야 집중할 수 있을까요?"  
- "저는 내성적인 편인데, 친구 사귀는 방법이 궁금해요."  
- "성격이 너무 급한데, 고칠 수 있을까요?"  

**Tip**: 챗봇은 한국어도 잘 알아들어요!
""")

# Hugging Face 챗봇 iframe (영구 무료)
st.components.v1.iframe("https://huggingface.co/spaces/yuntian-deng/ChatGPT", height=600)

# 푸터
st.markdown("---")
st.caption("🧡 Made with Streamlit + Hugging Face | 설치 없이 누구나 무료로 사용할 수 있어요.")
