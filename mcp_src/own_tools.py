from mcp.server.fastmcp import FastMCP
import logging

mcp = FastMCP("Demo")

@mcp.tool()
def add(a:int , b:int) -> int:
    """ add the two number a and b and return"""
    try:

        return a + b
    except Exception as e:
        logging.error("the error is >>> ")

@mcp.tool()
def increment(n: int) -> int:
    """Add 1 to the given number"""
    logging.info("adddderere 222")
    return n + 1

@mcp.resource("greeting://{msg}")
def greating_msg(msg: str) -> str:
    """ Print your message """
    return f"this is your msg {msg}"


@mcp.prompt()
def write_email(recipient: str, topic: str) -> str:
    """Template for writing professional emails"""
    return f"""
    Write a professional email to {recipient} about {topic}.
    
    Include:
    - Friendly greeting
    - Clear purpose
    - Professional closing
    """


if __name__ == "__main__":
    # mcp.run(transport="streamable-http")
    mcp.run(transport="stdio")


# mcp dev main.py