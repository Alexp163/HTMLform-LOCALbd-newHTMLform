from fastapi import APIRouter, status, Depends
from schema import PacientDataCreateSchema, PacientDataReadSchema
from load_data_pacient import SaveDataPacient


router2 = APIRouter(tags=["save_data"], prefix="/save_data")


@router2.post("/create_data_pacient", status_code=status.HTTP_201_CREATED, 
              response_model=PacientDataReadSchema)
async def save_data(pacient: PacientDataCreateSchema, 
                    repository: SaveDataPacient = Depends(SaveDataPacient)) -> PacientDataReadSchema:
    return repository.create_data_pacient(pacient)

