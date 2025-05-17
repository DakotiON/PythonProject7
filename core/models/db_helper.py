from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)

from core.config import settings


class DatabaseHelper:

    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
            autocommit=False,
        )

    def get_scoped_session(self):  # помощьник для создание scoped сессии
        session = async_scoped_session(
            session_factory=self.session_factory,  # передаем фабрику сессий
            scopefunc=current_task,  # передаем текущую задачу
        )
        return session

    # Нужна чтобы создавать подключение к бд во воремя запроса
    async def session_dependency(
        self,
    ) -> AsyncSession:  # метод создания сессии для каждого запроса
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(
        self,
    ) -> AsyncSession:
        session = self.get_scoped_session()  # метод создания сессии для каждого запроса
        yield session
        await session.remove()


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)
