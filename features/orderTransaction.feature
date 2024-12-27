Feature: Order Transaction
  Tests related to Order Transaction

  Scenario Outline: Verify Order success message shown in details page
    Given user place the item order with <username> and <password>
    And the user is on landing page
    When user login to portal with <username> and <password>
    And user navigate to orders page
    And user select the orderId
    Then order message is successfully displayed
    Examples:
      | username            | password        |
      | kunlyy2k2@yahoo.com | Uthman@01012021 |
