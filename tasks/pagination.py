from rest_framework.pagination import PageNumberPagination


class TaskPagination(PageNumberPagination):
    page_size = 10  # default number per page
    page_size_query_param = "limit"  # allow ?page_size=5
    max_page_size = 100
