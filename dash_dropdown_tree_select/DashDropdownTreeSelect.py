# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashDropdownTreeSelect(Component):
    """A DashDropdownTreeSelect component.


Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- className (string; optional): Additional classname for container. The container renders with a default classname of react-dropdown-tree-select.
- clearSearchOnChange (boolean; default False): Clear the input search if a node has been selected/unselected.
- data (list; optional): Data to be rendered
- keepTreeOnSearch (boolean; default True): Displays search results as a tree instead of flattened results
- keepChildrenOnSearch (boolean; default False): Displays children of found nodes to allow searching for a parent node on then selecting any child node of the found node. 
Defaults to false
- keepOpenOnSelect (boolean; default True): Keeps single selects open after selection. Defaults to false
NOTE this works only in combination with simpleSelect or radioSelect"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, clearSearchOnChange=Component.UNDEFINED, onChange=Component.UNDEFINED, onNodeToggle=Component.UNDEFINED, onAction=Component.UNDEFINED, data=Component.UNDEFINED, keepTreeOnSearch=Component.UNDEFINED, keepChildrenOnSearch=Component.UNDEFINED, keepOpenOnSelect=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'clearSearchOnChange', 'data', 'keepTreeOnSearch', 'keepChildrenOnSearch', 'keepOpenOnSelect', 'onChange']
        self._type = 'DashDropdownTreeSelect'
        self._namespace = 'dash_dropdown_tree_select'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'clearSearchOnChange', 'data', 'keepTreeOnSearch', 'keepChildrenOnSearch', 'keepOpenOnSelect']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashDropdownTreeSelect, self).__init__(**args)
