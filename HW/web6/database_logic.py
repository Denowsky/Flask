import databases
import sqlalchemy
from datetime import datetime

DATABASE_URL = "sqlite:///mydatabase.database"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer,
                      primary_key=True),
    sqlalchemy.Column("user_name", sqlalchemy.String(32), nullable=False),
    sqlalchemy.Column("user_surname", sqlalchemy.String(32), nullable=False),
    sqlalchemy.Column("user_email", sqlalchemy.String(128), nullable=False),
    sqlalchemy.Column("user_password", sqlalchemy.String(32), nullable=False)
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("order_id", sqlalchemy.Integer,
                      primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.user_id'), nullable=False),
    sqlalchemy.Column("good_id", sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('goods.good_id'), nullable=False),
    sqlalchemy.Column("data", sqlalchemy.Date(), default=datetime.utcnow),
    sqlalchemy.Column("status", sqlalchemy.String(32), nullable=False)
)

goods = sqlalchemy.Table(
    "goods",
    metadata,
    sqlalchemy.Column("good_id", sqlalchemy.Integer,
                      primary_key=True),
    sqlalchemy.Column("good_name", sqlalchemy.String(32), nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String(128), nullable=False),
    sqlalchemy.Column("price", sqlalchemy.Float(), nullable=False),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
