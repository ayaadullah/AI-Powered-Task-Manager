from fastapi import FastAPI

app = FastAPI(
    title="AI-Powered Task Manager API",
    version="0.1.0",
    description="Backend API for the AI-Powered Task Manager.",
)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
