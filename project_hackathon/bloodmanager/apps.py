from django.apps import AppConfig


class BloodManagerConfig(AppConfig):
    name = 'project_hackathon.bloodmanager'
    verbose_name = "BloodManager"

    def ready(self):
        """Override this to put in:
            BloodManager system checks
            BloodManager signal registration
        """
        try:
            import BloodManager.signals  # noqa F401
        except ImportError:
            pass
