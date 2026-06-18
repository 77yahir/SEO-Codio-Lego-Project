from config import get_api_key
from rebrickable_client import RebrickableClient
import json
import pandas as pd
import sqlalchemy as db

def main():
  API_KEY = get_api_key()
  client = RebrickableClient(API_KEY)

  # colors = client.get_colors(1, 10)
  # print(json.dumps(colors, indent=4))

  millenium_Results = client.search_sets(search="Millennium")
  all_Sets_Result = client.search_sets()
  sql_Query = "SELECT Year, COUNT(*) AS Amount FROM rebrickableSets GROUP BY(year);"

  # Load API data into database
  df = pd.DataFrame.from_dict(all_Sets_Result['results'])

  engine = db.create_engine('sqlite:///sets_database.db')

  df.to_sql('rebrickableSets', con=engine, if_exists='replace', index=False)

  with engine.connect() as connection:
    query_result = connection.execute(db.text(sql_Query)).fetchall()
    print(pd.DataFrame(query_result))

if __name__ == "__main__":
  main()

