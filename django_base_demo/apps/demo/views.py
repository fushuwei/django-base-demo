import logging

from django_base_demo.core.response import Response
from django_base_demo.core.viewsets import BaseViewSet

logger = logging.getLogger('django')


class DemoViewSet(BaseViewSet):

    def retrieve(self, request, *args, **kwargs):
        return Response.success("ok")
