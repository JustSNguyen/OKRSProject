from rest_framework.decorators import api_view
from rest_framework.response import Response

from main_app.decorators.auth import check_authentication


class ProjectViews:
    @api_view(["GET", "POST"])
    @check_authentication
    def projects_view(request):
        return Response({"status": "success"}, 201)
