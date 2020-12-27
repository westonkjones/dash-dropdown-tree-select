% Auto-generated: do not edit by hand
\name{dashDropdownTreeSelect}

\alias{dashDropdownTreeSelect}

\title{DashDropdownTreeSelect component}

\description{

}

\usage{
dashDropdownTreeSelect(id=NULL, className=NULL, clearSearchOnChange=NULL, onChange=NULL,
onNodeToggle=NULL, onAction=NULL, data=NULL, keepTreeOnSearch=NULL,
keepChildrenOnSearch=NULL, keepOpenOnSelect=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{className}{Character. Additional classname for container. The container renders with a default classname of react-dropdown-tree-select.}

\item{clearSearchOnChange}{Logical. Clear the input search if a node has been selected/unselected.}

\item{onChange}{Callback when the tree changes}

\item{onNodeToggle}{Callback for when a node is toggled}

\item{onAction}{Callback for when an action is performed}

\item{data}{Unnamed list. Data to be rendered}

\item{keepTreeOnSearch}{Logical. Displays search results as a tree instead of flattened results}

\item{keepChildrenOnSearch}{Logical. Displays children of found nodes to allow searching for a parent node on then selecting any child node of the found node. 
Defaults to false}

\item{keepOpenOnSelect}{Logical. Keeps single selects open after selection. Defaults to false
NOTE this works only in combination with simpleSelect or radioSelect}
}
