function App() {

    // To manage displaying components
    const [display, setDisplay] = React.useState({
        intro: true,
        play: false,
        grid: false,
    })
   
    const [difficulty, setDifficulty] = React.useState(null)
    
    function hideIntro() {
        setDisplay(prevState => ({
            ...prevState,
            intro: false,
            play: true,
        }))
    }

    
    function back() {
        setDisplay(prevState => ({
            ...prevState,
            grid: false,
            play: true,
        }))
    }
    
    // Render grid component with chosen difficulty
    function generate(event) {
        setDifficulty(event.target.value)
        setDisplay(prevState => ({
            ...prevState,
            play: false,
            grid: true,
        }))
    }

    return (
        <div>
            {display.intro && <Introduction hideIntro={hideIntro} />}
            {display.play && <Play generate={generate} />}
            {display.grid && <Grid difficulty={difficulty} back={back}  />}
        </div>
    )
}

ReactDOM.render(<App />, document.querySelector("#root"))