from mcp.server.fastmcp import FastMCP

def main():
    mcp = FastMCP("news")
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
