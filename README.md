## Steam Test project

This project aims to implement UI tests for Steam store website.

### Patterns and technologies used:
* pytest as test framework
* Page Object Model for pages
* Singleton pattern for webdriver instance
* Model classes for data

### Test Case 1 (test_privacy_policy)
| Steps  | Expected Results |
| ------------- | ------------- |
| 1. Navigate to main page | Main page is open |
| 2. Scroll and open "Privacy Policy" | Privacy policy page is open in new tab<br>Switch language elements list displayed<br>Supported languages: English, Spanish, French, German, Italian, Russian, Japanese, Portuguese, Brazilian<br>Policy revision signed in the current year |

### Test Case 2 (test_game_search)
| Steps  | Expected Results |
| ------------- | ------------- |
| 1. Navigate to main page | Main page is open |
| 2. Search "Dota 2" in the search field | Result page is open<br>Search box on result page contains searched name<br>The first name is equal to searched name |
| 3. Save information about the first and second result from the list (name, platforms, release date, review summary result, price) | |
| 4. Search the second name (received from result list in step 3) in the search field in the header | Search box on result page contains searched name<br>Result list contains 2 items stored during the previous search<br>Data saved in step 3 matches displayed data |
