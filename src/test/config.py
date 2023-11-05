from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

# for testing purpose

conn_str = URL.create(
    drivername="postgresql",
    username="admin",
    password="Admin2023!",
    host="localhost",
    database="fund_management_db_test",
    port=5432,
)


engine = create_engine(
    url=conn_str,
    pool_pre_ping=True,
)

session_factory = sessionmaker(
    bind=engine,
    autoflush=False,
)


def get_session():
    session = session_factory()
    try:
        yield session
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()
