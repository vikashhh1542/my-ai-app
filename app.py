import streamlit as st
import traceback

st.set_page_config(page_title="Mera Self-Modifying AI App", layout="wide")

st.title("🤖 Mera Smart Self-Modifying AI App")
st.write("Yahan aap apne app ke andar naye features khud add kar sakte hain!")

# Sidebar - Feature Request Box
st.sidebar.header("✨ Naya Feature Request Karein")
feature_prompt = st.sidebar.text_area("Aapko app me kya naya feature chahiye?")

if st.sidebar.button("AI Code Generate Karein"):
    if feature_prompt:
        with st.spinner("AI code likh raha hai..."):
            # Sample generated code based on user prompt
            sample_code = f"""
# Feature: {feature_prompt}
st.success("Naya feature safalta-purvak run ho gaya!")
st.info("Aapka naya feature yahan active ho chuka hai.")
st.balloons()
"""
        st.session_state['generated_code'] = sample_code.strip()
        st.sidebar.success("✅ Code generate ho gaya! Niche diye gaye box me copy ho gaya hai.")
    else:
        st.sidebar.warning("Pehle likhein ki kya feature chahiye.")

# Main Screen - Paste & Run Box (Jaisa aapne chaha tha)
st.subheader("🛠️ Paste & Run Box (Feature Adder)")
st.write("Upar se code copy karein ya niche diye gaye box me apna code paste karke **Run** button dabayein:")

default_code = st.session_state.get('generated_code', '''# Yahan apna code paste karein
st.write("Abhi koi naya feature run nahi ho raha hai.")''')

user_code = st.text_area("Yahan Code Paste Karein:", value=default_code, height=200)

if st.button("▶️ Code Run Karein aur Feature Jodein"):
    try:
        st.write("---")
        st.subheader("✨ Live Running Feature Output:")
        exec(user_code, {'st': st})
    except Exception as e:
        st.error("❌ Code me kuch galti hai:")
        st.code(traceback.format_exc())
