from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from .models import SiteProjects, SiteAdmin, ProjectDesigns
from .forms import SiteProjectsForm
from django.template.loader import render_to_string
from django.core.files import File
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

def manage_projects(request):
    site_projects = SiteProjects.objects.filter(prj_site__site_login='da.cabarcas@uniandes.edu.co')
    return render(request, 'manage_projects.html', {'site_projects': site_projects})


def save_project(request, form, template_name):
    data = dict()

    if request.method == "POST":
        if form.is_valid():
            if SiteProjects.objects.filter(prj_name=form.cleaned_data['prj_name'],
                                           prj_site__site_login='da.cabarcas@uniandes.edu.co'):
                form.save()
            else:
                prj_site = SiteAdmin.objects.get(site_login='da.cabarcas@uniandes.edu.co')
                project = SiteProjects.objects.create(
                    prj_site=prj_site,
                    prj_name=form.cleaned_data['prj_name'],
                    prj_description=form.cleaned_data['prj_description'],
                    prj_budget=form.cleaned_data['prj_budget'],
                    prj_creationdate=form.cleaned_data['prj_creationdate']
                )

            site_projects = SiteProjects.objects.filter(prj_site__site_login='da.cabarcas@uniandes.edu.co')
            data['form_is_valid'] = True
            data['html_project_list'] = render_to_string('core_projects.html', {'site_projects': site_projects})
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def new_project(request):
    if request.method == "POST":
        form = SiteProjectsForm(request.POST)
    else:
        form = SiteProjectsForm()
    return save_project(request, form, 'new_project.html')


def update_project(request, pk):
    project = get_object_or_404(SiteProjects, pk=pk)
    if request.method == "POST":
        form = SiteProjectsForm(request.POST, instance=project)
    else:
        form = SiteProjectsForm(instance=project)
    return save_project(request, form, 'update_project.html')


def delete_project(request, pk):
    project = get_object_or_404(SiteProjects, pk=pk)
    data = dict()

    if request.method == "POST":
        project.delete()
        data['form_is_valid'] = True
        project = SiteProjects.objects.filter(prj_site__site_login='da.cabarcas@uniandes.edu.co')
        data['html_project_list'] = render_to_string('core_projects.html', {'site_projects': project})
    else:
        context = {'site_projects': project}
        data['html_form'] = render_to_string('delete_project.html', context, request=request)

    return JsonResponse(data)


def view_projects(request):
    site_projects = SiteProjects.objects.filter(prj_site__site_login='da.cabarcas@uniandes.edu.co').order_by('prj_name')
    return render(request, 'view_projects.html', {'site_projects': site_projects})


def view_prj_designs(request, pk):
    data = dict()
    project_designs = ProjectDesigns.objects.filter(prjdsg_project_id=pk)
    context = {'project_designs': project_designs}
    data['html_project_list'] = render_to_string('core_prj_details.html', context)

    return JsonResponse(data)


def batch_load_image(request):
    data = {'Message': 'Bad request!'}

    if request.method == "POST":
        design_id = request.POST.get('design_id')
        filepath = request.POST.get('filepath')
        filepath = filepath.replace('#', '/')

        project_design = ProjectDesigns.objects.get(pk=design_id)

        with open(filepath, 'rb') as f:
            fdata = File(f)
            project_design.prjdsg_processed_file.save(filepath.rsplit('/', 1)[1], fdata, True)

        project_design.prjdsg_status = 'D'
        project_design.save()

        data = {'Message': 'OK!'}

    return JsonResponse(data)


def preview_design(request, imgurl):
    data = dict()
    imgurl = imgurl.replace('*', '/').lower()
    context = {'imgUrl': imgurl}
    data['html_design_img'] = render_to_string('preview_design.html', context)
    return JsonResponse(data)
