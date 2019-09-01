"""grp10proj01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from admdesign import views
from django.conf.urls import url,include


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name='home'),
    path('manage_projects/', views.manage_projects, name='manage_projects'),
    path('new_project/', views.new_project, name='new_project'),
    path('update_project/<int:pk>/', views.update_project, name="update_project"),
    path('delete_project/<int:pk>/', views.delete_project, name="delete_project"),
    path('view_projects/', views.view_projects, name="view_projects"),
    path('view_prj_designs/<int:pk>/', views.view_prj_designs, name="view_prj_designs"),
    path('batch_load_image/', views.batch_load_image, name='batch_load_image'),
    path('preview_design/<str:imgurl>/', views.preview_design, name='preview_design'),

    url(r'accounts/',include('accounts.urls',namespace='accounts')),
    url(r'accounts/',include('django.contrib.auth.urls')),
    url(r'test/$',views.TestPage.as_view(), name='test'),
    url(r'thanks/$',views.ThanksPage.as_view(), name='thanks')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
