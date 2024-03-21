import requests
import csv

league_ids = [39, 78, 61, 140, 135, 203, 2, 3]

base_url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

query_params = {
    "season": "2023",
    "from": "2023-08-01",
    "to": "2024-03-09"
}

headers = {
    "X-RapidAPI-Key": "3a6668fab9msh80dac915bfb5ee1p14135djsn7f1e975ec930",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

all_fixtures_data = []

for league_id in league_ids:
    query_params["league"] = league_id
    
    response = requests.get(base_url, headers=headers, params=query_params)

    if response.status_code == 200:
        fixtures_data = response.json().get('response', [])
        all_fixtures_data.extend(fixtures_data)  
    else:
        print(f"Error retrieving data for league ID {league_id}: {response.status_code}, {response.text}")

csv_file_path = "fixtures_data.csv"

if all_fixtures_data:
    csv_header = all_fixtures_data[0].keys()

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_header)
        writer.writeheader()
        for item in all_fixtures_data:
            writer.writerow(item)

    print(f"Data has been successfully written to {csv_file_path}")
else:
    print("No fixtures data available.")
