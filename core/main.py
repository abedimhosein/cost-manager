from typing import Dict

from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Response,
    Body,
)
from fastapi.responses import JSONResponse

COSTS_DB: Dict[int, dict] = {}
LAST_COST_ID: int = 1

app = FastAPI()


@app.post("/costs/", description='Cost Create')
async def cost_create(amount: float = Body(...), description: str = Body(...)):
    global LAST_COST_ID

    new_cost = {
        'id': LAST_COST_ID,
        'amount': amount,
        'description': description,
    }
    COSTS_DB[LAST_COST_ID] = new_cost
    LAST_COST_ID += 1

    return new_cost


@app.put("/costs/{cost_id}/", description='Cost Update')
async def cost_update(cost_id: int, amount: float = Body(...), description: str = Body(...)):
    if cost_data := COSTS_DB.get(cost_id):
        cost_data.update({'amount': amount, 'description': description})
        return JSONResponse(content=cost_data, status_code=status.HTTP_200_OK)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='cost not found.')


@app.delete("/costs/{cost_id}/", description='Cost Delete')
async def cost_delete(cost_id: int):
    if cost_id in COSTS_DB:
        COSTS_DB.pop(cost_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='cost not found.')


@app.get("/costs/{cost_id}/", description='Cost Detail')
async def cost_detail(cost_id: int):
    if cost_data := COSTS_DB.get(cost_id):
        return cost_data

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='cost not found.')


@app.get("/costs/", description='Cost List')
async def cost_list():
    return list(COSTS_DB.values())
