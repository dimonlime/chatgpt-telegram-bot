# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
#
# engine = create_async_engine(url="sqlite+aiosqlite:////var/gnd/database/db.sqlite3")
#
# async_session = async_sessionmaker(engine)
#
#
# class Base(AsyncAttrs, DeclarativeBase):
#     __abstract__ = True
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#
#
# async def async_main():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
