from dotenv import load_dotenv
import os

load_dotenv()

env = os.environ

# database config
drivername = env.get("drivername", "sqlite")
username = env.get("db_username")
password = env.get("password")
host = env.get("host")
database = env.get("database")
port = int(temp_port) if (temp_port := env.get("port")) else None
