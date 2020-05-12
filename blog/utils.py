from typing import Any, Dict

import django


def update(obj: django.db.models.Model, data: Dict[str, Any]):
    '''
    Update a django object with values from a dictionary.
    obj.save() should be called after this.
    '''
    for key, value in data.items():
        setattr(obj, key, value)
