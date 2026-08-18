from typing import List

from fastapi import APIRouter,Depends, File, UploadFile,status

from auth import get_current_user
from controllers.add_controller import get_states, get_districts, upload_bookdata
from schema.state_schema import StateSchema
from schema.district_schema import DistrictSchema

router = APIRouter(prefix="/api/v1", tags=["AddListing"])

@router.get(
    '/location/states',
    response_model = List[StateSchema],
    status_code = status.HTTP_200_OK,
    summary = "Fetch all Indian states.",
)
async def fetch_states():
    return await get_states()


@router.get("/location/districts/{state}",
            response_model = List[DistrictSchema],
            status_code = status.HTTP_200_OK,
            summary = "Fetch all Indian cities based on States")
async def fetch_districts(state: str):
    return await get_districts(state)


@router.post("/book")
async def add_book():
    return await upload_bookdata()
    
    
