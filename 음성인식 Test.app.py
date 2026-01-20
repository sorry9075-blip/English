import streamlit as st
from streamlit_mic_recorder import mic_recorder, speech_to_text

st.title("🛡️ 서원고 어법 DNA: 스피킹 테스트")
st.write("마이크 버튼을 누르고 아래 문장을 읽어보세요!")

# 1. 문제 설정
target_sentence = "The books lying on the table are mine"
st.info(f"📋 따라 읽을 문장: {target_sentence}")

# 2. 음성 인식 부품 (Google STT 엔진 사용)
# 따로 설정 안 해도 이 부품이 알아서 목소리를 텍스트로 변환해줍니다.
text = speech_to_text(
    start_prompt="🎤 녹음 시작",
    stop_prompt="⏹️ 녹음 완료",
    language='en', # 영어 인식
    use_container_width=True,
    key='STT'
)

# 3. 정답 판독 로직
if text:
    st.write(f"📢 내가 읽은 내용: {text}")
    
    # 대소문자 무시하고 마침표 빼고 순수하게 글자만 비교
    if target_sentence.lower() in text.lower():
        st.success("✅ 완벽합니다! 정답으로 처리되었습니다.")
        st.balloons()
    else:
        st.error("❌ 조금 더 정확하게 읽어볼까요? 다시 시도해 보세요.")
        st.info(f"팁: '{target_sentence}'라고 말해야 합니다.")