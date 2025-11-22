from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

app = FastAPI()

 # Define a Pydantic model for the expected webhook payload
class WebhookPayload(BaseModel):
    event_type: str
    data: dict
    # Add other fields as expected by the webhook sender

@app.post("/webhook")
async def receive_webhook(payload: WebhookPayload, request: Request):
    # Optional: Verify the webhook sender (e.g., using a secret or signature)
    # For example, if using a secret:
    # secret = request.headers.get("X-Webhook-Secret")
    # if sec
    # .
    # ret != "your_secret_key":
    #     raise HTTPException(status_code=403, detail="Unauthorized webhook")

    # Process the received webhook payload
    print(f"Received webhook event: {payload.event_type}")
    print(f"Webhook data: {payload.data}")

    # Perform actions based on the event type and data
    if payload.event_type == "payment_completed":
        # Handle payment completion logic
        pass
    elif payload.event_type == "user_created":
        # Handle new user creation logic
        pass

    return {"message": "Webhook received successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)