from fastapi import FastAPI

from backend.api.customers import router as customers_router


app = FastAPI(title="Customer Onboarding AI")


@app.get("/")
def root():
    return {
        "message": "Customer Onboarding AI is running!"
    }


app.include_router(customers_router)