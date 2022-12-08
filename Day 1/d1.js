let fs = require('fs');

let input = fs.readFileSync('./Day 1/d1_input.txt', {encoding: 'utf-8'})
    .replace(/\r/g, "")
    .trim()
    .split("\n\n")
    .map((x) => x.split("\n").map((z) => Number(z)))
    
//Getting the input in the form of a bi-dimentional array:
//[[1,2,3,4], [5,6,7]]

function part_1(array){
    for( el in array ){
        array[el] = array[el].reduce((a, b) => a + b)
    }

    return Math.max(...array)
}

function part_2(array){
    for( el in array ){
        array[el] = array[el].reduce((a, b) => a + b)
    }
    array.sort((a, b) => b - a)
    return array[0] + array[1] + array[2]
}

console.log(part_2(input))