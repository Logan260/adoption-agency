from flask import Flask, render_template, redirect, url_for, jsonify
from models import db, Pet, app
from form import addPet, editPet

@app.route("/")
def pet_list():
    pets = Pet.query.all()
    return render_template("pet_list.html", pets = pets)

@app.route("/add", methods = ["GET", "POST"])
def add_pet():
    form = addPet()
    if form.validate_on_submit():
        data = {c : v for c, v in form.data.items() if c != "crsf_token"}
        """This (**data) outputs all of the data this is a note to self moment lol"""
        new_pet = Pet(**data)
        db.seesion.add(new_pet)
        db.session.commit()
        return redirect(url_for("pet_list"))

    else:
        return render_template("add_pet.html", form = form)

@app.route("/<int:pet_id>", methods = ["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = editPet(obj=pet)
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect(url_for(pet_list))

    else:
        return render_template("edit_pet.html", form = form, pet = pet)

@app.route("/pets/<int:pet_id>", methods = ["GET"])
def pet_info(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    info = {"age" : pet.age, "name" : pet.name}
    return jsonify(info)