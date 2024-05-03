*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  aaaaaaa7
    Output Should Contain  New user registered 

Register With Already Taken Username And Valid Password
    Create default user
    Input Credentials  kalle  aaaaaaa7    
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  aaaaaaa7
    Output Should Contain  Username ka is too short min length is 3 

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  +++  aaaaaaa7
    Output Should Contain  Username +++ is invalid. Username can only contain letters from a-z. 

Register With Valid Username And Too Short Password
    Input Credentials  kalle  a7
    Output Should Contain  Password is invalid. Password must be at least 8 characters long and contain at least one non-letter character.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  aaaaaaaa
    Output Should Contain  Password is invalid. Password must be at least 8 characters long and contain at least one non-letter character.

*** Keywords ***
Create default user
    Create User  kalle  aaaaaaa7
