import requests
from app.core.news_config import NEWS_API_KEY

url = f"https://newsdata.io/api/1/latest?apikey={NEWS_API_KEY}&country=us&language=en"

headers = {
    "Authorization": f"Bearer {NEWS_API_KEY}",
    "Content-Type": "application/json"
}

def get_news():
    print("Getting news...\n")
    try:
        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            #debug and visualize purpose
            for article in data["results"]:
                print(f"Article: {article["category"]}")
                
            return data["results"]
        
        else:
            print(f"Failed fetching: {response.status_code} \n {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"A network error occurred: {e}")

if __name__ == "__main__":
    get_news()
