HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = "root"
PASSWORD = ""
DATABASE = "zhiliaooa"

DB_URI = f"mysql+pymysql://{ USERNAME }:{ PASSWORD }@{ HOSTNAME }:{ PORT }/{ DATABASE }?charset=utf8mb4"

SQLALCHEMY_DATABASE_URI = DB_URI