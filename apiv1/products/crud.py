from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from sqlalchemy.engine import Result
from sqlalchemy import select

from .schemas import ProductCreate


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(
        Product.id
    )  # statement - выбираем продукты и сортируем их по id
    result: Result = await session.execute(
        stmt
    )  # берем результат из stmt и ожидаем пока сессия сделает execute из бд
    products = (
        result.scalar().all()
    )  # помещаем результат в продукт и берем все элементы по scalar
    return list(products)


async def get_product_id(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(
        Product, product_id
    )  # возвращаем продукт отсортированный по id


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(
        **product_in.model_dump()
    )  # преобразовываем входящее сообщение и распаковываем его
    session.add(product)  # добавляем продукт в сессию
    await session.commit()
    return product
