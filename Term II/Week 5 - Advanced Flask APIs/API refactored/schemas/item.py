from ma import marsh
from models.item import ItemModel
from models.store import StoreModel


class ItemSchema(marsh.ModelSchema):
    class Meta:
        model = ItemModel
        load_only = ("store",)
        dump_only = ("id",)
        include_fk = True
