# Toy Problems by Dan Munene
Introduction

Welcome to Toy Problems, a collection of small coding challenges tackled by Dan Munene. These challenges cover various topics and are designed to be fun and educational.
Features

  ## Challenge-1: Convert to 24 Hours
        Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.

Your task is to return a four-digit string that encodes that time in 24-hour time.
Notes

By convention, noon is 12:00 pm, and midnight is 12:00 am.

On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On 24-hour clock, this translates to 0015. 

  ## Challenge-2: Exactly Two Positives
        Task:

Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.
Examples:

(2, 4, -3) == True
(-14, -3, -4) == False
(4, 6, 10) == False

  ## Challenge-3: Highest Value of Consonant Substrings
     Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
For the word "zodiacs", solve("zodiacs") = 26

For example, for the word "zodiacs", let's cross out the vowels. We get: "z d cs"

-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.

For the word "strength", solve("strength") = 57.

The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

## Installation

No installation required. Simply copy and paste the provided code snippets into your preferred Python environment.

## Usage
  ### Challenge-1: Convert to 24 Hours

  This challenge provides a function convertTo24Hrs to convert a 12-hour time format to a 24-hour format. Here's an example usage:

        time = convertTo24Hrs(8, 10, "pm")
        print(time)

  ### Challenge-2: Exactly Two Positives

  The twoPositives function checks if exactly two out of three numbers are positive. Example usage:


  print(twoPositives(1, -15, 10))

  ### Challenge-3: Highest Value of Consonant Substrings

  The solve function calculates the highest value of consonant substrings in a given word. Example usage:


  result1 = solve("zodiacs")
  print(result1)

## Contributing

Feel free to contribute by reporting issues, submitting feature requests, or providing code improvements. Follow these steps:

    Fork the repository.
    Create a new branch for your feature or bug fix.
    Make your changes and commit them.
    Push your changes to your fork.
    Create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
