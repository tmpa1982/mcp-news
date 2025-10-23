import httpx
import logging

class NewsClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        pass

    async def get_headlines(self):
        logging.info("Fetching news headlines.")
        client = httpx.AsyncClient()
        url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={self.api_key}"
        response = await client.get(url)
        return response.json()
