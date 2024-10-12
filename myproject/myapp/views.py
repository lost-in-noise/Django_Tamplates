from django.shortcuts import render

def post_detail(request):
    post = {
        'title': 'My First Blog Post',
        'content': 'This is the content of the blog post.',
        'date': '2024-10-12',
        'author': 'Nancy',
        'comments': [
            {'user': 'John', 'text': 'Great post!'},
            {'user': 'Alice', 'text': 'Thanks for sharing!'}
        ]
    }
    return render(request, 'myapp/post.html', {'post': post})
