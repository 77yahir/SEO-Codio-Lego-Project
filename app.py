from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from config import get_api_key
from rebrickable_client import RebrickableClient
from forms import RegistrationForm
import git

app = Flask(__name__)

app.config['SECRET_KEY'] = get_api_key()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(20), unique=True, nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   password = db.Column(db.String(60), unique=True, nullable=False)

   def __repr__(self):
      return f"User('{self.username}', '{self.email}')"
   
with app.app_context():
   db.create_all()

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/dashboard")
def dashboard():
  return render_template("dashboard.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationForm()

  if form.validate_on_submit(): # checks if entires are valid
    flash(f'Account created for {form.username.data}!', 'success')

    user = User(username=form.username.data, email=form.email.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('home'))
  
  return render_template("register.html", form=form)
    

# @app.route("/load-sets")
# def load_sets():
#   API_KEY = get_api_key()
#   client = RebrickableClient(API_KEY)

#   all_sets_result = client.search_sets()

#   df = pd.DataFrame.from_dict(all_sets_result['results'])

#   engine = db.create_engine('sqlite:///sets_database.db')

#   df.to_sql('rebrickableSets', con=engine, if_exists='replace', index=False)

#   return "Sets loaded into database!"

# @app.route("/sets-by-year")
# def sets_by_year():
#   engine = db.create_engine('sqlite:///sets_database.db')

#   sql_query = """
#   SELECT Year, COUNT(*) AS Amount
#   FROM rebrickableSets
#   GROUP BY Year;
#   """

#   with engine.connect() as connection:
#     query_result = connection.execute(db.text(sql_query)).fetchall()

#   return render_template("sets_by_year.html", results=query_result)

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/LegoSearch/SEO-Codio-Lego-Project')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

if __name__ == "__main__":
  app.run(debug=True)


