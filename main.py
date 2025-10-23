import logging

from mcp.server.fastmcp import FastMCP

def main():
    mcp = FastMCP("news")
    logging.info("MCP server starting.")
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
