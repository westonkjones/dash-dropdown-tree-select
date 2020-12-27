import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';
import DropdownTreeSelect from 'react-dropdown-tree-select'
import 'react-dropdown-tree-select/dist/styles.css'
export default class DashDropdownTreeSelect extends Component {

    render() {
        const {id, className, clearSearchOnChange, onChange, onNodeToggle, onAction, data, keepTreeOnSearch, keepChildrenOnSearch, keepOpenOnSelect, setProps} = this.props;

        return (
            <DropdownTreeSelect
              id={id}
              className={className}
              clearSearchOnChange={clearSearchOnChange}
              onChange={onChange}
              onNodeToggle={onNodeToggle}
              onAction={onAction}
              data={data}
              keepTreeOnSearch={keepTreeOnSearch}
              keepChildrenOnSearch={keepChildrenOnSearch}
              keepOpenOnSelect={keepOpenOnSelect}
            />
          );
    }

}

DashDropdownTreeSelect.defaultProps = {
    clearSearchOnChange: false,
    keepTreeOnSearch: true,
    keepChildrenOnSearch: false,
    keepOpenOnSelect: true,
};

DashDropdownTreeSelect.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Additional classname for container. The container renders with a default classname of react-dropdown-tree-select.
     */
    className: PropTypes.string,

    /**
     *  Clear the input search if a node has been selected/unselected.
     */
    clearSearchOnChange: PropTypes.bool,

    /**
     * Callback when the tree changes
     */
    onChange: PropTypes.func,

    /**
     * Callback for when a node is toggled
     */
    onNodeToggle: PropTypes.func,

    /**
     * Callback for when an action is performed
     */
    onAction: PropTypes.func,

    /**
     * Data to be rendered
     */
    data: PropTypes.array,

    /**
     * Displays search results as a tree instead of flattened results
     */
    keepTreeOnSearch: PropTypes.bool,

    /**
     * Displays children of found nodes to allow searching for a parent node on then selecting any child node of the found node. 
     * Defaults to false
     */
    keepChildrenOnSearch: PropTypes.bool,

    /**
     * Keeps single selects open after selection. Defaults to false
     * NOTE this works only in combination with simpleSelect or radioSelect
     */
    keepOpenOnSelect: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
