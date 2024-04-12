from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    df = pd.read_csv('cleaned_test_records_data.csv')

    rows = df.values.tolist()
    cols = df.columns.tolist()

    return render_template('index.html', rows=rows, cols=cols)

if __name__ == "__main__":
 app.run(host='0.0.0.0', port='8080') # indent this line
