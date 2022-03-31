from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.forms import MembershipForm
from .models import Entry, Membership
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_entry_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return Entry.objects.order_by('-pub_date')[:5]


class EntryDetailView(generic.DetailView):
    model = Entry
    #template_name = 'blog/detail.html'


class EntryMonthArchiveView(generic.dates.MonthArchiveView):
    queryset = Entry.objects.all()
    date_field = 'pub_date'


class MembershipFormView(SuccessMessageMixin, generic.CreateView):
    model = Membership
    form_class = MembershipForm
    success_message = "Thanks for subscribing!"

    def get_success_url(self):
        return reverse('blog:subscribe')


def comment(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    comment = ""
    try:
        comment = request.POST['comment'].strip()
        if len(comment) < 5:
            raise ValueError("Less than 5 characters in the comment")
    except (ValueError):
        # Redisplay the post comment form.
        return render(request, 'blog/entry_detail.html', {
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
