import logging

from mcp.server.fastmcp import FastMCP

from news_client import NewsClient

def main():
    news_client = NewsClient()
    mcp = FastMCP("news")
    @mcp.tool()
    async def fetch_news():
        return news_client.get_headlines()

    logging.info("MCP server starting.")
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
