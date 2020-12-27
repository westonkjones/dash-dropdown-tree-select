# AUTO GENERATED FILE - DO NOT EDIT

dashDropdownTreeSelect <- function(id=NULL, className=NULL, clearSearchOnChange=NULL, onChange=NULL, onNodeToggle=NULL, onAction=NULL, data=NULL, keepTreeOnSearch=NULL, keepChildrenOnSearch=NULL, keepOpenOnSelect=NULL) {
    
    props <- list(id=id, className=className, clearSearchOnChange=clearSearchOnChange, onChange=onChange, onNodeToggle=onNodeToggle, onAction=onAction, data=data, keepTreeOnSearch=keepTreeOnSearch, keepChildrenOnSearch=keepChildrenOnSearch, keepOpenOnSelect=keepOpenOnSelect)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashDropdownTreeSelect',
        namespace = 'dash_dropdown_tree_select',
        propNames = c('id', 'className', 'clearSearchOnChange', 'onChange', 'onNodeToggle', 'onAction', 'data', 'keepTreeOnSearch', 'keepChildrenOnSearch', 'keepOpenOnSelect'),
        package = 'dashDropdownTreeSelect'
        )

    structure(component, class = c('dash_component', 'list'))
}
