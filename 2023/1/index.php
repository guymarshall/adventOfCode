<?php

/*
    find first digit from left
    find last digit from right
    if only one digit, use it twice
    concat the two digits together e.g. 7 and 7 is 77
    find the total of all numbers
*/

const DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

function getFirstDigit(string $code): int
{
    $length = mb_strlen($code, 'UTF-8');

    for ($i = 0; $i < $length; $i++) {
        if (in_array($code[$i], DIGITS, true)) {
            return (int) $code[$i];
        }
    }

    throw new RuntimeException('Digit not found');
}

function getLastDigit(string $code): int
{
    $length = mb_strlen($code, 'UTF-8');

    for ($i = $length - 1; $i >= 0; $i--) {
        if (in_array($code[$i], DIGITS, true)) {
            return (int) $code[$i];
        }
    }

    throw new RuntimeException('Digit not found');
}

$codes = file('codes.txt', FILE_IGNORE_NEW_LINES);
$total = 0;

foreach ($codes as $code) {
    $firstDigit = getFirstDigit($code);
    $lastDigit = getLastDigit($code);
    $concat = $firstDigit . $lastDigit;
    $total += (int) $concat;
}

echo $total;