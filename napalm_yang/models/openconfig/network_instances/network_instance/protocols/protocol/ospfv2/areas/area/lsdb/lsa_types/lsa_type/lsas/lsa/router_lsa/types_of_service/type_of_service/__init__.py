
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import state
class type_of_service(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/router-lsa/types-of-service/type-of-service. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-type of service parameters for the LSA
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__tos','__state',)

  _yang_name = 'type-of-service'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tos = YANGDynClass(base=unicode, is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'router-lsa', u'types-of-service', u'type-of-service']

  def _get_tos(self):
    """
    Getter method for tos, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/router_lsa/types_of_service/type_of_service/tos (leafref)

    YANG Description: Reference to the type of service identifier which is
specified in the LSA
    """
    return self.__tos
      
  def _set_tos(self, v, load=False):
    """
    Setter method for tos, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/router_lsa/types_of_service/type_of_service/tos (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tos() directly.

    YANG Description: Reference to the type of service identifier which is
specified in the LSA
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tos must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__tos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tos(self):
    self.__tos = YANGDynClass(base=unicode, is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/router_lsa/types_of_service/type_of_service/state (container)

    YANG Description: Per-TOS parameters for the LSA
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/router_lsa/types_of_service/type_of_service/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Per-TOS parameters for the LSA
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  tos = __builtin__.property(_get_tos)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = {'tos': tos, 'state': state, }


import state
class type_of_service(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/router-lsa/types-of-service/type-of-service. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-type of service parameters for the LSA
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__tos','__state',)

  _yang_name = 'type-of-service'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tos = YANGDynClass(base=unicode, is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'router-lsa', u'types-of-service', u'type-of-service']

  def _get_tos(self):
    """
    Getter method for tos, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/router_lsa/types_of_service/type_of_service/tos (leafref)

    YANG Description: Reference to the type of service identifier which is
specified in the LSA
    """
    return self.__tos
      
  def _set_tos(self, v, load=False):
    """
    Setter method for tos, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/router_lsa/types_of_service/type_of_service/tos (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tos() directly.

    YANG Description: Reference to the type of service identifier which is
specified in the LSA
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tos must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__tos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tos(self):
    self.__tos = YANGDynClass(base=unicode, is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/router_lsa/types_of_service/type_of_service/state (container)

    YANG Description: Per-TOS parameters for the LSA
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/router_lsa/types_of_service/type_of_service/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Per-TOS parameters for the LSA
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  tos = __builtin__.property(_get_tos)
  state = __builtin__.property(_get_state)


  _pyangbind_elements = {'tos': tos, 'state': state, }

