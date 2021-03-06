from bottle import  default_app , run , get , post , view ,static_file





#################################################################
import updating_validation_post                           #POST
import delete_post                                        #POST
import signup_post                                        #POST
import login_post                                         #POST

import updating_get                                       #GET
import users_get                                          #GET
import login_get                                          #GET
import logout_get                                         #GET
import logingout_get                                      #GET
import signup_get                                         #GET
import tweet_get                                          #GET
#################################################################

@get("/")
@view("home.html")
def _():
  return 


#################################################################

@get("/app.css")
def _():
  return static_file("app.css" , root=".")

#################################################################


@get("/validator.js")
def _():
  return static_file("validator.js", root=".")
#################################################################


@get("/app.js")
def _():
  return static_file("app.js", root=".")
#################################################################



try:
  # Production
  import production
  application = default_app()
except:
  # Development
  run( host="127.0.0.1", port=3434, debug=True, reloader=True )