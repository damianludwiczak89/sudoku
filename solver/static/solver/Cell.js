window.Cell = function Cell(props) {

    return (
        <td id={props.index}>{props.isEditable ? (
            <input 
                value={props.value !== 0 ? Cell.value : ""}
                onChange={props.handleChange} 
                id={props.index} 
                maxLength={1}
                
            />
        ) : (
            <span>{props.value}</span>
        
        )}
            </td>
    )
}