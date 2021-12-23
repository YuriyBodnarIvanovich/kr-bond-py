from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime, date, timezone, timedelta
import sys
import os
from os import abort
from flask import current_app as app
# from app import app, bcrypt #  import current_app
import pytz
from . import product_bp
from app import db
from app.product.models import Product
from .form import FormProductCreate, FormProductUpdate


@product_bp.route('/')
def products():
    products = Product.query.order_by(Product.name)
    print(products[0])
    return render_template('products.html', products=products)

@product_bp.route('/create', methods=["GET", "POST"])
def product_create():
    form = FormProductCreate()
    if form.validate_on_submit():
        codeOfProduct = form.codeOfProduct.data
        name = form.name.data
        typeOfProduct = form.typeOfProduct.data
        is_product = form.is_product.data
        count = form.count.data
        price = form.price.data
        description = form.description.data
        product = Product(codeOfProduct=codeOfProduct, name=name,
                          typeOfProduct=typeOfProduct, is_product=is_product,
                          count=count, price=price, description=description)
        try:
            db.session.add(product)
            db.session.commit()
            flash('Data added in DB', 'success')
        except:
            db.session.rollback()
            flash('Error adding data in DB!', 'danger')
        return redirect(url_for('product_bp_in.products'))

    return render_template('product_create.html', form=form, title='Product create')

@product_bp.route('/product/<int:id>', methods=["GET", "POST"])
def product_show(id):
    product = Product.query.get_or_404(id)
    return render_template('product_show.html', product=product)

@product_bp.route('/task/<int:id>/update', methods=["GET", "POST"])
def product_update(id):
    form = FormProductUpdate()
    product = Product.query.get_or_404(id)
    if request.method == 'GET': # якщо ми відкрили сторнку для редагування, записуємо у поля форми значення з БД
        form.codeOfProduct.data = product.codeOfProduct
        form.name.data = product.name
        form.typeOfProduct.data = product.typeOfProduct
        form.is_product.data = product.is_product
        form.count.data = product.count
        form.price.data = product.price
        form.description.data = product.description

        return render_template('product_update.html', title='Task Update', form=form)

    elif form.validate_on_submit():
        product.codeOfProduct = form.codeOfProduct.data
        product.name = form.name.data
        product.typeOfProduct = form.typeOfProduct.data
        product.is_product = form.is_product.data
        product.count = form.count.data
        product.price = form.price.data
        product.description = form.description.data
        try:
            db.session.commit()
            flash('Product seccessfully updated', 'info')
        except:
            db.session.rollback()
            flash('Error while update product!', 'danger')
        return redirect(url_for('product_bp_in.products'))
    return render_template('product_update.html', title='Task Update',
                            form=form)


@product_bp.route('/product/<int:id>/delete', methods=["GET", "POST"])
def product_delete(id):
    product = Product.query.get_or_404(id)
    try:
        db.session.delete(product)
        db.session.commit()
        flash('Product seccessfully deleted', 'success')
    except:
        flash('Error while delete product!', 'danger')
    return redirect(url_for('.products'))