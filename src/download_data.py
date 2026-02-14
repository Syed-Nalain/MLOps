import os
import requests

def download_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    save_path = "data/raw/titanic.csv"
    
    if os.path.exists(save_path):
        print(f"Data already exists at {save_path}")
        return

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    print(f"Downloading data from {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print("Download complete.")
    else:
        print(f"Failed to download data. Status code: {response.status_code}")
        exit(1)

if __name__ == "__main__":
    download_data()
