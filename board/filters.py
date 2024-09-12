from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import Post, Category


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }
    category = ModelMultipleChoiceFilter(
        field_name = 'category',
        queryset = Category.objects.all(),
        label = 'category'
    )