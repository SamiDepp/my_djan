from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime

from blog.models import Article


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
        """)
def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second parappmètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if id_article > 100:
        raise Http404

    #return HttpResponse('<h1>Mon article ici</h1>')
    return redirect(view_redirection)

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")

def list_articles(request, year, month=1):
    return HttpResponse('Articles de %s/%s' % (year, month))
#---------------------------
def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())
def page(request):

    return render(request, 'blog/page.html')

#--------------------------------------
def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id,slug):

    # try:
    #     article = Article.objects.get(id=id)
    # except Article.DoesNotExist:
    #     raise Http404
    article = get_object_or_404(Article, id=id,sulg=slug)
    return render(request, 'blog/lire.html', {'article': article})