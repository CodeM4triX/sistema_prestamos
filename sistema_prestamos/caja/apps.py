from django.apps import AppConfig


class CajaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'caja'

    # ------- REGISTRAR SIGNAL-------
    """
    def ready(self):
        import caja.signals  # Importa las señales
    """
