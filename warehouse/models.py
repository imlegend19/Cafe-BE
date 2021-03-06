from django.db import models
from django.utils.text import gettext_lazy as _

from drfaddons.models import CreateUpdateModel

from stock.models import RawMaterialStock, StockCredit


class Warehouse(CreateUpdateModel):
    """
    Represents warehouses in the system

    Author: Himanshu Shankar (https://himanshus.com)
    """
    from business.models import Business

    from location.models import City

    name = models.CharField(verbose_name=_("Warehouse Name"), max_length=254,
                            unique=True)
    address = models.TextField(verbose_name=_("Address"))
    city = models.ForeignKey(to=City, on_delete=models.PROTECT,
                             verbose_name=_("City"))
    owner = models.ForeignKey(to=Business, on_delete=models.PROTECT,
                              verbose_name=_("Business Owner"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Warehouse")
        verbose_name_plural = _("Warehouses")


class WarehouseManager(CreateUpdateModel):
    """
    Represents Warehouse Managers in the System

    Author: Himanshu Shankar (https://himanshus.com)
    """
    from django.contrib.auth import get_user_model

    manager = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT,
                                verbose_name=_("Manager"),
                                related_name="manageswarehouse")
    is_active = models.BooleanField(verbose_name=_("Is Active?"), default=True)
    warehouse = models.ForeignKey(to=Warehouse, on_delete=models.PROTECT,
                                  verbose_name=_("Warehouse"))

    def __str__(self):
        return self.manager.name

    class Meta:
        verbose_name = _("Warehouse Manager")
        verbose_name_plural = _("Warehouse Managers")


class WarehouseStock(RawMaterialStock):
    warehouse = models.ForeignKey(to=Warehouse, on_delete=models.PROTECT,
                                  verbose_name=_("Warehouse"))

    def __str__(self):
        return self.warehouse.name + " - " + self.raw_material.name

    class Meta:
        unique_together = ('warehouse', 'raw_material')
        verbose_name = _("Warehouse Stock")
        verbose_name_plural = _("Warehouse Stocks")


class WarehouseInput(StockCredit):
    stock = models.ForeignKey(to=WarehouseStock, on_delete=models.PROTECT,
                              verbose_name=_("Stock"))

    class Meta:
        verbose_name = _("Warehouse Input")
        verbose_name_plural = _("Warehouse Inputs")
