window.Row = function Row(props) {

    const row = props.cells.map((cell, index) => {

        // Index of the value in the 2d game array
        const fullIndex = `${props.index}${index}`
        
        return (
            <Cell 
                value={cell.value}
                index={fullIndex}
                handleChange={props.handleChange}
                isEditable={cell.isEditable}
             />
        )
    })

    return (
        <tr>
            {row}
      </tr>
    )
}