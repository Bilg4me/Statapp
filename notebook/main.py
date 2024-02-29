import json
import pandas as pd
from pandas import json_normalize

def json_to_csv(json_file, csv_file):
    # Read JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Flatten the nested structure
    flat_data = []
    for entry in data['totalDataChart']:
        flat_data.append({'timestamp': entry[0], 'fee': entry[1]})

    for entry in data['totalDataChartBreakdown']:
        flat_data.append({'timestamp': entry[0], 'fee': list(entry[1]['ethereum'].values())[0]})
    # Convert flattened data to DataFrame
        
        
    df = pd.DataFrame(flat_data)

    # Save DataFrame to CSV file
    df.to_csv(csv_file, index=False)
    print(f"CSV file saved as {csv_file}")

# Example usage
json_file = 'notebook/data.json'
csv_file = 'notebook/data.csv'
json_to_csv(json_file, csv_file)
