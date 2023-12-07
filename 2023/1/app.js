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
    let firstDigit = code.length;

    digits.every(digit => {
        let position = code.indexOf(digit);

        if (position === -1) {
            return true;
        }

        if (position < firstDigit) {
            firstDigit = parseInt(digit);
        }

        return true;
    });

    return firstDigit;
}

function getLastDigit(code) {
    let lastDigit = 0;

    digits.every(digit => {
        let position = code.lastIndexOf(digit);

        if (position === -1) {
            return true;
        }

        if (position > lastDigit) {
            lastDigit = parseInt(digit);
        }

        return true;
    });

    return lastDigit;
}

let total = 0;

// do code.firstIndex(digit)
// get the lowest and highest and store values
// convert

codes.forEach(code => {
    const firstDigit = getFirstDigit(code);
    const lastDigit = getLastDigit(code);
    const concat = parseInt(`${firstDigit}${lastDigit}`);
    total += concat;
});

console.log(total);