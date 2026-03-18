import streamlit as st
import pandas as pd
import random
import numpy as np
from datetime import datetime

# --- 1. PRO-TERMINAL THEME ---
st.set_page_config(page_title="HARLEY TERMINAL v3", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    [data-testid="stMetricValue"] { color: #00FFA3 !important; font-family: 'Courier New', monospace; }
    .stTable { background-color: #1A1C24; border-radius: 10px; }
    </style>
    """, unsafe_allow_index=True)

# --- 2. PERSISTENT DATA ---
if "iq" not in st.session_state: st.session_state.iq = 142.5
if "credits" not in st.session_state: st.session_state.credits = 1200
if "history" not in st.session_state:
    # Starting profit data for the chart
    st.session_state.history = [0.0, 0.12, 0.08, 0.25, 0.45, 0.41, 0.65]
if "trades" not in st.session_state:
    st.session_state.trades = [
        {"Time": "19:45", "Token": "$SOL", "Action": "BUY", "Price": "145.20", "Profit": "---"},
        {"Time": "20:02", "Token": "$WIF", "Action": "SELL", "Price": "3.12", "Profit": "+12%"},
        {"Time": "20:15", "Token": "$BONK", "Action": "BUY", "Price": "0.00002", "Profit": "---"}
    ]

# --- 3. SIDEBAR (SECURITY & HARVEST) ---
with st.sidebar:
    st.title("🛡️ HARLEY CORE")
    mode = st.radio("Logic Mode", ["PAPER (Simulated)", "LIVE (Mainnet)"])
    
    st.divider()
    usage = (st.session_state.credits / 1000000)
    st.progress(min(usage, 1.0),
