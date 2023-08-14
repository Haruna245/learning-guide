from django.apps import AppConfig


class LearnappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'learnApp'

    def ready(self):
        import learnApp.signals 
