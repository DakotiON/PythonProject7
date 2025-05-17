from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .crud import update_product_partial
from .schemas import Product, ProductCreate, ProductUpdate

router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.post(
    "/",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}/", response_model=Product)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    product = await crud.get_product_id(session=session, product_id=product_id)
    if product is not None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found",
    )


@router.patch("/{product_id}/")
async def update_product_partial(
    product_update: ProductUpdate,
    product_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    product = await crud.get_product_id(session=session, product_id=product_id)
    if product is not None:
        return await crud.update_product_partial(
            session=session,
            product=product,
            product_update=product_update,
        )


@router.delete(
    "/{product_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_product(
    product_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    product = await crud.get_product_id(session=session, product_id=product_id)
    if product is not None:
        await crud.delete_product(session=session, product=product)
    return await crud.get_products(session=session)
