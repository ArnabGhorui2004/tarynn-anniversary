import streamlit as st
import time
from streamlit.components.v1 import html


st.set_page_config(page_title="Happy 2nd Monthiversary Tarynn ❤️", layout="centered")


# Custom CSS + Tailwind via CDN (works in Streamlit)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    body { font-family: 'Poppins', sans-serif; }
    .heart { animation: float 15s linear infinite; }
    @keyframes float { 0% { transform: translateY(100vh); } 100% { transform: translateY(-100vh); } }
    .sticker { animation: bounce 2s infinite ease-in-out; }
    @keyframes bounce { 0%,100% { transform: scale(1); } 50% { transform: scale(1.15); } }
</style>
""", unsafe_allow_html=True)


st.title("💚 Happy 2nd Monthiversary, **Tarynn** ❤️")
st.markdown("### From your **Sonu** who misses you every single day 💕")


# Floating hearts background simulation
hearts_html = """
<div style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:-1;overflow:hidden;">
""" + "".join([
    f'<div class="heart" style="position:absolute;left:{i*5}%;font-size:2rem;animation-delay:-{i}s;color:#22c55e;">💚</div>'
    for i in range(20)
]) + "</div>"
html(hearts_html, height=100)


# Do You Love Me Section
st.subheader("Do you love me, Tarynn? 🥰")


if 'only_positive' not in st.session_state:
    st.session_state.only_positive = False


col1, col2 = st.columns(2)


if not st.session_state.only_positive:
    if col1.button("Yes 💚", use_container_width=True):
        st.success("Yay! I knew my Tarynn loves her Sonu! 💖 This makes my day brighter than cyan skies.")
        st.balloons()
    if col2.button("Absolutely Yes 💖", use_container_width=True):
        st.success("Absolutely Yes?! My heart is exploding with happiness! 🥳💚")
        st.balloons()
    if col1.button("No 😢", use_container_width=True):
        st.error("Aww... 😿 It's okay my love, I know you do deep down 💚")
        time.sleep(5)
        st.rerun()
    if col2.button("Absolutely No 😭", use_container_width=True):
        st.markdown("### Oh no... 💔")
        st.markdown("![Crying cat](https://media.giphy.com/media/3o7TKsQ3f7j2b2b2b2/giphy.gif)")
        st.write("My poor Tarynn... but I still love you so much! ❤️")
        time.sleep(5)
        st.session_state.only_positive = True
        st.rerun()
else:
    # Only positive options after sad choice
    if st.button("Yes 💚", use_container_width=True):
        st.success("Yay! I knew it! 💖")
        st.balloons()
    if st.button("Absolutely Yes 💖", use_container_width=True):
        st.success("Absolutely Yes makes everything perfect! 🥳")
        st.balloons()


st.divider()


st.subheader("Choose another surprise, my love ✨")


tab1, tab2, tab3, tab4 = st.tabs(["💌 Love Letter", "📸 Our Memories", "🎉 Sticker Party", "🌟 Special Greeting"])


with tab1:
    st.markdown("### My Dearest Tarynn 💚")
    st.write("""
    It's our 2nd monthiversary on the 7th and every day with you feels magical. 
    Your favorite green reminds me of fresh beginnings — just like us. 
    From Sonu (01/08/2004) to Tarynn (26th December) — distance can't stop my love for you.
    """)
    st.image("https://media.giphy.com/media/4Q2M2phU5l2ORVKh3b/giphy.gif", width=300)


with tab2:
    st.write("### Our Beautiful Moments 📸")
    st.write("Replace these with your real photos (upload to Imgur and paste direct links)")
    col_a, col_b = st.columns(2)
    with col_a:
        st.image("https://via.placeholder.com/600x400/86efac/166534?text=Our+First+Smile", caption="Your smile that melts me 🥹")
    with col_b:
        st.image("https://via.placeholder.com/600x400/86efac/166534?text=Our+Moments", caption="Late night talks 💕")
    st.caption("More memories coming soon when we meet again...")


with tab3:
    st.write("### Sticker Party for my cutie! 🎀")
    cols = st.columns(4)
    with cols[0]: st.image("https://media.giphy.com/media/3o7TKsQ3f7j2b2b2b2/giphy.gif", width=120)
    with cols[1]: st.image("https://media.giphy.com/media/l0HlRnAWXxn0MhKLK/giphy.gif", width=120)
    with cols[2]: st.image("https://media.giphy.com/media/26ufnwz3wDUli7GU0/giphy.gif", width=120)
    with cols[3]: st.image("https://media.giphy.com/media/4Q2M2phU5l2ORVKh3b/giphy.gif", width=120)
    st.write("Pick any and send it back to me with a kiss 😘")


with tab4:
    st.write("### Surprise Greeting 🌟")
    st.write("Happy 2-Monthiversary my forever girl!")
    st.write("Here's to many more 7ths filled with laughter, calls, and dreams coming true together. I promise our next meeting will be magical 💫")
    st.balloons()


st.caption("Made with ❤️ by Sonu for Tarynn")