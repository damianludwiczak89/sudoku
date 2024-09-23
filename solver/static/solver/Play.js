window.Play = function Play(props) {

    return (
        <div id="general">
            <p>Choose difficulty:</p>
            <button value="easy" onClick={props.generate}>Easy</button>
            <button value="medium" onClick={props.generate}>Medium</button>
            <button value="hard" onClick={props.generate}>Hard</button>
            <br></br>
            <button value="custom" onClick={props.generate}>Customize</button>
        </div>
            
    )
}