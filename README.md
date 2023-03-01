## DemoQA project

This project aims to implement UI tests on various elements of https://demoqa.com/ training website. In this project I also try to make a simple framework to work with Selenium that consists of base classes for elements and forms (pages) utilizing explicit waits for them. 

### Patterns and technologies used:
* pytest as test framework
* Page Object Model for pages
* Singleton pattern and Page Factory
* Model classes for data

### Test Case 1 (test_alerts)
| Steps  | Expected Results |
| ------------- | ------------- |
| 1. Navigate to main page | Main page is open |
| 2. Click on "Alerts, Frame & Windows button<br>In menu click "Alerts" button | Alerts form has appeared on page |
| 3. Click on "Click Button to see alert" button | Alert with text "You clicked a button" is open |
| 4. Click "OK" button | Alert has closed |
| 5. Click on "On button click, confirm box will appear" button | Alert with text "Do you confirm action?" is open |
| 6. Click on "OK" button | Alert is closed<br>Text "You selected OK" has appeared on page |
| 7. Click on "On button click, prompt box will appear" button | Alert with text "Please enter your name" is open |
| 8. Enter **randomly generated** text, click "OK" button | Alert has closed<br>Appeared text equals to the one you've entered before |

### Test Case 2 (test_iframe)
| Steps  | Expected Results |
| ------------- | ------------- |
| 1. Navigate to main page | Main page is open |
| 2. Click on "Alerts, Frame & Windows button<br>In menu click "Nested Frames" button | Page with Nested Frames is open<br>There are messages "Parent frame" & "Child IFrame" present on page |
| 3. Select "Frames" options in a left menu | Page with Frames form is open<br>Message from upper frame is equal to the message from lower frame |

### Test Case 3 (test_tables)
This test case is parametrized with list of 2 user's data.

| Steps  | Expected Results |
| ------------- | ------------- |
| 1. Navigate to main page | Main page is open |
| 2. Click on "Elements" button<br>In the menu click a "Web Tables" button | Page with Web Tables form is open |
| 3. Click on "Add" button | Registration Form has appeared on page |
| 4. Enter data for User **n** from the table and then click "Submit" button | Registration form has closed<br>Data of User **n** has appeared in the table |
| 5. Click "Delete" button in a row which contains data of User **n** | Number of records in table has changed<br>Data of User **n** has been deleted from table |

### Test Case 4 (test_handles)
| Steps  | Expected Results |
| ------------- | ------------- |
| 1. Navigate to main page | Main page is open |
| 2. Click on "Alerts, Frame & Windows button<br>In menu click "Browser Windows" button | Page with Browser Windows form is open |
| 3. Click on "New Tab" button | New tab with sample page is open |
| 4. Close current tab | Page with Browser Windows form is open |
| 5. In the menu on the left click "Elements" then "Links" button | Page with Links form is open |
| 6. Click on "Home" link | New tab with main page is open |
| 7. Resume to previous tab | Page with Links form is open |
