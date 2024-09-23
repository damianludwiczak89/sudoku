window.Introduction = function Introduction(props) {
    return (
        <div id="general">
                <p>Welcome to Sudoku Solver!</p>
                    <p> Here you can generate a random Sudoku puzzle and solve it on your own or use AI solver if needed
                    but also you can customize your own game if you have a Sudoku from other source like a magazine or other website, 
                    you can input the values into the grid and use the AI solver to get the solution.</p>
                    <button onClick={props.hideIntro}>Continue</button>
        </div>
    )
}