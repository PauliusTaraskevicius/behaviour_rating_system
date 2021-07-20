from django import template
from django.db.models import Avg, F

from users.models import User
from ratings.models import Review

register = template.Library()


# gte more or equal to 0
# lte less or equal to 0
# filter(reviewed_user__work_office__lte=20)

@register.filter(name='users_count')
def users_count(request):
    users_count = User.objects.filter(is_active=True)

    return len(users_count)

# All users with rating above 80
@register.filter(name='overperforming_users_count')
def overperforming_users_count(request):
    overperforming_users_count = Review.objects.values('reviewed_user__first_name', 'reviewed_user__last_name').annotate(
        all=Avg(
            F('rate_professionalism')
            + F('rate_teamwork')
            + F('rate_communication')
            + F('rate_organize')
            + F('rate_problem_solving')
            + F('rate_personality')
            + F('rate_reliability')
            + F('rate_honesty_integrity')
            + F('rate_emotional_intelligence')
            + F('rate_willingness_to_learn')
        )).filter(all__gte=80)

    return len(overperforming_users_count)

# Percentage of users with rating above 80
@register.filter(name='overperforming_users_percentage')
def overperforming_users_percentage(request):
    user_count = users_count(request)
    overperforming_users_count = Review.objects.values('reviewed_user__first_name', 'reviewed_user__last_name').annotate(
        all=Avg(
            F('rate_professionalism')
            + F('rate_teamwork')
            + F('rate_communication')
            + F('rate_organize')
            + F('rate_problem_solving')
            + F('rate_personality')
            + F('rate_reliability')
            + F('rate_honesty_integrity')
            + F('rate_emotional_intelligence')
            + F('rate_willingness_to_learn')
        )).filter(all__gte=80)

    overperforming_users = len(
        overperforming_users_count) * 100 / user_count

    return overperforming_users

# All users with rating below 50
@register.filter(name='underperforming_users_count')
def underperforming_users_count(request):
    underperforming_users_count = Review.objects.values('reviewed_user__first_name', 'reviewed_user__last_name').annotate(
        all=Avg(
            F('rate_professionalism')
            + F('rate_teamwork')
            + F('rate_communication')
            + F('rate_organize')
            + F('rate_problem_solving')
            + F('rate_personality')
            + F('rate_reliability')
            + F('rate_honesty_integrity')
            + F('rate_emotional_intelligence')
            + F('rate_willingness_to_learn')
        )).filter(all__lte=50)

    return len(underperforming_users_count)

# Percentage of users with rating below 50
@register.filter(name='underperforming_users_percentage')
def underperforming_users_percentage(request):
    user_count = users_count(request)
    underperforming_users_count = Review.objects.values('reviewed_user__first_name', 'reviewed_user__last_name').annotate(
        all=Avg(
            F('rate_professionalism')
            + F('rate_teamwork')
            + F('rate_communication')
            + F('rate_organize')
            + F('rate_problem_solving')
            + F('rate_personality')
            + F('rate_reliability')
            + F('rate_honesty_integrity')
            + F('rate_emotional_intelligence')
            + F('rate_willingness_to_learn')
        )).filter(all__gte=50)

    underperforming_users = len(
        underperforming_users_count) * 100 / user_count

    return underperforming_users

# TOP PERFORMING OFFICES
@register.filter(name='top_performing_offices')
def top_performing_offices(request):
    offices_performance = Review.objects.values('reviewed_user__work_office__office_name').annotate(
        all=Avg(
            F('rate_professionalism')
            + F('rate_teamwork')
            + F('rate_communication')
            + F('rate_organize')
            + F('rate_problem_solving')
            + F('rate_personality')
            + F('rate_reliability')
            + F('rate_honesty_integrity')
            + F('rate_emotional_intelligence')
            + F('rate_willingness_to_learn')
        )).order_by('-all')[:10]

    return offices_performance

# Users overall(of all attributes combined) ratings
@register.filter(name='users_overall_rating')
def users_overall_rating(request):
    overall_ratings = Review.objects.values('reviewed_user__first_name', 'reviewed_user__last_name').annotate(
        all=Avg(
            F('rate_professionalism')
            + F('rate_teamwork')
            + F('rate_communication')
            + F('rate_organize')
            + F('rate_problem_solving')
            + F('rate_personality')
            + F('rate_reliability')
            + F('rate_honesty_integrity')
            + F('rate_emotional_intelligence')
            + F('rate_willingness_to_learn')
        )).order_by('-all')[:10]

    return overall_ratings

# Average rating of each users attribute
@register.filter(name='avg_user_rating')
def avg_user_rating(request):
    ratings = Review.objects.values('reviewed_user__first_name', 'reviewed_user__last_name').annotate(
        avg_professionalism=Avg('rate_professionalism'),
        avg_teamwork=Avg('rate_teamwork'),
        avg_communication=Avg('rate_communication'),
        avg_organize=Avg('rate_organize'),
        avg_problem_solving=Avg('rate_problem_solving'),
        avg_personality=Avg('rate_personality'),
        avg_reliability=Avg('rate_reliability'),
        avg_honesty_integrity=Avg('rate_honesty_integrity'),
        avg_emotional_intelligence=Avg('rate_emotional_intelligence'),
        avg_willingness_to_learn=Avg('rate_willingness_to_learn'),
    ).order_by('-avg_professionalism')

    return ratings

# Top 5 attributes by average rating
# @register.filter(name='top_attributes')
# def top_attributes(request):
#     attributes = Review.objects.annotate(
#         avg_professionalism=Avg('rate_professionalism'),
#         avg_teamwork=Avg('rate_teamwork'),
#         avg_communication=Avg('rate_communication'),
#         avg_organize=Avg('rate_organize'),
#         avg_problem_solving=Avg('rate_problem_solving'),
#         avg_personality=Avg('rate_personality'),
#         avg_reliability=Avg('rate_reliability'),
#         avg_honesty_integrity=Avg('rate_honesty_integrity'),
#         avg_emotional_intelligence=Avg('rate_emotional_intelligence'),
#         avg_willingness_to_learn=Avg('rate_willingness_to_learn')).filter(avg_professionalism__gte=5).filter(avg_teamwork__gte=5).filter(avg_communication__gte=5).filter(avg_organize__gte=5).filter(avg_problem_solving__gte=5).filter(avg_personality__gte=5).filter(avg_reliability__gte=5).filter(avg_honesty_integrity__gte=5).filter(avg_emotional_intelligence__gte=5).filter(avg_willingness_to_learn__gte=5)

#     return attributes