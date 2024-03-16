from fastapi import FastAPI, HTTPException
import requests
from app.utils import settings



app = FastAPI()

@app.post("/api/world-verify")
async def call_world_verify(body, headers):
    try:
        # Make the external API call using the param
        app_id = settings.world_app_id

        url = f"https://developer.worldcoin.org/api/v1/verify/{app_id}"

        response = requests.post(url, headers=headers, data=body)

        # Check if the request was successful
        if response.ok:
            # Return the response from the external API
            return response
        else:
            # Raise an HTTPException with appropriate status code and detail message
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from external API")

    except Exception as e:
        # Handle exceptions
        raise HTTPException(status_code=500, detail="Internal server error")