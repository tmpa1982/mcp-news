import logging
import os

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from news_client import NewsClient

load_dotenv()

def main():
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        raise ValueError("NEWS_API_KEY environment variable not set.")
    news_client = NewsClient(api_key=api_key)
    mcp = FastMCP("news")
    @mcp.tool()
    async def fetch_news():
        return await news_client.get_headlines()

    logging.info("MCP server starting.")
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
