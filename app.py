import streamlit as st

# -----------------------------
# Legit AI 2
# Microtask & Earning Site Checker
# -----------------------------

st.set_page_config(
    page_title="Legit AI 2",
    page_icon="🔎",
    layout="centered"
)

# Platform database
PLATFORMS = {
    "Microworkers": {
        "type": "Microtask platform",
        "description": "A platform where workers complete small online tasks posted by employers.",
        "status": "⚠️ Use with caution",
        "note": "Always check the individual task, employer requirements, payment history, and withdrawal rules.",
    },
    "SproutGigs": {
        "type": "Microtask / freelance platform",
        "description": "A platform offering small online jobs and freelance-style tasks.",
        "status": "⚠️ Use with caution",
        "note": "Check account rules, task requirements, employer reputation, and payment conditions.",
    },
    "Clickworker": {
        "type": "Microtask platform",
        "description": "An online platform offering various digital microtasks.",
        "status": "⚠️ Use with caution",
        "note": "Availability and tasks can vary by country. Check the official platform before starting.",
    },
    "Gemgala": {
        "type": "Gaming / referral earning app",
        "description": "An app involving games, referrals, and earning-related activities.",
        "status": "⚠️ Use with caution",
        "note": "Do not deposit money or submit sensitive documents until you independently verify the offer.",
    },
}

st.title("🔎 Legit AI 2")
st.subheader("Check earning websites and apps")

st.info(
    "This is an information tool, not an official verification service. "
    "A result marked as 'Use with caution' does not automatically mean the platform is a scam."
)

# -----------------------------
# Platform selector
# -----------------------------

st.markdown("### Select a platform")

selected = st.selectbox(
    "Choose an earning platform:",
    ["Select one..."] + list(PLATFORMS.keys())
)

if selected != "Select one...":

    data = PLATFORMS[selected]

    st.divider()

    st.header(selected)

    st.write(f"**Type:** {data['type']}")

    st.write(data["description"])

    st.warning(data["status"])

    st.markdown("### ⚠️ Important")

    st.write(data["note"])

    st.markdown("### Before you start")

    st.checkbox("I checked the platform's official website")
    st.checkbox("I understand that earnings are not guaranteed")
    st.checkbox("I will not send money to an unknown person")
    st.checkbox("I will not share passwords or private account information")

# -----------------------------
# Search/check unknown site
# -----------------------------

st.divider()

st.markdown("### 🌐 Check another earning site")

site_name = st.text_input(
    "Enter the name of an earning website or app:"
)

if st.button("🔎 Check website"):

    if not site_name.strip():

        st.error("Please enter a website or app name.")

    else:

        name = site_name.strip()

        # Check local database
        found = None

        for platform in PLATFORMS:
            if name.lower() == platform.lower():
                found = platform
                break

        if found:

            data = PLATFORMS[found]

            st.success(f"{found} is in the local database.")

            st.write(f"**Type:** {data['type']}")

            st.warning(data["status"])

            st.write(data["note"])

        else:

            st.warning("⚠️ Not verified by this prototype")

            st.write(
                f"I don't have verified information about **{name}** "
                "in the local database yet."
            )

            st.error(
                "Do not send money, passwords, cryptocurrency, "
                "or personal documents until you independently check the platform."
            )

# -----------------------------
# Safety section
# -----------------------------

st.divider()

st.markdown("### 🛡️ Earning Safety Tips")

tips = [
    "Never pay someone just to receive a job unless you fully understand the service.",
    "Never give another person your password or verification codes.",
    "Be careful with offers promising unusually high earnings for very little work.",
    "Check withdrawal requirements before spending time on a platform.",
    "Read the platform's terms and worker rules.",
    "Be careful with referral offers that require deposits.",
    "Do not install unknown APK files from strangers.",
    "Independently verify claims before trusting an earning app.",
]

for tip in tips:
    st.write("• " + tip)

# -----------------------------
# Footer
# -----------------------------

st.divider()

st.caption(
    "Legit AI 2 • Prototype • Information provided for educational purposes"
      )
