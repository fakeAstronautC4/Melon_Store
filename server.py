# =====================================   IMPORTS  =========================================
from flask import Flask, render_template, redirect, flash, request, session
from melons import *
from customers import *
from forms import LoginForm
import jinja2
# from flask_login import login_required, login_user, logout_user


app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = jinja2.StrictUndefined  # for debugging purposes(?????????)

# ======================================  ROUTES  =========================================
@app.route('/')
def main():
    return render_template('base.html')


@app.route('/login', methods=['GET','POST'])
def login():
   form = LoginForm(request.form)
   if form.validate_on_submit():
      username = form.username.data
      password = form.password.data
      if username in customers and customers[username]['password'] == password :
         session['username'] = username
         flash(f"Welcome {username}.")
         return redirect('/melons')
      else:
         flash(f'Log in failed. Check your credentials and try again or register')
         return redirect('/login')

   return render_template("login.html", form=form)

@app.route('/logout')
def logout():
   del session['username']
   flash(f'You have successfully logged out')
   return redirect('/login')

@app.route('/melons')
def melons():
    # melon_list = melons.list_melons()
    melon_list = list_melons() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    return render_template('melons.html', melon_list = melon_list)


@app.route("/melon/<melon_id>")
def one_melon(melon_id):
   melon = melon_finder(melon_id)
   return render_template("one_melon.html", melon = melon)


@app.route("/add_to_cart/<melon_id>")
def add_to_cart(melon_id):
   if 'username' not in session:
      return redirect("/login")
   if 'cart' not in session:                  
      session['cart'] = {}   # ================================================????????????   
   cart = session['cart']
   cart[melon_id] = cart.get(melon_id, 0) + 1 


   session.modified = True
   flash(f"Melon {melon_id} successfully added to cart.")

   return redirect("/cart")


@app.route("/cart")
def show_shopping_cart():
   if 'username' not in session:
      return redirect("/login")
   else:
      melon_lst = []
      total = 0
      cart = session.get("cart", {})  # ================================================????????????

      for melon_id, qty in cart.items():
         melon = melon_finder(melon_id) # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
         print(melon)
         total_cost = melon.price * qty
         total += total_cost

         melon.quantity = qty
         melon.total_cost = total_cost
         
         melon_lst.append(melon)

   
      return render_template("cart.html", melon_lst=melon_lst, total = total)    


@app.errorhandler(404)
def notfound(e):
   return render_template('404.html')

@app.route("/empty-cart")
def empty_cart():
   session['cart'] = {}
   return redirect ("/cart")


# @app.route('/lll')
# @login_required
# def hhh():
#    return render_template('/lll')

# ======================================= TRIGGER =========================================
if __name__ == '__main__':
    app.env = 'development'
    app.run(debug = True, port = 9000, host= 'localhost') 