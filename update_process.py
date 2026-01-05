import re

# خواندن فایل HTML
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# HTML جدید برای بخش process
new_process_html = '''<section class="process">
    <div class="container">
        <div class="header">
            <h1>Way of building</h1>
            <h2>Great Software</h2>
        </div>

        <div class="section">
            <div class="content">
                <h3>Build the right team to scale</h3>
                <p>Finding the right talent is not easy. We help you find the talent that suits your needs, follows your processes, and sticks with you long term <span class="highlight">(not the case with freelancers).</span></p>
                <p>Our <a href="#">delivery model</a> helps you cut costs and deliver within budget.</p>
                <blockquote class="quote">
                    "Simform is quick to identify larger problem with the Software so we decided to expand our scope to build new modules"
                </blockquote>
                <div class="author">
                    <img src="https://i.pravatar.cc/150?img=33" alt="Jeewa markram">
                    <div class="author-info">
                        <div class="author-name">Jeewa markram</div>
                        <div class="author-title">CEO</div>
                    </div>
                </div>
            </div>
            <div class="image-wrapper">
                <div class="circle-accent orange"></div>
                <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&h=600&fit=crop" alt="Team meeting">
                <div class="circle-accent pink"></div>
            </div>
        </div>

        <div class="section">
            <div class="content">
                <h3>Build the right team to scale</h3>
                <p>Finding the right talent is not easy. We help you find the talent that suits your needs, follows your processes, and sticks with you long term <span class="highlight">(not the case with freelancers).</span></p>
                <p>Our <a href="#">delivery model</a> helps you cut costs and deliver within budget.</p>
                <blockquote class="quote">
                    "Simform is quick to identify larger problem with the Software so we decided to expand our scope to build new modules"
                </blockquote>
                <div class="author">
                    <img src="https://i.pravatar.cc/150?img=34" alt="Sarah Johnson">
                    <div class="author-info">
                        <div class="author-name">Sarah Johnson</div>
                        <div class="author-title">CEO</div>
                    </div>
                </div>
            </div>
            <div class="image-wrapper">
                <div class="circle-accent orange"></div>
                <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&h=600&fit=crop" alt="Team discussion">
                <div class="circle-accent pink"></div>
            </div>
        </div>

        <div class="section">
            <div class="content">
                <h3>Build the right team to scale</h3>
                <p>Finding the right talent is not easy. We help you find the talent that suits your needs, follows your processes, and sticks with you long term <span class="highlight">(not the case with freelancers).</span></p>
                <p>Our <a href="#">delivery model</a> helps you cut costs and deliver within budget.</p>
                <blockquote class="quote">
                    "Simform is quick to identify larger problem with the Software so we decided to expand our scope to build new modules"
                </blockquote>
                <div class="author">
                    <img src="https://i.pravatar.cc/150?img=35" alt="Michael Chen">
                    <div class="author-info">
                        <div class="author-name">Michael Chen</div>
                        <div class="author-title">CTO</div>
                    </div>
                </div>
            </div>
            <div class="image-wrapper">
                <div class="circle-accent yellow"></div>
                <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&h=600&fit=crop" alt="Team brainstorming">
                <div class="circle-accent pink"></div>
            </div>
        </div>
    </div>
</section>'''

# جستجو و جایگزینی بخش process با استفاده از regex
pattern = r'<section class="process">.*?</section>'
content = re.sub(pattern, new_process_html, content, flags=re.DOTALL)

# نوشتن فایل به‌روزشده
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Process section successfully updated!")
