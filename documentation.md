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

#### Example of output:
Passing:
![pylint_example_image](https://github.com/ubsuny/23-Homework4G2/assets/143819849/76430a52-a20e-4e64-8e3b-3cd972495dc7)

Failing:
![image](https://github.com/ubsuny/23-Homework4G2/assets/143819849/b2b799aa-c4d0-41d1-ac26-265fdf4fed0d)


## Pytest
Pytest helps us unit test our code. We can tell it to test our code on every merge request to make sure nothing was accidently broken.  

It will return the amount of tests passed as well which test failed if any. 

#### Example:
Passing:
![pytest_example_image2](https://github.com/ubsuny/23-Homework4G2/assets/143819849/b4aac71e-5d27-40a8-830b-99a23d6b3cb0)

Failing:
![image](https://github.com/ubsuny/23-Homework4G2/assets/143819849/6bfcd995-0f5c-475c-b1f3-fb6fe6d1e24c)

## Changelog:
#### Pylint changes:
+ Removed unnecessary blank spaces
+ Added module docstring
+ Added class docstring

![image](https://github.com/ubsuny/23-Homework4G2/assets/143819849/3f94fb46-acc5-45ab-8c20-8bc5440ccf53)



#### Pytest changes:
Pytest said our calculation was about an order of 10 off so we fixed that in our code:

![image](https://github.com/ubsuny/23-Homework4G2/assets/143819849/1809d333-aa9a-49b0-96c5-4858b16f4005)
