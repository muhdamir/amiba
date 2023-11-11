import json
from contextlib import contextmanager

import pytest
from faker import Faker
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from domain.entities import Base, Fund, FundManager
from infrastructure.database import get_session
from main import app

from ..config import engine
from ..config import get_session as get_session_testing
from ..factory import FactoryFund, FactoryFundManager

app.dependency_overrides[get_session] = get_session_testing

# provide fake detail
fake = Faker()
client = TestClient(app)


@pytest.fixture
def init_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def fund_endpoint():
    return "/api/v1/fund"


@pytest.fixture
def session():
    with contextmanager(get_session_testing)() as test_session:
        yield test_session


def test_get_fund_empty_array(
    fund_endpoint: str,
    init_database,
):
    response = client.get(fund_endpoint)
    # test status code
    assert response.status_code == 200
    # test response body
    assert response.json() == []


def test_get_fund_with_entry(
    fund_endpoint,
    init_database,
    session: Session,
):
    # set FundManager
    factory_fund_manager = FactoryFundManager(session=session)
    fund_manager = factory_fund_manager()

    # set Fund
    factory_fund = FactoryFund(
        session=session,
        fund_manager_id=fund_manager.fund_manager_id,
    )
    fund = factory_fund()

    valid_data = [
        {
            "fundId": fund.fund_id,
            "fundName": fund.fund_name,
            "fundManagerId": fund.fund_manager_id,
            "fundDescription": fund.fund_description,
            "fundDateOfCreation": str(fund.fund_date_of_creation),
            "fundDateOfUpdate": str(fund.fund_date_of_update),
            "fundPerformance": fund.fund_performance,
            "fundManager": {
                "fundManagerId": fund_manager.fund_manager_id,
                "fundManagerName": fund_manager.fund_manager_name,
                "fundManagerEmail": fund_manager.fund_manager_email,
                "dateCreatedOn": str(fund_manager.date_created_on),
                "dateUpdatedOn": str(fund_manager.date_updated_on),
            },
        }
    ]

    response = client.get(fund_endpoint)
    assert response.status_code == 200
    assert response.json() == valid_data


def test_create_fund(
    fund_endpoint,
    init_database,
    session: Session,
):
    # set FundManager
    factory_fund_manager = FactoryFundManager(session=session)
    fund_manager = factory_fund_manager()

    post_data = {
        "fundName": "demo fund",
        "fundManagerId": fund_manager.fund_manager_id,
        "fundDescription": "string",
        "fundPerformance": 0,
    }

    a = client.post(fund_endpoint, json=post_data)
    assert a.status_code == 200
    assert a.json()["fundName"] == "demo fund"
