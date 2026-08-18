import streamlit as st

# ============================================================
# LEGIT AI 2
# EARNING PLATFORM CHECKER + BEGINNER GUIDE
# ============================================================

st.set_page_config(
    page_title="Legit AI 2",
    page_icon="🔎",
    layout="centered"
)

# ============================================================
# PLATFORM DATABASE
# ============================================================

PLATFORMS = {

    "Microworkers": {

        "type": "Microtask platform",

        "status": "⚠️ Use with caution",

        "about": """
Microworkers is a microtask platform where workers complete
small online jobs for employers.

Jobs can include research, data work, categorization,
social-media-related activities, surveys, testing and other
small online tasks.

The exact jobs available depend on your account and location.
""",

        "what_you_need": [
            "Microworkers worker account",
            "A valid email address",
            "A phone/device suitable for the task",
            "Internet connection",
            "A web browser such as Chrome",
            "A smartphone for tasks that require mobile apps",
            "Reddit account — only for jobs that specifically require Reddit",
            "Instagram account — only for Instagram-related jobs",
            "TikTok account — only for TikTok-related jobs",
            "Facebook account — only for Facebook-related jobs",
            "YouTube account — only for YouTube-related jobs"
        ],

        "important_note": """
You do NOT need every social-media account to use Microworkers.

For example, if a particular job says "use Reddit",
you need a Reddit account for that job. If another job
requires Instagram, you need Instagram.

Always read the individual job requirements first.
""",

        "how_it_works": [
            "Create your Microworkers account.",
            "Complete the required account verification.",
            "Open the Jobs section.",
            "Look through available jobs.",
            "Read the complete instructions before accepting a job.",
            "Check what account, app or website the job requires.",
            "Check what proof you must submit.",
            "Accept the job only if you can complete it correctly.",
            "Complete the task exactly as instructed.",
            "Submit the required proof.",
            "Wait for the employer to review your work.",
            "Keep your success rate high."
        ],

        "easy_tasks": [
            "Simple data collection",
            "Data categorization",
            "Basic research",
            "Simple social-media tasks",
            "Short legitimate surveys when available",
            "Simple app-testing tasks",
            "Image or content classification"
        ],

        "step_by_step": [
            "Open the Jobs page.",
            "Choose a simple job.",
            "Read the instructions from beginning to end.",
            "Check the required account or application.",
            "Check the payment.",
            "Check the proof requirement.",
            "Accept the job.",
            "Perform only the requested actions.",
            "Take the required screenshot or collect the required proof.",
            "Submit the proof.",
            "Wait for the employer's decision."
        ],

        "success_tips": [
            "Start with simple jobs.",
            "Never accept a task you do not understand.",
            "Read the proof requirements before starting.",
            "Do not submit fake or copied proof.",
            "Do not rush through tasks.",
            "Keep your temporary success rate above the platform requirement.",
            "Use only one Microworkers account.",
            "Avoid prohibited VPN/proxy use."
        ],

        "avoid": [
            "Fake screenshots",
            "Fake reviews",
            "Multiple accounts",
            "VPN/proxy use where prohibited",
            "Submitting false proof",
            "Tasks asking you to pay money",
            "Giving out sensitive financial information",
            "Jobs you cannot complete"
        ],

        "beginner_flow":
            "Create account → Verify → Jobs → Read requirements → "
            "Accept suitable task → Complete → Submit proof → "
            "Employer reviews → Earn"
    },


    "SproutGigs": {

        "type": "Microtask / freelance platform",

        "status": "⚠️ Use with caution",

        "about": """
SproutGigs is a marketplace where freelancers can complete
small online microjobs and other gigs.

Examples include data collection, promotion-related jobs,
surveys/offers, app testing and other small digital tasks.
""",

        "what_you_need": [
            "SproutGigs account",
            "Valid email address",
            "Internet connection",
            "Smartphone or computer depending on the job",
            "Web browser",
            "Social-media account — only when a specific job requires it",
            "Reddit — only when the task specifically requires Reddit",
            "Instagram — only when the task specifically requires Instagram",
            "TikTok — only when the task specifically requires TikTok",
            "Facebook — only when the task specifically requires Facebook"
        ],

        "important_note": """
You do not need every social-media account.

The requirements depend on the individual job.
Always read the job instructions before accepting it.
""",

        "how_it_works": [
            "Create your freelancer account.",
            "Complete your profile accurately.",
            "Open the Micro Jobs section.",
            "Browse jobs available to you.",
            "Read the complete instructions.",
            "Check the required proof.",
            "Check the payment.",
            "Accept a suitable job.",
            "Complete the requested work.",
            "Submit the required proof.",
            "Wait for the job to be reviewed."
        ],

        "easy_tasks": [
            "Simple data collection",
            "Basic research",
            "Short surveys",
            "Some app-testing jobs",
            "Simple online actions",
            "Small data-entry tasks",
            "Other short microjobs"
        ],

        "step_by_step": [
            "Open Micro Jobs.",
            "Find a job you understand.",
            "Read every requirement.",
            "Check whether the job requires another account.",
            "Check the proof requirements.",
            "Accept the job.",
            "Complete the work.",
            "Prepare the required proof.",
            "Submit the proof.",
            "Wait for review."
        ],

        "success_tips": [
            "Start with easy jobs.",
            "Read all instructions.",
            "Check the required proof before starting.",
            "Do not submit fake evidence.",
            "Choose jobs you can finish correctly.",
            "Build your reputation gradually."
        ],

        "avoid": [
            "Fake accounts",
            "Fake proof",
            "Multiple accounts where prohibited",
            "Jobs requiring prohibited payments",
            "Providing sensitive financial information",
            "Tasks that violate platform rules"
        ],

        "beginner_flow":
            "Register → Complete profile → Micro Jobs → "
            "Read requirements → Accept → Complete → "
            "Submit proof → Review → Payment"
    },


    "Clickworker": {

        "type": "Microtask platform",

        "status": "⚠️ Availability varies by country and account",

        "about": """
Clickworker provides different types of digital microtasks.

Depending on availability, workers may find surveys,
research, text creation, app testing, photo tasks,
audio recording, video recording and other jobs.
""",

        "what_you_need": [
            "Clickworker account",
            "Valid email address",
            "Internet connection",
            "Smartphone for mobile tasks",
            "Camera for photo tasks",
            "Microphone for audio tasks",
            "Camera/video capability for video tasks",
            "Web browser",
            "Additional qualifications for some specialized jobs"
        ],

        "important_note": """
You do not need every device or qualification.

The requirements depend on the individual Clickworker job.
Some jobs may require a smartphone, camera, microphone,
specific qualifications or a particular location.
""",

        "how_it_works": [
            "Create your Clickworker account.",
            "Complete your profile.",
            "Complete available qualifications.",
            "Open the available jobs.",
            "Read the job requirements.",
            "Choose a task suitable for your device and skills.",
            "Complete the task.",
            "Submit the requested result.",
            "Wait for the task to be processed or reviewed."
        ],

        "easy_tasks": [
            "Surveys",
            "Simple research",
            "Photo capturing",
            "Short audio recordings",
            "Some video tasks",
            "Simple app-testing tasks",
            "Basic data-related tasks"
        ],

        "step_by_step": [
            "Open the Clickworker app or website.",
            "Check available jobs.",
            "Read the requirements.",
            "Check whether the job requires a qualification.",
            "Check whether you need a smartphone, camera or microphone.",
            "Accept the appropriate job.",
            "Complete it carefully.",
            "Upload or submit your result.",
            "Wait for processing or review."
        ],

        "success_tips": [
            "Complete your profile accurately.",
            "Take available qualifications seriously.",
            "Check the app regularly for new jobs.",
            "Start with tasks you understand.",
            "Use a good internet connection.",
            "Follow photo, audio and video instructions carefully."
        ],

        "avoid": [
            "Low-quality submissions",
            "Guessing on qualification tests",
            "Submitting someone else's work",
            "Ignoring task requirements",
            "Accepting tasks you cannot complete"
        ],

        "beginner_flow":
            "Register → Profile → Qualifications → Available jobs → "
            "Choose task → Complete → Submit → Review/payment"
    },


    "Gemgala": {

        "type": "Social gaming / referral platform",

        "status": "⚠️ Check current reward and withdrawal rules",

        "about": """
Gemgala is a social gaming platform with party rooms,
mini-games and social features.

It also has referral and agent-related earning features.
Rewards and referral activity are subject to the platform's
current rules and verification.
""",

        "what_you_need": [
            "Gemgala account",
            "Android or compatible mobile device",
            "Internet connection",
            "The official Gemgala application",
            "Email/phone information required by registration",
            "A genuine friend/referral if you are using the referral system"
        ],

        "important_note": """
Gemgala is different from a traditional microtask platform.

It focuses on gaming and social activities. Referral rewards
can depend on the quality of invitations and verification.

Do not assume that every game reward automatically equals
cash that can immediately be withdrawn.
""",

        "how_it_works": [
            "Install the official Gemgala application.",
            "Create your account.",
            "Explore the available games and social features.",
            "Play the available games.",
            "Check the current tasks or reward activities.",
            "If using referrals, use your genuine referral link.",
            "Invite genuine users rather than creating fake accounts.",
            "Follow the current referral requirements.",
            "Check the reward status after verification.",
            "Check the current withdrawal requirements."
        ],

        "easy_tasks": [
            "Playing available mini-games",
            "Puzzle and casual game activities",
            "Daily activities when available",
            "Genuine referrals",
            "Exploring available competitions or rankings"
        ],

        "step_by_step": [
            "Install Gemgala from an official source.",
            "Register an account.",
            "Open the game section.",
            "Choose an available game.",
            "Follow the game's rules.",
            "Check whether the activity gives gems or another reward.",
            "If using referrals, open the referral section.",
            "Invite genuine friends.",
            "Check your reward after verification.",
            "Review withdrawal rules before expecting cash."
        ],

        "success_tips": [
            "Use one genuine account.",
            "Use genuine referrals.",
            "Read the current reward rules.",
            "Check withdrawal requirements.",
            "Do not pay strangers for guaranteed rewards.",
            "Keep records of important reward conditions."
        ],

        "avoid": [
            "Self-referrals",
            "Fake accounts",
            "Referral abuse",
            "Fake screenshots",
            "Promises of guaranteed income",
            "Sending money to unknown people",
            "Assuming every in-game reward is immediately withdrawable"
        ],

        "beginner_flow":
            "Install → Register → Play/explore → Complete eligible "
            "activities → Earn in-app rewards → Verify → Check withdrawal"
    }
}


# ============================================================
# HEADER
# ============================================================

st.title("🔎 Legit AI 2")

st.subheader(
    "Earning platform checker + beginner task guide"
)

st.info(
    "Learn what each platform does, what you may need, "
    "which tasks are easier for beginners and how to complete them."
)


# ============================================================
# PLATFORM SELECTOR
# ============================================================

st.markdown("## 📚 Choose a platform")

selected = st.selectbox(
    "Select an earning platform:",
    ["Select one..."] + list(PLATFORMS.keys())
)


# ============================================================
# PLATFORM GUIDE
# ============================================================

if selected != "Select one...":

    data = PLATFORMS[selected]

    st.divider()

    st.header("🔎 " + selected)

    st.write("**Type:** " + data["type"])

    st.warning(data["status"])

    # --------------------------------------------------------
    # ABOUT
    # --------------------------------------------------------

    with st.expander("📖 What is " + selected + "?", expanded=True):

        st.write(data["about"])

    # --------------------------------------------------------
    # WHAT YOU NEED
    # --------------------------------------------------------

    with st.expander("🧰 What do I need to start?", expanded=True):

        for item in data["what_you_need"]:
            st.write("✅ " + item)

        st.info(data["important_note"])

    # --------------------------------------------------------
    # HOW IT WORKS
    # --------------------------------------------------------

    with st.expander("⚙️ How does it work?", expanded=True):

        for i, step in enumerate(data["how_it_works"], 1):
            st.write(f"**{i}.** {step}")

    # --------------------------------------------------------
    # EASY TASKS
    # --------------------------------------------------------

    with st.expander("🟢 Easy tasks for beginners", expanded=True):

        for task in data["easy_tasks"]:
            st.write("• " + task)

    # --------------------------------------------------------
    # STEP BY STEP
    # --------------------------------------------------------

    with st.expander("📋 How to complete a task step-by-step"):

        for i, step in enumerate(data["step_by_step"], 1):
            st.write(f"**Step {i}:** {step}")

    # --------------------------------------------------------
    # TIPS
    # --------------------------------------------------------

    with st.expander("⭐ Tips to make tasks easier"):

        for tip in data["success_tips"]:
            st.write("💡 " + tip)

    # --------------------------------------------------------
    # AVOID
    # --------------------------------------------------------

    with st.expander("🚨 What should I avoid?"):

        for warning in data["avoid"]:
            st.write("❌ " + warning)

    # --------------------------------------------------------
    # QUICK FLOW
    # --------------------------------------------------------

    st.markdown("### 🚀 Beginner flow")

    st.success(data["beginner_flow"])


# ============================================================
# SEARCH / CHECKER
# ============================================================

st.divider()

st.markdown("## 🌐 Check another earning site")

site_name = st.text_input(
    "Enter the name of an earning website or app:"
)

if st.button("🔎 Check website"):

    if not site_name.strip():

        st.error("Please enter a platform name.")

    else:

        name = site_name.strip()

        found = None

        for platform in PLATFORMS:

            if name.lower() == platform.lower():

                found = platform
                break

        if found:

            data = PLATFORMS[found]

            st.success(
                "✅ " + found + " is in the Legit AI 2 database."
            )

            st.write("**Type:** " + data["type"])

            st.warning(data["status"])

            st.write(data["about"])

            st.info(
                "Select " + found +
                " from the platform menu above to see the "
                "complete beginner guide."
            )

        else:

            st.warning("⚠️ Not verified by this prototype")

            st.write(
                "Legit AI 2 does not currently have a platform "
                "profile for **" + name + "**."
            )

            st.error(
                "Do not send money, passwords, verification codes "
                "or sensitive documents until you independently "
                "verify the platform."
            )


# ============================================================
# GENERAL SAFETY
# ============================================================

st.divider()

st.markdown("## 🛡️ General microtask safety")

safety = [
    "Read the complete task instructions before accepting.",
    "Check what proof is required before starting.",
    "Only use accounts that you genuinely own.",
    "Do not create fake social-media accounts for tasks.",
    "Do not submit fake screenshots or fake proof.",
    "Do not share passwords or verification codes.",
    "Be careful with tasks requiring payments or deposits.",
    "Check withdrawal rules before spending lots of time.",
    "Never assume that high advertised earnings are guaranteed.",
    "Follow each platform's current rules."
]

for item in safety:
    st.write("• " + item)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Legit AI 2 • Beginner earning-platform guide • "
    "Information can change; always check the platform's current rules."
)
