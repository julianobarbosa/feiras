from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )


class FeiraLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class FeiraPageNumberPagination(PageNumberPagination):
    page_size = 10
