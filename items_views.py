from fastapi import APIRouter

router = APIRouter(prefix="/items",tags=["items"])

@router.get("/")
async def get_items(item: str):
    return item

@router.get("/{item_id}")
async def get_items_id(item: str):
    return item

@router.get("/latest/")
async def get_items_id(item: str):
    return item

@router.post("/{item_id}")
async def post_items(item: str):
    return item

@router.delete("/{item_id}")
async def del_items_id(item: str):
    return item