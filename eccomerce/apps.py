# eccomerce/apps.py
from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class EccomerceConfig(AppConfig):
    name = 'eccomerce'

    def ready(self):
        # Log when the app is ready
        logger.info("Eccomerce app is ready")
        from . import scheduler  # Import the scheduler
        scheduler.start()  # Start the scheduler
