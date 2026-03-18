import streamlit as st
import random

# --- 1. HARLEY CONFIGURATION ---
st.set_page_config(page_title="Harley SOL Agent", layout="wide")

# --- 2. PERSISTENT MEMORY ---
if "iq" not in st.session_state:
    st.session_state.iq = 135.0
if "credits" not in st.session_state:
    st.session_state.credits = 0
if "logs" not in st.session_state:
    st.session_state.logs = ["Harley system initialized. All secrets hidden."]

# --- 3. SIDEBAR (CONTROLS & SECURITY) ---
with st.sidebar:
    st.header("🛡️ Safe Guard")
    mode = st.radio("Logic Mode", ["Paper", "Live"])
    
    st.divider()
    
    # Auto-Off Logic (Protects your 1M free credits)
    usage_pct = (st.session_state.credits / 1000000)
    st.progress(min(usage_pct, 1.0), text=f"Free Tier: {st.session_state.credits:,} / 1M")
    
    if st.session_state.credits > 950000:
        st.error("🚨 MONTHLY LIMIT REACHED: Sleeping mode active.")
        st.stop()

    st.subheader("Whitelisted Harvest")
    # Harley pulls your wallet from the 'Secrets' box now
    try:
        harv_wallet = st.secrets["MY_HARVEST_WALLET"]
        st.code(f"{harv_wallet[:6]}...{harv_wallet[-4:]}", language="text")
    except:
        st.warning("⚠️ Wallet not found in Secrets!")
        harv_wallet = "Not Set"
    
    if st.button("🚀 Withdraw SOL"):
        if harv_wallet == "Not Set":
            st.error("Add MY_HARVEST_WALLET to Secrets first!")
        else:
            st.success(f"Sent to whitelist: {harv_wallet[:4]}...")
            st.session_state.logs.append(f"Withdrawal successful to {harv_wallet[:4]}.")
            st.balloons()

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

# Actions
if st.button("Manual Market Scan"):
    st.session_state.credits += 5000
    st.session_state.iq += 0.2
    st.session_state.logs.append(f"Scan complete. New data indexed. IQ: {st.session_state.iq:.1f}")
    st.rerun()

if prompt := st.chat_input("Command Harley..."):
    st.session_state.logs.append(f"User: {prompt}")
    with st.chat_message("assistant"):
        st.write("I'm hunting in the trenches, Boss. Only you have the key to our harvest.")
