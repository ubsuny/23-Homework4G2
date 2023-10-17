# Github Actions:
Github actions let you automate specific actions

For example, in this assignment we have automated unit testing and linting.
We can use:
~~~
on: push
~~~

We can use this to run our action on every merge request.

## Pylint
For our linting we use pylint. 

Pylint checks for errors in your code as well as giving suggestions to make your code more readable. 

Example of output:

![pylint_example_image](https://github.com/ubsuny/23-Homework4G2/assets/143819849/76430a52-a20e-4e64-8e3b-3cd972495dc7)


## Pytest
Pytest helps us unit test our code. We can tell it to test our code on every merge request to make sure nothing was accidently broken.  

It will return the amount of tests passed. 

Example:

![pytest_example_image2](https://github.com/ubsuny/23-Homework4G2/assets/143819849/b4aac71e-5d27-40a8-830b-99a23d6b3cb0)


## Changelog:
(provide list of changes to original code)
