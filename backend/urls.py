"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie

from . import views

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('graphql/', jwt_cookie(GraphQLView.as_view(graphiql=True)), name='graphql'),
    re_path('^(.*)$', never_cache(ensure_csrf_cookie(views.IndexView.as_view())), name='catch_all'),
]
