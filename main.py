from mcp.server.fastmcp import FastMCP


mcp = FastMCP("IntroductionMCP")


@mcp.tool()
def greet(name: str) -> str:
    """Saúda uma pessoa pelo nome."""
    return f"Olá, {name}!"


if __name__ == "__main__":
    mcp.run()
