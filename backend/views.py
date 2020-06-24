from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    Route for displaying all routes within a single-page-application.
    
    This method relies on the SPA to manage routing (e.g. with react-router).

    The url pointing to this view should always be after every other path.
    
    **Template**

    Requires only a single :template:`index.html` page. It should be located
    in the build folder, and is created by npm run build.
    """
    template_name = 'index.html'
