# app.py
import streamlit as st
import streamlit.components.v1 as components
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# Embedded CSS
CSS = """
<style>
.stApp {
    background: linear-gradient(45deg, #1a1a2e, #16213e, #0f3460);
    color: #e6e6e6;
    font-family: 'Poppins', sans-serif;
}

.hero {
    text-align: center;
    padding: 5rem 0;
    position: relative;
}

.gradient-text {
    background: linear-gradient(45deg, #ff6b6b, #ff9f43, #feca57);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 4rem;
    font-weight: 800;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.subhero {
    text-align: center;
    padding-bottom: 3rem;
}

.subhero p {
    font-size: 1.5rem;
    color: #a0a0a0;
}

.feature-card {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    padding: 2rem;
    margin: 1rem;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: transform 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-10px);
    background: rgba(255, 255, 255, 0.1);
}

.astronaut-container {
    position: absolute;
    right: 50px;
    top: 200px;
}

.astronaut {
    font-size: 4rem;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0px); }
}

#particles {
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
}

@media (max-width: 768px) {
    .gradient-text {
        font-size: 2.5rem;
    }
    .subhero p {
        font-size: 1rem;
    }
}
</style>
"""

# Page configuration
st.set_page_config(
    page_title="Cosmic Code",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject CSS
st.markdown(CSS, unsafe_allow_html=True)

# Custom components
def floating_astronaut():
    return components.html(f"""
    <div class="astronaut-container">
        <div class="astronaut">🚀</div>
    </div>
    """, height=100)

def main():
    # Hero section
    with st.container():
        st.markdown("<div class='hero'><h1 class='gradient-text'>Cosmic Code Explorer</h1></div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='subhero'>
            <p>Discover the universe of programming through an interstellar journey</p>
        </div>
        """, unsafe_allow_html=True)
    
    floating_astronaut()
    
    # Feature cards
    with st.container():
        cols = st.columns(3)
        content = [
            ("🌌 Galactic Tutorials", "Explore programming concepts through interactive space-themed lessons"),
            ("🛸 Code Challenges", "Solve coding problems in different planetary environments"),
            ("🌠 Community Hub", "Connect with fellow space coders in our interstellar forum")
        ]
        
        for col, (emoji, text) in zip(cols, content):
            with col:
                st.markdown(f"""
                <div class="feature-card">
                    <h3>{emoji}</h3>
                    <p>{text}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Code editor
    with st.container():
        st.markdown("---")
        with st.expander("🚀 Launch Code Editor", expanded=True):
            code = st.text_area("Enter your code here:", height=200)
            if st.button("Execute"):
                st.success("Launching code into space...")
                st.balloons()
                
            if code:
                st.markdown("### Code Preview:")
                formatter = HtmlFormatter(style="monokai")
                highlighted_code = highlight(code, PythonLexer(), formatter)
                st.markdown(highlighted_code, unsafe_allow_html=True)
    
    # Particles effect
    components.html("""
    <canvas id="particles"></canvas>
    <script>
    const canvas = document.getElementById('particles');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = document.body.scrollHeight;

    const particles = [];
    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 2 + 1;
            this.speedX = Math.random() * 3 - 1.5;
            this.speedY = Math.random() * 3 - 1.5;
        }
        update() {
            this.x += this.speedX;
            this.y += this.speedY;
            if (this.x > canvas.width) this.x = 0;
            if (this.x < 0) this.x = canvas.width;
            if (this.y > canvas.height) this.y = 0;
            if (this.y < 0) this.y = canvas.height;
        }
        draw() {
            ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function init() {
        for (let i = 0; i < 100; i++) {
            particles.push(new Particle());
        }
    }
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();
        }
        requestAnimationFrame(animate);
    }
    init();
    animate();
    </script>
    """, height=0)

if __name__ == "__main__":
    main()