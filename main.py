
import streamlit as st
import random

# --- 🔒 CHANGE THIS TO YOUR PERSONAL WALLET ---
MY_HARVEST_WALLET = EpBqneQtFRPnxSx5hi36EJREV1njcxm3SoUv9UApU1jT

st.set_page_config(page_title="Harley SOL Agent")

# Memory (IQ & Progress)
if "iq" not in st.session_state: st.session_state.iq = 135.0
if "credits" not in st.session_state: st.session_state.credits = 0
if "logs" not in st.session_state: st.session_state.logs = []

# --- SIDEBAR (LIMITS) ---
with st.sidebar:
    st.header("🛡️ Safe Guard")
    mode = st.radio("Mode", ["Paper", "Live"])
    
    # Auto-Off Logic
    usage = (st.session_state.credits / 1000000) * 100
    st.progress(min(int(usage), 100), text=f"Free Tier: {st.session_state.credits:,}/1M")
    
    if st.session_state.credits > 950000:
        st.error("Monthly Limit Hit! Harley is Sleeping.")
        st.stop()

    st.write(f"**Harvest Target:**\n`{MY_HARVEST_WALLET[:6]}...`")
    if st.button("🚀 Withdraw SOL"):
        st.success("Sent to Whitelisted Wallet!")
        st.session_state.logs.append("Withdrawal successful.")

# --- DASHBOARD ---
st.title(f"🤖 Harley ({mode})")
col1, col2 = st.columns(2)
col1.metric("Harley IQ", f"{st.session_state.iq}", "+0.5")
col2.metric("Trading Wallet", "0.85 SOL")

st.subheader("📝 Activity Feed")
for log in reversed(st.session_state.logs[-3:]):
    st.caption(f"• {log}")

if st.button("Manual Market Scan"):
    st.session_state.credits += 5000
    st.session_state.iq += 0.2
    st.session_state.logs.append("Scan: Found $SOL patterns. IQ Up.")
    st.rerun()

if p := st.chat_input("Talk to Harley..."):
    with st.chat_message("assistant"):
        st.write("I'm here, Boss. Only you have the key to our harvest.")
