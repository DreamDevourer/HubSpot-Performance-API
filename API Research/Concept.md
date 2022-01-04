# Process to get a Performance API

### Pages Paths Step
1. Get all pages by path
2. Store the paths inside a variable
3. Convert the variable to JSON and export it to a json file with a list.

### Domain Step

1. Get the main domain.
2. Print it.
3. Save a file with the list of all domains.

### Performance API Step

1. Load the JSON file with the pages paths.
2. Store the list inside a list variable.
3. Make 'for each' with the list to get page status individually.

### Email Step

1. If a page is with 404 status countdown 10 minutes, check if it still has 404 status, if so countdown 10 minutes, check and send an email if it still has 404 status.
