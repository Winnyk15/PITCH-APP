from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail



login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

#<<added this lines
app = Flask(__name__ )


#database url from https://data.heroku.com/datastores/b7ccc52e-18b9-4072-b498-5d0de81e7a5f#administration setting 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://dpinhyejcurryu:b5a93b86d0144606e7ed0bb646ea370638c540c016ee841545822ad51f10cc0b@ec2-54-158-122-162.compute-1.amazonaws.com:5432/d5ptlprq1btrh9"

app.config['SECRET_KEY'] = "KJBJBJHBjksdooqpsdtywdncnmzloTUHUIHKNKBJVJ" # secret key combinations
app.config['MAIL_USERNAME'] = 'kahendahwinnie@gmail.com' # email to be used to send mails
app.config['MAIL_PASSWORD'] = 'Oyollo2030' # password of the email
#end>>


#<<modified this
db = SQLAlchemy(app)
  #end>>

photos = UploadSet('photos', IMAGES)
mail = Mail()
# Initializing application
def create_app(config_name):
    ## commented this line
    #app = Flask(__name__ )
    
    
    #Initializing extensions
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap = Bootstrap(app)
    mail.init_app(app)
    
    
   
    

    #setting up configuration
    if config_options is None:
        app.config.from_object(config_options[config_name])
        app.config.from_object(configure_uploads(app, photos))
    else:
        app.config.from_object(config_options)
        db.init_app(app)
    
   
    
    #registering a blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')
    
    
    
    #will return the app
    return app
