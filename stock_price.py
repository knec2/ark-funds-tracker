import config
import alpaca_trade_api as tradeapi
import psycopg2
import psycopg2.extras
connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
api = tradeapi.REST(config.API_KEY, config.API_SECRET,config.API_URL)   
cursor = connection.cursor() 
assets = api.list_assets()

cursor.execute("""SELECT * FROM stock""")

   

connection.commit()