import json
import re

try:
    from .operationids import operations
    from .graphene_types import String, Optional, Id, JsonObj
except (ImportError, SystemError):
    from operationids import operations
    from graphene_types import String, Optional, Id, JsonObj


class GrapheneObject(object):
    """ Core abstraction class

        This class is used for any JSON reflected object in Graphene.

        * ``instance.__json__()``: encodes data into json format
        * ``bytes(instance)``: encodes data into wire format
        * ``str(instances)``: dumps json object as string

    """
    def __init__(self, data=None):
        self.data = data

    def __bytes__(self):
        if self.data is None:
            return bytes()
        b = b""
        for name, value in self.data.items():
            if isinstance(value, str):
                b += bytes(value, 'utf-8')
            else:
                b += bytes(value)
        return b

    def __json__(self):
        if self.data is None:
            return {}
        d = {}  # JSON output is *not* ordered
        for name, value in self.data.items():
            if isinstance(value, Optional) and value.isempty():
                continue

            if isinstance(value, String):
                d.update({name: str(value)})
            else:
                try:
                    d.update({name: JsonObj(value)})
                except Exception:
                    d.update({name: value.__str__()})
        return d

    def __str__(self):
        return json.dumps(self.__json__())

    def toJson(self):
        return self.__json__()

    def json(self):
        return self.__json__()


class Operation:
    def __init__(self, op: GrapheneObject):
        self.op = op
        self.name = type(self.op).__name__  # also store name
        self.opId = operations[to_method_name(self.name)].value

    def operations(self):
        return operations

    def _getklass(self, name):
        module = __import__("graphenebase.operations", fromlist=["operations"])
        class_ = getattr(module, name)
        return class_

    def __bytes__(self):
        return bytes(Id(self.opId)) + bytes(self.op)

    def __str__(self):
        return json.dumps([to_method_name(self.name), self.op.toJson()])


class StaticVariantObject:
    def __init__(self, obj_type, objects):
        self.objects = objects
        self.obj_type = obj_type
        self.name = None
        self.id = None

    def get_id(self, name: str):
        try:
            return self.objects.index(name)
        except ValueError:
            raise Exception("no such %s %s" % (type(self).__name__, name))

    @staticmethod
    def get_name(obj_type):
        """ Take a name of a class, like ClassName and turn it into method name like class_name."""
        return to_method_name(type(obj_type).__name__)

    def __bytes__(self):
        return bytes(Id(self.id)) + bytes(self.obj_type)

    def __str__(self):
        return json.dumps([self.name, self.obj_type.toJson()])


def isArgsThisClass(self, args):
    return (len(args) == 1 and type(args[0]).__name__ == type(self).__name__)


def to_method_name(class_name: str):
    """ Take a name of a class, like FeedPublish and turn it into method name like feed_publish. """
    words = re.findall('[A-Z][^A-Z]*', class_name)
    return '_'.join(map(str.lower, words))
