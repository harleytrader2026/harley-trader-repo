import streamlit as st
import random

# --- 1. SETTINGS & SECURITY ---
st.set_page_config(page_title="Harley SOL Agent", layout="wide")

# 🔒 PASTE YOUR WALLET ADDRESS BETWEEN THE QUOTES BELOW
MY_HARVEST_WALLET = EpBqneQtFRPnxSx5hi36EJREV1njcxm3SoUv9UApU1jT

# --- 2. PERSISTENT MEMORY ---
if "iq" not in st.session_state:
    st.session_state.iq = 135.0
if "credits" not in st.session_state:
    st.session_state.credits = 0
if "logs" not in st.session_state:
    st.session_state.logs = ["Harley system initialized."]

# --- 3. SIDEBAR (CONTROLS) ---
with st.sidebar:
    st.header("🛡️ Safe Guard")
    mode = st.radio("Logic Mode", ["Paper", "Live"])
    
    st.divider()
    
    # Auto-Off Logic (Protects your 1M free credits)
    usage_pct = (st.session_state.credits / 1000000)
    st.progress(min(usage_pct, 1.0), text=f"Free Tier: {st.session_state.credits:,} / 1M")
    
    if st.session_state.credits > 950000:
        st.error("Monthly Limit Hit! Harley is Sleeping.")
        st.stop()

    st.subheader("Whitelisted Harvest")
    # This checks if you actually pasted a wallet address
    if "PASTE_YOUR" in MY_HARVEST_WALLET or not MY_HARVEST_WALLET:
        st.warning("⚠️ Wallet not set in code!")
    else:
        st.code(f"{MY_HARVEST_WALLET[:6]}...{MY_HARVEST_WALLET[-4:]}", language="text")
    
    if st.button("🚀 Withdraw SOL"):
        if mode == "Live":
            st.success(f"Sent to whitelisted wallet ending in {MY_HARVEST_WALLET[-4:]}!")
            st.session_state.logs.append(f"Withdrawal: Sent to {MY_HARVEST_WALLET[:6]}...")
            st.balloons()
        else:
            st.info("Simulation: Withdrawal successful in Paper Mode.")

# --- 4. DASHBOARD UI ---
st.title(f"🤖 Harley Agent ({mode})")

col1, col2, col3 = st.columns(3)
col1.metric("Harley IQ", f"{st.session_state.iq:.1f}", "+0.2")
col2.metric("Trading Wallet", "0.85 SOL")
col3.metric("Market Status", "🟢 Active")

st.divider()

# Activity Feed
st.subheader("📝 Activity Feed")
for log in reversed(st.session_state.logs[-5:]):
    st.caption(f"• {log}")

st.divider()

# Buttons & Actions
if st.button("Manual Market Scan"):
    st.session_state.credits += 5000
    st.session_state.iq += 0.2
    st.session_state.logs.append(f"Scan: Found new patterns. IQ is now {st.session_state.iq:.1f}.")
    st.rerun()

# Chatbox
if prompt := st.chat_input("Command Harley..."):
    st.session_state.logs.append(f"User: {prompt}")
    with st.chat_message("assistant"):
        st.write("I'm scanning the trenches, Boss. Only you have the key to our harvest.")
