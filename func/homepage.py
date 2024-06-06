import streamlit as st

def homepage():
    st.markdown(
        """
        <style>
            :root {
                --text-color: #666666;
                --background-color: #f8f9fa;
                --card-background: #ffffff;
                --card-shadow: rgba(0, 0, 0, 0.1);
            }

            @media (prefers-color-scheme: dark) {
                :root {
                    --text-color: #cccccc;
                    --background-color: #1e1e1e;
                    --card-background: #2c2c2c;
                    --card-shadow: rgba(255, 255, 255, 0.1);
                }
            }

            body {
                color: var(--text-color);
                background-color: var(--background-color);
            }

            .header-text {
                font-size: 36px;
                color: var(--text-color);
                text-align: left;
                margin-bottom: 30px;
            }

            .main-text {
                font-size: 18px;
                color: var(--text-color);
                text-align: justify;
                margin-bottom: 30px;
            }

            .info-text {
                font-size: 16px;
                color: var(--text-color);
                text-align: justify;
            }

            .card {
                background-color: var(--card-background);
                color: var(--text-color);
                padding: 20px;
                margin: 20px 0;
                border-radius: 8px;
                box-shadow: 0 4px 8px var(--card-shadow);
                animation: slideFromLeft 1s ease-out;
            }

            @keyframes slideFromLeft {
                from {
                    opacity: 0;
                    transform: translateX(-30%);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }

            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: var(--background-color);
                color: var(--text-color);
                text-align: center;
                padding: 10px 0;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h1 class='header-text'>Sole Savant</h1>", unsafe_allow_html=True)
    
    st.markdown("<h5 class='header-text'>Tentang Sole Savant</h5>", unsafe_allow_html=True)
    
    sole_savant_info = """
        Sole Savant adalah platform website canggih yang menggunakan teknologi kecerdasan buatan untuk mengklasifikasikan produk sepatu dan menganalisis sentimen pelanggan. 
        Dengan fitur utama seperti klasifikasi sepatu berdasarkan kategori, harga, dan merek, serta analisis sentimen ulasan pelanggan melalui Natural Language Processing (NLP), 
        Sole Savant membantu pengguna menemukan produk yang sesuai dan memberikan wawasan berharga bagi pemilik bisnis tentang tren pasar dan preferensi pelanggan. 
        Antarmuka yang user-friendly dan kemampuan integrasi yang luas menjadikan Sole Savant solusi ideal untuk meningkatkan pengalaman belanja dan strategi pemasaran dalam industri sepatu.
    """
    
    st.markdown(
        f"""
        <div class="card">
            {sole_savant_info}
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h5 class='header-text'>Fitur Utama</h5>", unsafe_allow_html=True)
    
    # List of features
    feature_content = [
        "Klasifikasi sepatu berdasarkan kategori, harga, dan merek",
        "Analisis sentimen ulasan pelanggan melalui Natural Language Processing (NLP)",
        "Wawasan berharga bagi pemilik bisnis tentang tren pasar dan preferensi pelanggan",
        "Antarmuka yang user-friendly dan integrasi yang luas"
    ]
    
    for feature in feature_content:
        with st.expander(feature):
            st.markdown(
                f"""
                <div class="card">
                    {feature}
                </div>
                """,
                unsafe_allow_html=True
            )

    # Footer
    st.markdown(
        """
        <div class="footer">
            &copy; 2024 Sole Savant. Developed by Kelompok 45 .All rights reserved.
        </div>
        """,
        unsafe_allow_html=True
    )
