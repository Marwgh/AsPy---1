from bottle import get , view , request ,response

@get("/login")
@view("login.html")
def _():
  
  error = request.params.get("error")
  user_email = request.params.get("user_email")
  return  dict(error=error , user_email=user_email)


