from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy / Neon connection string
DATABASE_URL = "postgresql+psycopg://neondb_owner:npg_u0GVOSZ1kPjq@ep-red-dew-a41ffyk1-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


