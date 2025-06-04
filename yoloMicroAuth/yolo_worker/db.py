from sqlalchemy import create_engine, Column, Integer, String, Float, Table, MetaData
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///data/results.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

detections = Table(
    "detections", metadata,
    Column("id", Integer, primary_key=True),
    Column("label", String),
    Column("confidence", Float),
    Column("x1", Float),
    Column("y1", Float),
    Column("x2", Float),
    Column("y2", Float),
    Column("image_path", String)
)

metadata.create_all(engine)
Session = sessionmaker(bind=engine)
