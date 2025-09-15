
# Backend (Thunderstorm & Gale Force Wind Prediction API)

This folder (`backend/`) contains the Flask-based backend API for the Thunderstorm and Gale Force Wind prediction system. It exposes endpoints to process weather data and return predictions using trained LSTM models.

---

## 🔹 Features

- **REST API** for weather event classification (Normal / Strong Wind / Thunderstorm).
- **Wind Speed Prediction** using regression model.
- **Scalable** Flask backend for integration with frontend or external services.
- Supports **batch inputs** for weather data.

---

## 🔹 Folder Structure

```
backend/
│── app.py                # Main Flask API application
│── routes/
│   └── weatherRoutes.py  # API route definitions
│── config.py             # Configuration (API keys, model paths)
│── requirements.txt      # Python dependencies
│── README.md             # Documentation (this file)
```

---

## 🔹 Setup Instructions

1. **Navigate to the backend folder**
   ```bash
   cd backend
   ```
2. **Create & activate virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask API**
   ```bash
   python app.py
   ```
5. **Test the API**

   - **Base URL:** http://127.0.0.1:5000
   - **Example endpoint:** `/predict`
   - **Method:** POST

   **Payload example:**
   ```json
   {
     "city": "Mumbai",
     "data": {
       "temperature_2m": 30,
       "relative_humidity_2m": 70,
       "pressure_msl": 1010,
       "wind_speed_10m": 28,
       "precipitation": 12
     }
   }
   ```

   **Response example:**
   ```json
   {
     "event": "Thunderstorm",
     "confidence": 0.87,
     "wind_speed": 32.5,
     "reason": "High precipitation + humidity"
   }
   ```

---

## 🔹 API Endpoints

- `POST /predict`: Takes weather data for a city, returns event classification and wind speed prediction.
  - **Input format:** JSON (see payload example above).
  - **Output:** JSON with event, confidence, wind speed, and reason.

---

## 🔹 Requirements

See `requirements.txt` for the full list of dependencies. Key libraries:

- Flask
- Torch
- Numpy
- Pandas
- Scikit-learn

---

## 🔹 Notes

- Ensure model files (`lstm_class_multi.pth`, `lstm_reg_multi.pth`, `scaler.pkl`) are available. If large (>100MB), host externally (e.g., Google Drive) and update `config.py` with paths.
- This backend is designed for production use and can be integrated with the frontend or external apps.
- For demo purposes, use the `simulation/` folder.

---

## 🔹 License

This project is released under the MIT License.