from django_filters import FilterSet, ModelMultipleChoiceFilter, ModelChoiceFilter
from .models import Post, Category, UserResponse



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


class ResponseFilter(FilterSet):
    post = ModelChoiceFilter(
        empty_label='Все объявления',
        field_name='post',
        queryset=Post.objects.none(),
        label='Отклики на объявление'
    )

    class Meta:
       model = UserResponse
       fields = {'post'}

    def __init__(self, *args, **kwargs):
        author_id = kwargs.pop('author_id', None)
        super().__init__(*args, **kwargs)
        self.filters['ad'].queryset = Post.objects.filter(author__id=author_id)    