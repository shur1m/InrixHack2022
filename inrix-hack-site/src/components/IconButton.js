import React from 'react'
import PropTypes from 'prop-types'

const IconButton = ({icon, onClick}) => {
  return (
    <button
			className = 'bg-gray-700 text-white rounded-xl p-2'
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
	//icon should be type icon obviously
	onClick : PropTypes.func,
}

export default IconButton
