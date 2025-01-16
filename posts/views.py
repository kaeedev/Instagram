from django.shortcuts import render
from django.views.generic.edit import CreateView
from posts.models import Post
from posts.forms import PostCreateForm, CommentCreateForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

@method_decorator(login_required, name='dispatch') #Protegemos la vista de usuarios no logeados
class PostCreateView(CreateView):
    template_name= 'posts/post_create.html'
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user #De esta manera asignamos como usuario del post el usuario que esta logeado actualmente
        messages.add_message(self.request, messages.SUCCESS, 'Publicación creada correctamente.')
        return super(PostCreateView, self).form_valid(form) #Hace el save 
    

class PostDetailView(DetailView, CreateView): #Createview para poder utilizar el formulario de comentarios, ya que crea nuevos datos
    template_name= 'posts/post_detail.html'
    model = Post
    context_object_name='post'
    form_class = CommentCreateForm

    def form_valid(self, form): #A las instancias que creemos (comentarios), le indicamos el usuario que lo crea y el post al q pertenece
        form.instance.user = self.request.user
        form.instance.post = self.get_object()
        return super(PostDetailView, self).form_valid(form)
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Comentario añadido correctamente.')
        return reverse('post_detail', args=[self.get_object().pk])

@login_required
def like_post(request, pk):  #Funcion para el me gusta. Si ya se le ha dado like lo quita. Sin embargo esta recarga la pagina. USAR LA DE AJAX
    post = Post.objects.get(pk=pk)
    if request.user in post.likes.all():
        messages.add_message(request, messages.INFO, 'Ya no te gusta la publicación')
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        messages.add_message(request, messages.INFO, 'Te gusta esta publicación')
    return HttpResponseRedirect(reverse('post_detail', args=[pk]))

@login_required  
def like_post_ajax(request,pk):  #View hecho con javascript ajax para que no recargue la pagina al dar o quitar un me gusta
    post = Post.objects.get(pk=pk)
    if request.user in post.likes.all():
        post.unlike(request.user)
        return JsonResponse(
            {
                'message': 'Ya no te gusta esta publicacion',
                'liked': False,
                'nlikes': post.likes.all().count()
            }
        )
    else:
        post.like(request.user)
        return JsonResponse(
            {
                'message': 'Tte gusta esta publicacion',
                'liked': True,
                'nlikes': post.likes.all().count()
            }
        )