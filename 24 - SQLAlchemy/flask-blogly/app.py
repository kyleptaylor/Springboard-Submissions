"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenPotPie"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Added for app context
app.app_context().push() 

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def show_home():
    """ Display homepage """
    all_posts = Post.get_all_posts()
    all_tags = Tag.get_all_tags()
    return render_template('home.html', all_posts=all_posts, all_tags=all_tags)

# USER ROUTES

@app.route('/new-user')
def show_new_user_form():
    """ Display user form """
    return render_template('new_user.html')

@app.route('/new-user', methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form.get("image_url")
    if not image_url:
        image_url = None

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f'/users/{new_user.id}')

@app.route('/users')
def show_users():
    """ List all users from db """
    users = User.get_all_users()
    return render_template('users.html', users=users)

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """ Show details for user based on id, get user posts based on user id"""
    user = User.query.get_or_404(user_id)
    posts = Post.get_user_posts(user_id)
    return render_template('user.html', user=user, posts=posts)

@app.route('/edit-user/<int:user_id>')
def show_edit_user_form(user_id):
    """ Get user and display eidt user form """
    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user=user)

@app.route('/edit-user/<int:user_id>', methods=["POST"])
def edit_user(user_id):
    
    # Get user from db 
    current_user = User.query.get_or_404(user_id)

    # Get the form data
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form.get("image_url")

    if not image_url:
        image_url = None

    current_user.first_name = first_name
    current_user.last_name = last_name
    current_user.image_url = image_url

    db.session.commit()

    return redirect(f'/users/{current_user.id}')

@app.route('/delete-user/<int:user_id>', methods=["POST"])
def delete_user(user_id):
    """ Remove user from db """
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect(f'/users')

# POST ROUTES

@app.route('/users/<int:user_id>/posts/<int:post_id>')
def show_post(user_id, post_id):
    """ Show details for post based on id """
    post = Post.query.get(post_id)
    user = User.query.get(user_id)
    return render_template('post.html', post=post, user=user)

@app.route('/users/<int:user_id>/new-post')
def show_new_post_form(user_id):
    """ Display post form """
    tags = Tag.get_all_tags()
    return render_template('new_post.html', user_id=user_id, tags=tags)

@app.route('/users/<int:user_id>/new-post', methods=["POST"])
def new_post(user_id):

    # Get the form data
    title = request.form["title"]
    content = request.form["content"]
    tag_ids = request.form.getlist('tags')

    # Create new post and add it to db
    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    # Loop over tags and add to db
    for tag_id in tag_ids:
        tag = Tag.query.get(tag_id)  # Retrieve the Tag object by ID
        if tag:
            new_post.tags.append(tag)

    db.session.commit()

    return redirect(f'/users/{user_id}/posts/{new_post.id}')

@app.route('/users/<int:user_id>/posts/<int:post_id>/edit-post')
def show_edit_post_form(user_id, post_id):
    """ Display edit post form """
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    tags = Tag.get_all_tags()
    return render_template('edit_post.html', user=user, post=post, tags=tags)

@app.route('/users/<int:user_id>/posts/<int:post_id>/edit-post', methods=["POST"])
def edit_post(user_id, post_id):

    current_post = Post.query.get_or_404(post_id)

    # Get the form data
    title = request.form["title"]
    content = request.form["content"]
    tag_ids = request.form.getlist('tags')

    current_post.title = title
    current_post.content = content

    db.session.commit()

    current_post.tags.clear()

    # Loop over tags and add to db
    for tag_id in tag_ids:
        tag = Tag.query.get(tag_id)  # Retrieve the Tag object by ID
        if tag:
            current_post.tags.append(tag)

    db.session.commit()

    return redirect(f'/users/{user_id}/posts/{current_post.id}')

@app.route('/users/<int:user_id>/posts/<int:post_id>/delete-post', methods=["POST"])
def delete_post(user_id, post_id):
    """ Remove post from db """
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(f'/users/{user_id}')

# TAG ROUTES

@app.route('/tags/<int:tag_id>')
def show_tag(tag_id):
    """ Display tag and associated posts """
    tag = Tag.query.get_or_404(tag_id)
    return render_template('tag.html', tag=tag)

@app.route('/tags')
def show_all_tags():
    """ Display all tags """
    tags = Tag.get_all_tags()
    return render_template('tags.html', tags=tags)

@app.route('/new-tag')
def show_new_tag_form():
    """ Display tag form """
    return render_template('new_tag.html')

@app.route('/new-tag', methods=["POST"])
def new_tag():
    # Get the form data
    tag_name = request.form["tag_name"]

    new_tag = Tag(name=tag_name)
    db.session.add(new_tag)
    db.session.commit()

    return redirect('/tags')

@app.route('/tags/<int:tag_id>/edit-tag')
def show_edit_tag_form(tag_id):
    """ Display tag form """
    tag = Tag.query.get_or_404(tag_id)
    return render_template('edit_tag.html', tag=tag)

@app.route('/tags/<int:tag_id>/edit-tag', methods=["POST"])
def edit_tag(tag_id):

    # Get the current tag
    current_tag = Tag.query.get_or_404(tag_id)

    # Get the form data
    tag_name = request.form["tag_name"]
    
    current_tag.name = tag_name

    db.session.add(current_tag)
    db.session.commit()

    return redirect('/tags')

@app.route('/tags/<int:tag_id>/delete-tag', methods=["POST"])
def delete_tag(tag_id):

    # Get the current tag
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()

    return redirect('/tags')