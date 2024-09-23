window.Grid = function Grid(props) {

  // To validate input
  const valid_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ""]

  // To hold and update values for the grid
  const [game, setGame] = React.useState("")

  // We need to keep unchanged starting values if we want to generate an answer after game itself 
  // has been changed by the user
  const [startingValues, setStartingValues] = React.useState("")


  // Triggers fetch call to get solution 
  const [triggerSolutionFetch, setTriggerSolutionFetch] = React.useState(false)

  // Converts game from 2d array of objects {value, isEditable} to 2d array of values
  function convertGameToArrayWithOnlyValues(game) {
    return game.map(row =>(
      row.map(cell => cell.value)
    ))
  }
  
  function isFinished() {
    const gameValuesArray = convertGameToArrayWithOnlyValues(game)

    for (let row of gameValuesArray) {
      if (row.includes(0) === true) {
        return false
      }
    }
    return true
  }


  function handleChange(event) {
    // In case user clicked reveal solution, but values were invalid and did not get one, trigger solution fetch 
    // has to be changed back to false
    (triggerSolutionFetch === true && setTriggerSolutionFetch(false))

    // Id is set to store index of the value in the game 2d array
    let {value, id} = event.target

    if (valid_values.includes(value) == false) {
      value = 0
      alert("Only numbers 1-9 allowed")
      }
    
    // If User deleted his input, set the value to 0
    value = value === "" ? 0 : value

    // Deep copy to force rerender of component which will update visible values in the grid
    let gameCopy = game.map(row => row.map(cell => ({ ...cell })))
    gameCopy[id[0]][id[1]].value = parseInt(value)
    setGame(gameCopy)
    
  }
  
  // Fetch values and set game variable
  React.useEffect(() =>{
    fetch(`play/${props.difficulty}`)
      .then(result => result.json())
      .then(result => {
        const creatingGame = result.map(row => {
          return row.map(cell => ({
            value: cell,
            isEditable: cell === 0 ? true : false,
          }));
        });
        setGame(creatingGame) 
        setStartingValues(result)
      })
  }, [])

  React.useEffect(() => {
    // Run only after game has been fetched and set, then check if game is finished
    if (game.length > 0 && (isFinished() || triggerSolutionFetch === true)) {
      console.log('check')
      fetch('/check_answer', {
        method: 'POST',
        body: JSON.stringify({
            board: convertGameToArrayWithOnlyValues(game)
        })
      })
      .then(response => response.json())
      .then(result => {
          if (result === true) {
            alert("Solved");
          }
          else {
            alert("Invalid solution");
          }
      });
    }
  }, [game])
  
  // Initiate rows empty, it needs to exist on the component and wait for fetch to setGame with values
  let rows = []

  // When game is set by fetch, map objects
  if (game.length > 0) {
    rows = game.map((item, index) => {
      return (
        <Row 
          cells={item} 
          index={index}
          handleChange={handleChange}
        />
      )
    })
  }

  // Generates a solution in case user clicks button to solve automatically
  React.useEffect(() => {
    if (triggerSolutionFetch === true) {
      // If user is playing easy/medium/hard game, generate solution from starting values
      // If user is playing custom game, generate from the current game state
      const valuesToCheck = props.difficulty === "custom" ? convertGameToArrayWithOnlyValues(game) : startingValues
      fetch('/solution', {
        method: 'POST',
        body: JSON.stringify({
            board: valuesToCheck
        })
      })
      .then(response => response.json())
      .then(result => {
        if (result === false) {
          alert("Invalid values")
          return
        } 
        const getSolution = result.map(row => {
          return row.map(cell => ({
            value: cell,
            isEditable: cell === 0 ? true : false,
          }));
        });
        setGame(getSolution)
      })
    }
  }, [triggerSolutionFetch])

  return (
    <div id="general">
      <table>
      <colgroup>
        <col /><col /><col />
        <col /><col /><col />
        <col /><col /><col />
      </colgroup>
        <tbody>
          {rows}
        </tbody>
      </table>
      <button onClick={() => setTriggerSolutionFetch(true)} >Reveal Solution</button>
      <button onClick={props.back}>Back</button>
    </div>
)
}
