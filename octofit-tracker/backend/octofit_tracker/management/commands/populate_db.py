from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="user1@example.com", name="User One", password="password1")
        user2 = User.objects.create(email="user2@example.com", name="User Two", password="password2")

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha", members=[user1.id, user2.id])

        # Create test activities
        Activity.objects.create(user=user1, activity_type="Running", duration=30, date="2025-04-01")
        Activity.objects.create(user=user2, activity_type="Cycling", duration=45, date="2025-04-02")

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Create test workouts
        Workout.objects.create(name="Workout A", description="Description for Workout A")
        Workout.objects.create(name="Workout B", description="Description for Workout B")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
