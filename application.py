from flask import Flask, render_template, request
import sys

application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("index.html")

@application.route("/list")
def view_list():
    return render_template("list.html")

@application.route("/review")
def view_review():
    return render_template("review.html")

@application.route("/reg_items")
def reg_item():
    return render_template("reg_items.html")

@application.route("/reg_reviews")
def reg_review():
    return render_template("reg_reviews.html")

@application.route("/submit_item", methods=['POST'])
def reg_item_submit():
    if request.method == 'POST':
        name = request.form.get("name")
        seller = request.form.get("seller")
        addr = request.form.get("addr")
        email = request.form.get("email")
        category = request.form.get("category")
        card = request.form.get("card")
        status = request.form.get("status")
        phone = request.form.get("phone")
        
        print(name, seller, addr, email, category, card, status, phone)
    return render_template("reg_item.html")

@application.route("/submit_item_post", methods=['POST'])
def reg_item_submit_post():
<<<<<<< HEAD
    image_file = request.files["file"]
=======
    
    image_file=request.files["file"]
>>>>>>> a9345187ec02f7edeb216590e32401c70e6fa054
    image_file.save("static/images/{}".format(image_file.filename))
    data = request.form
    
    return render_template("submit_item_result.html", data=data, img_path="static/images/{}".format(image_file.filename))

<<<<<<< HEAD
if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
=======
if __name__=="__main__":
    application.run(host='0.0.0.0', debug=True)
>>>>>>> a9345187ec02f7edeb216590e32401c70e6fa054
