"""
Views
"""
import logging

from django.http import FileResponse, HttpResponse
from django.views.generic import View

from .models import Professional, Resume

logger = logging.getLogger(__name__)

class PortfolioPdfView(View):
    """

    """

    def get(self, request, guid):
        """

        :param request:
        :return:
        """
        try:
            import pdb; pdb.set_trace()
            professional = Professional.objects.filter(guid=guid)
            if professional.exists():
                professional = professional.last()
                resume = Resume.objects.filter(professional=professional)
                if resume.exists():
                    resume = resume.latest("created")
                    return FileResponse(open(resume.resume.path, 'rb'), content_type='application/pdf')

        except Exception as exception:
            logger.error(exception)

        return HttpResponse("<h1>File does not exist</h1>")