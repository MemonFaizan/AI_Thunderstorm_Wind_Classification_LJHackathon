# 🌩️ Thunderstorm & Gale Force Wind Simulation (Flask App)

This folder (`simulation/`) contains a **Flask-based demo application** that allows you to interactively test the trained LSTM models for weather event classification and wind speed prediction.  
The app provides a simple **web interface** where you can select a city and view predictions in real-time.

---

## 🔹 Features
- **Interactive Web Interface** → Select from predefined cities (Ahmedabad, Delhi, Mumbai, Bangalore).  
- **Event Classification** → Predicts whether conditions are **Normal**, **Strong Wind**, or **Thunderstorm**.  
- **Wind Speed Regression** → Forecasts expected wind speed using LSTM.  
- **Confidence Score** → Displays how confident the model is in its classification.  
- **Reason Explanation** → Short descriptive reason for the predicted outcome.  
- **Easy Setup** → Minimal steps to run locally.  

---

## 🔹 Folder Structure
```

simulation/
│── app.py                        # Main Flask simulation app
│── templates/
│   └── index.html                 # UI page (form + results)
│── lstm\_class\_multi.pth           # Trained classification model
│── lstm\_reg\_multi.pth             # Trained regression model
│── scaler.pkl                     # Scaler used during preprocessing
│── multi\_city\_labeled\_fixed.csv   # Sample dataset (for demo/testing)
│── requirements.txt               # Dependencies
│── README.md                      # Documentation (this file)

````

---

## 🔹 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/ThunderStorm_and_ForceWind_Classification_LJHackthone.git
cd ThunderStorm_and_ForceWind_Classification_LJHackthone/simulation
````

### 2. Create & activate virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000/
```

---

## 🔹 Usage

1. Start the Flask app.
2. Open the browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).
3. Select a city from the dropdown (Ahmedabad, Delhi, Mumbai, Bangalore).
4. The app fetches the latest 120 weather records for the selected city.
5. Predictions will be displayed:

   * **Event** (Normal / Wind / Thunderstorm)
   * **Confidence** score
   * **Predicted Wind Speed** (m/s)
   * **Reason** for prediction

---

## 🔹 Example Output

```
City: Mumbai
Event: Thunderstorm
Confidence: 0.87
Predicted Wind Speed: 32.5 m/s
Reason: High precipitation + humidity
```

---

## 🔹 Requirements

See `requirements.txt` for the full list of dependencies.
Key libraries include:

* Flask
* Torch
* Numpy
* Pandas
* Scikit-learn

---

## 🔹 Notes

* Ensure `lstm_class_multi.pth`, `lstm_reg_multi.pth`, and `scaler.pkl` are available in this folder.
* If model files are large (>100MB), consider hosting them on **Google Drive / OneDrive** and provide links here.
* This simulation app is meant for **demo and testing only**. The production backend is implemented separately in the main project.

---

## 🔹 License

This project is released under the **MIT License**.
