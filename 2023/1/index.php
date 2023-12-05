<?php

/*
    find first digit from left
    find last digit from right
    if only one digit, use it twice
    concat the two digits together e.g. 7 and 7 is 77
    find the total of all numbers
*/

const DIGITS = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
];

function getFirstDigit(string $code): int
{
    $firstDigit = 0;

    foreach (DIGITS as $digit) {
        $position = strpos($code, $digit);

        if (!$position) {
            continue;
        }

        if ($position < $firstDigit) {
            $firstDigit = (int) $digit;
            break;
        }
    }

    return $firstDigit;
}

function getLastDigit(string $code): int
{
    $lastDigit = mb_strlen($code, 'UTF-8');

    foreach (DIGITS as $digit) {
        $position = strpos($code, $digit);

        if (!$position) {
            continue;
        }

        if ($position < $lastDigit) {
            $lastDigit = (int) $digit;
            break;
        }
    }

    return $lastDigit;
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