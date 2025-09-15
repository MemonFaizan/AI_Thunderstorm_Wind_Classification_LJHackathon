npm (v8 or higher)

# Frontend (Thunderstorm & Gale Force Wind Prediction UI)

This folder (`frontend/`) contains the web-based frontend for the Thunderstorm and Gale Force Wind Prediction system. Built with React, it provides a user-friendly interface to interact with the backend API and display weather predictions.

---

## 🔹 Features

- **Interactive UI** – Select a city and view weather predictions.
- **Real-time Results** – Displays event classification (Normal / Strong Wind / Thunderstorm), confidence score, and predicted wind speed.
- **Responsive Design** – Works on desktop and mobile browsers.
- **Tailwind CSS** – Clean and modern styling.

---

## 🔹 Folder Structure

```
frontend/
│── src/
│   ├── components/      # React components
│   ├── App.js           # Main React app
│   ├── index.js         # Entry point
│── public/
│   └── index.html       # HTML template
│── package.json         # Node dependencies and scripts
│── README.md            # Documentation (this file)
```

---

## 🔹 Setup Instructions

1. **Navigate to the frontend folder**
	```bash
	cd frontend
	```
2. **Install dependencies**
	```bash
	npm install
	```
3. **Start the development server**
	```bash
	npm start
	```
4. **Open in browser**
	- URL: http://localhost:3000
	- Ensure the backend API (backend/app.py) is running at http://127.0.0.1:5000.

---

## 🔹 Usage

1. Open http://localhost:3000 in your browser.
2. Select a city from the dropdown (e.g., Ahmedabad, Delhi, Mumbai, Bangalore).
3. Submit to fetch predictions from the backend API.
4. View results:
	- Predicted Event (Normal / Wind / Thunderstorm)
	- Confidence Score
	- Predicted Wind Speed (m/s)
	- Reason for prediction

---

## 🔹 Requirements

- Node.js (v16 or higher)
- npm (v8 or higher)
- See package.json for dependencies, including:
  - React
  - Axios (for API calls)
  - Tailwind CSS

---

## 🔹 Notes

- Ensure the backend API is running before starting the frontend.
- For demo purposes, use the `simulation/` folder for a standalone Flask-based UI.
- Environment variables (e.g., API URL) can be set in `.env` (not included in repo).

---

## 🔹 License

This project is released under the MIT License.