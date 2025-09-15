# 🌩️ AI Thunderstorm & Gale Force Wind Classification (LJ Hackathon 2025)

This project, developed for **LJ Hackathon 2025**, uses **AI/ML** to predict thunderstorms and gale-force winds for airfield safety. It includes a **Flask backend API**, a **React frontend**, a **Flask-based simulation app**, and **Jupyter notebooks** for model training and evaluation.

---

## 🔹 Problem Statement

Thunderstorms and gale-force winds pose significant risks to airfield operations. This project builds **LSTM-based models** to classify weather conditions (Normal / Strong Wind / Thunderstorm) and predict wind speed, using API-derived weather datasets.

---

## 🔹 Features

- **Event Classification**: Predicts Normal, Strong Wind, or Thunderstorm using LSTM.
- **Wind Speed Prediction**: Regresses future wind speed with high accuracy.
- **Interactive Demo**: Flask-based simulation app for manual testing.
- **Web Interface**: React frontend for user-friendly interaction with predictions.
- **Explainability**: Includes reasons for predictions (e.g., high precipitation).

---

## 🔹 Folder Structure

```text
AI_Thunderstorm_Wind_Classification_LJHackathon/
│── backend/            # Flask API for production predictions
│   ├── app.py
│   ├── routes/
│   ├── config.py
│   ├── requirements.txt
│   └── README.md
│── frontend/           # React-based web interface
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
│── simulation/         # Flask-based demo app for manual testing
│   ├── app.py
│   ├── templates/
│   ├── requirements.txt
│   └── README.md
│── notebooks/          # Jupyter notebooks for model training
│   └── Final.ipynb
│── data/               # Sample datasets
│   └── multi_city_hist.csv  # Small sample for demo
│── models/             # Trained models and scalers
│   ├── lstm_class_multi.pth
│   ├── lstm_reg_multi.pth
│   └── scaler.pkl
│── thunderstorm_gale_force_wind.pdf   # Supporting documents
│── demo_video.mp4      # Video demo of the project
│── README.md           # Project overview (this file)
│── LICENSE             # MIT License
│── .gitignore          # Git ignore rules
```

---

## 🔹 Setup Instructions

### Prerequisites

- **Python 3.9+** (for backend, simulation, notebooks)
- **Node.js v16+ & npm v8+** (for frontend)
- **Git** (to clone the repo)

### 1. Clone the repository

```bash
git clone https://github.com/MemonFaizan/AI_Thunderstorm_Wind_Classification_LJHackathon.git
cd AI_Thunderstorm_Wind_Classification_LJHackathon
```

### 2. Explore Components

- **Backend**: See `backend/README.md` for API setup and usage.
- **Frontend**: See `frontend/README.md` for React app setup.
- **Simulation**: See `simulation/README.md` for demo app instructions.
- **Notebooks**: Run `notebooks/Final.ipynb` to explore model training.

### 3. Run the Full Application

**Start the backend API (`backend/`):**
```bash
cd backend
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**Start the frontend (`frontend/`):**
```bash
cd frontend
npm install
npm start
```

Access the app at [http://localhost:3000](http://localhost:3000).

### 4. Run the Simulation (Demo)

Follow `simulation/README.md` to run the standalone Flask demo app.
URL: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔹 Dataset

- **Source**: Weather data collected via API (e.g., NOAA, OpenWeatherMap).
- **Sample**: `data/multi_city_hist.csv` includes a small subset for demo.
- **Full Dataset**: Available via [Google Drive link] (update with actual link if hosted externally).

## 🔹 Models

- **LSTM Classification**: Predicts Normal / Strong Wind / Thunderstorm.
- **LSTM Regression**: Predicts wind speed.
- **Training**: See `notebooks/Final.ipynb` for details.
- **Saved Models**: `models/lstm_class_multi.pth`, `models/lstm_reg_multi.pth`, `models/scaler.pkl` (move to external storage if >100MB and update README).

## 🔹 Results

- **Classification**: F1-score ~0.91 (Thunderstorm), ~0.88 (Strong Wind).
- **Regression**: Mean Absolute Error ~1.2 m/s for wind speed.
- **Visuals**: Confusion matrix, ROC curves in `notebooks/Final.ipynb`.

## 🔹 Demo


- Watch the demo video below:

<video width="600" controls>
  <source src="https://github.com/MemonFaizan/AI_Thunderstorm_Wind_Classification_LJHackathon/blob/main/demo.gif" type="video/mp4">
</video>

- **Interactive demo**: Run the `simulation/` app.

## 🔹 Documentation

- **PPT**: `thunderstorm_gale_force_wind.pdf`.
- **Detailed setup**: See individual folder READMEs.

## 🔹 Contributing

Fork the repo, create a branch (`feature/xxx`), and submit a PR. Follow code style and add tests for new features.

## 🔹 License

This project is released under the MIT License (see `LICENSE`).

## 🔹 Team

- **Team Name**: Noorix
- **Team Leader**: Faizan Memon
- **Team Members:**
  - Umer Vohra
  - Yasin Memon
  - Amima Hawa

## 🔹 Contact

- **Author**: Faizan Memon
- **Email**: [memonfaisal145@gmail.com]
- Built for LJ Hackathon 2025.