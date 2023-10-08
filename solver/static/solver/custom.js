let valid_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ""];

// Get a 2d array of values in the sudoku grid
function gatherValues() {
    let values = [];
    let row_values = [];

    let row = 0;
    document.querySelectorAll('td').forEach(function(value) {

        if (value.innerText == ""){
            // If cell was empty, check if there is an input, if not, set to 0
            if (value.querySelector('input').value === "") {
            value = 0;
            }
            else {
                value = parseInt(value.querySelector('input').value);
            }
        }
        else {
            value = parseInt(value.innerText);
        }
        row_values.push(value);
        row++;
        if (row == 9) {
            values.push(row_values);
            row = 0;
            row_values = []
        }
        });
    return values;
};

function spreadValues(board) {
    let row = 0;
    let column = 0;
    document.querySelectorAll('td').forEach(function(value) {
        value.innerText = board[row][column];
        column++;
        if (column === 9) {
            column = 0;
            row++;
        }

    });
}

// Check if all cells are filled
function isFinished() {
    let values = gatherValues();
    for (value of values) {
        if (value.includes(0) == true) {
            return false;
        }};
    return true;
};

document.addEventListener('DOMContentLoaded', function() {


    // Only 1-9 numbers input allowed
    document.querySelectorAll('input').forEach(function(input) {
        input.addEventListener("change", () =>{
            if (valid_values.includes(input.value) == false) {
                input.value = "";
                alert("Only numbers 1-9 allowed");
            }
            if (isFinished() === true) {
                fetch('/check_answer', {
                    method: 'POST',
                    body: JSON.stringify({
                        board: gatherValues()
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
        });
    });


    let solution = document.querySelector('#solution');
    solution.addEventListener("click", () => {
            fetch('/check_answer', {
                    method: 'POST',
                    body: JSON.stringify({
                        board: gatherValues()
                    })
                  })
                  .then(response => response.json())
                  .then(result => {
                      if (result === false) {
                        alert("Invalid values");
                      }
                      else {
                        fetch('/solution', {
                            method: 'POST',
                            body: JSON.stringify({
                                board: gatherValues()
                            })
                        })
                        .then(response => response.json())
                        .then(result => {
                            if (result === "no solution") {
                                alert('No possible solution');
                            }
                            else {
                            spreadValues(result);
                            }
                        });
            }
          });
        });
});