from sqlalchemy import create_engine, Column, Integer, TIMESTAMP, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()

class AttributeIssueCount(Base):
    __tablename__ = 'attribute_issue_count'
    issue_count_id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(Integer, nullable=False)
    integration_id = Column(Integer, nullable=False)
    meta_data_id = Column(Integer, nullable=False)
    created_month = Column(TIMESTAMP(timezone=True), nullable=False)
    issue_count = Column(Integer, nullable=False)
    issue_details = Column(JSON, nullable=False)
    data_set_id = Column(Integer, nullable=False)
    env_id = Column(Integer, nullable=False)

class DatasetIssueCount(Base):
    __tablename__ = 'dataset_issue_count'
    issue_count_id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(Integer, nullable=False)
    integration_id = Column(Integer, nullable=False)
    data_set_id = Column(Integer, nullable=False)
    created_month = Column(TIMESTAMP(timezone=True), nullable=False)
    issue_count = Column(Integer, nullable=False)
    issue_details = Column(JSON, nullable=False)
    env_id = Column(Integer, nullable=False)

class DatasourceIssueCount(Base):
    __tablename__ = 'datasource_issue_count'
    issue_count_id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(Integer, nullable=False)
    env_id = Column(Integer, nullable=False)
    integration_id = Column(Integer, nullable=False)
    created_month = Column(TIMESTAMP(timezone=True), nullable=False)
    issue_count_dataset_level = Column(Integer, nullable=False)
    issue_details_dataset_level = Column(JSON, nullable=False)
    issue_count_attribute_level = Column(Integer, nullable=False)
    issue_details_attribute_level = Column(JSON, nullable=False)
db_url = 'postgresql+psycopg2://postgres:sugu2002@localhost:5433/sugumar'
engine = create_engine(db_url, echo=True)
Base.metadata.create_all(bind=engine)
attribute_issue_count_data = [
    (1664, 2566, 322384, '2023-11-01 00:00:00.000000', 1, '{"44961": 1}', 55396, 1485),
    (1664, 2566, 322386, '2023-11-01 00:00:00.000000', 2, '{"44961": 1, "44982": 1}', 55396, 1485),
    (1664, 2566, 322388, '2023-11-01 00:00:00.000000', 1, '{"44961": 1}', 55396, 1485),
    (1664, 2566, 322382, '2023-11-01 00:00:00.000000', 1, '{"44967": 1}', 55396, 1485),
    (1664, 2566, 322383, '2023-11-01 00:00:00.000000', 1, '{"44961": 1}', 55397, 1485),
    (1664, 2566, 322385, '2023-11-01 00:00:00.000000', 2, '{"44961": 1, "44982": 1}', 55397, 1485),
    (1664, 2566, 322387, '2023-11-01 00:00:00.000000', 1, '{"44961": 1}', 55397, 1485),
    (1664, 2566, 322393, '2023-11-01 00:00:00.000000', 1, '{"44967": 1}', 55397, 1485),
]

Session = sessionmaker(bind=engine)
session = Session()

for data in attribute_issue_count_data:
    session.add(AttributeIssueCount(
        tenant_id=data[0],
        integration_id=data[1],
        meta_data_id=data[2],
        created_month=data[3],
        issue_count=data[4],
        issue_details=data[5],
        data_set_id=data[6],
        env_id=data[7]
    ))
dataset_issue_count_data = [
    (1664, 2566, 55396, '2023-11-01 00:00:00.000000', 3, '{"44961": 1, "44967": 1, "44982": 1}', 1485),
    (1664, 2566, 55397, '2023-11-01 00:00:00.000000', 3, '{"44961": 1, "44967": 1, "44982": 1}', 1485),
]

for data in dataset_issue_count_data:
    session.add(DatasetIssueCount(
        tenant_id=data[0],
        integration_id=data[1],
        data_set_id=data[2],
        created_month=data[3],
        issue_count=data[4],
        issue_details=data[5],
        env_id=data[6]
    ))
session.commit()
integration_ids = [322384, 322386, 322388, 322382, 322383, 322385, 322387, 322393]

for integration_id in integration_ids:
    attribute_counts = (
        session.query(
            func.sum(AttributeIssueCount.issue_count).label('issue_count_attribute_level'),
            func.jsonb_object_agg(func.cast(AttributeIssueCount.issue_details, JSON).cast(JSON), AttributeIssueCount.issue_count).label('issue_details_attribute_level')
        )
        .filter(AttributeIssueCount.integration_id == integration_id)
        .group_by(AttributeIssueCount.data_set_id)
        .all()
    )

    total_issue_count_attribute_level = sum(entry.issue_count_attribute_level for entry in attribute_counts)
    total_issue_details_attribute_level = {}
    for entry in attribute_counts:
        total_issue_details_attribute_level.update(entry.issue_details_attribute_level)
    dataset_counts = (
        session.query(
            func.sum(DatasetIssueCount.issue_count).label('issue_count_dataset_level'),
            func.jsonb_object_agg(func.cast(DatasetIssueCount.issue_details, JSON).cast(JSON), DatasetIssueCount.issue_count).label('issue_details_dataset_level')
        )
        .filter(DatasetIssueCount.integration_id == integration_id)
        .group_by(DatasetIssueCount.data_set_id)
        .all()
    )

    total_issue_count_dataset_level = sum(entry.issue_count_dataset_level for entry in dataset_counts)
    total_issue_details_dataset_level = {}
    for entry in dataset_counts:
        total_issue_details_dataset_level.update(entry.issue_details_dataset_level)
    datasource_issue_count_entry = DatasourceIssueCount(
        tenant_id=1664,
        env_id=1485,
        integration_id=integration_id,
        created_month='2023-11-01 00:00:00.000000',
        issue_count_dataset_level=total_issue_count_dataset_level,
        issue_details_dataset_level=total_issue_details_dataset_level,
        issue_count_attribute_level=total_issue_count_attribute_level,
        issue_details_attribute_level=total_issue_details_attribute_level
    )

    session.add(datasource_issue_count_entry)
session.commit()

