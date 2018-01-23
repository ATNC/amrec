from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True, db_index=True)

    def get_parents(self):
        """
        Return list of all parent.

        :return: list
        """
        list_of_parents = []
        parent = self.parent
        while True:
            if parent:
                list_of_parents.append(parent)
                parent = parent.parent
            if not parent:
                break
        return list_of_parents


