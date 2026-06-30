from flask import Flask
from config import get_api_key
from rebrickable_client import RebrickableClient
import json
import pandas as pd
import sqlalchemy as db

app = Flask(__name__)

@app.route("/")
def home():
  return "Lego Flask app is running!"

@app.route("/load-sets")
def load_sets():
  API_KEY = get_api_key()
  client = RebrickableClient(API_KEY)

  all_sets_result = client.search_sets()

  df = pd.DataFrame.from_dict(all_sets_result['results'])

  engine = db.create_engine('sqlite:///sets_database.db')

  df.to_sql('rebrickableSets', con=engine, if_exists='replace', index=False)

  return "Sets loaded into database!"

@app.route("/sets-by-year")
def sets_by_year():
  engine = db.create_engine('sqlite:///sets_database.db')

  sql_query = """
  SELECT Year, COUNT(*) AS Amount
  FROM rebrickableSets
  GROUP BY Year;
  """

  with engine.connect() as connection:
    query_result = connection.execute(db.text(sql_query)).fetchall()

  results = []
  for row in query_result:
    results.append({
      "Year": row[0],
      "Amount": row[1]
    })

  return results

if __name__ == "__main__":
  app.run(debug=True)

  
  # colors = client.get_colors(1, 10)
  # print(json.dumps(colors, indent=4))

