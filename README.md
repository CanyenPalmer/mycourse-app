# ⛳ MyCourse: Intelligent Golf Round Benchmarking App

Welcome to **MyCourse** — a mobile-first web application that lets golfers track, analyze, and improve their game by comparing performance to PGA Tour benchmarks.

---

## 🎯 Purpose & Impact

**MyCourse** empowers amateur golfers with pro-level analysis:
- 📈 **Track your rounds** hole-by-hole on real-world courses
- 🧠 **Compare your performance** to PGA Tour Top 100, Top 50, and Top 10 averages
- 💬 **Receive personalized improvement feedback** based on your worst-performing area
- 📒 **Reflect on your game** with "After Round Thoughts" saved per round

Most golf apps track stats — but **MyCourse helps players understand what to improve and why**.

---

## 🧪 Data Science Contributions

This application demonstrates key applied data science principles in a real-world sports context:

### 1. **Benchmark Analytics**
- Compares user stats to structured pro benchmark tiers
- Identifies highest deviation (worst stat) dynamically
- Translates performance gaps into natural language tips using rule-based modeling

### 2. **User-Level Time-Series Tracking**
- Rounds are stored by user with timestamps
- Enables longitudinal performance trend analysis (future enhancement: stroke gains over time)

### 3. **Contextual Data Capture**
- Course name, tee box, number of holes, and starting hole are all user-selected
- Supports more advanced contextual models (e.g., expected performance by course)

---

## 📱 Features

- ✅ Secure User Login with session tracking
- ✅ Hole-by-hole stat entry: Score, FIR, GIR, Putts
- ✅ Dynamic tee box + hole configuration
- ✅ Personalized round summaries
- ✅ Custom improvement tips using benchmark deltas
- ✅ "After Round Thoughts" modal (saved per round)
- ✅ Mobile-friendly UI (Tailwind CSS)

---

## ⚙️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: Jinja2 + Tailwind CSS
- **Database**: SQLite (lightweight and portable)
- **Auth**: Flask-Login
- **APIs**: Ready for integration with GolfAPI.io (for real course data)

---

## 🧠 Future Enhancements

- 🧮 Strokes Gained analytics
- 📊 Performance trends dashboard (putting %, GIR over time)
- 📍 GPS hole tracking + real map overlays
- 📤 CSV/PDF export of round data
- 📱 PWA (Progressive Web App) or Mobile App (Flutter/Kivy)

---

## 👨‍💻 Author

**Canyen Palmer**  
Lead Analyst @ Iconic Care Inc.  
📚 B.A. Mathematics | A.S. Computer Science  
🎓 M.S. Data Science (In Progress) – University of Pittsburgh  
🔗 [Portfolio](https://mycaddy.onrender.com) | [LinkedIn](https://linkedin.com) | [GitHub](https://github.com)

---

## 📥 Installation

```bash
git clone https://github.com/YOUR_USERNAME/mycourse-app.git
cd mycourse-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
