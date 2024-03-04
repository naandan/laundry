from import_export import resources  
from myapp.models import Transaksi

class TransaksiResources(resources.ModelResource):

    class Meta:
        model = Transaksi