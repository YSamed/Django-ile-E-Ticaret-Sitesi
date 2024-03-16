from django.apps import AppConfig

class ProductConfig(AppConfig):
    # Django tarafından oluşturulan varsayılan otomatik alan türünü belirtir.
    default_auto_field = 'django.db.models.BigAutoField'

    # Uygulamanın adını belirtir.
    name = 'product'
