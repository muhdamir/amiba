from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

from config import database, drivername, host, password, port, username

conn_str = URL.create(
    drivername=drivername,
    username=username,
    password=password,
    host=host,
    database=database,
    port=port,
)

print(conn_str)

engine = create_engine(
    url=conn_str,
    pool_pre_ping=True,
    echo=True,
    echo_pool=True,
)

session_factory = sessionmaker(
    bind=engine,
    autoflush=False,
)


async def get_session():
    """
    To be used along with fastapi's dependency injection
    """
    session = session_factory()
    try:
        yield session
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()
