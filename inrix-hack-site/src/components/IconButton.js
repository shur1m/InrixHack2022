import React from 'react'
import PropTypes from 'prop-types'

const IconButton = ({icon, onClick}) => {
  return (
    <button
			className = 'bg-gray-700 text-white rounded-lg p-2'
			onClick = {onClick}
		> 
        {icon}
    </button>
  )
}

IconButton.defaultProps = {
	color : 'steelBlue'
}

IconButton.propTypes = {
	text : PropTypes.string,
	onClick : PropTypes.func,
}

export default IconButton
