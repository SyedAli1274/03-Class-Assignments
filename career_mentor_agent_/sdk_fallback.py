# sdk_fallback.py

def agent(func):
    # Ye decorator kuch nahi karega — sirf function ko return karega
    return func

def tool(func):
    return func
