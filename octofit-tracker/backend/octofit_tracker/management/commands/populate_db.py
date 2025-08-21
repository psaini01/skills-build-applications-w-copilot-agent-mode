from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (Superheroes)
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, type='run', duration=30, calories=300)
        Activity.objects.create(user=captain, type='cycle', duration=45, calories=400)
        Activity.objects.create(user=batman, type='swim', duration=60, calories=500)
        Activity.objects.create(user=superman, type='run', duration=50, calories=450)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, points=1000)
        Leaderboard.objects.create(user=captain, points=900)
        Leaderboard.objects.create(user=batman, points=950)
        Leaderboard.objects.create(user=superman, points=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
