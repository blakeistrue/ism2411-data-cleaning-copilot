What Copilot Generated

I also used GitHub Copilot to start writing two important parts of the code as soon as possible, by telling it what I needed with short comments, and it gave the basic lines of code on the spot.

Loading Data: I wrote a simple comment saying I needed to read the CSV file. Copilot immediately suggested the line df = pd.read_csv(RAW_PATH). This was perfect and let me start working with the data right away.

Bad Numbers Removal (Negative Values): I asked Copilot to help me filter for only the rows that had zero or a positive price and quantity. This was Step 6. It returned the line df = df[(df['price'] >= 0) & (df['qty'] >= 0)]. This filtering code was exactly what I needed in order to find those bad rows and remove them.

What I Changed

Even though Copilot gave me a great starting point for code, there were a number of key changes and additions that I needed to make in order for the script to actually run without crashing. This was because the raw data was much messier than Copilot knew.

Cleaning Column Names: The First Problem My script was crashing due to a KeyError because of strange symbols or extra spacing in the column names of the raw data. So, my initial cleaning code was not strong enough. I had to add an extra, stronger line of code in Step 2 to remove any non-letter or non-number characters from columns. An example would be: df.columns = df.columns.str.replace('[^a-z0-9_]', '', regex=True). This was essential not only to prevent errors but also to assure that all columns were correctly named, like prodname and category.

Data Type Repair (The Big Problem): The code broke with a TypeError in the check for negative numbers, because some of the data in the price and qty columns was read in as text (strings). I realized I had to insert an entirely new step - Step 4, df['price'] = pd.to_numeric(df['price'], errors='coerce')-which explicitly converts those columns to numbers and allowed for the ultimate comparison and filtering -Step 6-to function.

What I Learned

This project taught me two important things about cleaning data in Python.

First, I learned you must always check the data type before you try to do math or make comparisons. It feels like the most simple problem - is the price a number or not? - but if one cell has a space or weird character, the whole column breaks. Using the pd.to_numeric function explicitly is now a step I won't forget. Second, Copilot is a powerful helper, but the results are mine. This means that Copilot will often write the code for the common tasks in no time, but when the code failed due to bad data-like wrong column names or the string error-I had to debug using my knowledge and the error messages to find out what exactly went wrong and add the specific fixes. My role was to debug the specific problems in the raw file that Copilot could not foresee.