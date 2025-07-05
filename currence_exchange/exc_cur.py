from flask import Flask , render_template, request, redirect, url_for, flash # render_template - HTML
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import io
import base64
import matplotlib.pyplot as plt  
import matplotlib.dates as mdates


app = Flask(__name__)  #create obj
app.secret_key = 'mysecretkey' # from flash-massages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gold_cur.db' #sqlite - type, gold_cur.db - name

db =SQLAlchemy(app) #create object BD

ALLOWER_CURRENCIES = ['EUR','GBR','CNY'] #use only 3 currency


class Currence(db.Model):  #create class BD
    id = db.Column(db.Integer, primary_key = True)
    currency = db.Column(db.String(50), nullable = False)
    price_in_dollar = db.Column(db.Float, nullable = False)
    date = db.Column(db.DateTime, default = datetime.utcnow)

@app.route('/')
def base_page():
    latest = {}
    current_data = {}
    for cur in ALLOWER_CURRENCIES:
        entry = Currence.query.filter_by(currency=cur).order_by(Currence.date.desc()).first() #filter, last cur
        if entry:
            latest[cur] = entry

        data = Currence.query.filter_by(currency=cur).order_by(Currence.date.asc()).limit(30).all()
        current_data[cur] = data

    img = io.BytesIO()
    plt.figure(figsize = (10,5))

    for cur in ALLOWER_CURRENCIES:
        data = current_data[cur]
        if not data:
            continue  # if not cur - contin
        dates = [e.date for e in data]
        prices = [e.price_in_dollar for e in data]
        plt.plot(dates, prices, marker='o', label=cur) 

    plt.title("Currency Trends (Last 30 records)")
    plt.xlabel("Date")
    plt.ylabel("Price in USD")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d')) # x - date

    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode() #for imput in html

    return render_template("base_page.html", latest=latest, plot_url=plot_url)


@app.route('/add', methods = ['GET', 'POST'])
def page_add():
    if request.method == 'POST':
        name = request.form['currency'].strip().upper()
        price = request.form['price']
        
        if not name or not price:
            flash('fill in the fields','error')
            return redirect(url_for('page_add'))

        if name not in ALLOWER_CURRENCIES :
            flash('enter only "EUR","GBR","CNY"','error')
            return redirect(url_for('page_add'))

        try:
            new_entry = Currence(currency=name, price_in_dollar=float(price))
            db.session.add(new_entry)
            db.session.commit()
            flash('Currency added', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f"Database error:{e}", "error")

        return redirect(url_for('page_add'))
    return render_template('add_page.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    entry = Currence.query.get_or_404(id)

    if request.method == 'POST':
        try:
            entry.price_in_dollar = float(request.form['price'])
            db.session.commit()
            flash("Updated successfully!", "success")
            return redirect(url_for('base_page'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {e}", "error")
            return redirect(url_for('edit', id=id))

    return render_template("edit.html", entry=entry)


@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    entry = Currence.query.get_or_404(id)
    try:
        db.session.delete(entry)
        db.session.commit()
        flash("Deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Delete error: {e}", "error")

    return redirect(url_for('base_page'))


if __name__ == "__main__":
    app.run(debug=True)