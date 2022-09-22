from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post, Category


class PostFilter(FilterSet):
   category = ModelMultipleChoiceFilter(
       field_name='postcategory__categoryThrough',
       queryset=Category.objects.all(),
       label='Category',
       conjoined=True,
   )
   added_after = DateTimeFilter(
       field_name='dateCreation',
       lookup_expr='gt',
       widget=DateTimeInput(
           format='%Y-%m-%dT%H:%M',
           attrs={'type': 'datetime-local'},
       ),
   )

   class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
       }


#DateTimeFilter
#from django.forms import DateTimeInput