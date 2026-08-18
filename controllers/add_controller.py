import json
from typing import List
from pathlib import Path

from fastapi import HTTPException, UploadFile
from schema.state_schema import StateSchema
from schema.district_schema import DistrictSchema

JSON_FILE = Path(__file__).parent.parent / "india_states_and_districts.json"

with open(JSON_FILE, "r", encoding="utf-8") as file:
    locations = json.load(file)

async def get_states() -> List[StateSchema]:

    # JSON_FILE = Path(__file__).parent.parent / "india_states_and_districts.json"

    with open(JSON_FILE, "r", encoding="utf-8") as file:
        locations = json.load(file)
        return [
            {
              "id": item["id"],
              "name": item["name"]
            }
            for item in locations
            ]


async def get_districts(state:str) -> List[DistrictSchema]:
    for item in locations:

        if item["name"].lower() == state.lower():
            return item["districts"]

    raise HTTPException(
        status_code=404,
        detail="District not found"
    )

async def upload_bookdata(photos:List[UploadFile]):
    pass
