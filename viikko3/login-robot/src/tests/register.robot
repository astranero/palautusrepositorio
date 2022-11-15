*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  takenuser  kallekalle123
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  as  kallekalle123
    Output Should Contain  Username has to be at least length of 3 with symbols [a-z]

Register With Valid Username And Too Short Password
    Input Credentials   kalle  asds
    Output Should Contain  Password has to be at least length of 8 and it shouldn't contain only characters from a-z

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password has to be at least length of 8 and it shouldn't contain only characters from a-z

*** Keywords ***
Input New Command And Create User
    Input New Command 
    Create User  takenuser  toimivasalasana123
