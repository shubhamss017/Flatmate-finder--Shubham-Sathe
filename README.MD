# 🏠 RoomieAI – AI Powered Rental & Roommate Matching Platform

## 🌐 Live Frontend
https://flatmate-finder--sappham-sathe-znqqrawojknlyg2wm4jiy9.streamlit.app/

## 🚀 Live Backend (API & Swagger)
https://flatmate-finder-shubham-sathe.onrender.com

---

# 📌 Overview

RoomieAI is an AI-powered rental and roommate matching platform that connects tenants with suitable rental listings based on their preferences and lifestyle.

Instead of only filtering by budget and location, RoomieAI considers multiple compatibility factors such as food preferences, cleanliness, work mode, sleep schedule, hobbies, languages, and lifestyle habits to provide intelligent recommendations.

The platform also includes an end-to-end rental workflow including property listings, AI-based matching, interests, owner approval, messaging, and dashboards.

---

# ✨ Features

### 👤 Authentication
- Secure JWT Authentication
- Owner & Tenant Roles
- Login & Registration
- Password Hashing using BCrypt

### 🏠 Property Listings
- Create Rental Listings
- View Listings
- Update Listings
- Delete Listings
- Search Available Properties

### 🤖 AI Matching
- Intelligent compatibility scoring
- Preference-based matching
- Lifestyle compatibility
- AI-generated explanation for every match
- Optimized API usage with cached responses

### ❤️ Interest Management
- Tenant can send interest
- Owner receives requests
- Accept / Reject requests
- Interest status tracking

### 💬 Chat System
- Tenant ↔ Owner Messaging
- Real-time conversation history
- Secure communication after matching

### 📊 Dashboards

#### Tenant Dashboard
- Recommended Listings
- Match Scores
- Interest Status
- Profile Summary

#### Owner Dashboard
- My Listings
- Recent Interests
- Dashboard Statistics
- Incoming Requests

### 👤 Profile Management

Tenant Profile includes

- Budget
- Occupation
- Food Preference
- Smoking
- Drinking
- Pets
- Languages
- Hobbies
- Work Mode
- Sleep Schedule
- Cleanliness

Owner Profile includes

- Property Details
- Contact Information
- Address

---

# 🛠 Tech Stack

## Backend
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- JWT Authentication
- Passlib (BCrypt)
- Pydantic
- Groq LLM (AI Matching)

## Frontend
- Streamlit
- Requests
- Python

## Database
- PostgreSQL

## Deployment
- Render (Backend + PostgreSQL)
- Streamlit Community Cloud (Frontend)

---

# 📂 Project Structure

```
RoomieAI
│
├── backend
│   ├── app
│   ├── routers
│   ├── models
│   ├── services
│   ├── schemas
│   ├── auth
│   ├── database
│   ├── seed.py
│   └── requirements.txt
│
├── frontend
│   ├── app.py
│   ├── pages
│   ├── api
│   ├── utils
│   └── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <repository-url>
cd RoomieAI
```

---

## Backend Setup

```bash
cd backend

pip install -r requirements.txt
```

Create a `.env` file and configure:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
GROQ_API_KEY=your_groq_api_key
```

Run backend

```bash
uvicorn app.main:app --reload
```

---

## Frontend Setup

```bash
cd frontend

pip install -r requirements.txt

streamlit run app.py
```

---

# 🧪 Demo Credentials

## Owner

```
Email:
owner1@gmail.com

Password:
Password@123
```

## Tenant

```
Email:
tenant1@gmail.com

Password:
Password@123
```

---

# 🤖 AI Matching Parameters

The recommendation engine considers:

- Budget Compatibility
- Preferred Location
- Food Preference
- Property Type
- Gender Preference
- Smoking Preference
- Drinking Preference
- Pet Preference
- Work Mode
- Sleep Schedule
- Cleanliness
- Languages
- Hobbies

Each recommendation includes:

- Compatibility Score
- AI Explanation
- Match Ranking

---

# 📸 Screenshots

Add screenshots here after deployment.

- Login Page
- Tenant Dashboard
- Owner Dashboard
- Property Listings
- AI Matching
- Chat System

---

# 🚀 Future Enhancements

- Image Uploads
- Google Maps Integration
- Email Notifications
- Real-time Chat (WebSockets)
- AI Roommate Personality Analysis
- Recommendation Learning
- Mobile Application

---

# 👨‍💻 Developer

**Shubham Sathe**

B.Tech Artificial Intelligence & Data Science

---

# 📄 License

This project was developed for educational and demonstration purposes.
