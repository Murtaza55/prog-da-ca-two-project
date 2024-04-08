import requests
from bs4 import BeautifulSoup

# Cricket Test Matches Records
url = "https://www.espncricinfo.com/records/highest-career-batting-average-282910"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", class_="ds-table")

    if table:
        print("Table found!")
        
    else:
        print("Table not found!")

    data = []
        
    rows = table.find_all("tr")

    #selecting the whole class of the element to get the header row
    header_row = table.find("thead", class_="ds-bg-fill-content-alternate ds-text-left")
    print("Header row:", header_row)
    if header_row:
        column_names = [th.text.strip() for th in header_row]
        print("Column Names:", column_names)
        
    else:
        print("Header row not found!")

    for row in rows[1:]:
        columns = row.find_all("td")
        player_name = columns[0].text.strip()
        span = columns[1].text.strip()
        matches = int(columns[2].text.strip())
        innings = int(columns[3].text.strip())
        not_outs = int(columns[4].text.strip())
        runs = int(columns[5].text.strip())
        highest_score = columns[6].text.strip()
        average = float(columns[7].text.strip())
        bf = columns[8].text.strip()
        sr = columns[9].text.strip()
        centuries = int(columns[10].text.strip())
        fifties = int(columns[11].text.strip())
        zeros = int(columns[12].text.strip())
        fours = columns[13].text.strip()
        sixes = columns[14].text.strip()
        
        data.append({
            "Player": player_name,
            "Span": span,
            "Matches": matches,
            "Innings": innings,
            "Not Outs": not_outs,
            "Runs": runs,
            "Highest Score": highest_score,
            "Average": average,
            "Balls Faced": bf,
            "Strike Rate": sr,
            "100s": centuries,
            "50s": fifties,
            "0s": zeros,
            "4s": fours,
            "6s": sixes
        })

    # print(data)