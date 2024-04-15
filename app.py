from flask import Flask, request, render_template
import pandas as pd
import sqlite3
app = Flask(__name__)

df = pd.read_csv('cleaned_test_records_data.csv')

def create_database():
    conn = sqlite3.connect('cricket_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS test_cricket_records (
            Player TEXT,
            Matches INTEGER,
            Inns INTEGER,
            Not_Outs INTEGER,
            Runs INTEGER,
            Highest_Score INTEGER,
            Batting_Average REAL,
            Balls_Faced INTEGER
            Strike_Rate REAL
            Hundreds INTEGER
            Fifties INTEGER
            Zeros INTEGER
            Fours INTEGER
            Sixes INTEGER
            Start_Year INTEGER
            Final_Year INTEGER
            Country TEXT
        )
    ''')
    df.to_sql('test_cricket_records', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

def fetch_data_from_db():
    conn = sqlite3.connect('cricket_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM test_cricket_records")
    data_from_db = cursor.fetchall()

    return data_from_db

#Route to fetch the data from database
@app.route('/data_fetched_from_db')
def route_fetch_data_database():
    data = fetch_data_from_db()
    data_df = pd.DataFrame(data)
    rows = data_df.values.tolist()
    cols = df.columns.tolist()
    # return 'data returning'
    return render_template('cleaned_data.html', rows=rows, cols=cols)

# Route to create the database
@app.route('/create_database')
def route_create_database():
    create_database()
    return 'Database created successfully!'

@app.route('/', methods=['GET'])
def home_page():
    df = pd.read_csv('cleaned_test_records_data.csv')

    rows = df.values.tolist()
    cols = df.columns.tolist()

    return render_template('index.html', rows=rows, cols=cols)

if __name__ == "__main__":
    #port for local server
    # app.run(port=5000, debug=True)

    #port for flask server
    app.run(host='0.0.0.0', port='8080')
