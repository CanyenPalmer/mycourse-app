# 🏌️‍♂️ MyCourse: Golf Performance Tracker and Analytics App

**MyCourse** is a full-stack web application designed to help golfers track their rounds, analyze performance trends, and benchmark against PGA Tour data — all in a clean, mobile-friendly experience.

Built using Flask, SQLite, and Matplotlib, MyCourse provides amateur players and coaches with actionable insights into scoring patterns, consistency, and areas for improvement, while also serving as a personal case study in applied data science.

---

## 🚀 Features

### ⛳ Round Management
- Start and complete 9 or 18-hole rounds
- Select from public course data or manually enter scorecard info
- Track strokes, putts, penalties, FIR, GIR, and more

### 📊 Data Analytics Dashboard
- Line chart comparing score vs par over last 10 rounds
- Visual stat summaries for recent rounds
- Auto-identified weaknesses with improvement recommendations
- Per-hole strokes gained feedback (coming soon)

### 📚 Course Templates & Search
- Searchable course database with tee box options
- Save and reuse custom templates
- Real-time filtering by course name

### 🔒 User Accounts
- Secure registration and login with password hashing
- Persistent user history and round data
- After-round notes stored with each session

---

## 💡 Why It Matters

### For Golfers:
- Replaces vague “feel-based” evaluations with data-backed feedback
- Helps identify scoring leaks (e.g., 3-putts, tee shot penalties)
- Supports deliberate practice based on trends, not guesswork

### For Data Scientists:
- Demonstrates the end-to-end application of data science: from collection and storage, to visualization and interpretation
- Illustrates real-world usage of SQLAlchemy ORM, Flask Blueprints, and CSRF-protected forms
- Showcases user-centered data tracking in a structured yet intuitive format

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS (Bootstrap-style classes)
- **Backend**: Python (Flask), Jinja2 Templates
- **Database**: SQLite via SQLAlchemy ORM
- **Authentication**: Flask-Login, Flask-WTF
- **Data Visualization**: Matplotlib (rendered in base64)
- **Deployment**: Render.com
- **APIs (Planned)**: Real-time golf course scorecard loading via GolfAPI.io or similar

---

## 📈 Coming Soon

- Strokes Gained analysis vs PGA Top 100, 50, 10 benchmarks
- User-defined filters for performance trend graphs
- Mobile app companion version using Kivy or Flutter
- GPS-based round tracking with satellite overlay
- Community leaderboard and anonymized performance sharing

---

## 👨‍💻 Author

**Canyen Palmer**  
Data Scientist  
- B.A. in Mathematics, A.S. in Computer Science  
- Master’s in Data Science (in progress) at the University of Pittsburgh  
- Passionate about transforming raw data into better outcomes — on the course and in healthcare

---

## 📬 Contact

Interested in contributing, collaborating, or hiring?

📧 Email: [your-email@example.com]  
🌐 Portfolio: [https://mycaddy.onrender.com](https://mycaddy.onrender.com)  
📊 Blog: [Palmer Projects](https://your-blog-link.com)

---

> “Better data. Better decisions. Better golf.”
