import json
from .models import Post, Tag
from datetime import datetime
from django.db.models import Q
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404



# REQUIRED
def index(request):
    # Function to return all posts
    
    # START CODE HERE
    # 1- Retrieve all posts
    posts = Post.objects.all()


    # END CODE

    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

# REQUIRED
def show(request, id):
    # Function to show a single post
    # START CODE HERE

    # 1- Get post by id
    post = Post.objects.get(id=id)

    # 2- Create the context
    context = {
        'post': post
    }

    # 3- return template 'posts/show.html' with context

    return render(request,'posts/show.html', context)
    
    # END CODE

def create(request):
    # Functionn to show post_creation_form template
    return render(request, 'posts/create.html')

def findBySlug(request,slug):

    post = Post.objects.get(slug=slug)  #col=val

    # 2- Create the context
    context = {
        'post': post
    }

    # 3- return template 'posts/show.html' with context

    return render(request,'posts/show.html', context)
# REQUIRED
def store(request):
    # Function to store new post

    if request.method == "POST":
        # Recieve form data & Create new post
        title, body, image, tags = request.POST.get('title'), request.POST['body'], request.POST['image'],request.POST.getlist('tags')
        
        # STAR CODE HERE
        # 1- Create new post, given the previous variables
        created_post = Post.objects.create(title=title, body=body, image=image, user=request.user)  # hena lazem a3mel var l awel 3ashan tkon readable
        # created_post.body = ""
        created_post.save()

        tag_objects = Tag.objects.filter(name__in=tags)
        created_post.tags.add(*tag_objects)  #  *arr => (arr[0], arr[1], ...)

        # 2- Create context with the created post
        context = {
            'post': created_post
            }
        # 3- return template 'posts/show.html' with context
        return render(request,'posts/show.html', context)
        # END CODE

    else:
        # request method is not POST
        return redirect('/posts')


# REQUIRED
def edit(request, id):
    # Function to show post_editing_form template
    if request.method == "GET":

        # START CODE HERE

        # 1- Get post by id
        post = Post.objects.get(id=id)

        # END CODE

        # if post exists
        if post is not None:
            context = {
                'post' : post
            }
            return render(request, 'posts/edit.html', context)
        else:
            # Post is not found
            return render(request, 'posts/not_found.html')
    else:
        # request method is not GET
        return redirect('/dashboard')


# REQUIRED
def update(request, id):
    # Function to update a row of existing post
    if request.method == "POST":
        # check that request method is PUT
        _method = request.POST['_method'].upper()
        if _method == "PUT":

            # START CODE HERE PART 1
            post = Post.objects.get(id=id)
            
            # END CODE PART 1

            # check that post exists
            if post is not None:
                # Recieve new data & Update post
                title, body, image = request.POST['title'], request.POST['body'], request.POST['image']
                
                
                # START CODE HERE PART 2
                # 1- Update post values
                post.title = title
                post.body = body
                post.image = image
                # post.tags = tags
                post.save()
                # 2- Apply the update to the database
                
                # END CODE PART 2

                context = {
                    'post' : post,
                    'alert' : {
                        'type' : 'success',
                        'message' : 'Your post is updated successfully.'
                    }
                }
                return render(request, 'posts/show.html', context)
            else:
                # Post is not found
                return render(request, 'posts/not_found.html')
        else:
            # request method is not PUT
            return redirect('/posts')
    else:
        # request method is not POST
        return redirect('/posts')


#REQUIRED
def destroy(request, id):
    # Function to delete existing post
    if request.method == 'POST':
        _method = request.POST['_method'].upper()
        if _method == "DELETE":
            # Init context & retrieve post
            context = {}

            # START CODE HERE PART 1

            # 1- Find post by id
            post = Post.objects.get(id=id)
            # END CODE PART 1

            # if post exists -> delete it
            if post is not None:

                # START CODE HERE PART 2
                
                # 1- Delete post
                post.delete()
                # END CODE PART 2

                # Return success message
                context = {
                    'alert': {
                        'type' : 'success',
                        'message' : 'Your post is removed successfully'
                    }
                }
            else:
                # Post is not found, return fail message
                context ={
                    'alert': {
                        'type' : 'danger',
                        'message' : 'Something went wrong, please try again.'
                    }
                }
            # assign alert to session, to redirect with context
            request.session['alert'] = context['alert']
            return redirect('/')
        else:
            # request method is not DELETE
            return redirect('/')
    else:
        # request method is not POST
        return redirect('/')

            
def myposts(request):
    # Function to return all posts
    
    # START CODE HERE
    # 1- Retrieve all posts
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'posts/myposts.html', context)