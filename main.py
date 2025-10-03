from fastapi import FastAPI, Request

app = FastAPI()

# temporary in-memory storage
hex_storage = []

@app.post("/sensor")
async def receive_data(request: Request):
    body = await request.json()
    hex_value = body.get("hex_value")

    if not hex_value:
        return {"status": "error", "message": "Missing hex_value"}

    hex_storage.append(hex_value)

    # optional: convert hex → string
    try:
        readable = bytes.fromhex(hex_value).decode("utf-8", errors="ignore")
    except Exception:
        readable = None

    return {
        "status": "ok",
        "hex_value": hex_value,
        "decoded": readable
    }

@app.get("/data")
async def get_data():
    return {"stored": hex_storage}
