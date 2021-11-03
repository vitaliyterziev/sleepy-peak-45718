from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Entry
from django.utils import timezone
#from django.db.models.functions import ExtractMonth, ExtractYear
from django.views.generic.dates import MonthArchiveView

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_entry_list'

    def get_queryset(self):
        """Return the last five published posts."""
        #t = Entry.objects.annotate(year=ExtractYear('pub_date'), month=ExtractMonth('pub_date')).values('year', 'month')
        return Entry.objects.order_by('-pub_date')[:5]


class EntryDetailView(generic.DetailView):
    model = Entry
    #template_name = 'blog/detail.html'


class EntryMonthArchiveView(MonthArchiveView):
    queryset = Entry.objects.all()
    date_field = "pub_date"


def comment(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    comment = ""
    try:
        comment = request.POST['comment'].strip()
        if len(comment) < 5:
            raise ValueError("Less than 5 characters in the comment")
    except (ValueError):
        # Redisplay the post comment form.
        return render(request, 'blog/detail.html', {
            'entry': entry,
            'error_message': "You didn't enter at least 5 characters.",
        })
    else:
        entry.comment_set.create(comment_text=comment, pub_date=timezone.now())
        entry.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blog:detail', args=(entry.id,)))
