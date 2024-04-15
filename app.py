from flask import Flask, request, render_template
import pandas as pd
import sqlite3
import plotly.graph_objs as go
from plotly.offline import plot

app = Flask(__name__)

df = pd.read_csv('cleaned_test_records_data.csv')

df_top_10_highest_top_scorers = df.nlargest(10, 'Highest_Score')[['Player', 'Highest_Score']].reset_index(drop=True)
df_top_10_highest_strike_rates = df.nlargest(10, 'Strike_Rate')[['Player', 'Strike_Rate']].reset_index(drop=True)
df_top_10_highest_batting_averages = df.nlargest(10, 'Batting_Average')[['Player', 'Batting_Average']].reset_index(drop=True)

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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS highest_top_scorers (
            Player TEXT,
            Highest_Score INTEGER
        )
    ''')
    df_top_10_highest_top_scorers.to_sql('highest_top_scorers', conn, if_exists='replace', index=False)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS highest_batting_averages (
            Player TEXT,
            Batting_Average REAL
        )
    ''')
    df_top_10_highest_batting_averages.to_sql('highest_batting_averages', conn, if_exists='replace', index=False)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS highest_strike_rates (
            Player TEXT,
            Strike_Rate REAL
        )
    ''')
    df_top_10_highest_strike_rates.to_sql('highest_strike_rates', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

def fetch_all_test_records():
    conn = sqlite3.connect('cricket_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM test_cricket_records")
    data_from_db = cursor.fetchall()

    return data_from_db

def fetch_top_scorer_data():
    conn = sqlite3.connect('cricket_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM highest_top_scorers")
    top_scorer_data = cursor.fetchall()
    conn.close()

    columns = ['Player', 'Highest_Score']
    top_scorer_df = pd.DataFrame(top_scorer_data, columns=columns)

    return top_scorer_df

def fetch_batting_averages_data():
    conn = sqlite3.connect('cricket_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM highest_batting_averages")
    batting_averages_data = cursor.fetchall()
    conn.close()

    columns = ['Player', 'Batting_Average']
    batting_averages_df = pd.DataFrame(batting_averages_data, columns=columns)

    return batting_averages_df

def fetch_strike_rate_data():
    conn = sqlite3.connect('cricket_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM highest_strike_rates")
    strike_rates_data = cursor.fetchall()
    conn.close()

    columns = ['Player', 'Strike_Rate']
    strike_rates_df = pd.DataFrame(strike_rates_data, columns=columns)

    return strike_rates_df

#routes

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

#Route to fetch the data from database
@app.route('/data_fetched_from_db')
def route_fetch_all_test_records():
    data = fetch_all_test_records()
    data_df = pd.DataFrame(data)
    rows = data_df.values.tolist()
    cols = df.columns.tolist()
    # return 'data returning'
    return render_template('cleaned_data.html', rows=rows, cols=cols)

@app.route('/test_records_analysis')
def route_fetch_top_scorer_data():
    return render_template('cricket_data_analysis.html')

# To fetch top scorers from db for graph and set route
@app.route('/render_top_scorer_graph')
def route_render_top_scorer_graph():
    data = fetch_top_scorer_data()
    data_df = pd.DataFrame(data)
    print(data_df)

    trace = go.Bar(
        x=data_df['Player'],
        y=data_df['Highest_Score'],
        marker=dict(color='#3C7DFF')
    )
    layout = go.Layout(
        title='Top 10 Players with Highest Scores in Test',
        xaxis=dict(title='Player'),
        yaxis=dict(title='Highest Score')
    )
    fig = go.Figure(data=[trace], layout=layout)

    # Save plot as HTML file
    plot(fig, filename='templates/top_10_players_scores.html', auto_open=False)
    return render_template('top_10_players_scores.html')

#fetch batting averages from db for graph and set route
@app.route('/render_batting_averages_graph')
def route_render_top_batting_avg_graph():
    data = fetch_batting_averages_data()
    data_df = pd.DataFrame(data)
    print(data_df)

    trace = go.Bar(
        x=data_df['Player'],
        y=data_df['Batting_Average'],
        marker=dict(color='#79ccb3')
    )
    layout = go.Layout(
        title='Top 10 Players with Highest Batting Average in Test',
        xaxis=dict(title='Player'),
        yaxis=dict(title='Batting Average')
    )
    fig = go.Figure(data=[trace], layout=layout)

    # Save plot as HTML file
    plot(fig, filename='templates/top_10_batting_averages.html', auto_open=False)
    return render_template('top_10_batting_averages.html')

# route for strike rates graph
@app.route('/render_strike_rates_graph')
def route_render_top_strike_rate_graph():
    data = fetch_strike_rate_data()
    data_df = pd.DataFrame(data)
    print(data_df)


    trace = go.Bar(
        x=data_df['Player'],
        y=data_df['Strike_Rate'],
        marker=dict(color='#e9724d')
    )
    layout = go.Layout(
        title='Top 10 Players with Highest Strike Rate in Test',
        xaxis=dict(title='Player'),
        yaxis=dict(title='Strike Rate')
    )
    fig = go.Figure(data=[trace], layout=layout)

    # Save plot as HTML file
    plot(fig, filename='templates/top_10_strike_rates.html', auto_open=False)
    return render_template('top_10_strike_rates.html')

if __name__ == "__main__":
    #port for local server
    # app.run(port=5000, debug=True)

    #port for flask server
    app.run(host='0.0.0.0', port='8080')
