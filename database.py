

# Engine → connection to database 🔌
# Session → a conversation with the database 💬
# sessionmaker → a factory that creates sessions 🏭

# Why not directly use Session?
# You don’t want to manually configure session every time
# sessionmaker stores config once, then reuses it
# Clean + reusable + scalable

# A session:
# tracks objects you added/modified
# queues SQL operations
# sends them to DB at the right time

# What a session actually does
# Inside a session, you can:

# db.add(obj)        # insert
# db.query(Model)    # read
# db.commit()        # save changes
# db.refresh(obj)    # sync with DB
# db.delete(obj)     # delete

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://manoj@localhost:5432/manoj"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False ,autoflush = False, bind = engine)

