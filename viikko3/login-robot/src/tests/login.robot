*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
