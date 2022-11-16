*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page To Register

*** Test Cases ***
Register With Valid Username And Password
    Set Username  bobbuy
    Set Password  kalle123kalle123
    Set Password Confirmation  kalle123kalle123
    Submit Register Credentials
    Registration Should Succeed
# ...

Register With Too Short Username And Valid Password
    Set Username  s
    Set Password  kalle123kalle
    Set Password Confirmation  kalle123kalle
    Submit Register Credentials
    Registration Should Fail With Message  Username has to contain only symbols [a-z] and be at least length of 3

# ...

Register With Valid Username And Too Short Password
    Set Username  bobbuy
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Register Credentials
    Registration Should Fail With Message  Password has to be at least length of 8 and it shouldn't contain only characters from a-z


# ...

Register With Nonmatching Password And Password Confirmation
    Set Username  bobbuy
    Set Password  kalle123kalle123
    Set Password Confirmation  kalle123kalle
    Submit Register Credentials
    Registration Should Fail With Message  Passwords don't match
# ...

Login After Successful Registration
    Set Username  testuser
    Set Password  kalle123kalle123
    Set Password Confirmation  kalle123kalle123
    Submit Register Credentials
    Registration Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  testuser
    Set Password  kalle123kalle123
    Submit Login Credentials
    Login Should Succeed
# ...

Login After Failed Registration
    Set Username  te
    Set Password  kalle123kalle123
    Set Password Confirmation  kalle123kalle123
    Submit Register Credentials
    Registration Should Fail
    Go To Login Page
    Login Page Should Be Open
    Set Username  te
    Set Password  kalle123kalle123
    Submit Login Credentials
    Login Should Fail
# ...

*** Keywords ***
Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Registration Should Fail With Message
    [Arguments]   ${message}
    Register Page Should Be Open
    Page Should Contain   ${message}

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail
    Login Page Should Be Open

Go To Register Page To Register
    Go To Register Page
    Register Page Should Be Open
  