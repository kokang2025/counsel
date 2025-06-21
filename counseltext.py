import streamlit as st
import urllib.parse

st.set_page_config(page_title="💬 맞춤 상담 챗봇 링크", layout="centered")

st.title("💬 상담 주제별 맞춤 챗봇 연결")
st.markdown("상담 주제를 선택하면, 해당 주제에 맞는 질문 문구가 포함된 링크를 안내합니다. 링크를 눌러 무료 챗봇에서 상담을 시작하세요!")

# 상담 주제와 맞춤 프롬프트
topics = {
    "진로 고민": "저는 앞으로 어떤 직업이 저에게 잘 맞을지 고민하고 있습니다. 조언을 부탁드려요.",
    "성격 분석": "제 성격을 이해하고 장단점을 분석해 주세요.",
    "학습 습관": "효율적인 공부 방법과 습관을 알고 싶습니다. 어떻게 하면 좋을까요?",
    "친구 관계": "친구와의 갈등이나 어려움을 어떻게 해결하면 좋을지 상담 받고 싶어요.",
    "가족 문제": "가족과의 갈등으로 고민이 많아요. 조언을 구하고 싶습니다.",
}

selected = st.selectbox("🧠 상담 주제를 선택하세요:", list(topics.keys()))
prompt = topics[selected]

st.info(f"💡 **추천 질문 예시:**\n\n> {prompt}")

st.markdown("---")

# 챗봇 링크 베이스 (예: ChatGPT 공식, 로그인 필요)
base_chatgpt_url = "https://chat.openai.com/"

# Hugging Face DialoGPT는 URL 파라미터 지원 안 해서 그냥 링크만 제공
chatbot_links = {
    "ChatGPT 공식 (로그인 필요)": base_chatgpt_url,
    "Hugging Face DialoGPT (영어)": "https://huggingface.co/spaces/microsoft/DialoGPT",
    "Yuntian Deng ChatGPT (한글 가능)": "https://huggingface.co/spaces/yuntian-deng/ChatGPT",
}

st.subheader("👉 아래에서 챗봇을 선택해 상담을 시작하세요!")

def make_chatgpt_url_with_prompt(base_url, prompt_text):
    # ChatGPT는 URL로 프롬프트 넘기는 기능 공식 지원 안 해서
    # 그냥 기본 링크만 열어줌
    return base_url

for name, url in chatbot_links.items():
    if st.button(f"{name} 열기"):
        final_url = url
        if "openai" in url:
            final_url = make_chatgpt_url_with_prompt(url, prompt)
        st.markdown(f"[{name} 바로가기]({final_url})", unsafe_allow_html=True)
        st.write("새 탭에서 열립니다.")

st.caption("💡 ChatGPT 공식 링크는 프롬프트를 URL에 포함하는 기능을 공식 지원하지 않습니다. 직접 질문을 복사해 붙여넣어 주세요.")
