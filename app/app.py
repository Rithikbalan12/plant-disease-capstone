# import streamlit as st
# import requests
# from PIL import Image
# import html
# import textwrap


# # =========================================================
# # HTML RENDER HELPER
# # =========================================================

# def render_html(content):
#     st.markdown(
#         textwrap.dedent(content),
#         unsafe_allow_html=True
#     )


# # =========================================================
# # PAGE CONFIG
# # =========================================================

# st.set_page_config(
#     page_title="PlantCare AI",
#     page_icon="🌿",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )


# # =========================================================
# # FASTAPI URL
# # =========================================================

# API_URL = "http://127.0.0.1:8000/predict"


# # =========================================================
# # CUSTOM CSS
# # =========================================================

# render_html("""
# <style>

# #MainMenu {
#     visibility: hidden;
# }

# header {
#     visibility: hidden;
# }

# footer {
#     visibility: hidden;
# }

# .stApp {
#     background: #0b1220;
#     color: #e5e7eb;
# }

# .block-container {
#     max-width: 1250px;
#     padding-top: 2rem;
#     padding-bottom: 4rem;
# }


# /* =====================================================
#    SIDEBAR
#    ===================================================== */

# section[data-testid="stSidebar"] {
#     background: linear-gradient(
#         180deg,
#         #071d14 0%,
#         #0b3b25 100%
#     );

#     border-right: 1px solid #1f5138;
# }

# section[data-testid="stSidebar"] * {
#     color: #f0fdf4 !important;
# }

# .brand {
#     text-align: center;
#     padding: 20px 5px 30px;
# }

# .brand-icon {
#     font-size: 58px;
# }

# .brand-title {
#     font-size: 26px;
#     font-weight: 800;
#     margin-top: 5px;
# }

# .brand-subtitle {
#     font-size: 13px;
#     color: #a7f3c0 !important;
# }

# .step {
#     background: rgba(74, 222, 128, 0.10);
#     border: 1px solid rgba(134, 239, 172, 0.18);
#     border-radius: 12px;
#     padding: 13px;
#     margin: 10px 0;
#     font-size: 14px;
# }


# /* =====================================================
#    HERO
#    ===================================================== */

# .hero {
#     background:
#         radial-gradient(
#             circle at 85% 20%,
#             rgba(74, 222, 128, 0.22),
#             transparent 30%
#         ),
#         linear-gradient(
#             135deg,
#             #092b1c,
#             #126238
#         );

#     border: 1px solid #1d6b43;
#     border-radius: 25px;
#     padding: 45px;
#     color: white;
#     box-shadow: 0 18px 45px rgba(0, 0, 0, 0.35);
#     margin-bottom: 30px;
# }

# .hero-small {
#     color: #86efac;
#     font-size: 14px;
#     font-weight: 700;
#     letter-spacing: 1px;
#     text-transform: uppercase;
# }

# .hero-title {
#     font-size: 48px;
#     margin: 10px 0;
#     font-weight: 800;
#     color: white;
# }

# .hero-text {
#     font-size: 18px;
#     color: #d1fae5;
#     max-width: 750px;
#     line-height: 1.6;
# }


# /* =====================================================
#    FEATURE CARDS
#    ===================================================== */

# .feature-card {
#     background: #111827;
#     border: 1px solid #263244;
#     border-radius: 18px;
#     padding: 22px;
#     box-shadow: 0 8px 25px rgba(0, 0, 0, 0.22);
#     min-height: 145px;
# }

# .feature-icon {
#     font-size: 30px;
# }

# .feature-title {
#     color: #f3f4f6;
#     font-weight: 750;
#     font-size: 17px;
#     margin-top: 8px;
# }

# .feature-text {
#     color: #9ca3af;
#     font-size: 13px;
#     margin-top: 5px;
#     line-height: 1.6;
# }


# /* =====================================================
#    SECTION
#    ===================================================== */

# .section-title {
#     font-size: 27px;
#     font-weight: 800;
#     color: #f0fdf4;
#     margin-top: 35px;
#     margin-bottom: 8px;
# }

# .section-description {
#     color: #9ca3af;
#     margin-bottom: 20px;
# }


# /* =====================================================
#    UPLOADER
#    ===================================================== */

# [data-testid="stFileUploader"] {
#     background: #111827;
#     border: 2px dashed #348b5b;
#     border-radius: 20px;
#     padding: 20px;
# }

# [data-testid="stFileUploaderDropzone"] {
#     background: #0f172a;
#     border-radius: 15px;
# }

# [data-testid="stFileUploader"] label,
# [data-testid="stFileUploader"] small {
#     color: #d1d5db !important;
# }


# /* =====================================================
#    BUTTON
#    ===================================================== */

# .stButton > button {
#     width: 100%;
#     height: 55px;
#     border-radius: 14px;
#     border: 1px solid #39a866;
#     background: linear-gradient(
#         135deg,
#         #15803d,
#         #22c55e
#     );
#     color: white;
#     font-size: 17px;
#     font-weight: 750;
# }

# .stButton > button:hover {
#     border-color: #86efac;
#     box-shadow: 0 10px 25px rgba(34, 197, 94, 0.3);
# }


# /* =====================================================
#    RESULT
#    ===================================================== */

# .result-card {
#     background: linear-gradient(
#         145deg,
#         #111827,
#         #0f172a
#     );

#     border: 1px solid #2b3b50;
#     border-left: 5px solid #22c55e;
#     border-radius: 22px;
#     padding: 28px;
#     margin-top: 15px;
# }

# .result-label {
#     color: #9ca3af;
#     font-size: 13px;
#     font-weight: 700;
#     text-transform: uppercase;
#     letter-spacing: 1px;
# }

# .result-disease {
#     color: #86efac;
#     font-size: 28px;
#     font-weight: 850;
#     margin: 8px 0 15px;
# }

# .confidence-number {
#     font-size: 38px;
#     font-weight: 850;
#     color: #4ade80;
# }

# .confidence-text {
#     color: #9ca3af;
#     font-size: 14px;
# }


# /* =====================================================
#    CARE CARDS
#    ===================================================== */

# .medicine-card {
#     background: linear-gradient(
#         145deg,
#         #172033,
#         #111827
#     );

#     border: 1px solid #36506b;
#     border-left: 5px solid #60a5fa;
#     border-radius: 18px;
#     padding: 22px;
#     min-height: 260px;
# }

# .protection-card {
#     background: linear-gradient(
#         145deg,
#         #10271c,
#         #0f2118
#     );

#     border: 1px solid #24583a;
#     border-left: 5px solid #22c55e;
#     border-radius: 18px;
#     padding: 22px;
#     min-height: 260px;
# }

# .warning-card {
#     background: #2a2110;
#     border: 1px solid #725b22;
#     border-left: 5px solid #f59e0b;
#     border-radius: 16px;
#     padding: 16px 20px;
#     color: #fde68a;
#     line-height: 1.6;
#     margin-top: 18px;
# }


# /* =====================================================
#    EMPTY CARD
#    ===================================================== */

# .empty-card {
#     background: #111827;
#     border-radius: 22px;
#     padding: 50px 25px;
#     text-align: center;
#     border: 1px solid #263244;
#     color: #9ca3af;
#     min-height: 180px;
# }

# .empty-card h3 {
#     color: #e5e7eb;
# }

# .empty-icon {
#     font-size: 55px;
# }


# /* =====================================================
#    READY BOX
#    ===================================================== */

# .ready-box {
#     background: #0d2b1c;
#     padding: 15px;
#     border-radius: 12px;
#     margin-bottom: 18px;
#     color: #86efac;
#     border: 1px solid #1e5c3a;
# }


# /* =====================================================
#    ABOUT
#    ===================================================== */

# .about-card {
#     background: #0f2118;
#     border-radius: 22px;
#     padding: 30px;
#     margin-top: 35px;
#     border: 1px solid #24583a;
#     color: #d1d5db;
#     line-height: 1.7;
# }

# .about-card h3 {
#     color: #86efac !important;
# }


# /* =====================================================
#    FOOTER
#    ===================================================== */

# .footer {
#     text-align: center;
#     color: #6b7280;
#     font-size: 13px;
#     padding: 30px 0 10px;
# }


# /* =====================================================
#    STREAMLIT TEXT
#    ===================================================== */

# h1,
# h2,
# h3 {
#     color: #f3f4f6 !important;
# }

# </style>
# """)


# # =========================================================
# # DISEASE CARE DATA
# # =========================================================

# DISEASE_CARE = {

#     "tomato late blight": {
#         "medicine": (
#             "For confirmed late blight, use a locally approved "
#             "fungicide exactly according to the product label. "
#             "Remove badly infected leaves and fruit."
#         ),
#         "treatment": (
#             "Remove severely infected plant material, improve "
#             "air circulation, and avoid overhead watering."
#         ),
#         "protection": (
#             "Keep foliage dry, water at soil level, space plants "
#             "well, remove infected debris, and inspect nearby plants."
#         ),
#         "warning": (
#             "Late blight can spread quickly. Confirm the diagnosis "
#             "before applying chemical treatment."
#         )
#     },

#     "tomato early blight": {
#         "medicine": (
#             "For confirmed disease, a locally approved fungicide "
#             "may be used strictly according to the product label."
#         ),
#         "treatment": (
#             "Remove affected lower leaves and improve airflow."
#         ),
#         "protection": (
#             "Use mulch to reduce soil splash, water at the base, "
#             "rotate crops when possible, and remove diseased debris."
#         ),
#         "warning": (
#             "Monitor lower leaves regularly because symptoms often "
#             "begin near the bottom of the plant."
#         )
#     },

#     "tomato septoria leaf spot": {
#         "medicine": (
#             "A locally approved fungicide can be considered for "
#             "confirmed disease. Follow the label exactly."
#         ),
#         "treatment": (
#             "Remove infected leaves and improve ventilation. "
#             "Keep foliage dry when practical."
#         ),
#         "protection": (
#             "Avoid overhead irrigation, use mulch, provide good "
#             "spacing, and remove fallen infected leaves."
#         ),
#         "warning": (
#             "Sanitation is important because infected debris can "
#             "help the disease persist."
#         )
#     },

#     "tomato bacterial spot": {
#         "medicine": (
#             "Use only locally approved treatments for bacterial "
#             "diseases and follow the product label."
#         ),
#         "treatment": (
#             "Remove severely affected leaves and avoid handling "
#             "plants while they are wet."
#         ),
#         "protection": (
#             "Use clean planting material, avoid overhead watering, "
#             "improve airflow, and sanitize tools."
#         ),
#         "warning": (
#             "Do not move wet plant material between healthy and "
#             "affected plants."
#         )
#     },

#     "tomato target spot": {
#         "medicine": (
#             "A locally approved fungicide may help for confirmed "
#             "disease when used according to its label."
#         ),
#         "treatment": (
#             "Remove badly affected foliage and improve airflow."
#         ),
#         "protection": (
#             "Avoid prolonged leaf wetness, provide plant spacing, "
#             "use mulch, and remove infected debris."
#         ),
#         "warning": (
#             "Inspect new growth regularly and keep the canopy open."
#         )
#     },

#     "tomato leaf mold": {
#         "medicine": (
#             "For severe confirmed disease, use a locally approved "
#             "fungicide according to its label."
#         ),
#         "treatment": (
#             "Remove affected leaves and increase ventilation."
#         ),
#         "protection": (
#             "Reduce humidity, increase spacing, improve greenhouse "
#             "ventilation, and avoid wet leaves."
#         ),
#         "warning": (
#             "High humidity strongly favors leaf mold."
#         )
#     },

#     "tomato spider mites": {
#         "medicine": (
#             "For persistent infestations, use an appropriate locally "
#             "approved miticide or insecticide according to its label."
#         ),
#         "treatment": (
#             "Rinse foliage gently with water and remove heavily "
#             "infested leaves."
#         ),
#         "protection": (
#             "Reduce plant stress, inspect leaf undersides, and "
#             "encourage beneficial insects where appropriate."
#         ),
#         "warning": (
#             "Avoid unnecessary broad-spectrum insecticides because "
#             "they can harm beneficial predators."
#         )
#     },

#     "tomato mosaic virus": {
#         "medicine": (
#             "There is no curative medicine for a virus-infected plant. "
#             "Management focuses on removal and prevention."
#         ),
#         "treatment": (
#             "Remove severely infected plants to reduce spread and "
#             "control weeds and volunteer plants."
#         ),
#         "protection": (
#             "Wash hands and tools, use clean planting material, and "
#             "do not propagate from infected plants."
#         ),
#         "warning": (
#             "Viral diseases are best managed through prevention "
#             "and sanitation."
#         )
#     },

#     "tomato yellow leaf curl virus": {
#         "medicine": (
#             "There is no curative medicine once a plant is infected. "
#             "Control the insect vectors that spread the virus."
#         ),
#         "treatment": (
#             "Remove badly infected plants and manage whiteflies "
#             "using locally appropriate methods."
#         ),
#         "protection": (
#             "Use healthy planting material, monitor whiteflies, "
#             "remove infected plants, and use physical barriers "
#             "where practical."
#         ),
#         "warning": (
#             "Early vector control and removal of infected plants "
#             "help limit spread."
#         )
#     },

#     "tomato healthy": {
#         "medicine": (
#             "No disease medicine is needed because the model "
#             "classified the leaf as healthy."
#         ),
#         "treatment": (
#             "Continue normal watering, nutrition, pruning, and "
#             "routine plant monitoring."
#         ),
#         "protection": (
#             "Maintain good airflow, water at soil level, inspect "
#             "leaves regularly, and keep the growing area clean."
#         ),
#         "warning": (
#             "Continue monitoring because an apparently healthy "
#             "plant can develop symptoms later."
#         )
#     }
# }


# # =========================================================
# # GET CARE INFORMATION
# # =========================================================

# def get_care_info(predicted_class):

#     key = str(predicted_class).lower()

#     key = key.replace("___", " ")
#     key = key.replace("_", " ")
#     key = " ".join(key.split())

#     for disease_name, info in DISEASE_CARE.items():

#         if disease_name in key:
#             return info

#     return {
#         "medicine": (
#             "No specific medicine guide is configured for this "
#             "class. Confirm the diagnosis with a local agricultural "
#             "expert before applying chemical products."
#         ),
#         "treatment": (
#             "Isolate suspicious plants, remove severely damaged "
#             "tissue where appropriate, and monitor symptoms."
#         ),
#         "protection": (
#             "Keep foliage dry, improve airflow, sanitize tools, "
#             "remove infected debris, and avoid moving plant material "
#             "between healthy and affected plants."
#         ),
#         "warning": (
#             "AI predictions should be confirmed before applying "
#             "any chemical treatment."
#         )
#     }


# # =========================================================
# # CLEAN CLASS NAME
# # =========================================================

# def clean_class_name(predicted_class):

#     value = str(predicted_class)

#     value = value.replace("___", " - ")
#     value = value.replace("_", " ")

#     return " ".join(value.split()).strip()


# # =========================================================
# # CALL FASTAPI
# # =========================================================

# def predict_from_api(uploaded_file):

#     files = {
#         "file": (
#             uploaded_file.name,
#             uploaded_file.getvalue(),
#             uploaded_file.type or "image/jpeg"
#         )
#     }

#     response = requests.post(
#         API_URL,
#         files=files,
#         timeout=120
#     )

#     response.raise_for_status()

#     result = response.json()

#     if "prediction" not in result:
#         raise ValueError(
#             "Prediction missing from API response."
#         )

#     if "confidence" not in result:
#         raise ValueError(
#             "Confidence missing from API response."
#         )

#     return result


# # =========================================================
# # SIDEBAR
# # =========================================================

# with st.sidebar:

#     render_html("""
#     <div class="brand">

#         <div class="brand-icon">🌿</div>

#         <div class="brand-title">
#             PlantCare AI
#         </div>

#         <div class="brand-subtitle">
#             Intelligent Plant Health Detection
#         </div>

#     </div>
#     """)

#     st.markdown("### 🔍 How it works")

#     render_html("""
#     <div class="step">① Upload a clear leaf image</div>
#     <div class="step">② AI analyzes the image</div>
#     <div class="step">③ Disease is identified</div>
#     <div class="step">④ Confidence is displayed</div>
#     <div class="step">⑤ Medicine & protection shown</div>
#     """)

#     st.markdown("---")

#     st.markdown("### 🧠 AI Model")

#     st.write("Deep Learning")
#     st.write("TensorFlow / Keras")
#     st.write("224 × 224 image input")
#     st.write("FastAPI Backend")

#     st.markdown("---")

#     st.caption("PlantCare AI")
#     st.caption("End-to-End AI Deployment Capstone")


# # =========================================================
# # HERO
# # =========================================================

# render_html("""
# <div class="hero">

#     <div class="hero-small">
#         AI-Powered Plant Health
#     </div>

#     <div class="hero-title">
#         🌿 PlantCare AI
#     </div>

#     <div class="hero-text">
#         Detect plant diseases from leaf images using deep learning.
#         Upload a leaf and get an AI prediction, confidence score,
#         medicine guidance, treatment advice, and plant protection tips.
#     </div>

# </div>
# """)


# # =========================================================
# # FEATURES
# # =========================================================

# c1, c2, c3 = st.columns(3)


# with c1:

#     render_html("""
#     <div class="feature-card">

#         <div class="feature-icon">
#             📸
#         </div>

#         <div class="feature-title">
#             Easy Upload
#         </div>

#         <div class="feature-text">
#             Upload JPG, JPEG or PNG leaf images.
#         </div>

#     </div>
#     """)


# with c2:

#     render_html("""
#     <div class="feature-card">

#         <div class="feature-icon">
#             🧠
#         </div>

#         <div class="feature-title">
#             AI Analysis
#         </div>

#         <div class="feature-text">
#             FastAPI sends the image to the trained AI model.
#         </div>

#     </div>
#     """)


# with c3:

#     render_html("""
#     <div class="feature-card">

#         <div class="feature-icon">
#             🛡️
#         </div>

#         <div class="feature-title">
#             Care & Protection
#         </div>

#         <div class="feature-text">
#             Get treatment, medicine and prevention guidance.
#         </div>

#     </div>
#     """)


# # =========================================================
# # ANALYSIS TITLE
# # =========================================================

# render_html("""
# <div class="section-title">
#     🔬 Plant Health Analysis
# </div>
# """)

# render_html("""
# <div class="section-description">
#     Upload a clear plant leaf image to start the AI analysis.
# </div>
# """)


# # =========================================================
# # TWO COLUMNS
# # =========================================================

# left, right = st.columns(
#     [1, 1],
#     gap="large"
# )


# # =========================================================
# # LEFT SIDE - UPLOAD
# # =========================================================

# with left:

#     st.markdown("### 📤 Upload Leaf")

#     uploaded_file = st.file_uploader(
#         "Drag and drop your image here",
#         type=[
#             "jpg",
#             "jpeg",
#             "png"
#         ],
#         key="leaf_uploader"
#     )

#     image = None

#     if uploaded_file is not None:

#         try:

#             image = Image.open(
#                 uploaded_file
#             ).convert("RGB")

#             st.image(
#                 image,
#                 caption="Uploaded Leaf Image",
#                 use_container_width=True
#             )

#         except Exception:

#             st.error(
#                 "❌ Unable to read this image. "
#                 "Please upload a valid JPG or PNG file."
#             )

#     else:

#         render_html("""
#         <div class="empty-card">

#             <div class="empty-icon">
#                 🌱
#             </div>

#             <h3>
#                 No image selected
#             </h3>

#             <p>
#                 Upload a plant leaf image to begin.
#             </p>

#         </div>
#         """)


# # =========================================================
# # RIGHT SIDE - AI DIAGNOSIS
# # =========================================================

# with right:

#     st.markdown("### 🤖 AI Diagnosis")

#     if uploaded_file is not None and image is not None:

#         render_html("""
#         <div class="ready-box">
#             ✅ Image ready for AI analysis
#         </div>
#         """)

#         analyze = st.button(
#             "🔍 Analyze Plant Leaf",
#             key="analyze_leaf"
#         )

#         if analyze:

#             try:

#                 with st.spinner(
#                     "🧠 AI is analyzing the leaf..."
#                 ):

#                     result = predict_from_api(
#                         uploaded_file
#                     )

#                 # =================================================
#                 # RESULT
#                 # =================================================

#                 predicted_class = result["prediction"]

#                 confidence = float(
#                     result["confidence"]
#                 )

#                 display_class = clean_class_name(
#                     predicted_class
#                 )

#                 safe_class = html.escape(
#                     display_class
#                 )

#                 # =================================================
#                 # RESULT CARD
#                 # =================================================

#                 render_html(f"""
#                 <div class="result-card">

#                     <div class="result-label">
#                         Prediction Result
#                     </div>

#                     <div class="result-disease">
#                         🌿 {safe_class}
#                     </div>

#                     <div class="result-label">
#                         AI Confidence
#                     </div>

#                     <div class="confidence-number">
#                         {confidence:.2f}%
#                     </div>

#                     <div class="confidence-text">
#                         Model confidence for this prediction
#                     </div>

#                 </div>
#                 """)

#                 # =================================================
#                 # PROGRESS BAR
#                 # =================================================

#                 confidence_ratio = min(
#                     max(
#                         confidence / 100,
#                         0.0
#                     ),
#                     1.0
#                 )

#                 st.progress(
#                     confidence_ratio
#                 )

#                 # =================================================
#                 # CONFIDENCE MESSAGE
#                 # =================================================

#                 if confidence >= 80:

#                     st.success(
#                         "🟢 High confidence prediction"
#                     )

#                 elif confidence >= 60:

#                     st.info(
#                         "🟡 Moderate confidence prediction"
#                     )

#                 else:

#                     st.warning(
#                         "🟠 Low confidence — "
#                         "try a clearer leaf image."
#                     )

#                 # =================================================
#                 # CARE INFORMATION
#                 # =================================================

#                 care = get_care_info(
#                     predicted_class
#                 )

#                 render_html("""
#                 <div class="section-title"
#                      style="font-size:22px;">
#                     💊 Medicine, Treatment & Protection
#                 </div>
#                 """)

#                 medicine_col, protection_col = st.columns(2)

#                 safe_medicine = html.escape(
#                     care["medicine"]
#                 )

#                 safe_treatment = html.escape(
#                     care["treatment"]
#                 )

#                 safe_protection = html.escape(
#                     care["protection"]
#                 )

#                 # =================================================
#                 # MEDICINE / TREATMENT
#                 # =================================================

#                 with medicine_col:

#                     render_html(f"""
#                     <div class="medicine-card">

#                         <div class="feature-icon">
#                             💊
#                         </div>

#                         <div class="feature-title">
#                             Medicine / Treatment
#                         </div>

#                         <div class="feature-text">
#                             {safe_medicine}
#                         </div>

#                         <br>

#                         <div class="feature-title">
#                             🌱 Immediate Care
#                         </div>

#                         <div class="feature-text">
#                             {safe_treatment}
#                         </div>

#                     </div>
#                     """)

#                 # =================================================
#                 # PROTECTION
#                 # =================================================

#                 with protection_col:

#                     render_html(f"""
#                     <div class="protection-card">

#                         <div class="feature-icon">
#                             🛡️
#                         </div>

#                         <div class="feature-title">
#                             Plant Protection
#                         </div>

#                         <div class="feature-text">
#                             {safe_protection}
#                         </div>

#                     </div>
#                     """)

#                 # =================================================
#                 # WARNING
#                 # =================================================

#                 safe_warning = html.escape(
#                     care["warning"]
#                 )

#                 render_html(f"""
#                 <div class="warning-card">

#                     <b>⚠️ Important:</b>
#                     {safe_warning}

#                 </div>
#                 """)

#             # =====================================================
#             # CONNECTION ERROR
#             # =====================================================

#             except requests.exceptions.ConnectionError:

#                 st.error(
#                     "❌ FastAPI server is not running."
#                 )

#                 st.code(
#                     "uvicorn app.main:app --reload"
#                 )

#             # =====================================================
#             # TIMEOUT
#             # =====================================================

#             except requests.exceptions.Timeout:

#                 st.error(
#                     "❌ API took too long to respond. "
#                     "Please try again."
#                 )

#             # =====================================================
#             # HTTP ERROR
#             # =====================================================

#             except requests.exceptions.HTTPError as e:

#                 st.error(
#                     f"❌ FastAPI HTTP error: {e}"
#                 )

#                 try:

#                     st.json(
#                         e.response.json()
#                     )

#                 except Exception:

#                     pass

#             # =====================================================
#             # OTHER ERROR
#             # =====================================================

#             except Exception as e:

#                 st.error(
#                     f"❌ Prediction failed: {e}"
#                 )

#     else:

#         render_html("""
#         <div class="empty-card">

#             <div class="empty-icon">
#                 🧠
#             </div>

#             <h3>
#                 AI is waiting
#             </h3>

#             <p>
#                 Upload a leaf image and click
#                 <b>Analyze Plant Leaf</b>.
#             </p>

#         </div>
#         """)


# # =========================================================
# # ABOUT
# # =========================================================

# render_html("""
# <div class="about-card">

#     <h3>
#         💡 About PlantCare AI
#     </h3>

#     <p>
#         PlantCare AI uses a deep-learning image classification
#         model to recognize plant diseases from leaf images.
#     </p>

#     <p>
#         The Streamlit frontend communicates with a FastAPI backend
#         to generate the disease prediction and confidence score.
#     </p>

#     <p>
#         The application also provides general medicine,
#         treatment and plant-protection guidance.
#     </p>

#     <p style="color:#9ca3af;font-size:13px;">
#         Treatment information is general educational guidance.
#         Always follow the label of any agricultural product and
#         local agricultural expert recommendations.
#     </p>

# </div>
# """)


# # =========================================================
# # FOOTER
# # =========================================================

# render_html("""
# <div class="footer">

#     🌿 PlantCare AI
#     &nbsp;•&nbsp;
#     Deep Learning Plant Disease Detection
#     &nbsp;•&nbsp;
#     End-to-End AI Deployment Capstone

# </div>
# """)




import streamlit as st
import requests
from PIL import Image
import html

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# FASTAPI BACKEND URL
# =========================================================

API_URL = "http://127.0.0.1:8000/predict"

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>
    /* =========================
       HIDE STREAMLIT DEFAULT UI
       ========================= */
    #MainMenu { visibility: hidden; }
    header { visibility: hidden; }
    footer { visibility: hidden; }

    /* =========================
       MAIN APP
       ========================= */
    .stApp {
        background: #0b1220;
        color: #e5e7eb;
    }
    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* =========================
       SIDEBAR
       ========================= */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #071d14 0%, #0b3b25 100%);
        border-right: 1px solid #1f5138;
    }
    section[data-testid="stSidebar"] * {
        color: #f0fdf4 !important;
    }
    .brand {
        text-align: center;
        padding: 20px 5px 30px;
    }
    .brand-icon { font-size: 58px; }
    .brand-title {
        font-size: 26px;
        font-weight: 800;
        margin-top: 5px;
    }
    .brand-subtitle {
        font-size: 13px;
        color: #a7f3c0 !important;
    }
    .step {
        background: rgba(74, 222, 128, 0.10);
        border: 1px solid rgba(134, 239, 172, 0.18);
        border-radius: 12px;
        padding: 13px;
        margin: 10px 0;
        font-size: 14px;
    }

    /* =========================
       HERO
       ========================= */
    .hero {
        background: radial-gradient(circle at 85% 20%, rgba(74, 222, 128, 0.22), transparent 30%),
                    linear-gradient(135deg, #092b1c, #126238);
        border: 1px solid #1d6b43;
        border-radius: 25px;
        padding: 45px;
        color: white;
        box-shadow: 0 18px 45px rgba(0, 0, 0, 0.35);
        margin-bottom: 30px;
    }
    .hero-small {
        color: #86efac;
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .hero-title {
        font-size: 48px;
        margin: 10px 0;
        font-weight: 800;
        color: white;
    }
    .hero-text {
        font-size: 18px;
        color: #d1fae5;
        max-width: 750px;
        line-height: 1.6;
    }

    /* =========================
       FEATURE CARDS
       ========================= */
    .feature-card {
        background: #111827;
        border: 1px solid #263244;
        border-radius: 18px;
        padding: 22px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.22);
        min-height: 145px;
    }
    .feature-icon { font-size: 30px; }
    .feature-title {
        color: #f3f4f6;
        font-weight: 750;
        font-size: 17px;
        margin-top: 8px;
    }
    .feature-text {
        color: #9ca3af;
        font-size: 13px;
        margin-top: 5px;
        line-height: 1.6;
    }

    /* =========================
       SECTION
       ========================= */
    .section-title {
        font-size: 27px;
        font-weight: 800;
        color: #f0fdf4;
        margin-top: 35px;
        margin-bottom: 8px;
    }
    .section-description {
        color: #9ca3af;
        margin-bottom: 20px;
    }

    /* =========================
       FILE UPLOADER
       ========================= */
    [data-testid="stFileUploader"] {
        background: #111827;
        border: 2px dashed #348b5b;
        border-radius: 20px;
        padding: 20px;
    }
    [data-testid="stFileUploaderDropzone"] {
        background: #0f172a;
        border-radius: 15px;
    }
    [data-testid="stFileUploader"] label,
    [data-testid="stFileUploader"] small {
        color: #d1d5db !important;
    }

    /* =========================
       BUTTON
       ========================= */
    .stButton > button {
        width: 100%;
        height: 55px;
        border-radius: 14px;
        border: 1px solid #39a866;
        background: linear-gradient(135deg, #15803d, #22c55e);
        color: white;
        font-size: 17px;
        font-weight: 750;
    }
    .stButton > button:hover {
        border-color: #86efac;
        box-shadow: 0 10px 25px rgba(34, 197, 94, 0.3);
    }

    /* =========================
       RESULT CARD
       ========================= */
    .result-card {
        background: linear-gradient(145deg, #111827, #0f172a);
        border: 1px solid #2b3b50;
        border-left: 5px solid #22c55e;
        border-radius: 22px;
        padding: 28px;
        margin-top: 15px;
    }
    .result-label {
        color: #9ca3af;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .result-disease {
        color: #86efac;
        font-size: 28px;
        font-weight: 850;
        margin: 8px 0 15px;
    }
    .confidence-number {
        font-size: 38px;
        font-weight: 850;
        color: #4ade80;
    }
    .confidence-text {
        color: #9ca3af;
        font-size: 14px;
    }

    /* =========================
       CARE CARDS
       ========================= */
    .medicine-card {
        background: linear-gradient(145deg, #172033, #111827);
        border: 1px solid #36506b;
        border-left: 5px solid #60a5fa;
        border-radius: 18px;
        padding: 22px;
        min-height: 260px;
    }
    .protection-card {
        background: linear-gradient(145deg, #10271c, #0f2118);
        border: 1px solid #24583a;
        border-left: 5px solid #22c55e;
        border-radius: 18px;
        padding: 22px;
        min-height: 260px;
    }
    .warning-card {
        background: #2a2110;
        border: 1px solid #725b22;
        border-left: 5px solid #f59e0b;
        border-radius: 16px;
        padding: 16px 20px;
        color: #fde68a;
        line-height: 1.6;
        margin-top: 18px;
    }

    /* =========================
       EMPTY CARD
       ========================= */
    .empty-card {
        background: #111827;
        border-radius: 22px;
        padding: 50px 25px;
        text-align: center;
        border: 1px solid #263244;
        color: #9ca3af;
        min-height: 180px;
    }
    .empty-card h3 { color: #e5e7eb !important; }
    .empty-icon { font-size: 55px; }

    /* =========================
       READY BOX
       ========================= */
    .ready-box {
        background: #0d2b1c;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 18px;
        color: #86efac;
        border: 1px solid #1e5c3a;
    }

    /* =========================
       ABOUT
       ========================= */
    .about-card {
        background: #0f2118;
        border-radius: 22px;
        padding: 30px;
        margin-top: 35px;
        border: 1px solid #24583a;
        color: #d1d5db;
        line-height: 1.7;
    }
    .about-card h3 { color: #86efac !important; }

    /* =========================
       FOOTER
       ========================= */
    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 13px;
        padding: 30px 0 10px;
    }

    h1, h2, h3 { color: #f3f4f6 !important; }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# DISEASE CARE DATA
# =========================================================

DISEASE_CARE = {
    "tomato late blight": {
        "medicine": "For confirmed late blight, use a locally approved fungicide exactly according to the product label. Remove badly infected leaves and fruit.",
        "treatment": "Remove severely infected plant material, improve air circulation, and avoid overhead watering.",
        "protection": "Keep foliage dry, water at soil level, space plants well, remove infected debris, and inspect nearby plants.",
        "warning": "Late blight can spread quickly. Confirm the diagnosis before applying chemical treatment."
    },
    "tomato early blight": {
        "medicine": "For confirmed disease, a locally approved fungicide may be used strictly according to the product label.",
        "treatment": "Remove affected lower leaves and improve airflow.",
        "protection": "Use mulch to reduce soil splash, water at the base, rotate crops when possible, and remove diseased debris.",
        "warning": "Monitor lower leaves regularly because symptoms often begin near the bottom of the plant."
    },
    "tomato septoria leaf spot": {
        "medicine": "A locally approved fungicide can be considered for confirmed disease. Follow the label exactly.",
        "treatment": "Remove infected leaves and improve ventilation. Keep foliage dry when practical.",
        "protection": "Avoid overhead irrigation, use mulch, provide good spacing, and remove fallen infected leaves.",
        "warning": "Sanitation is important because infected debris can help the disease persist."
    },
    "tomato bacterial spot": {
        "medicine": "Use only locally approved treatments for bacterial diseases and follow the product label.",
        "treatment": "Remove severely affected leaves and avoid handling plants while they are wet.",
        "protection": "Use clean planting material, avoid overhead watering, improve airflow, and sanitize tools.",
        "warning": "Do not move wet plant material between healthy and affected plants."
    },
    "tomato target spot": {
        "medicine": "A locally approved fungicide may help for confirmed disease when used according to its label.",
        "treatment": "Remove badly affected foliage and improve airflow.",
        "protection": "Avoid prolonged leaf wetness, provide plant spacing, use mulch, and remove infected debris.",
        "warning": "Inspect new growth regularly and keep the canopy open."
    },
    "tomato leaf mold": {
        "medicine": "For severe confirmed disease, use a locally approved fungicide according to its label.",
        "treatment": "Remove affected leaves and increase ventilation.",
        "protection": "Reduce humidity, increase spacing, improve greenhouse ventilation, and avoid wet leaves.",
        "warning": "High humidity strongly favors leaf mold."
    },
    "tomato spider mites": {
        "medicine": "For persistent infestations, use an appropriate locally approved miticide or insecticide according to its label.",
        "treatment": "Rinse foliage gently with water and remove heavily infested leaves.",
        "protection": "Reduce plant stress, inspect leaf undersides, and encourage beneficial insects where appropriate.",
        "warning": "Avoid unnecessary broad-spectrum insecticides because they can harm beneficial predators."
    },
    "tomato mosaic virus": {
        "medicine": "There is no curative medicine for a virus-infected plant. Management focuses on removal and prevention.",
        "treatment": "Remove severely infected plants to reduce spread and control weeds and volunteer plants.",
        "protection": "Wash hands and tools, use clean planting material, and do not propagate from infected plants.",
        "warning": "Viral diseases are best managed through prevention and sanitation."
    },
    "tomato yellow leaf curl virus": {
        "medicine": "There is no curative medicine once a plant is infected. Control the insect vectors that spread the virus.",
        "treatment": "Remove badly infected plants and manage whiteflies using locally appropriate methods.",
        "protection": "Use healthy planting material, monitor whiteflies, remove infected plants, and use physical barriers where practical.",
        "warning": "Early vector control and removal of infected plants help limit spread."
    },
    "tomato healthy": {
        "medicine": "No disease medicine is needed because the model classified the leaf as healthy.",
        "treatment": "Continue normal watering, nutrition, pruning, and routine plant monitoring.",
        "protection": "Maintain good airflow, water at soil level, inspect leaves regularly, and keep the growing area clean.",
        "warning": "Continue monitoring because an apparently healthy plant can develop symptoms later."
    }
}

# =========================================================
# HELPER FUNCTIONS
# =========================================================

def get_care_info(predicted_class):
    key = str(predicted_class).lower()
    key = key.replace("___", " ").replace("_", " ")
    key = " ".join(key.split())

    for disease_name, info in DISEASE_CARE.items():
        if disease_name in key:
            return info

    return {
        "medicine": "No specific medicine guide is configured for this class. Confirm the diagnosis with a local agricultural expert before applying chemical products.",
        "treatment": "Isolate suspicious plants, remove severely damaged tissue where appropriate, and monitor symptoms.",
        "protection": "Keep foliage dry, improve airflow, sanitize tools, remove infected debris, and avoid moving plant material between healthy and affected plants.",
        "warning": "AI predictions should be confirmed before applying any chemical treatment."
    }

def clean_class_name(predicted_class):
    value = str(predicted_class).replace("___", " - ").replace("_", " ")
    return " ".join(value.split()).strip()

def predict_from_api(uploaded_file):
    files = {
        "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type or "image/jpeg")
    }
    response = requests.post(API_URL, files=files, timeout=120)
    response.raise_for_status()
    result = response.json()

    if "prediction" not in result:
        raise ValueError("Prediction missing from API response.")
    if "confidence" not in result:
        raise ValueError("Confidence missing from API response.")

    return result

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown(
        """
        <div class="brand">
            <div class="brand-icon">🌿</div>
            <div class="brand-title">PlantCare AI</div>
            <div class="brand-subtitle">Intelligent Plant Health Detection</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🔍 How it works")
    st.markdown(
        """
        <div class="step">① Upload a clear leaf image</div>
        <div class="step">② AI analyzes the image</div>
        <div class="step">③ Disease is identified</div>
        <div class="step">④ Confidence is displayed</div>
        <div class="step">⑤ Medicine & protection shown</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown("### 🧠 AI Model")
    st.write("Deep Learning")
    st.write("TensorFlow / Keras")
    st.write("224 × 224 image input")
    st.write("FastAPI Backend")
    st.markdown("---")
    st.caption("PlantCare AI")
    st.caption("End-to-End AI Deployment Capstone")

# =========================================================
# MAIN CONTENT
# =========================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-small">AI-Powered Plant Health</div>
        <div class="hero-title">🌿 PlantCare AI</div>
        <div class="hero-text">
            Detect plant diseases from leaf images using deep learning. 
            Upload a leaf and get an AI prediction, confidence score, 
            medicine guidance, treatment advice, and plant protection tips.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">📸</div>
            <div class="feature-title">Easy Upload</div>
            <div class="feature-text">Upload JPG, JPEG or PNG leaf images.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">AI Analysis</div>
            <div class="feature-text">FastAPI sends the image to the trained AI model.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🛡️</div>
            <div class="feature-title">Care & Protection</div>
            <div class="feature-text">Get treatment, medicine and prevention guidance.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <div class="section-title">🔬 Plant Health Analysis</div>
    <div class="section-description">Upload a clear plant leaf image to start the AI analysis.</div>
    """,
    unsafe_allow_html=True
)

left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown("### 📤 Upload Leaf")
    uploaded_file = st.file_uploader(
        "Drag and drop your image here",
        type=["jpg", "jpeg", "png"],
        key="leaf_uploader"
    )

    image = None
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, caption="Uploaded Leaf Image", use_container_width=True)
        except Exception:
            st.error("❌ Unable to read this image. Please upload a valid JPG or PNG file.")
    else:
        st.markdown(
            """
            <div class="empty-card">
                <div class="empty-icon">🌱</div>
                <h3>No image selected</h3>
                <p>Upload a plant leaf image to begin.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

with right:
    st.markdown("### 🤖 AI Diagnosis")
    if uploaded_file is not None and image is not None:
        st.markdown(
            """
            <div class="ready-box">✅ Image ready for AI analysis</div>
            """,
            unsafe_allow_html=True
        )

        analyze = st.button("🔍 Analyze Plant Leaf", key="analyze_leaf")
        if analyze:
            try:
                with st.spinner("🧠 AI is analyzing the leaf..."):
                    result = predict_from_api(uploaded_file)

                predicted_class = result["prediction"]
                confidence = float(result["confidence"])
                display_class = clean_class_name(predicted_class)
                safe_class = html.escape(display_class)

                st.markdown(
                    f"""
                    <div class="result-card">
                        <div class="result-label">Prediction Result</div>
                        <div class="result-disease">🌿 {safe_class}</div>
                        <div class="result-label">AI Confidence</div>
                        <div class="confidence-number">{confidence:.2f}%</div>
                        <div class="confidence-text">Model confidence for this prediction</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                confidence_ratio = min(max(confidence / 100, 0.0), 1.0)
                st.progress(confidence_ratio)

                if confidence >= 80:
                    st.success("🟢 High confidence prediction")
                elif confidence >= 60:
                    st.info("🟡 Moderate confidence prediction")
                else:
                    st.warning("🟠 Low confidence — try a clearer leaf image.")

                care = get_care_info(predicted_class)
                st.markdown(
                    """
                    <div class="section-title" style="font-size:22px;">
                        💊 Medicine, Treatment & Protection
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                medicine_col, protection_col = st.columns(2)
                safe_medicine = html.escape(care["medicine"])
                safe_treatment = html.escape(care["treatment"])
                safe_protection = html.escape(care["protection"])
                safe_warning = html.escape(care["warning"])

                with medicine_col:
                    st.markdown(
                        f"""
                        <div class="medicine-card">
                            <div class="feature-icon">💊</div>
                            <div class="feature-title">Medicine / Treatment</div>
                            <div class="feature-text">{safe_medicine}</div><br>
                            <div class="feature-title">🌱 Immediate Care</div>
                            <div class="feature-text">{safe_treatment}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with protection_col:
                    st.markdown(
                        f"""
                        <div class="protection-card">
                            <div class="feature-icon">🛡️</div>
                            <div class="feature-title">Plant Protection</div>
                            <div class="feature-text">{safe_protection}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.markdown(
                    f"""
                    <div class="warning-card">
                        <b>⚠️ Important:</b> {safe_warning}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except requests.exceptions.ConnectionError:
                st.error("❌ FastAPI server is not running.")
                st.code("uvicorn app.main:app --reload")
            except requests.exceptions.Timeout:
                st.error("❌ API took too long to respond. Please try again.")
            except requests.exceptions.HTTPError as e:
                st.error(f"❌ FastAPI HTTP error: {e}")
                if e.response is not None:
                    try:
                        st.json(e.response.json())
                    except Exception:
                        st.write(e.response.text)
            except Exception as e:
                st.error(f"❌ Prediction failed: {e}")
    else:
        st.markdown(
            """
            <div class="empty-card">
                <div class="empty-icon">🧠</div>
                <h3>AI is waiting</h3>
                <p>Upload a leaf image and click <b>Analyze Plant Leaf</b>.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# ABOUT & FOOTER
# =========================================================

st.markdown(
    """
    <div class="about-card">
        <h3>💡 About PlantCare AI</h3>
        <p>PlantCare AI uses a deep-learning image classification model to recognize plant diseases from leaf images.</p>
        <p>The Streamlit frontend communicates with a FastAPI backend to generate the disease prediction and confidence score.</p>
        <p>The application also provides general medicine, treatment and plant-protection guidance.</p>
        <p style="color:#9ca3af;font-size:13px;">Treatment information is general educational guidance. Always follow the label of any agricultural product and local agricultural expert recommendations.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="footer">
        🌿 PlantCare AI &nbsp;•&nbsp; Deep Learning Plant Disease Detection &nbsp;•&nbsp; End-to-End AI Deployment Capstone
    </div>
    """,
    unsafe_allow_html=True
)