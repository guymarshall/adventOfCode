/*
    find first digit from left
    find last digit from right
    if only one digit, use it twice
    concat the two digits together e.g. 7 and 7 is 77
    find the total of all numbers
*/

import { digits } from "./digits";
import { codes } from "./codes";

function getFirstDigit(code) {
    let firstDigit = 0;

    digits.forEach(digit => {
        let position = code.indexOf(digit);

        if (position === -1) {
            continue;
        }

        if (position < firstDigit) {
            firstDigit = parseInt(digit);
            // TODO: got to here
            break;
        }
    });

    return firstDigit;
}

function getLastDigit(code) {
    let lastDigit = code.length;

    digits.forEach(digit => {
        let position = strpos(code, digit);

        if (position === -1) {
            continue;
        }

        if (position < lastDigit) {
            lastDigit = parseInt(digit);
            break;
        }
    });

    return lastDigit;
}

let total = 0;

codes.forEach(code => {
    firstDigit = getFirstDigit(code);
    lastDigit = getLastDigit(code);
    concat = firstDigit . lastDigit;
    total += (int) concat;
});

console.log(total);