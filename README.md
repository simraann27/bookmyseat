# 🎬 BookMySeat - Modern Cinema Ticket Booking Web App

[![Live Demo](https://img.shields.io/badge/Live%20Demo-BookMySeat-f84464?style=for-the-badge&logo=vercel)](https://bookmyseatt.vercel.app/)
[![Django](https://img.shields.io/badge/Django-5.1.1-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-000000?style=for-the-badge&logo=vercel)](https://bookmyseatt.vercel.app/)

A full-featured, visually stunning BookMyShow clone built with Django 5, interactive JavaScript seat selection, real-time ticket price calculation, payment checkout simulation, and complete ticket cancellation & history management.

🌐 **Live Website Link**: [https://bookmyseatt.vercel.app/](https://bookmyseatt.vercel.app/)

---

## ✨ Key Features

- 🎟️ **Interactive Seat Selection Grid**:
  - Real-time seat picker with visual state toggling (Available, Selected, Sold).
  - Dynamic live counter of selected seats and total amount (`seats × ticket price`).
  - Transaction-safe seat reservation logic preventing double bookings.

- 💳 **Integrated Checkout Modal**:
  - Simulated payment checkout with support for UPI (Google Pay, PhonePe, Paytm) and Credit/Debit cards.

- ❌ **Ticket Cancellation & Status Tracking**:
  - User profile displays all booked tickets with status badges (**Active** vs **Cancelled**).
  - One-click ticket cancellation that frees up seats for other users in real time.

- 🔍 **Instant Search & Movie Showcase**:
  - Interactive live filtering for movies and showtimes.
  - Movie details, rating badges, language tags, and cinema amenities (Dolby Atmos, M-Ticket, Food & Beverage, Parking).

- 🎨 **Modern BookMyShow Design Aesthetics**:
  - Dark header navbar, red brand accent (`#f84464`), hero carousel banner, Google Fonts (`Outfit` & `Plus Jakarta Sans`), and mobile-responsive layout.

- 🔐 **Complete Auth System**:
  - User registration, login with automatic query parameter redirects (`?next=`), profile updates, and password resets.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.13, Django 5.1.1, Gunicorn, WhiteNoise
- **Frontend**: HTML5, CSS3, JavaScript (ES6 & jQuery), Bootstrap 4.6, FontAwesome 6
- **Database**: SQLite3 (Local) / PostgreSQL (Production ready via `dj-database-url`)
- **Deployment**: Vercel Serverless Functions (`@vercel/python` & `api/index.py`)

---

## 🚀 Getting Started Locally

### Prerequisites
- Python 3.10+ installed on your machine.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/simraann27/bookmyseat.git
   cd bookmyseat
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the local development server**:
   ```bash
   python manage.py runserver
   ```

6. **Open in browser**:
   Visit `http://127.0.0.1:8000/` in your browser.

---

## ☁️ Vercel Deployment Settings

- **Serverless Entrypoint**: `api/index.py`
- **Vercel Config**: `vercel.json`
- **Framework Preset**: `Other`
- **Build Command**: *(Leave empty / default)*
- **Output Directory**: *(Leave empty / default)*

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
