from fastapi import FastAPI

app = FastAPI(title="Customer Onboarding AI")


@app.get("/")
def root():
    return {
        "message": "Customer Onboarding AI is running!"
    }