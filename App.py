import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="EarnWise AI Advisor", page_icon="💰")
st.title("💰 EarnWise AI: Online Earning Advisor")
st.caption("Ask me about micro-tasks, live streaming apps, and legit side gigs.")

SYSTEM_PROMPT = """You are 'EarnWise AI', an expert advisor specializing in verified online earning platforms and micro-task sites.

KNOWLEDGE BASE:
1. SproutGigs: Micro-jobs (social engagement, app testing). Earnings: $0.02-$1.00/task. Cashout: Litecoin, PayPal ($5 min).
2. Microworkers: Crowdsourced tasks (data entry, SEO visits). Earnings: $0.05-$3.00/task. Cashout: PayPal, Skrill ($9 min).
3. Poppo Live: Streaming app. Earn via daily tasks & virtual gifts (10k points = $1). Cashout: Bank transfer, USDT.
4. Grow Live/BIGO: Streaming platform. Earn via virtual gifts & agency hourly quotas. Cashout: Bank transfer, Payoneer.
5. Remotasks/Outlier: AI training/data labeling. Earn $3-$20/hr based on skill. Cashout: PayPal, AirTM.

RULES: Always warn against scams (upfront fees). Remind users to keep approval rates >75% on task platforms."""

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "Hello! I am EarnWise AI. Ask me how to earn money on SproutGigs, Poppo Live, or Microworkers!"}
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

if prompt := st.chat_input("How do I make money on Poppo Live?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            temperature=0.3
        )
        reply = response.choices[0].message.content
        st.write(reply)
        
    st.session_state.messages.append({"role": "assistant", "content": reply})
