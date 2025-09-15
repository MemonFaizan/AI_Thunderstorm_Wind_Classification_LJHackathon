from flask import Flask, render_template, request
import torch
import torch.nn as nn
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)

# LSTM Models
class LSTMClass(nn.Module):
    def __init__(self, input_size=6, hidden=50, num_classes=3):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden, batch_first=True)
        self.fc = nn.Linear(hidden, num_classes)
    def forward(self, x):
        _, (hn, _) = self.lstm(x)
        return self.fc(hn[-1])

class LSTMReg(nn.Module):
    def __init__(self, input_size=6, hidden=50):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden, batch_first=True)
        self.fc = nn.Linear(hidden, 1)
    def forward(self, x):
        _, (hn, _) = self.lstm(x)
        return self.fc(hn[-1])

# Load models and scaler
model_c = LSTMClass()
model_c.load_state_dict(torch.load('../lstm_class_multi.pth'))
model_c.eval()
model_r = LSTMReg()
model_r.load_state_dict(torch.load('../lstm_reg_multi.pth'))
model_r.eval()
scaler = pickle.load(open('../scaler.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def predict():
    cities = ['Ahmedabad', 'Delhi', 'Mumbai', 'Bangalore']
    coords = {'Ahmedabad': (23.07, 72.63), 'Delhi': (28.61, 77.21), 'Mumbai': (19.08, 72.87), 'Bangalore': (12.97, 77.59)}
    
    if request.method == 'POST':
        city = request.form['city']
        df = pd.read_csv('../multi_city_labeled_fixed.csv')
        sample_data = df[df['city'] == city][['temperature_2m', 'relative_humidity_2m', 'pressure_msl', 'wind_speed_10m', 'precipitation']].tail(120).values
        
        event_code = np.zeros((120, 1))
        X = np.hstack((event_code, scaler.transform(sample_data)))
        X_t = torch.tensor(X, dtype=torch.float32).unsqueeze(0)
        
        with torch.no_grad():
            probs = torch.softmax(model_c(X_t), dim=1).numpy()[0]
            wind_pred = model_r(X_t).numpy().flatten()[0]
        
        event = ['normal', 'wind', 'thunderstorm'][np.argmax(probs)]
        reason = "High precip + humidity" if event == 'thunderstorm' else "High wind speed" if event == 'wind' else "Stable conditions"
        
        return render_template('index.html', 
                             cities=cities, city=city, lat=coords[city][0], lon=coords[city][1],
                             event=event, confidence=float(max(probs)), wind_speed=float(wind_pred),
                             reason=reason, alert_class='success' if event == 'normal' else 'warning' if event == 'wind' else 'danger')
    
    return render_template('index.html', cities=cities)

if __name__ == '__main__':
    app.run(debug=True)